from django.core.management.base import BaseCommand
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Update product categories for cannabis/natural medical focus'

    def handle(self, *args, **options):
        # Update existing categories for cannabis/natural medical focus
        categories_data = [
            {
                'name': 'CBD Products',
                'slug': 'cbd-products',
                'description': 'High-quality CBD oils, tinctures, and capsules for therapeutic use'
            },
            {
                'name': 'Hemp-Based Remedies',
                'slug': 'hemp-remedies',
                'description': 'Natural hemp-derived products for wellness and pain management'
            },
            {
                'name': 'Herbal Tinctures',
                'slug': 'herbal-tinctures',
                'description': 'Concentrated herbal extracts for various health conditions'
            },
            {
                'name': 'Organic Topicals',
                'slug': 'organic-topicals',
                'description': 'Natural topical creams and balms for skin and muscle relief'
            },
            {
                'name': 'Wellness Supplements',
                'slug': 'wellness-supplements',
                'description': 'Natural supplements for overall health and vitality'
            },
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'description': cat_data.get('description', '')
                }
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )
            else:
                # Update existing category
                category.name = cat_data['name']
                category.description = cat_data.get('description', '')
                category.save()
                self.stdout.write(
                    self.style.WARNING(f'Updated category: {category.name}')
                )

        # Update existing products with cannabis/natural medical focus
        products_updates = [
            {
                'slug': 'advanced-pain-relief-formula',
                'name': 'Advanced Hemp Pain Relief Formula',
                'description': 'Full-spectrum hemp extract combined with natural anti-inflammatory compounds for comprehensive pain management.',
                'composition': 'Hemp extract (500mg), turmeric curcumin, white willow bark, boswellia serrata, vegetable capsules',
                'usage_instructions': 'Take 1-2 capsules daily with food. Start with one capsule to assess tolerance.',
                'creation_method': 'CO2 extraction from organic hemp, combined with standardized herbal extracts',
                'benefits': 'Reduces chronic pain, inflammation, and supports joint mobility and comfort',
                'category_slug': 'hemp-remedies'
            },
            {
                'slug': 'joint-mobility-formula',
                'name': 'CBD Joint Mobility Complex',
                'description': 'Premium CBD oil with glucosamine and chondroitin for optimal joint health and flexibility.',
                'composition': 'CBD isolate (300mg), glucosamine sulfate, chondroitin sulfate, MSM, hyaluronic acid',
                'usage_instructions': 'Take 1 capsule twice daily with meals for best absorption and results.',
                'creation_method': 'Pharmaceutical-grade CBD combined with clinically studied joint support compounds',
                'benefits': 'Improves joint flexibility, reduces stiffness, supports cartilage health',
                'category_slug': 'cbd-products'
            },
            {
                'slug': 'antioxidant-shield',
                'name': 'Organic Antioxidant Shield Tincture',
                'description': 'Powerful herbal tincture combining adaptogenic herbs with antioxidant-rich botanicals.',
                'composition': 'Organic elderberry, astragalus root, echinacea, ginkgo biloba, alcohol base',
                'usage_instructions': 'Take 1-2 droppers full under tongue, hold for 30 seconds before swallowing.',
                'creation_method': 'Traditional alcohol extraction method preserving active compounds',
                'benefits': 'Boosts immune system, fights free radicals, supports cellular health',
                'category_slug': 'herbal-tinctures'
            },
            {
                'slug': 'digestease-pro',
                'name': 'Hemp Digestive Wellness Complex',
                'description': 'Hemp seed oil combined with digestive enzymes and probiotics for gut health.',
                'composition': 'Hemp seed oil, digestive enzyme blend, probiotic cultures, prebiotic fiber',
                'usage_instructions': 'Take 1-2 capsules before meals to support healthy digestion.',
                'creation_method': 'Cold-pressed hemp seed oil with live probiotic cultures',
                'benefits': 'Improves digestion, reduces bloating, supports healthy gut microbiome',
                'category_slug': 'wellness-supplements'
            },
            {
                'slug': 'respiclear-lung-support',
                'name': 'Organic Respiratory Relief Balm',
                'description': 'Natural topical balm with eucalyptus and menthol for respiratory comfort.',
                'composition': 'Organic coconut oil, eucalyptus oil, menthol crystals, camphor, beeswax',
                'usage_instructions': 'Apply to chest and throat area. Massage gently. Use 2-3 times daily.',
                'creation_method': 'Hand-crafted with organic ingredients and essential oils',
                'benefits': 'Soothes respiratory discomfort, opens airways, provides cooling relief',
                'category_slug': 'organic-topicals'
            },
        ]

        for prod_data in products_updates:
            try:
                product = Product.objects.get(slug=prod_data['slug'])
                category = Category.objects.get(slug=prod_data['category_slug'])
                
                product.name = prod_data['name']
                product.description = prod_data['description']
                product.composition = prod_data['composition']
                product.usage_instructions = prod_data['usage_instructions']
                product.creation_method = prod_data['creation_method']
                product.benefits = prod_data['benefits']
                product.category = category
                product.save()
                
                self.stdout.write(
                    self.style.SUCCESS(f'Updated product: {product.name}')
                )
            except Product.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Product not found: {prod_data["slug"]}')
                )
            except Category.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'Category not found: {prod_data["category_slug"]}')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully updated categories and products for cannabis/natural medical focus')
        )