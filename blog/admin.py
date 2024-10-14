from django.contrib import admin
from .models import Post
from django.forms import ModelForm
from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget
from .models import TestModel

admin.site.register(Post)

class TestModelForm(ModelForm):
    class Meta:
        model = TestModel
        fields = "__all__"
        widgets = {
            "published": DjangoToggleSwitchWidget(klass="django-toggle-switch-dark-primary"),
            "is_demo": DjangoToggleSwitchWidget(round=True, klass="django-toggle-switch-success"),
        }

class TestModeldmin(admin.ModelAdmin):
    form = TestModelForm

admin.site.register(TestModel, TestModeldmin)