from django.contrib import admin
from .models import Portfolio
from .models import Inventory
from .models import Session
# Register your models here.


admin.site.register(Portfolio)
admin.site.register(Inventory)
admin.site.register(Session)

