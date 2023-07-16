from django import template

register = template.Library()

@register.filter
def truncate_string(value, args):
    max_len, trunc_len = [int(arg) for arg in args.split(",")]
    if len(value) > max_len:
        return value[:trunc_len] + '...'
    else:
        return value