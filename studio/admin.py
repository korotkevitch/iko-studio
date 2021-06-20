from django.contrib import admin


from .models import TmpGallery
class TmpGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'prefix', 'tmp_gallery_preview',)
admin.site.register(TmpGallery, TmpGalleryAdmin)


from .models import Header
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'description', 'logo_preview', 'fon_preview', 'slide_preview',)
admin.site.register(Header, HeaderAdmin)


from .models import Area
class AreaAdmin(admin.ModelAdmin):
    list_display = ('area', 'description', 'prefix', 'id')
    prepopulated_fields = {'slug': ('area',)}
admin.site.register(Area, AreaAdmin)


from .models import Tmpl
class TmplAdmin(admin.ModelAdmin):
    list_display = ('title', 'area', 'created_date', 'title_short', 'title_crumb', 'image_preview', 'image_cat_preview', 'caption',
                    'description_short', 'description_long', 'price', 'tmpl_name')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Tmpl, TmplAdmin)


from .models import FeedbackIndex
class FeedbackIndexAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message',)
admin.site.register(FeedbackIndex, FeedbackIndexAdmin)


from .models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phone', 'template_number', 'massage',)
admin.site.register(Feedback, FeedbackAdmin)


from .models import FeedbackBuy
class FeedbackBuyAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phone', 'template_number', 'massage',)
admin.site.register(FeedbackBuy, FeedbackBuyAdmin)


from .models import FeedbackAdm
class FeedbackAdmAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phone', 'template_number', 'massage',)
admin.site.register(FeedbackAdm, FeedbackAdmAdmin)


from .models import Funny
class FunnyAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_foods', 'order_phone', 'contact_phone', 'email', 'head_description', 'download_menu',
                    'first_title', 'first_text', 'second_title', 'second_text', 'address', 'work_time',)
admin.site.register(Funny, FunnyAdmin)


from .models import FunnyGallery
class FunnyGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image',)
admin.site.register(FunnyGallery, FunnyGalleryAdmin)


from .models import FunnyMenuFirst
class FunnyMenuFirstAdmin(admin.ModelAdmin):
    list_display = ('food', 'price')
admin.site.register(FunnyMenuFirst, FunnyMenuFirstAdmin)


from .models import FunnyMenuSecond
class FunnyMenuSecondAdmin(admin.ModelAdmin):
    list_display = ('food', 'price')
admin.site.register(FunnyMenuSecond, FunnyMenuSecondAdmin)


from .models import FunnyMenuThird
class FunnyMenuThirdAdmin(admin.ModelAdmin):
    list_display = ('food', 'price')
admin.site.register(FunnyMenuThird, FunnyMenuThirdAdmin)


from .models import FunnyFeedback
class FunnyFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'massage',)
admin.site.register(FunnyFeedback, FunnyFeedbackAdmin)


from .models import PizzaImages
class PizzaImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'pizza_images_preview',)
admin.site.register(PizzaImages, PizzaImagesAdmin)


from .models import PizzaMenu
class PizzaMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'price', 'pizza_menu_preview',)
admin.site.register(PizzaMenu, PizzaMenuAdmin)


from .models import PizzaPopular
class PizzaPopularAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'price', 'pizza_popular_preview',)
admin.site.register(PizzaPopular, PizzaPopularAdmin)


from .models import PizzaGallery
class PizzaGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'pizza_gallery_preview',)
admin.site.register(PizzaGallery, PizzaGalleryAdmin)


from .models import PizzaMenu12
class PizzaMenu12Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'price', 'pizza_menu12_preview',)
admin.site.register(PizzaMenu12, PizzaMenu12Admin)


from .models import PizzaPersonal
class PizzaPersonalAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'description', 'image', 'pizza_personal_preview',)
admin.site.register(PizzaPersonal, PizzaPersonalAdmin)


from .models import PizzaFeedback
class PizzaFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'massage',)
admin.site.register(PizzaFeedback, PizzaFeedbackAdmin)


from .models import PizzaInfo
class PizzaInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'download_menu',)
admin.site.register(PizzaInfo, PizzaInfoAdmin)


from .models import VenueText
class VenueTextAdmin(admin.ModelAdmin):
    list_display = ('name', 'reservation_phone', 'download_menu', 'first_title', 'second_title', 'third_title',
                    'first_text_section_1', 'second_text_section_1', 'third_text_section_1', 'menu_slogan', 'menu_name',
                    'menu_intro_1', 'menu_intro_2', 'sign_menu_slogan', 'sign_menu_name', 'footer_text', 'footer_address',
                    'footer_phone', 'footer_email')
admin.site.register(VenueText, VenueTextAdmin)


from .models import VenueImage
class VenueImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'top_fon_image_preview', 'first_image_section_1_preview', 'second_image_section_1_preview',
                    'video_preview_preview', 'video_name', 'video_link', 'img_1_preview', 'img_2_preview',
                    'img_3_preview', 'bottom_fon_image_preview')
admin.site.register(VenueImage, VenueImageAdmin)


from .models import VenueMenu
class VenueMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'contents_1', 'contents_2', 'contents_3', 'contents_4', 'price', 'sign_img_preview')
admin.site.register(VenueMenu, VenueMenuAdmin)


from .models import VenueTeam
class VenueTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'slogan', 'team_intro_1', 'team_intro_2', 'img_1_preview', 'name_1', 'post_1',
                    'img_2_preview', 'name_2', 'post_2', 'img_3_preview', 'name_3', 'post_3', 'img_4_preview', 'name_4',
                    'post_4',)
