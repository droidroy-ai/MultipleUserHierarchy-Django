from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from .models import Cart, Product, ProductInCart, Order, Deal, Customer, Seller, Contact #UserType

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

#admin.site.unregister(User)
#dmin.site.register(User, UserAdmin)

admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.register(Cart)
# admin.site.register(ProductInCart)
class ProductInCartInLine(admin.TabularInline):
    model = ProductInCart

class ProductInLine(admin.TabularInline):
    model = Product


class CartInLine(admin.TabularInline):
    model = Cart

class DealInLine(admin.TabularInline):
    model = Deal.user.through           # for many to many 

# class UserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'get_cart', 'is_staff', 'is_active',)
#     list_filter = ('username', 'is_staff', 'is_active')
#     fieldsets = (
#         (None, {'fields':('username', 'password')}),
#         ('Permissions', {'fields': ('is_staff', ('is_active', 'is_superuser'), )}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#         #('Cart', {'fields': ('get_cart',)})
#         ('Advanced options', {
#             'classes': ('collapse',),
#             'fields': ('groups', 'user_permissions'),
#         }),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),   # class for css (django css)
#             'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups')} #fields shown on create user
#         ),
#     )
#     inlines = [
#         CartInLine, DealInLine
#     ]

#     def get_cart(self, obj):     #this function only works in list display // also the obj here is the instance of User
#         return obj.cart             #through reverse related relationship
    
#     search_fields = ('username',)       #search_filter for search bar
#     ordering = ('username',)


#registering models through class with decorators
@admin.register(Cart) #through register decorator
class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('staff', 'user', 'created_on',)
    list_filter = ('user', 'created_on')
    #fields = ('staff',)
    fieldsets = (
        (None, {'fields': ('user', 'created_on',)}),
        #('Product', {'fields': ('product',)})
        #('User', {'fields': ('staff',)}),
    )
    
    inlines = (ProductInCartInLine,    
    )
    
    #to display only in list
    def staff(self, obj):
        return obj.user.is_staff
    # staff.empty_value_display = '???'
    # def product(self, obj):
    #     return 
    staff.admin_order_field = 'user__is_staff' #Allows column order sorting
    staff.short_description = 'Is Staff User'  #Renames column head

    #Filtering on side
    list_filter = ['user__is_staff', 'created_on']
    search_fields = ['user__username']

class DealAdmin(admin.ModelAdmin):
    inlines = [
        DealInLine,
    ]
    exclude = ('user',)

admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Order)
admin.site.register(Deal, DealAdmin)
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Contact)
#admin.site.register(UserType)
