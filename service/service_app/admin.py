from django.contrib import admin
from service_app.models import Access,Topic,Web,User
# Register your models here.

admin.site.register(Access);
admin.site.register(Topic);
admin.site.register(Web);
admin.site.register(User);