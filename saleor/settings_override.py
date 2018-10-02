PAYMENT_VARIANTS = {
    # 'default': ('payments.dummy.DummyProvider', {}),
    'default': ('django_payments_cod.CODProvider', {}),
    }

CHECKOUT_PAYMENT_CHOICES = [
    # ('default', 'Dummy provider'),
    ('default', 'Cash on delivery'),
    ]

from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('en', _('English')),
]