admin.site.register(VenueTeam, VenueTeamAdmin)


from .models import VenueTestimonial
class VenueTestimonialAdmin(admin.ModelAdmin):
    list_display = ('person', 'who_is', 'id', 'image_preview', 'testimonial', 'name', 'slogan')
admin.site.register(VenueTestimonial, VenueTestimonialAdmin)


from .models import VenueHit
class VenueHitAdmin(admin.ModelAdmin):
    list_display = ('slogan', 'title', 'name', 'image_preview', 'contents_1', 'contents_2', 'contents_3', 'contents_4', 'price')
admin.site.register(VenueHit, VenueHitAdmin)


from .models import VenueFeedback
class VenueFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'massage',)
admin.site.register(VenueFeedback, VenueFeedbackAdmin)


from .models import VenueRes
class VenueResAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'number',)
admin.site.register(VenueRes, VenueResAdmin)


from .models import VenueThanks
class VenueThanksAdmin(admin.ModelAdmin):
    list_display = ('phrase', 'image_preview',)
admin.site.register(VenueThanks, VenueThanksAdmin)


from .models import CoffeeFeedback
class CoffeeFeedbackAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'date', 'time', 'phone', 'massage',)
admin.site.register(CoffeeFeedback, CoffeeFeedbackAdmin)


from .models import CoffeeInfo
class CoffeeInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'download_menu',)
admin.site.register(CoffeeInfo, CoffeeInfoAdmin)


from .models import CoffeeMenu
class CoffeeMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'price', 'coffee_menu_preview',)
admin.site.register(CoffeeMenu, CoffeeMenuAdmin)


from .models import CoffeePopular
class CoffeePopularAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'price', 'coffee_popular_preview',)
admin.site.register(CoffeePopular, CoffeePopularAdmin)


from .models import CoffeeGallery
class CoffeeGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'coffee_gallery_preview',)
admin.site.register(CoffeeGallery, CoffeeGalleryAdmin)


from .models import CoffeeMenu9
class CoffeeMenu9Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'price', 'coffee_menu9_preview',)
admin.site.register(CoffeeMenu9, CoffeeMenu9Admin)


from .models import CoffeeTestimonial
class CoffeeTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'who_is', 'id', 'image_preview', 'testimonial')
admin.site.register(CoffeeTestimonial, CoffeeTestimonialAdmin)


from .models import KusinaTop
class KusinaTopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'subtitle', 'image_preview', 'img_1_preview', 'descr_1', 'img_2_preview', 'descr_2',
                    'img_3_preview', 'descr_3')
admin.site.register(KusinaTop, KusinaTopAdmin)


from .models import KusinaAbout
class KusinaAboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'description', 'video_preview', 'video_link', 'subtitle', 'img_1_preview',
                    'descr_1', 'img_2_preview', 'descr_2',
                    'img_3_preview', 'descr_3')
admin.site.register(KusinaAbout, KusinaAboutAdmin)


from .models import KusinaStatistics
class KusinaStatisticsAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'p_1_name', 'p_1_value', 'p_2_name', 'p_2_value', 'p_3_name', 'p_3_value',
                    'p_4_name', 'p_4_value',)
admin.site.register(KusinaStatistics, KusinaStatisticsAdmin)


from .models import KusinaMenu
class KusinaMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'contents_1', 'contents_2', 'contents_3', 'contents_4', 'price')
admin.site.register(KusinaMenu, KusinaMenuAdmin)


from .models import KusinaTestimonial
class KusinaTestimonialAdmin(admin.ModelAdmin):
    list_display = ('person', 'testimonial', 'photo_preview', 'who_is')
admin.site.register(KusinaTestimonial, KusinaTestimonialAdmin)


from .models import KusinaTeam
class KusinaTeamAdmin(admin.ModelAdmin):
    list_display = ('person', 'img_preview', 'who_is')
admin.site.register(KusinaTeam, KusinaTeamAdmin)


from .models import KusinaReservation
class KusinaReservationAdmin(admin.ModelAdmin):
    list_display = ('second_name', 'first_name',  'date', 'time', 'phone', 'person',)
admin.site.register(KusinaReservation, KusinaReservationAdmin)


from .models import KusinaNewsletter
class KusinaNewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
admin.site.register(KusinaNewsletter, KusinaNewsletterAdmin)


from .models import KusinaInsta
class KusinaInstaAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')
admin.site.register(KusinaInsta, KusinaInstaAdmin)


from .models import KusinaDownloadMenu
class KusinaDownloadMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu')
admin.site.register(KusinaDownloadMenu, KusinaDownloadMenuAdmin)


from .models import BeeGallery
class BeeGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'bee_gallery_preview',)
admin.site.register(BeeGallery, BeeGalleryAdmin)


from .models import ConstructoGallery
class ConstructoGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'constructo_gallery_preview',)
admin.site.register(ConstructoGallery, ConstructoGalleryAdmin)


from .models import BusHead
class BusHeadAdmin(admin.ModelAdmin):
    list_display = ('logo', 'title', 'title_on_image', 'image_preview')
admin.site.register(BusHead, BusHeadAdmin)


from .models import BusGallery
class BusGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'bus_gallery_preview')
admin.site.register(BusGallery, BusGalleryAdmin)