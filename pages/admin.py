from django.contrib import admin
from .models import Post, Comments 

# Register your models here.



class CommentInLine(admin.StackedInline):
    model = Comments

class PostAdmin(admin.ModelAdmin):
    inlines =[
        CommentInLine,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comments)