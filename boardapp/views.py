from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
    user2 = User.objects.get(username="taro")
    print(user2.email)
    #リクエストがgetで届いたのかpostで届いたのかによって処理を分ける
    if request.method == 'POST':
        #signup.htmlの中で指定したusernameをdjango側に引っ張ってくる
        username2 = request.POST['username']
        password2 = request.POST['password']
        #名前の重複エラーをキャッチするtry except構文を作る
        try: #重複があった場合
            #User.objects.get()でuserデータを持ってこれる
            User.objects.get(username=username2)
            #tryに引っかかるとerrorを持って来れるようになる
            return render(request, 'signup.html',{'error':'このユーザーはすでにいる'})
        except:#重複がなかった場合
            #djangoが用意しているcreate_userテーブルをimportしてそこにデータを当てはめる
            #使うにはmigrateしてuserのテーブルを作る必要がある
            #migrateするだけでデフォルトで作られる
            user = User.objects.create_user(username2, '',password2)
            return render(request, 'signup.html',{'some':100})
    #renderを使うことでテンプレートとモデルを組み合わせてレスポンスを返すことができる
    #{}内で辞書型でデータを扱う 文字も数字も行ける
    return render(request, 'signup.html',{'some':100})
    
def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        #この認証ができてるかどうかを他のページのフラグで使う
        user = authenticate(request, username=username2, password=password2)
        if user is not None:#ユーザーが居る場合
            #ログイン処理
            login(request, user)
            #renderとredirectの違い
            #renderはあくまでファイルをレスポンスしてるだけでurlとの齟齬が出る
            #例：loginページなのにsignupのページが開いている
            #redirectはurlから呼び出してリクエストを送り直す
            return redirect('list')
        else:#ユーザーがいない場合
            return redirect('login')
    #POSTじゃなかったときの処理も書かないとエラーになる
    return render(request, 'login.html')

#ログインしていなかったらログイン画面に戻す処理
#setting.py内でLOGIN_URLを指定
@login_required
def listfunc(request):
    #BoradModelのオブジェクトを全部持ってくる
    object_list = BoardModel.objects.all()
    return render(request, 'list.html',{'object_list':object_list})
    
#ログアウト処理。非常にシンプル
def logoutfunc(request):
    logout(request)
    return redirect('login')
    
#詳細画面
def detailfunc(request,pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html',{'object':object})
    
#いいねの実装
def goodfunc(request,pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good+1
    #オブジェクト内のデータを書き換えてそれを保存する
    post.save()
    return redirect('list')
    
def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    #既読ボタンはすでに押されていたら数が増えないようにする必要がある
    #既読した人のリストからそれを参照する
    
    #既読しようとしている人の名前
    post_username = request.user.get_username()
    #readtextはmodels.pyで定義した既読した人のリスト
    if post_username in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext=post.readtext+''+post_username
        post.save()
        return redirect('list')
        
class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    #いいねとか既読はcreateの際には不要
    #ここではユーザーが自分で設定するもののみ。autherは別で自動で入れる機能を実装
    fields = ('title','content','auther','images')
    success_url = reverse_lazy('list')
    