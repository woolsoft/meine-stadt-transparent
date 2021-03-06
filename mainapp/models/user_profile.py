# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, related_name="profile", verbose_name=_(u'User'),
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')

    def __unicode__(self):
        return "User profile: %s" % self.user.username

    def has_unverified_email_adresses(self):
        for email in self.user.emailaddress_set.all():
            if not email.verified:
                return True
        return False
