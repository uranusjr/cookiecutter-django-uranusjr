from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user class.

    This is modelled very closely after Django's built-in user, but replace
    the awkward first/last name fields with one single display_name field.
    """
    username = models.CharField(
        verbose_name=_('username'),
        max_length=150, unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and '
            '@/./+/-/_ only.'
        ),
    )
    display_name = models.CharField(
        verbose_name=_('display name'),
        max_length=100, blank=True,
    )
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255, blank=True,
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'),
        default=timezone.now,
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    def get_short_name(self):
        """A short name to identify this user.

        This is provided for compatibility with the admin.
        """
        return self.display_name

    def get_full_name(self):
        """A name to identify this user.

        This is provided for compatibility with the admin.
        """
        return self.display_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
