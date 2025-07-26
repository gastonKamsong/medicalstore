from products.models import Product, Category
from django.utils.text import slugify

def create_alien_og():
    product_data = {
        "category_slug": "thc-flower",  # Adjust based on your actual category
        "base_data": {
            "name": "AK-47",
            "price": "210.00",  # Removed € for DecimalField
            "image": "products/ak-47.avif",
            "description": "AK-47 is a legendary sativa-dominant hybrid strain known for its potent cerebral effects and earthy, skunky aroma. Ideal for daytime use, it promotes creativity and euphoria.",
            "composition": "THC: 18-24%, CBD: <1%, Terpenes: Myrcene, Pinene, Caryophyllene",
            "usage_instructions": "Best consumed by smoking or vaporizing. Start with small doses due to its high THC content.",
            "creation_method": "Grown indoors under controlled conditions, hand-trimmed, and slow-cured for optimal flavor.",
            "benefits": "Stress relief, mood enhancement, pain relief, and appetite stimulation.",
            "meta_description": "Premium AK-47 cannabis strain - sativa-dominant hybrid with high THC content.",
            "meta_keywords": "ak47, cannabis, sativa, hybrid, thc, weed, marijuana",
            "is_active": True,
            "featured": True,
            "stock_quantity": 50,
            "strain_type": "sativa",
            "preferred_ratio": "70:30",
            "recommended_methods": ["smoking", "vaporizing"]
        },
        "translations": {
            # Translations for all 11 languages below

            "da": {
                "name": "AK-47",
                "description": "AK-47 er en legendarisk sativa-dominant hybrid med kraftige cerebrale effekter og en jordlig, skunkagtig aroma. Ideel til daglig brug, fremmer kreativitet og eufori.",
                "composition": "THC: 18-24%, CBD: <1%, Terpener: Myrcen, Pinen, Caryophyllen",
                "usage_instructions": "Bedst nydt ved rygning eller fordampning. Start med små doser på grund af høj THC-indhold.",
                "creation_method": "Dyrket indendørs under kontrollerede forhold, håndklippet og langsomt tørret for optimal smag.",
                "benefits": "Stressreduktion, humørforbedring, smertelindring og appetitstimulering.",
                "meta_description": "Premium AK-47 cannabis - sativa-dominant hybrid med højt THC-indhold.",
                "meta_keywords": "ak47, cannabis, sativa, hybrid, thc, hash, marihuana"
            },
            "fi": {
                "name": "AK-47",
                "description": "AK-47 on legendaarinen sativa-valtainen hybridikannabis, joka tunnetaan voimakkaista mielialaa parantavista vaikutuksistaan ja maankaltaisesta, skunkin tuoksusta. Sopii päiväkäyttöön, edistää luovuutta ja euforiaa.",
                "composition": "THC: 18-24%, CBD: <1%, Terpeenit: Myrseeni, Pineeni, Karyofylleeni",
                "usage_instructions": "Parhaiten nautittuna polttamalla tai höyrystämällä. Aloita pienillä annoksilla korkean THC-pitoisuuden vuoksi.",
                "creation_method": "Viljelty sisätiloissa hallituissa olosuhteissa, käsileikattu ja hitaasti kuivattu optimaalisen maun saavuttamiseksi.",
                "benefits": "Stressin lievitys, mielialan parantaminen, kivun lievitys ja ruokahalun lisääntyminen.",
                "meta_description": "Premium AK-47 kannabis - sativa-valtainen hybridi, jossa on korkea THC-pitoisuus.",
                "meta_keywords": "ak47, kannabis, sativa, hybridi, thc, pilvi, marihuana"
            },
            "fr": {
                "name": "AK-47",
                "description": "L'AK-47 est une variété hybride légendaire à dominance sativa, connue pour ses effets cérébraux puissants et son arôme terreux et skunk. Idéale pour une utilisation diurne, elle favorise la créativité et l'euphorie.",
                "composition": "THC: 18-24%, CBD: <1%, Terpènes: Myrcène, Pinène, Caryophyllène",
                "usage_instructions": "À consommer de préférence en fumant ou en vaporisant. Commencez par de petites doses en raison de sa forte teneur en THC.",
                "creation_method": "Cultivé en intérieur dans des conditions contrôlées, taillé à la main et séché lentement pour un goût optimal.",
                "benefits": "Soulagement du stress, amélioration de l'humeur, réduction de la douleur et stimulation de l'appétit.",
                "meta_description": "Variété premium AK-47 - hybride à dominance sativa avec une forte teneur en THC.",
                "meta_keywords": "ak47, cannabis, sativa, hybride, thc, weed, marijuana"
            },
            "de": {
                "name": "AK-47",
                "description": "AK-47 ist eine legendäre, sativa-dominante Hybride, bekannt für ihre starken zerebralen Effekte und erdig-skunkigen Aromen. Ideal für den Tagesgebrauch, fördert Kreativität und Euphorie.",
                "composition": "THC: 18-24%, CBD: <1%, Terpene: Myrcen, Pinen, Caryophyllen",
                "usage_instructions": "Am besten durch Rauchen oder Verdampfen konsumieren. Wegen des hohen THC-Gehalts mit kleinen Dosen beginnen.",
                "creation_method": "Unter kontrollierten Bedingungen indoor angebaut, handbeschnitten und langsam getrocknet für optimalen Geschmack.",
                "benefits": "Stressabbau, Stimmungsaufhellung, Schmerzlinderung und Appetitanregung.",
                "meta_description": "Premium AK-47 Cannabis - sativa-dominante Hybride mit hohem THC-Gehalt.",
                "meta_keywords": "ak47, cannabis, sativa, hybrid, thc, gras, marihuana"
            },
            "it": {
                "name": "AK-47",
                "description": "L'AK-47 è una leggendaria varietà ibrida a predominanza sativa, nota per i suoi potenti effetti cerebrali e l'aroma terroso e pungente. Ideale per l'uso diurno, promuove creatività ed euforia.",
                "composition": "THC: 18-24%, CBD: <1%, Terpeni: Mircene, Pinene, Caryofillene",
                "usage_instructions": "Si consiglia di fumare o vaporizzare. Iniziare con piccole dosi a causa dell'alto contenuto di THC.",
                "creation_method": "Coltivata indoor in condizioni controllate, tagliata a mano ed essiccata lentamente per un sapore ottimale.",
                "benefits": "Riduzione dello stress, miglioramento dell'umore, sollievo dal dolore e stimolazione dell'appetito.",
                "meta_description": "Varietà premium AK-47 - ibrido a predominanza sativa con alto contenuto di THC.",
                "meta_keywords": "ak47, cannabis, sativa, ibrido, thc, erba, marijuana"
            },
            "hu": {
                "name": "AK-47",
                "description": "Az AK-47 egy legendás sativa-domináns hibrid törzs, erős mentális hatásokkal és földes, skunkszerű aromával. Ideális nappali használatra, kreativitást és eufóriát elősegít.",
                "composition": "THC: 18-24%, CBD: <1%, Terpének: Mircén, Pinén, Kariofillén",
                "usage_instructions": "Legjobb dohányzással vagy párologtatással fogyasztani. Kezdje kis adagokkal a magas THC-tartalom miatt.",
                "creation_method": "Beltéri körülmények között termesztve, kézzel nyesve és lassan szárítva az optimális íz érdekében.",
                "benefits": "Stresszcsökkentés, hangulatjavítás, fájdalomcsillapítás és étvágygerjesztés.",
                "meta_description": "Prémium AK-47 kannabisz - sativa-domináns hibrid magas THC-tartalommal.",
                "meta_keywords": "ak47, kannabisz, sativa, hibrid, thc, weed, marihuána"
            },
            "no": {
                "name": "AK-47",
                "description": "AK-47 er en legendarisk sativa-dominant hybrid med potente mentale effekter og en jordlig, skunkaktig aroma. Ideell for daglig bruk, fremmer kreativitet og eufori.",
                "composition": "THC: 18-24%, CBD: <1%, Terpener: Myrcen, Pinen, Caryofylleen",
                "usage_instructions": "Best nytes ved røyking eller fordamping. Begynn med små doser på grunn av høyt THC-innhold.",
                "creation_method": "Dyrket innendørs under kontrollerte forhold, håndklippet og langsomt tørket for optimal smak.",
                "benefits": "Stressreduksjon, humørforbedring, smertelindring og appetittstimulering.",
                "meta_description": "Premium AK-47 cannabis - sativa-dominant hybrid med høyt THC-innhold.",
                "meta_keywords": "ak47, cannabis, sativa, hybrid, thc, weed, marihuana"
            },
            "ga": {
                "name": "AK-47",
                "description": "Is cineál hibrideach sativa-dominantach é AK-47 atá cáiliúil as a éifeachtaí láidre inchinne agus a aromach cré-úil. Ideálta le húsáid san iarnóin, cothaíonn sé cruthaitheacht agus eofóra.",
                "composition": "THC: 18-24%, CBD: <1%, Teirpíní: Myrcene, Pinene, Caryophyllene",
                "usage_instructions": "Is fearr é a ithe trí chaitheamh nó galú. Tosaigh le dáileoga beaga mar gheall ar an ard-tháirge THC.",
                "creation_method": "Á fhás faoi dhion faoi choinníollacha rialaithe, gearrtha de láimh agus triomaithe go mall le haghaidh blas is fearr.",
                "benefits": "Faoiseamh strus, feabhsú meoin, faoiseamh pian agus spreagadh goile.",
                "meta_description": "Cannabis AK-47 premium - hibrideach sativa-dominantach le ard-tháirge THC.",
                "meta_keywords": "ak47, cannabis, sativa, hibrideach, thc, féar, marijuana"
            },
            "es": {
                "name": "AK-47",
                "description": "AK-47 es una cepa híbrida legendaria dominante en sativa, conocida por sus potentes efectos cerebrales y aroma terroso y skunk. Ideal para uso diurno, promueve la creatividad y la euforia.",
                "composition": "THC: 18-24%, CBD: <1%, Terpenos: Mirceno, Pineno, Caryofileno",
                "usage_instructions": "Se recomienda fumar o vaporizar. Comience con dosis pequeñas debido a su alto contenido de THC.",
                "creation_method": "Cultivado en interiores en condiciones controladas, recortado a mano y secado lentamente para un sabor óptimo.",
                "benefits": "Alivio del estrés, mejora del estado de ánimo, alivio del dolor y estimulación del apetito.",
                "meta_description": "AK-47 premium - híbrido dominante en sativa con alto contenido de THC.",
                "meta_keywords": "ak47, cannabis, sativa, híbrido, thc, marihuana, hierba"
            },
            "sv": {
                "name": "AK-47",
                "description": "AK-47 är en legendarisk sativa-dominant hybridstam känd för sina potenta mentala effekter och jordiga, skunkaktiga arom. Idealisk för daglig användning, främjar kreativitet och eufori.",
                "composition": "THC: 18-24%, CBD: <1%, Terpener: Myrcen, Pinen, Caryofylleen",
                "usage_instructions": "Bäst att njuta av genom rökning eller förångning. Börja med små doser på grund av högt THC-innehåll.",
                "creation_method": "Odlas inomhus under kontrollerade förhållanden, handklippt och långsamt torkat för optimal smak.",
                "benefits": "Stresslindring, humörförbättring, smärtlindring och aptitstimulering.",
                "meta_description": "Premium AK-47 cannabis - sativa-dominant hybrid med högt THC-innehåll.",
                "meta_keywords": "ak47, cannabis, sativa, hybrid, thc, gräs, marijuana"
            },
        }
    }

    try:
        category = Category.objects.get(slug=product_data["category_slug"])
    except Category.DoesNotExist:
        print("Error: Category not found!")
        return

    # Create base product
    product = Product(**product_data["base_data"], category=category)
    product.save()

    # Add translations (assuming django-parler)
    for lang_code, trans in product_data["translations"].items():
        product.translations.create(
            language_code=lang_code,
            **trans
        )
    print(f"Successfully created Alien OG in 11 languages!")

# Execute
create_alien_og()