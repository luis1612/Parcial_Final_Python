from django.shortcuts import render, redirect,  get_object_or_404
from django.views.decorators.cache import cache_control
from django.db.models import Q
from post.forms import CreatePostForm,UpdatePostForm, CommentForm
from post.models import Post,Like, Comment
from activity.models import Notification
from account.models import Account
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy



def create_post_view(request):
	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('home')

	form = CreatePostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=request.user.email).first()
		obj.author = author
		obj.save()
		context['success_message'] = "Publicado con éxito"
		form = CreatePostForm()

	context['form'] = form

	return render(request, 'post/create_post.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_post_view(request, slug):
	context = {}

	user = request.user

	if not user.is_authenticated:
		return redirect("login")

	post = get_object_or_404(Post, slug=slug)

	if user != post.author:
		return redirect("home")

	if request.POST:
		form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Actualizado"
			post = obj
	form = UpdatePostForm(
			initial={
				"body" : post.caption,
				"image" : post.image,
			}
		)

	context['form'] = form	



	return render(request, 'post/edit_post.html', context)


def detail_post_view(request, slug):
	context = {}

	user = request.user

	if not user.is_authenticated:
		return redirect("login")

	try:
		post = Post.objects.get(slug=slug)
	except Post.DoesNotExist:
		return redirect("home")

	context['current_post'] = post

	if Like.objects.filter(liker=user, post=post).exists():
		context['liked'] = 'liked'

	comment = Comment.objects.filter(post=post)
	context['comments'] = comment

	like_count = Like.objects.filter(post=post).count()
	context['like_count'] = like_count

	form = CommentForm(request.POST)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.commenter = user
		obj.post = post
		obj.save()
		return redirect('post:detail_post' , post.slug)

	return render(request, 'post/detail_post.html', context)

def delete_post_view(request, slug):
	user = request.user

	context = {}

	if not user.is_authenticated:
		return redirect("login")

	post = get_object_or_404(Post, slug=slug)
	
	if request.user != post.author:
		return redirect("home")

	deleted = 'Publicación eliminada correctamente'

	post.delete()

	return redirect('account_detail', user.slug)




def like_post(request, slug):
	user = request.user

	

	try:
		post = Post.objects.get(slug=slug)

	except Post.DoesNotExist:
		message.warning(
			request,
			'La publicación no existe'
		)

	created = Like.objects.get_or_create(liker=user, post=post)
	if(user != post.author):
		like_notification = Notification.objects.create(notification_type='like',user=post.author, notification_by=user, post=post)
	messages.success(request, 'Publicación Liked')

	return redirect('post:detail_post', post.slug)

def unlike_post(request, slug):
	user = request.user

	try:
		post = Post.objects.get(slug=slug)
	
		created = Like.objects.get(liker=user, post=post)
		created.delete()
		like_notification = Notification.objects.get(notification_type='like',user=post.author, notification_by=user, post=post)
		like_notification.delete()

	except Post.DoesNotExist:
		message.warning(
			request,
			'La publicación no existe'
		)


	return redirect('post:detail_post', post.slug)
    


def likes_view(request, slug):
	user = request.user
	context = {}

	try:
		post = Post.objects.get(slug=slug)
	
	except Post.DoesNotExist:
		return redirect("home")

	likes = Like.objects.filter(post=post)

	context['users'] = likes
	context['response'] = "Likes"

	return render(request, 'account/connection.html', context)



def get_post_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = Post.objects.filter(
				Q(caption__icontains=q) 
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))
