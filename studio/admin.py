from django.contrib import admin


from .models import ExampleList
class ExampleListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'title_short', 'title_crumb', 'intro_title', 'intro_text', 'ps_title', 'ps_text')
    list_display_links = ('id', 'title')
admin.site.register(ExampleList, ExampleListAdmin)


from .models import ExampleDetail
class ExampleDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_activated', 'created_date', 'title_short', 'title_crumb', 'image_preview', 'caption',
                    'description_short', 'description_long', 'testimonial_text', 'testimonial_author',
                    'example_url', 'hosting', 'partner_prefix')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(ExampleDetail, ExampleDetailAdmin)


from .models import Price
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'landing_cost', 'site_cost', 'support_cost')
    list_display_links = ('id', 'landing_cost')
admin.site.register(Price, PriceAdmin)


from .models import ContactForm
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message', 'created_date')
    list_display_links = ('id', 'name')
admin.site.register(ContactForm, ContactFormAdmin)



# from .models import Area
# class AreaAdmin(admin.ModelAdmin):
#     list_display = ('area', 'description', 'slug')
#     prepopulated_fields = {'slug': ('area',)}
# admin.site.register(Area, AreaAdmin)


# from .models import Tmpl
# class TmplAdmin(admin.ModelAdmin):
#     list_display = ('title', 'area', 'is_activated', 'created_date', 'title_short', 'title_crumb', 'image_preview', 'image_cat_preview', 'caption',
#                     'description_short', 'description_long', 'price', 'tmpl_name')
#     prepopulated_fields = {'slug': ('title',)}
# admin.site.register(Tmpl, TmplAdmin)