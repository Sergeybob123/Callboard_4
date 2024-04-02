from ckeditor_uploader import forms
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Response)

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.Charfield(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'