from django.shortcuts import render
from account.models import Account, Connection
from django.db.models import Q



def suggest_accounts_view(request):	
	user = request.user
	context = {}
	if user.is_authenticated:
		accounts = Account.objects.all()
	else:
		redirect('home.html')
	
	context['user'] = user

	connection_followers = Connection.objects.filter(
		followers=user, request=False
	)

	context['connections'] = connection_followers
	
	context['accounts'] = accounts
	return render(request, 'explore/account_suggestion.html', context)