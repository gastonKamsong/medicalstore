from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    help = 'Populate database with sample medical products'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample categories and products...')

        # Create categories
        categories_data = [
            {
                'name': 'Pain Relief',
                'description': 'Effective pain management solutions for various conditions including chronic pain, acute injuries, and post-operative care.',
                'meta_description': 'Professional pain relief products with detailed composition and usage instructions.',
                'meta_keywords': 'pain relief, analgesics, pain management, medical products'
            },
            {
                'name': 'Cardiovascular Health',
                'description': 'Comprehensive cardiovascular support products designed to promote heart health and circulatory system function.',
                'meta_description': 'Cardiovascular health products with proven benefits and scientific backing.',
                'meta_keywords': 'cardiovascular, heart health, circulation, blood pressure'
            },
            {
                'name': 'Digestive Health',
                'description': 'Digestive system support products for optimal gastrointestinal health and nutrient absorption.',
                'meta_description': 'Digestive health solutions with detailed composition and usage guidelines.',
                'meta_keywords': 'digestive health, gastrointestinal, probiotics, digestion'
            },
            {
                'name': 'Immune Support',
                'description': 'Immune system strengthening products to help maintain optimal immune function and overall wellness.',
                'meta_description': 'Immune support products with comprehensive health benefits information.',
                'meta_keywords': 'immune support, immunity, wellness, health supplements'
            },
            {
                'name': 'Respiratory Care',
                'description': 'Respiratory health products designed to support lung function and breathing comfort.',
                'meta_description': 'Respiratory care products with detailed usage instructions and benefits.',
                'meta_keywords': 'respiratory care, lung health, breathing, pulmonary'
            },
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            {
                'name': 'Advanced Pain Relief Formula',
                'category': 'Pain Relief',
                'price': 29.99,
                'description': 'A comprehensive pain relief formula combining natural and synthetic compounds for effective pain management. Suitable for chronic pain conditions and acute injuries.',
                'composition': 'Active ingredients: Acetaminophen 500mg, Ibuprofen 200mg, Natural willow bark extract 100mg. Inactive ingredients: Microcrystalline cellulose, magnesium stearate, silicon dioxide.',
                'usage_instructions': 'Take 1-2 tablets every 6-8 hours as needed for pain. Do not exceed 6 tablets in 24 hours. Take with food to reduce stomach irritation. Consult healthcare provider for use beyond 10 days.',
                'creation_method': 'Manufactured using pharmaceutical-grade equipment in GMP-certified facilities. Active ingredients are precisely measured and combined using advanced tablet compression technology.',
                'benefits': 'Provides fast-acting pain relief, reduces inflammation, improves mobility, and enhances quality of life. Effective for headaches, muscle pain, joint pain, and minor injuries.',
                'stock_quantity': 150,
                'featured': True,
            },
            {
                'name': 'CardioSupport Plus',
                'category': 'Cardiovascular Health',
                'price': 45.50,
                'description': 'Premium cardiovascular support supplement designed to promote heart health and maintain healthy blood pressure levels.',
                'composition': 'Coenzyme Q10 100mg, Omega-3 fatty acids 1000mg, Magnesium 200mg, Hawthorn extract 150mg, Garlic extract 100mg.',
                'usage_instructions': 'Take 2 capsules daily with meals. For best results, take consistently at the same time each day. Consult physician before use if taking blood thinners.',
                'creation_method': 'Cold-pressed extraction methods preserve active compounds. Encapsulated in vegetarian capsules using pharmaceutical-grade equipment.',
                'benefits': 'Supports healthy cholesterol levels, promotes circulation, maintains blood pressure within normal range, and provides antioxidant protection for the cardiovascular system.',
                'stock_quantity': 200,
                'featured': True,
            },
            {
                'name': 'DigestEase Pro',
                'category': 'Digestive Health',
                'price': 32.75,
                'description': 'Advanced digestive enzyme complex with probiotics to support optimal digestion and gut health.',
                'composition': 'Digestive enzyme blend 300mg (amylase, protease, lipase), Probiotic blend 10 billion CFU (Lactobacillus, Bifidobacterium), Prebiotic fiber 200mg.',
                'usage_instructions': 'Take 1 capsule with each meal, up to 3 times daily. Store in cool, dry place. Refrigeration recommended after opening.',
                'creation_method': 'Enzymes are derived from plant sources and stabilized using proprietary technology. Probiotics are freeze-dried to maintain viability.',
                'benefits': 'Improves digestion, reduces bloating and gas, supports nutrient absorption, maintains healthy gut flora, and promotes regular bowel movements.',
                'stock_quantity': 120,
                'featured': False,
            },
            {
                'name': 'ImmunoShield Complex',
                'category': 'Immune Support',
                'price': 38.25,
                'description': 'Comprehensive immune system support formula with vitamins, minerals, and herbal extracts.',
                'composition': 'Vitamin C 1000mg, Vitamin D3 2000IU, Zinc 15mg, Elderberry extract 300mg, Echinacea extract 200mg, Astragalus root 150mg.',
                'usage_instructions': 'Take 2 tablets daily with food. During times of increased immune challenge, may increase to 3 tablets daily for up to 7 days.',
                'creation_method': 'Standardized herbal extracts are combined with pharmaceutical-grade vitamins and minerals using advanced coating technology.',
                'benefits': 'Strengthens immune system, reduces duration of seasonal challenges, provides antioxidant protection, and supports overall wellness.',
                'stock_quantity': 180,
                'featured': True,
            },
            {
                'name': 'RespiClear Lung Support',
                'category': 'Respiratory Care',
                'price': 41.00,
                'description': 'Natural respiratory support formula designed to promote clear breathing and lung health.',
                'composition': 'N-Acetyl Cysteine 600mg, Quercetin 250mg, Bromelain 200mg, Mullein leaf extract 150mg, Eucalyptus oil 50mg.',
                'usage_instructions': 'Take 1-2 capsules twice daily between meals. Drink plenty of water. Not recommended for children under 12.',
                'creation_method': 'Herbal extracts are standardized for active compounds and combined with amino acids using gentle processing methods.',
                'benefits': 'Supports respiratory function, promotes clear airways, provides antioxidant protection for lung tissue, and helps maintain comfortable breathing.',
                'stock_quantity': 95,
                'featured': False,
            },
            {
                'name': 'Joint Mobility Formula',
                'category': 'Pain Relief',
                'price': 52.99,
                'description': 'Advanced joint support formula combining glucosamine, chondroitin, and anti-inflammatory compounds.',
                'composition': 'Glucosamine sulfate 1500mg, Chondroitin sulfate 1200mg, MSM 1000mg, Turmeric extract 500mg, Boswellia extract 300mg.',
                'usage_instructions': 'Take 3 capsules daily with meals. Allow 4-6 weeks for optimal benefits. Continue use for sustained joint health.',
                'creation_method': 'Pharmaceutical-grade ingredients are combined using advanced encapsulation technology to ensure stability and bioavailability.',
                'benefits': 'Supports joint flexibility, reduces stiffness, promotes cartilage health, and helps maintain comfortable joint movement.',
                'stock_quantity': 75,
                'featured': True,
            },
            {
                'name': 'Heart Rhythm Support',
                'category': 'Cardiovascular Health',
                'price': 48.75,
                'description': 'Specialized formula to support healthy heart rhythm and electrical conduction.',
                'composition': 'Magnesium glycinate 400mg, Potassium citrate 300mg, Taurine 500mg, L-Carnitine 250mg, Hawthorn berry 200mg.',
                'usage_instructions': 'Take 2 capsules daily, preferably with evening meal. Monitor heart rate if taking cardiac medications.',
                'creation_method': 'Chelated minerals are combined with amino acids using pharmaceutical manufacturing standards.',
                'benefits': 'Supports healthy heart rhythm, promotes electrical stability, maintains mineral balance, and supports overall cardiac function.',
                'stock_quantity': 110,
                'featured': False,
            },
            {
                'name': 'Probiotic Defense',
                'category': 'Digestive Health',
                'price': 35.50,
                'description': 'High-potency probiotic formula with multiple strains for comprehensive digestive and immune support.',
                'composition': '50 billion CFU multi-strain blend: Lactobacillus acidophilus, L. rhamnosus, L. casei, Bifidobacterium longum, B. bifidum, Saccharomyces boulardii.',
                'usage_instructions': 'Take 1 capsule daily on empty stomach or as directed by healthcare provider. Refrigerate after opening.',
                'creation_method': 'Probiotics are freeze-dried using proprietary technology and encapsulated in acid-resistant capsules.',
                'benefits': 'Restores healthy gut flora, supports digestive health, enhances immune function, and promotes nutrient absorption.',
                'stock_quantity': 160,
                'featured': True,
            },
            {
                'name': 'Antioxidant Shield',
                'category': 'Immune Support',
                'price': 42.25,
                'description': 'Powerful antioxidant complex to protect against free radical damage and support cellular health.',
                'composition': 'Alpha-lipoic acid 300mg, Resveratrol 200mg, Green tea extract 150mg, Grape seed extract 100mg, Selenium 200mcg.',
                'usage_instructions': 'Take 1-2 capsules daily with meals. Best taken with healthy fats for optimal absorption.',
                'creation_method': 'Antioxidants are extracted using CO2 methods to preserve potency and combined in light-resistant capsules.',
                'benefits': 'Provides cellular protection, supports healthy aging, enhances immune function, and promotes cardiovascular health.',
                'stock_quantity': 140,
                'featured': False,
            },
            {
                'name': 'Bronchial Comfort',
                'category': 'Respiratory Care',
                'price': 36.99,
                'description': 'Soothing respiratory formula with herbs traditionally used to support bronchial comfort.',
                'composition': 'Ivy leaf extract 300mg, Thyme extract 200mg, Marshmallow root 150mg, Licorice root 100mg, Menthol 25mg.',
                'usage_instructions': 'Take 1 capsule 2-3 times daily. May be taken with warm water or herbal tea for enhanced comfort.',
                'creation_method': 'Traditional herbal extracts are standardized and combined using gentle processing to maintain therapeutic properties.',
                'benefits': 'Soothes respiratory passages, supports comfortable breathing, provides natural expectorant action, and promotes respiratory comfort.',
                'stock_quantity': 85,
                'featured': False,
            },
        ]

        for product_data in products_data:
            category_name = product_data.pop('category')
            product_data['category'] = categories[category_name]
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {Category.objects.count()} categories and {Product.objects.count()} products'
            )
        )