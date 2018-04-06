# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.admin.helpers import ActionForm
from django.forms import SelectDateWidget

import datetime


class SetCertificationDateForm(ActionForm):
    certification_date = forms.DateField(
        widget=SelectDateWidget,
        initial=(datetime.date.today())
    )
