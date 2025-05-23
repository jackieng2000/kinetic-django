from django.contrib import admin



from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_by', 'created_at', 'updated_at')
    search_fields = ('title', )

admin.site.register(Post, PostAdmin)

