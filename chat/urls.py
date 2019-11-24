from django.urls import path
from chat.views import(
	message_view,
	inbox_view,
	add_new_chat,
	delete_chat,
	delete_message,
)


app_name = 'chat'


urlpatterns = [
	path('<slug>/', message_view, name="message"),
	path('account/inbox', inbox_view, name="inbox"),
	path('new/<slug>/', add_new_chat, name="add_chat"),
	path('<id>/dc/delete', delete_chat, name="delete_chat"),
	path('<slug>/dm/<id>', delete_message, name="delete_message"),

]