from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Agent_Name),
admin.site.register(Announced_Lga_Results),
admin.site.register(Announced_Pu_Results),
admin.site.register(Announced_State_Results),
admin.site.register(Announced_Ward_Results),
admin.site.register(Lga),
admin.site.register(Party),
admin.site.register(Polling_Unit),
admin.site.register(States),
admin.site.register(Ward)