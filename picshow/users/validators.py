import re

from django.core.exceptions import ValidationError


def validate_username(value):
    disallowed_symbols = re.findall(r'[^\w.@+-]', value)
    if value == 'me' or disallowed_symbols:
        error_msg = 'Имя me недоступно. Выберите другое.'
        if disallowed_symbols:
            error_msg += f' Недопустимые символы: {"".join(disallowed_symbols)}'
        raise ValidationError(error_msg)
    return value


def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Пароль должен содержать не менее 8 символов')
