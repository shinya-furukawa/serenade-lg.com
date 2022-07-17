import imp
from django.contrib import admin
from register.models import User,Customer,Address

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'is_active',
        'id',
    )
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','zipcode','address','building')
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
    )

admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Customer, CustomerAdmin)