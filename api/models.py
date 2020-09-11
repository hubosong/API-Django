# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# used to import time
from django.utils import timezone

# used to create db data
class Pictures(models.Model):
    name = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/%Y/%m', null = True, blank = True)

