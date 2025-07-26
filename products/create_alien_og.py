from products.models import Product, Category
from django.utils.text import slugify

products_data = [
    {
        "name": "Apple Jack",
        "price": 235.00,
        "image": "products/apple-jack.webp",
        "category_slug": "thc-flower",
        "description": {
            'en': "A perfectly balanced hybrid with sweet apple flavors and relaxing effects.",
            'da': "En perfekt balanceret hybrid med søde æblesmag og afslappende effekter.",
            'fi': "Täydellisesti tasapainotettu hybridi, jossa on makea omenamaku ja rentouttava vaikutus.",
            'fr': "Un hybride parfaitement équilibré avec des saveurs de pomme douce et des effets relaxants.",
            'de': "Ein perfekt ausgewogener Hybrid mit süßem Apfelgeschmack und entspannender Wirkung.",
            'it': "Un ibrido perfettamente bilanciato con sapori dolci di mela ed effetti rilassanti.",
            'hu': "Tökéletesen kiegyensúlyozott hibrid, édes alma ízekkel és lazító hatásokkal.",
            'no': "En perfekt balansert hybrid med søt eplesmak og avslappende effekter.",
            'ga': "Hibrideach foirfe cothromaithe le blasanna milis úll agus éifeachtaí scíth a ligeann.",
            'es': "Un híbrido perfectamente equilibrado con sabores dulces de manzana y efectos relajantes.",
            'sv': "En perfekt balanserad hybrid med söt äppelsmak och avslappnande effekter."
        },
        "composition": {
            'en': "THC: 18-22%, CBD: <1%, Terpenes: Myrcene, Pinene, Caryophyllene",
            'da': "THC: 18-22%, CBD: <1%, Terpener: Myrcen, Pinen, Caryophyllen",
            'fi': "THC: 18-22%, CBD: <1%, Terpeenit: Myrseeni, Pineeni, Karyofylleeni",
            'fr': "THC : 18-22 %, CBD : <1 %, Terpènes : Myrcène, Pinène, Caryophyllène",
            'de': "THC: 18-22%, CBD: <1%, Terpene: Myrcen, Pinen, Caryophyllen",
            'it': "THC: 18-22%, CBD: <1%, Terpeni: Mircene, Pinene, Caryophyllene",
            'hu': "THC: 18-22%, CBD: <1%, Terpének: Mircén, Pinén, Cariofillén",
            'no': "THC: 18-22%, CBD: <1%, Terpener: Myrcen, Pinen, Caryophyllen",
            'ga': "THC: 18-22%, CBD: <1%, Terpéin: Myrcene, Pinene, Caryophyllene",
            'es': "THC: 18-22%, CBD: <1%, Terpenos: Mirceno, Pineno, Caryofileno",
            'sv': "THC: 18-22%, CBD: <1%, Terpener: Myrcen, Pinen, Caryofylleen"
        },
        "usage_instructions": {
            'en': "Start with small doses. Smoke or vaporize. Effects appear within minutes.",
            'da': "Start med små doser. Ryg eller fordampe. Virkningen viser sig inden for få minutter.",
            'fi': "Aloita pienillä annoksilla. Polta tai höyrystä. Vaikutukset ilmenevät minuuteissa.",
            'fr': "Commencez par de petites doses. Fumez ou vaporisez. Les effets apparaissent en quelques minutes.",
            'de': "Beginnen Sie mit kleinen Dosen. Rauchen oder verdampfen. Die Wirkung setzt innerhalb von Minuten ein.",
            'it': "Iniziare con piccole dosi. Fumare o vaporizzare. Gli effetti compaiono entro pochi minuti.",
            'hu': "Kezdje kis adagokkal. Dohányozzon vagy párologtasson. A hatás perceken belül megjelenik.",
            'no': "Start med små doser. Røyk eller fordampe. Virkningen vises innen få minutter.",
            'ga': "Tosaigh le dáileoga beaga. Deataigh nó galú. Feictear na héifeachtaí laistigh de nóiméid.",
            'es': "Comience con pequeñas dosis. Fumar o vaporizar. Los efectos aparecen en minutos.",
            'sv': "Börja med små doser. Rök eller förånga. Effekterna visas inom minuter."
        },
        "creation_method": {
            'en': "Indoor grown using organic methods, hand-trimmed, slow-cured for optimal flavor.",
            'da': "Dyrket inde ved hjælp af økologiske metoder, håndtrimmet, langsomt hærdet for optimal smag.",
            'fi': "Sisäkasvatettu orgaanisin menetelmin, käsinleikattu, hitaasti paranneltu optimaalisen maun saavuttamiseksi.",
            'fr': "Cultivé en intérieur selon des méthodes biologiques, taillé à la main, séché lentement pour une saveur optimale.",
            'de': "Im Innenbereich mit biologischen Methoden angebaut, von Hand getrimmt, langsam ausgehärtet für optimalen Geschmack.",
            'it': "Coltivato al chiuso con metodi biologici, tagliato a mano, stagionato lentamente per un sapore ottimale.",
            'hu': "Fedél alatt termesztett biológiai módszerekkel, kézzel nyesve, lassan érlelt az optimális ízért.",
            'no': "Innendørs dyrket ved hjelp av økologiske metoder, håndklippet, sakte herdet for optimal smak.",
            'ga': "Ar fáil faoi thalamh ag baint úsáide as modhanna orgánacha, lámh-bearrtha, leigheas go mall le haghaidh blas is fearr.",
            'es': "Cultivado en interiores con métodos orgánicos, recortado a mano, curado lentamente para un sabor óptimo.",
            'sv': "Odlas inomhus med organiska metoder, handtrimmas, långsamt härdas för optimal smak."
        },
        "benefits": {
            'en': "Relieves stress, enhances mood, may help with mild pain and insomnia.",
            'da': "Lindrer stress, forbedrer humøret, kan hjælpe ved mild smerte og søvnløshed.",
            'fi': "Lieventää stressiä, parantaa mielialaa, voi auttaa lievään kipuun ja unettomuuteen.",
            'fr': "Soulage le stress, améliore l'humeur, peut aider contre les douleurs légères et l'insomnie.",
            'de': "Lindert Stress, verbessert die Stimmung, kann bei leichten Schmerzen und Schlaflosigkeit helfen.",
            'it': "Allevia lo stress, migliora l'umore, può aiutare con il dolore lieve e l'insonnia.",
            'hu': "Stressz csökkentés, hangulatjavítás, enyhe fájdalom és álmatlanság esetén segíthet.",
            'no': "Lindrer stress, forbedrer humøret, kan hjelpe ved mild smerte og søvnløshet.",
            'ga': "Faigheann sé faoiseamh ó strus, feabhsaíonn sé an giúmar, d'fhéadfadh cabhrú le pian éadrom agus néaltrú.",
            'es': "Alivia el estrés, mejora el estado de ánimo, puede ayudar con el dolor leve y el insomnio.",
            'sv': "Lindrar stress, förbättrar humöret, kan hjälpa vid mild smärta och sömnlöshet."
        },
        "meta_description": {
            'en': "Premium Apple Jack hybrid cannabis with sweet apple flavors and balanced effects.",
            'da': "Premium Apple Jack hybrid cannabis med søde æblesmag og afbalanceret virkning.",
            'fi': "Premium Apple Jack hybridi kannabis, jossa on makea omenamaku ja tasapainoiset vaikutukset.",
            'fr': "Cannabis hybride Apple Jack premium avec des saveurs de pomme douce et des effets équilibrés.",
            'de': "Premium Apple Jack Hybrid-Cannabis mit süßem Apfelgeschmack und ausgewogener Wirkung.",
            'it': "Cannabis ibrido Apple Jack premium con sapori dolci di mela ed effetti bilanciati.",
            'hu': "Prémium Apple Jack hibrid kannabisz édes alma ízekkel és kiegyensúlyozott hatásokkal.",
            'no': "Premium Apple Jack hybrid cannabis med søt eplesmak og balansert virkning.",
            'ga': "Cannabis hibrideach Apple Jack premium le blasanna milis úll agus éifeachtaí cothromaithe.",
            'es': "Cannabis híbrido Apple Jack premium con sabores dulces de manzana y efectos equilibrados.",
            'sv': "Premium Apple Jack hybrid cannabis med söt äppelsmak och balanserad effekt."
        },
        "meta_keywords": {
            'en': "apple jack, hybrid cannabis, premium weed, organic, thc",
            'da': "apple jack, hybrid cannabis, premium weed, økologisk, thc",
            'fi': "apple jack, hybridi kannabis, premium weed, orgaaninen, thc",
            'fr': "apple jack, cannabis hybride, weed premium, biologique, thc",
            'de': "apple jack, hybrid cannabis, premium weed, bio, thc",
            'it': "apple jack, cannabis ibrido, erba premium, biologico, thc",
            'hu': "apple jack, hibrid kannabisz, prémium weed, organikus, thc",
            'no': "apple jack, hybrid cannabis, premium weed, økologisk, thc",
            'ga': "apple jack, cannabis hibrideach, premium weed, orgánach, thc",
            'es': "apple jack, cannabis híbrido, hierba premium, orgánico, thc",
            'sv': "apple jack, hybrid cannabis, premium weed, ekologisk, thc"
        },
        "strain_type": "hybrid",
        "preferred_ratio": "1:1",
        "recommended_methods": ["flower", "vape"],
        "is_active": True,
        "featured": True,
        "stock_quantity": 100,
        "translations": {
            'da': {'name': "Apple Jack"},
            'fi': {'name': "Apple Jack"},
            'fr': {'name': "Apple Jack"},
            'de': {'name': "Apple Jack"},
            'it': {'name': "Apple Jack"},
            'hu': {'name': "Apple Jack"},
            'no': {'name': "Apple Jack"},
            'ga': {'name': "Apple Jack"},
            'es': {'name': "Apple Jack"},
            'sv': {'name': "Apple Jack"}
        }
    },
    {
        "name": "Banana Kush",
        "price": 250.00,
        "image": "products/banana-kush.avif",
        "category_slug": "thc-flower",
        "description": {
            'en': "A potent indica strain with sweet banana aroma and deep relaxation effects.",
            'da': "En potent indica-stamme med sød bananaroma og dyb afslapningseffekt.",
            'fi': "Voimakas indica-kanta, jossa on makea banaanin tuoksu ja syvä rentouttava vaikutus.",
            'fr': "Une puissante variété indica avec un arôme sucré de banane et des effets de relaxation profonde.",
            'de': "Eine starke Indica-Sorte mit süßem Bananenaroma und tiefen Entspannungseffekten.",
            'it': "Una potente varietà indica con aroma dolce di banana ed effetti di profondo rilassamento.",
            'hu': "Erős indica törzs, édes banán aromával és mély relaxáló hatásokkal.",
            'no': "En potent indica-stamme med søt bananaroma og dyp avslappingseffekt.",
            'ga': "Cineál láidir indica le cumhra bánáin milis agus éifeachtaí domhaine scíth a ligeann.",
            'es': "Una potente cepa índica con aroma dulce a plátano y efectos de relajación profunda.",
            'sv': "En potent indica-stam med söt bananarom och djup avslappnande effekt."
        },
        "composition": {
            'en': "THC: 20-24%, CBD: <0.5%, Terpenes: Limonene, Myrcene, Linalool",
            'da': "THC: 20-24%, CBD: <0.5%, Terpener: Limonen, Myrcen, Linalool",
            'fi': "THC: 20-24%, CBD: <0.5%, Terpeenit: Limoneeni, Myrseeni, Linalooli",
            'fr': "THC : 20-24 %, CBD : <0,5 %, Terpènes : Limonène, Myrcène, Linalol",
            'de': "THC: 20-24%, CBD: <0.5%, Terpene: Limonen, Myrcen, Linalool",
            'it': "THC: 20-24%, CBD: <0.5%, Terpeni: Limonene, Mircene, Linalolo",
            'hu': "THC: 20-24%, CBD: <0.5%, Terpének: Limonén, Mircén, Linalool",
            'no': "THC: 20-24%, CBD: <0.5%, Terpener: Limonen, Myrcen, Linalool",
            'ga': "THC: 20-24%, CBD: <0.5%, Terpéin: Limonene, Myrcene, Linalool",
            'es': "THC: 20-24%, CBD: <0.5%, Terpenos: Limoneno, Mirceno, Linalool",
            'sv': "THC: 20-24%, CBD: <0.5%, Terpener: Limonen, Myrcen, Linalool"
        },
        "usage_instructions": {
            'en': "Best for evening use. Start with small amounts. Smoke or vaporize.",
            'da': "Bedst til aftenbrug. Start med små mængder. Ryg eller fordampe.",
            'fi': "Parhaimmillaan illalla käytettäväksi. Aloita pienillä määrillä. Polta tai höyrystä.",
            'fr': "Idéal pour une utilisation en soirée. Commencez par de petites quantités. Fumez ou vaporisez.",
            'de': "Am besten für den abendlichen Gebrauch. Beginnen Sie mit kleinen Mengen. Rauchen oder verdampfen.",
            'it': "Ideale per l'uso serale. Iniziare con piccole quantità. Fumare o vaporizzare.",
            'hu': "Legjobb esti használatra. Kezdje kis mennyiséggel. Dohányozzon vagy párologtasson.",
            'no': "Best til kveldstid. Start med små mengder. Røyk eller fordampe.",
            'ga': "Is fearr le haghaidh úsáide tráthnóna. Tosaigh le méideanna beaga. Deataigh nó galú.",
            'es': "Ideal para uso nocturno. Comience con pequeñas cantidades. Fumar o vaporizar.",
            'sv': "Bäst för kvällsbruk. Börja med små mängder. Rök eller förånga."
        },
        "creation_method": {
            'en': "Organic soil grown, hand-harvested, slow-dried to preserve terpenes.",
            'da': "Økologisk jorddyrkning, håndhøstet, langsomt tørret for at bevare terpenerne.",
            'fi': "Luomumaaperä kasvatettu, käsin korjattu, hitaasti kuivattu terpeenien säilyttämiseksi.",
            'fr': "Cultivé en terreau biologique, récolté à la main, séché lentement pour préserver les terpènes.",
            'de': "Biologisch im Boden angebaut, von Hand geerntet, langsam getrocknet, um Terpene zu erhalten.",
            'it': "Coltivato in terreno biologico, raccolto a mano, essiccato lentamente per preservare i terpeni.",
            'hu': "Organikus talajban termesztett, kézzel betakarított, lassan szárított a terpének megőrzése érdekében.",
            'no': "Økologisk jorddyrket, håndhøstet, sakte tørket for å bevare terpenene.",
            'ga': "Ar fáil i ithir orgánach, bainte de láimh, triomaithe go mall chun terpéin a chaomhnú.",
            'es': "Cultivado en suelo orgánico, cosechado a mano, secado lentamente para preservar terpenos.",
            'sv': "Ekologisk jordodling, handskördad, långsamt torkad för att bevara terpenerna."
        },
        "benefits": {
            'en': "Promotes deep relaxation, helps with insomnia, may relieve muscle tension.",
            'da': "Fremmer dyb afslapning, hjælper ved søvnløshed, kan lindre muskelspændinger.",
            'fi': "Edistää syvää rentoutumista, auttaa unettomuuteen, voi lievittää lihasjännitystä.",
            'fr': "Favorise une relaxation profonde, aide contre l'insomnie, peut soulager les tensions musculaires.",
            'de': "Fördert tiefe Entspannung, hilft bei Schlaflosigkeit, kann Muskelverspannungen lindern.",
            'it': "Promuove il rilassamento profondo, aiuta con l'insonnia, può alleviare la tensione muscolare.",
            'hu': "Elősegíti a mély relaxációt, segít az álmatlanság ellen, enyhítheti az izomfeszültséget.",
            'no': "Fremmer dyp avslapning, hjelper ved søvnløshet, kan lindre muskelspenninger.",
            'ga': "Cothaíonn sé scíth dhomhain, cabhraíonn sé le néaltrú, d'fhéadfadh fáil réidh le teannas matáin.",
            'es': "Promueve relajación profunda, ayuda con el insomnio, puede aliviar la tensión muscular.",
            'sv': "Främjar djup avslappning, hjälper vid sömnlöshet, kan lindra muskelspänningar."
        },
        "meta_description": {
            'en': "Premium Banana Kush indica with sweet tropical aroma and relaxing effects.",
            'da': "Premium Banana Kush indica med sød tropisk aroma og afslappende virkning.",
            'fi': "Premium Banana Kush indica makealla trooppisella aromilla ja rentouttavilla vaikutuksilla.",
            'fr': "Indica Banana Kush premium avec un arôme tropical sucré et des effets relaxants.",
            'de': "Premium Banana Kush Indica mit süßem tropischem Aroma und entspannender Wirkung.",
            'it': "Indica Banana Kush premium con aroma tropicale dolce ed effetti rilassanti.",
            'hu': "Prémium Banana Kush indica édes trópusi aromával és lazító hatásokkal.",
            'no': "Premium Banana Kush indica med søt tropisk aroma og avslappende virkning.",
            'ga': "Indica Banana Kush premium le cumhra trópaiceach milis agus éifeachtaí scíth a ligeann.",
            'es': "Índica Banana Kush premium con aroma tropical dulce y efectos relajantes.",
            'sv': "Premium Banana Kush indica med söt tropisk arom och avslappnande effekt."
        },
        "meta_keywords": {
            'en': "banana kush, indica, tropical strain, relaxing, thc",
            'da': "banana kush, indica, tropisk stamme, afslappende, thc",
            'fi': "banana kush, indica, trooppinen kanta, rentouttava, thc",
            'fr': "banana kush, indica, variété tropicale, relaxant, thc",
            'de': "banana kush, indica, tropische sorte, entspannend, thc",
            'it': "banana kush, indica, varietà tropicale, rilassante, thc",
            'hu': "banana kush, indica, trópusi törzs, relaxáló, thc",
            'no': "banana kush, indica, tropisk stamme, avslappende, thc",
            'ga': "banana kush, indica, cineál trópaiceach, scíth a ligeann, thc",
            'es': "banana kush, índica, cepa tropical, relajante, thc",
            'sv': "banana kush, indica, tropisk stam, avslappande, thc"
        },
        "strain_type": "indica",
        "preferred_ratio": "1:2",
        "recommended_methods": ["flower", "edible"],
        "is_active": True,
        "featured": True,
        "stock_quantity": 85,
        "translations": {
            'da': {'name': "Banana Kush"},
            'fi': {'name': "Banana Kush"},
            'fr': {'name': "Banana Kush"},
            'de': {'name': "Banana Kush"},
            'it': {'name': "Banana Kush"},
            'hu': {'name': "Banana Kush"},
            'no': {'name': "Banana Kush"},
            'ga': {'name': "Banana Kush"},
            'es': {'name': "Banana Kush"},
            'sv': {'name': "Banana Kush"}
        }
    },
    {
        "name": "Bio-Jesus Hybrid Weed",
        "price": 235.00,
        "image": "products/bio-jesus-hybrid-weed.webp",
        "category_slug": "thc-flower",
        "description": {
            'en': "A spiritual hybrid experience with earthy flavors and balanced effects.",
            'da': "En spirituel hybridoplevelse med jordagtige smage og afbalanceret virkning.",
            'fi': "Henkinen hybridikokema maanläheisillä mauilla ja tasapainoisilla vaikutuksilla.",
            'fr': "Une expérience hybride spirituelle avec des saveurs terreuses et des effets équilibrés.",
            'de': "Eine spirituelle Hybrid-Erfahrung mit erdigen Aromen und ausgewogener Wirkung.",
            'it': "Un'esperienza ibrida spirituale con sapori terrosi ed effetti bilanciati.",
            'hu': "Lelki hibrid élmény földes ízekkel és kiegyensúlyozott hatásokkal.",
            'no': "En spirituell hybridopplevelse med jordaktige smaker og balansert virkning.",
            'ga': "Taithí hibrideach spioradálta le blasanna cré-úire agus éifeachtaí cothromaithe.",
            'es': "Una experiencia híbrida espiritual con sabores terrosos y efectos equilibrados.",
            'sv': "En spirituell hybridupplevelse med jordiga smaker och balanserad effekt."
        },
        "composition": {
            'en': "THC: 16-20%, CBD: 1-2%, Terpenes: Pinene, Humulene, Terpinolene",
            'da': "THC: 16-20%, CBD: 1-2%, Terpener: Pinen, Humulen, Terpinolen",
            'fi': "THC: 16-20%, CBD: 1-2%, Terpeenit: Pineeni, Humuleeni, Terpinoleeni",
            'fr': "THC : 16-20 %, CBD : 1-2 %, Terpènes : Pinène, Humulène, Terpinolène",
            'de': "THC: 16-20%, CBD: 1-2%, Terpene: Pinen, Humulen, Terpinolen",
            'it': "THC: 16-20%, CBD: 1-2%, Terpeni: Pinene, Humulene, Terpinolene",
            'hu': "THC: 16-20%, CBD: 1-2%, Terpének: Pinén, Humulén, Terpinolén",
            'no': "THC: 16-20%, CBD: 1-2%, Terpener: Pinen, Humulen, Terpinolen",
            'ga': "THC: 16-20%, CBD: 1-2%, Terpéin: Pinene, Humulene, Terpinolene",
            'es': "THC: 16-20%, CBD: 1-2%, Terpenos: Pineno, Humuleno, Terpinoleno",
            'sv': "THC: 16-20%, CBD: 1-2%, Terpener: Pinen, Humulen, Terpinolen"
        },
        "usage_instructions": {
            'en': "Ideal for meditation or creative activities. Use moderately.",
            'da': "Ideel til meditation eller kreative aktiviteter. Brug moderat.",
            'fi': "Ihanteellinen meditaatioon tai luoviin aktiviteetteihin. Käytä kohtuudella.",
            'fr': "Idéal pour la méditation ou les activités créatives. À utiliser avec modération.",
            'de': "Ideal für Meditation oder kreative Aktivitäten. In Maßen verwenden.",
            'it': "Ideale per la meditazione o le attività creative. Usare con moderazione.",
            'hu': "Ideális meditációhoz vagy kreatív tevékenységekhez. Használja mérsékeltan.",
            'no': "Ideell til meditasjon eller kreative aktiviteter. Bruk med måte.",
            'ga': "Ideálach le haghaidh machnaimh nó gníomhaíochtaí cruthaitheacha. Úsáid go measartha.",
            'es': "Ideal para meditación o actividades creativas. Usar con moderación.",
            'sv': "Ideellt för meditation eller kreativa aktiviteter. Använd med måtta."
        },
        "creation_method": {
            'en': "Biodynamically grown, sun-cured, hand-processed with spiritual intention.",
            'da': "Biodynamisk dyrket, solhærdet, håndbearbejdet med spirituel intention.",
            'fi': "Biodynaamisesti kasvatettu, aurinkokäsitelty, käsinkäsitelty hengellisellä tarkoituksella.",
            'fr': "Cultivé en biodynamie, séché au soleil, transformé à la main avec une intention spirituelle.",
            'de': "Biodynamisch angebaut, sonnengetrocknet, handverarbeitet mit spiritueller Absicht.",
            'it': "Coltivato biodinamicamente, essiccato al sole, lavorato a mano con intenzione spirituale.",
            'hu': "Biodinamikusan termesztett, napon szárított, kézzel feldolgozott spirituális szándékkal.",
            'no': "Biodynamisk dyrket, solherdet, håndverket med spirituell intensjon.",
            'ga': "Ar fáil go bithdinimiciúil, leigheas gréine, próiseáilte de láimh le hintinn spioradálta.",
            'es': "Cultivado biodinámicamente, curado al sol, procesado a mano con intención espiritual.",
            'sv': "Biodynamiskt odlad, solhärdad, handbearbetad med spirituell avsikt."
        },
        "benefits": {
            'en': "Enhances mindfulness, promotes spiritual connection, may help with mild anxiety.",
            'da': "Forbedrer opmærksomhed, fremmer spirituel forbindelse, kan hjælpe ved mild angst.",
            'fi': "Parantaa tietoisuutta, edistää henkistä yhteyttä, voi auttaa lievään ahdistukseen.",
            'fr': "Améliore la pleine conscience, favorise la connexion spirituelle, peut aider contre l'anxiété légère.",
            'de': "Fördert Achtsamkeit, stärkt die spirituelle Verbindung, kann bei leichter Angst helfen.",
            'it': "Migliora la consapevolezza, promuove la connessione spirituale, può aiutare con lieve ansia.",
            'hu': "Fokozza a tudatosságot, elősegíti a spirituális kapcsolatot, segíthet enyhe szorongás esetén.",
            'no': "Forbedrer oppmerksomhet, fremmer spirituell tilknytning, kan hjelpe ved mild angst.",
            'ga': "Feabhsaíonn sé aird, cothaíonn sé nasc spioradálta, d'fhéadfadh cabhrú le himní éadrom.",
            'es': "Mejora la atención plena, promueve conexión espiritual, puede ayudar con ansiedad leve.",
            'sv': "Främjar mindfulness, främjar andlig förbindelse, kan hjälpa vid mild ångest."
        },
        "meta_description": {
            'en': "Bio-Jesus hybrid cannabis for spiritual experiences with earthy flavors.",
            'da': "Bio-Jesus hybrid cannabis til spirituelle oplevelser med jordagtige smage.",
            'fi': "Bio-Jesus hybridikannabis henkisiin kokemuksiin maanläheisillä mauilla.",
            'fr': "Cannabis hybride Bio-Jesus pour des expériences spirituelles avec des saveurs terreuses.",
            'de': "Bio-Jesus Hybrid-Cannabis für spirituelle Erfahrungen mit erdigen Aromen.",
            'it': "Cannabis ibrido Bio-Jesus per esperienze spirituali con sapori terrosi.",
            'hu': "Bio-Jesus hibrid kannabisz spirituális élményekhez földes ízekkel.",
            'no': "Bio-Jesus hybrid cannabis for spirituelle opplevelser med jordaktige smaker.",
            'ga': "Cannabis hibrideach Bio-Jesus le haghaidh eispéiris spioradálta le blasanna cré-úire.",
            'es': "Cannabis híbrido Bio-Jesús para experiencias espirituales con sabores terrosos.",
            'sv': "Bio-Jesus hybrid cannabis för andliga upplevelser med jordiga smaker."
        },
        "meta_keywords": {
            'en': "bio jesus, hybrid, spiritual, earthy, thc",
            'da': "bio jesus, hybrid, spirituel, jordagtig, thc",
            'fi': "bio jesus, hybridi, henkinen, maanläheinen, thc",
            'fr': "bio jesus, hybride, spirituel, terreux, thc",
            'de': "bio jesus, hybrid, spirituell, erdig, thc",
            'it': "bio jesus, ibrido, spirituale, terroso, thc",
            'hu': "bio jesus, hibrid, spirituális, földes, thc",
            'no': "bio jesus, hybrid, spirituell, jordaktig, thc",
            'ga': "bio jesus, hibrideach, spioradálta, cré-úir, thc",
            'es': "bio jesus, híbrido, espiritual, terroso, thc",
            'sv': "bio jesus, hybrid, andlig, jordig, thc"
        },
        "strain_type": "hybrid",
        "preferred_ratio": "1:1",
        "recommended_methods": ["flower", "oil"],
        "is_active": True,
        "featured": False,
        "stock_quantity": 60,
        "translations": {
            'da': {'name': "Bio-Jesus Hybrid Weed"},
            'fi': {'name': "Bio-Jesus Hybrid Weed"},
            'fr': {'name': "Bio-Jesus Hybrid Weed"},
            'de': {'name': "Bio-Jesus Hybrid Weed"},
            'it': {'name': "Bio-Jesus Hybrid Weed"},
            'hu': {'name': "Bio-Jesus Hybrid Weed"},
            'no': {'name': "Bio-Jesus Hybrid Weed"},
            'ga': {'name': "Bio-Jesus Hybrid Weed"},
            'es': {'name': "Bio-Jesus Hybrid Weed"},
            'sv': {'name': "Bio-Jesus Hybrid Weed"}
        }
    }
]
for product_data in products_data:
    category = Category.objects.get(slug=product_data['category_slug'])
    product, created = Product.objects.get_or_create(
        name=product_data['name'],
        defaults={
            'slug': slugify(str(product_data['name'])),
            'category': category,
            'price': product_data['price'],
            'image': product_data['image'],
            'description': product_data['description']['en'],
            'composition': product_data['composition']['en'],
            'usage_instructions': product_data['usage_instructions']['en'],
            'creation_method': product_data['creation_method']['en'],
            'benefits': product_data['benefits']['en'],
            'meta_description': product_data['meta_description']['en'],
            'meta_keywords': product_data['meta_keywords']['en'],
            'is_active': product_data['is_active'],
            'featured': product_data['featured'],
            'stock_quantity': product_data['stock_quantity'],
            'strain_type': product_data['strain_type'],
            'preferred_ratio': product_data['preferred_ratio'],
            'recommended_methods': product_data['recommended_methods']
        }
    )
    for lang_code in product_data['translations'].keys():
        if lang_code != 'en':
            activate(lang_code)
            product.name = product_data['translations'][lang_code]['name']
            product.description = product_data['description'][lang_code]
            product.composition = product_data['composition'][lang_code]
            product.usage_instructions = product_data['usage_instructions'][lang_code]
            product.creation_method = product_data['creation_method'][lang_code]
            product.benefits = product_data['benefits'][lang_code]
            product.meta_description = product_data['meta_description'][lang_code]
            product.meta_keywords = product_data['meta_keywords'][lang_code]
            product.save()  # django-parler method
    activate('en')  # Reset to default language
    print(f"Successfully created Alien OG product with 11 translations!")
    

