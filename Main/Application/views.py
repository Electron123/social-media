from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Content
from .forms import Meme
from django.contrib.auth.decorators import login_required

def index(request):

	Post = Content.objects.all()

	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
		return redirect('home')	
	else:
		form = AuthenticationForm()
	return render(request, "index.html", {"form": form, "Content": Post})

@login_required
def post(request):
	
	Post = Meme(request.POST, request.FILES)
	if Post.is_valid():
		form = Post.save(commit=False)
		form.author = request.user
		form.save()
		return redirect("home")
	return render(request, "post_meme.html", {"Post": Post})



def log_out(request):
	if request.method == "POST":
		logout(request)
		return redirect('home')

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			print("Accout has been created")
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, "signup.html", {"form": form})