from django import template

register = template.Library()

@register.filter
def following_check(some_list, current_account):
    try:
        return some_list.get(following=int(current_account) + 1)        
    except:
        return ''