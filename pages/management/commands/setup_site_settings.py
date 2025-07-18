from django.core.management.base import BaseCommand
from pages.models import SiteSettings

class Command(BaseCommand):
    help = 'Setup initial site settings'

    def handle(self, *args, **options):
        # Create or update site settings
        site_settings, created = SiteSettings.objects.get_or_create(
            id=1,
            defaults={
                'site_name': 'NaturalMed Store',
                'tagline': 'Premium Natural Medical Products & Cannabis Solutions',
                'about_text': 'Your trusted source for premium natural medical products, including CBD, hemp-based remedies, and organic therapeutic solutions. All products are carefully selected for quality and efficacy.',
                'email': 'info@naturalmedstore.com',
                'phone': '+33 1 23 45 67 89',
                'address': '123 Rue de la Santé, 75014 Paris, France',
                'business_hours': 'Mon-Fri: 9:00-19:00\nSat: 10:00-17:00\nSun: Closed',
                'facebook_url': 'https://facebook.com/naturalmedstore',
                'twitter_url': 'https://twitter.com/naturalmedstore',
                'instagram_url': 'https://instagram.com/naturalmedstore',
                'privacy_policy': 'We respect your privacy and protect your personal data in accordance with GDPR regulations. We collect only necessary information and never share your data with third parties without consent.',
                'terms_of_service': 'By using our services, you agree to our terms and conditions. All products are for educational and wellness purposes only and have not been evaluated by the FDA.',
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS('Successfully created site settings')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Site settings already exist')
            )