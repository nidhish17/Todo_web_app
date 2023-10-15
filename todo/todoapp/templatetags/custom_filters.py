from django import template
from datetime import datetime
from django.utils import timezone
import pytz

register = template.Library()

@register.filter()
def truncate_with_ellipsis(value, max_length):
    if len(value) > max_length:
        return value[:max_length] + '...'
    return value

@register.simple_tag(takes_context=True)
def calculate_due(context, due_date):
    request = context["request"]

    user_timezone = pytz.timezone(request.session["user_timezone"])

    today_date = datetime.now(tz=user_timezone)

    time_diff = due_date - today_date.date()

    print(time_diff)

    if time_diff.total_seconds() < 0:
        print("POST DUE")
        return [1, time_diff]
    elif time_diff.total_seconds() == 0:
        print("DUE TODAY")
        return [2, time_diff]
    else:
        print("ON TIME")
        return [0, time_diff]






