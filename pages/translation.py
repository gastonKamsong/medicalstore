from modeltranslation.translator import register, TranslationOptions
from .models import SiteSettings


@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('site_name', 'tagline', 'address', 'business_hours', 'about_text', 
              'privacy_policy', 'terms_of_service')