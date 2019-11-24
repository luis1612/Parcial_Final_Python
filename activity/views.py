from django.shortcuts import render, redirect,  get_object_or_404
from activity.models import Notification


def all_notification_view(request):
	context = {}
	user = request.user
	notifications = Notification.objects.filter(user=user)
	context['notifications'] = notifications
	context['response'] = 'all'

	return render(request, 'activity/notifications.html', context)


def request_notification_view(request):
	context = {}
	user = request.user
	notifications = Notification.objects.get(user=user, notification_type='request')
	context['notification'] = notification
	context['response'] = 'request'

	return render(request, 'activity/notifications.html', context)
