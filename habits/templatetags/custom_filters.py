from django import template

register = template.Library()

@register.filter
def percentage(value, max_value):
    try:
        return (value / max_value) * 100
    except (ValueError, ZeroDivisionError):
        return 0


@register.filter
def get_badge(total_completed):
    user_badges = []
    if total_completed >= 1:
        user_badges.append("Starter Badge")
    if total_completed >= 5:
        user_badges.append("Consistency Badge")
    if total_completed >= 10:
        user_badges.append("Master Badge")
    return user_badges