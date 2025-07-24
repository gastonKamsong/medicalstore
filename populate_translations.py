#!/usr/bin/env python3
"""
Script to populate basic translations for the medical store application.
"""

import os
import sys

# Add Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicalstore.settings')

# Setup Django
import django
django.setup()

# Translation mappings for common terms
TRANSLATIONS = {
    'da': {  # Danish
        'Products': 'Produkter',
        'About': 'Om',
        'Contact': 'Kontakt',
        'Login': 'Log ind',
        'Register': 'Registrer',
        'Logout': 'Log ud',
        'Profile': 'Profil',
        'Order History': 'Ordrehistorik',
        'Search products...': 'Søg produkter...',
        'Quick Links': 'Hurtige links',
        'About Us': 'Om os',
        'FAQ': 'FAQ',
        'Legal': 'Juridisk',
        'Legal Notice': 'Juridisk meddelelse',
        'Privacy Policy': 'Privatlivspolitik',
        'Accept': 'Accepter',
        'Learn more': 'Lær mere',
        'All rights reserved.': 'Alle rettigheder forbeholdes.',
        'Site Name': 'Sidenavn',
        'Tagline': 'Tagline',
        'Email': 'E-mail',
        'Phone': 'Telefon',
        'Address': 'Adresse',
        'Business Hours': 'Åbningstider',
        'About Text': 'Om tekst',
        'Terms of Service': 'Servicevilkår',
        'Site Settings': 'Sideindstillinger',
        'Contact Info': 'Kontaktinfo',
        'natural medical products, cannabis, CBD, hemp, organic medicine, herbal remedies': 'naturlige medicinske produkter, cannabis, CBD, hamp, økologisk medicin, urtemedicin',
        'We use cookies to improve your experience. By continuing to use our site, you accept our use of cookies.': 'Vi bruger cookies for at forbedre din oplevelse. Ved at fortsætte med at bruge vores side accepterer du vores brug af cookies.',
        'Medical Disclaimer:': 'Medicinsk ansvarsfraskrivelse:',
        'The information provided is for educational purposes only and should not replace professional medical advice.': 'De oplysninger, der gives, er kun til uddannelsesformål og bør ikke erstatte professionel medicinsk rådgivning.'
    },
    'fi': {  # Finnish
        'Products': 'Tuotteet',
        'About': 'Tietoja',
        'Contact': 'Yhteystiedot',
        'Login': 'Kirjaudu sisään',
        'Register': 'Rekisteröidy',
        'Logout': 'Kirjaudu ulos',
        'Profile': 'Profiili',
        'Order History': 'Tilaushistoria',
        'Search products...': 'Etsi tuotteita...',
        'Quick Links': 'Pikalinkit',
        'About Us': 'Tietoja meistä',
        'FAQ': 'UKK',
        'Legal': 'Oikeudellinen',
        'Legal Notice': 'Oikeudellinen ilmoitus',
        'Privacy Policy': 'Tietosuojakäytäntö',
        'Accept': 'Hyväksy',
        'Learn more': 'Lue lisää',
        'All rights reserved.': 'Kaikki oikeudet pidätetään.',
        'Site Name': 'Sivuston nimi',
        'Tagline': 'Tunnuslause',
        'Email': 'Sähköposti',
        'Phone': 'Puhelin',
        'Address': 'Osoite',
        'Business Hours': 'Aukioloajat',
        'About Text': 'Tietoja teksti',
        'Terms of Service': 'Käyttöehdot',
        'Site Settings': 'Sivuston asetukset',
        'Contact Info': 'Yhteystiedot',
        'natural medical products, cannabis, CBD, hemp, organic medicine, herbal remedies': 'luonnolliset lääketuotteet, kannabis, CBD, hamppu, luomulaakinta, yrttilääkintä',
        'We use cookies to improve your experience. By continuing to use our site, you accept our use of cookies.': 'Käytämme evästeitä parantaaksemme kokemustasi. Jatkamalla sivustomme käyttöä hyväksyt evästeiden käyttömme.',
        'Medical Disclaimer:': 'Lääketieteellinen vastuuvapauslauseke:',
        'The information provided is for educational purposes only and should not replace professional medical advice.': 'Annetut tiedot ovat vain koulutuksellisia tarkoituksia varten, eivätkä ne saa korvata ammattimaista lääketieteellistä neuvontaa.'
    },
    'de': {  # German
        'Products': 'Produkte',
        'About': 'Über',
        'Contact': 'Kontakt',
        'Login': 'Anmelden',
        'Register': 'Registrieren',
        'Logout': 'Abmelden',
        'Profile': 'Profil',
        'Order History': 'Bestellhistorie',
        'Search products...': 'Produkte suchen...',
        'Quick Links': 'Schnelle Links',
        'About Us': 'Über uns',
        'FAQ': 'FAQ',
        'Legal': 'Rechtliches',
        'Legal Notice': 'Rechtlicher Hinweis',
        'Privacy Policy': 'Datenschutzrichtlinie',
        'Accept': 'Akzeptieren',
        'Learn more': 'Mehr erfahren',
        'All rights reserved.': 'Alle Rechte vorbehalten.',
        'Site Name': 'Seitenname',
        'Tagline': 'Slogan',
        'Email': 'E-Mail',
        'Phone': 'Telefon',
        'Address': 'Adresse',
        'Business Hours': 'Geschäftszeiten',
        'About Text': 'Über Text',
        'Terms of Service': 'Nutzungsbedingungen',
        'Site Settings': 'Seiteneinstellungen',
        'Contact Info': 'Kontaktinfo',
        'natural medical products, cannabis, CBD, hemp, organic medicine, herbal remedies': 'natürliche medizinische Produkte, Cannabis, CBD, Hanf, Bio-Medizin, Kräuterheilmittel',
        'We use cookies to improve your experience. By continuing to use our site, you accept our use of cookies.': 'Wir verwenden Cookies, um Ihre Erfahrung zu verbessern. Durch die weitere Nutzung unserer Website akzeptieren Sie unsere Verwendung von Cookies.',
        'Medical Disclaimer:': 'Medizinischer Haftungsausschluss:',
        'The information provided is for educational purposes only and should not replace professional medical advice.': 'Die bereitgestellten Informationen dienen nur Bildungszwecken und sollten keine professionelle medizinische Beratung ersetzen.'
    },
    'it': {  # Italian
        'Products': 'Prodotti',
        'About': 'Chi siamo',
        'Contact': 'Contatti',
        'Login': 'Accedi',
        'Register': 'Registrati',
        'Logout': 'Esci',
        'Profile': 'Profilo',
        'Order History': 'Cronologia ordini',
        'Search products...': 'Cerca prodotti...',
        'Quick Links': 'Link rapidi',
        'About Us': 'Chi siamo',
        'FAQ': 'FAQ',
        'Legal': 'Legale',
        'Legal Notice': 'Avviso legale',
        'Privacy Policy': 'Informativa sulla privacy',
        'Accept': 'Accetta',
        'Learn more': 'Scopri di più',
        'All rights reserved.': 'Tutti i diritti riservati.',
        'Site Name': 'Nome del sito',
        'Tagline': 'Slogan',
        'Email': 'Email',
        'Phone': 'Telefono',
        'Address': 'Indirizzo',
        'Business Hours': 'Orari di apertura',
        'About Text': 'Testo informativo',
        'Terms of Service': 'Termini di servizio',
        'Site Settings': 'Impostazioni del sito',
        'Contact Info': 'Info contatto',
        'natural medical products, cannabis, CBD, hemp, organic medicine, herbal remedies': 'prodotti medici naturali, cannabis, CBD, canapa, medicina biologica, rimedi erboristici',
        'We use cookies to improve your experience. By continuing to use our site, you accept our use of cookies.': 'Utilizziamo i cookie per migliorare la tua esperienza. Continuando a utilizzare il nostro sito, accetti il nostro uso dei cookie.',
        'Medical Disclaimer:': 'Disclaimer medico:',
        'The information provided is for educational purposes only and should not replace professional medical advice.': 'Le informazioni fornite sono solo a scopo educativo e non dovrebbero sostituire il consiglio medico professionale.'
    },
    'hu': {  # Hungarian
        'Products': 'Termékek',
        'About': 'Rólunk',
        'Contact': 'Kapcsolat',
        'Login': 'Bejelentkezés',
        'Register': 'Regisztráció',
        'Logout': 'Kijelentkezés',
        'Profile': 'Profil',
        'Order History': 'Rendelési előzmények',
        'Search products...': 'Termékek keresése...',
        'Quick Links': 'Gyors linkek',
        'About Us': 'Rólunk',
        'FAQ': 'GYIK',
        'Legal': 'Jogi',
        'Legal Notice': 'Jogi nyilatkozat',
        'Privacy Policy': 'Adatvédelmi irányelvek',
        'Accept': 'Elfogad',
        'Learn more': 'Tudj meg többet',
        'All rights reserved.': 'Minden jog fenntartva.',
        'Site Name': 'Oldal neve',
        'Tagline': 'Szlogen',
        'Email': 'Email',
        'Phone': 'Telefon',
        'Address': 'Cím',
        'Business Hours': 'Nyitvatartás',
        'About Text': 'Bemutatkozó szöveg',
        'Terms of Service': 'Szolgáltatási feltételek',
        'Site Settings': 'Oldal beállítások',
        'Contact Info': 'Kapcsolati információ',
        'natural medical products, cannabis, CBD, hemp, organic medicine, herbal remedies': 'természetes gyógyászati termékek, kannabisz, CBD, kender, bio gyógyászat, gyógynövényes szerek',
        'We use cookies to improve your experience. By continuing to use our site, you accept our use of cookies.': 'Sütiket használunk a felhasználói élmény javítása érdekében. Az oldal további használatával elfogadja a sütik használatát.',
        'Medical Disclaimer:': 'Orvosi felelősségkizárás:',
        'The information provided is for educational purposes only and should not replace professional medical advice.': 'A megadott információk csak oktatási célokat szolgálnak, és nem helyettesíthetik a szakmai orvosi tanácsot.'
    },
    'no': {  # Norwegian
        'Products': 'Produkter',
        'About': 'Om',
        'Contact': 'Kontakt',
        'Login': 'Logg inn',
        'Register': 'Registrer',
        'Logout': 'Logg ut',
        'Profile': 'Profil',
        'Order History': 'Bestillingshistorikk',
        'Search products...': 'Søk produkter...',
        'Quick Links': 'Hurtiglenker',
        'About Us': 'Om oss',
        'FAQ': 'FAQ',
        'Legal': 'Juridisk',
        'Legal Notice': 'Juridisk merknad',
        'Privacy Policy': 'Personvernregler',
        'Accept': 'Godta',
        'Learn more': 'Lær mer',
        'All rights reserved.': 'Alle rettigheter forbeholdt.',
        'Site Name': 'Nettstedsnavn',
        'Tagline': 'Slagord',
        'Email': 'E-post',
        'Phone': 'Telefon',
        'Address': 'Adresse',
        'Business Hours': 'Åpningstider',
        'About Text': 'Om tekst',
        'Terms of Service': 'Tjenestevilkår',
        'Site Settings': 'Nettstedsinnstillinger',
        'Contact Info': 'Kontaktinfo',
        'natural medical products, cannabis, CBD, hemp, organic medicine, herbal remedies': 'naturlige medisinske produkter, cannabis, CBD, hamp, økologisk medisin, urteremedier',
        'We use cookies to improve your experience. By continuing to use our site, you accept our use of cookies.': 'Vi bruker informasjonskapsler for å forbedre opplevelsen din. Ved å fortsette å bruke nettstedet vårt, godtar du vår bruk av informasjonskapsler.',
        'Medical Disclaimer:': 'Medisinsk ansvarsfraskrivelse:',
        'The information provided is for educational purposes only and should not replace professional medical advice.': 'Informasjonen som gis er kun for utdanningsformål og bør ikke erstatte profesjonell medisinsk rådgivning.'
    },
    'ga': {  # Irish
        'Products': 'Táirgí',
        'About': 'Faoi',
        'Contact': 'Teagmháil',
        'Login': 'Logáil isteach',
        'Register': 'Cláraigh',
        'Logout': 'Logáil amach',
        'Profile': 'Próifíl',
        'Order History': 'Stair Orduithe',
        'Search products...': 'Cuardaigh táirgí...',
        'Quick Links': 'Naisc Thapa',
        'About Us': 'Fúinn',
        'FAQ': 'Ceisteanna Coitianta',
        'Legal': 'Dlíthiúil',
        'Legal Notice': 'Fógra Dlíthiúil',
        'Privacy Policy': 'Polasaí Príobháideachta',
        'Accept': 'Glac leis',
        'Learn more': 'Foghlaim níos mó',
        'All rights reserved.': 'Gach ceart ar cosaint.',
        'Site Name': 'Ainm an tSuímh',
        'Tagline': 'Mana',
        'Email': 'Ríomhphost',
        'Phone': 'Fón',
        'Address': 'Seoladh',
        'Business Hours': 'Uaireanta Gnó',
        'About Text': 'Téacs Faoi',
        'Terms of Service': 'Téarmaí Seirbhíse',
        'Site Settings': 'Socruithe Suímh',
        'Contact Info': 'Eolas Teagmhála',
        'natural medical products, cannabis, CBD, hemp, organic medicine, herbal remedies': 'táirgí leighis nádúrtha, cannabas, CBD, cnáib, leigheas orgánach, leigheasanna luibheanna',
        'We use cookies to improve your experience. By continuing to use our site, you accept our use of cookies.': 'Úsáidimid fianáin chun d\'eispéireas a fheabhsú. Trí leanúint ar aghaidh ag úsáid ár suímh, glacann tú lenár n-úsáid fianán.',
        'Medical Disclaimer:': 'Séanadh Leighis:',
        'The information provided is for educational purposes only and should not replace professional medical advice.': 'Tá an fhaisnéis a chuirtear ar fáil le haghaidh críocha oideachais amháin agus níor cheart di comhairle leighis ghairmiúil a chur in ionad.'
    },
    'es': {  # Spanish
        'Products': 'Productos',
        'About': 'Acerca de',
        'Contact': 'Contacto',
        'Login': 'Iniciar sesión',
        'Register': 'Registrarse',
        'Logout': 'Cerrar sesión',
        'Profile': 'Perfil',
        'Order History': 'Historial de pedidos',
        'Search products...': 'Buscar productos...',
        'Quick Links': 'Enlaces rápidos',
        'About Us': 'Acerca de nosotros',
        'FAQ': 'FAQ',
        'Legal': 'Legal',
        'Legal Notice': 'Aviso legal',
        'Privacy Policy': 'Política de privacidad',
        'Accept': 'Aceptar',
        'Learn more': 'Saber más',
        'All rights reserved.': 'Todos los derechos reservados.',
        'Site Name': 'Nombre del sitio',
        'Tagline': 'Eslogan',
        'Email': 'Correo electrónico',
        'Phone': 'Teléfono',
        'Address': 'Dirección',
        'Business Hours': 'Horario comercial',
        'About Text': 'Texto acerca de',
        'Terms of Service': 'Términos de servicio',
        'Site Settings': 'Configuración del sitio',
        'Contact Info': 'Información de contacto',
        'natural medical products, cannabis, CBD, hemp, organic medicine, herbal remedies': 'productos médicos naturales, cannabis, CBD, cáñamo, medicina orgánica, remedios herbales',
        'We use cookies to improve your experience. By continuing to use our site, you accept our use of cookies.': 'Utilizamos cookies para mejorar su experiencia. Al continuar usando nuestro sitio, acepta nuestro uso de cookies.',
        'Medical Disclaimer:': 'Descargo de responsabilidad médica:',
        'The information provided is for educational purposes only and should not replace professional medical advice.': 'La información proporcionada es solo para fines educativos y no debe reemplazar el consejo médico profesional.'
    },
    'sv': {  # Swedish
        'Products': 'Produkter',
        'About': 'Om',
        'Contact': 'Kontakt',
        'Login': 'Logga in',
        'Register': 'Registrera',
        'Logout': 'Logga ut',
        'Profile': 'Profil',
        'Order History': 'Beställningshistorik',
        'Search products...': 'Sök produkter...',
        'Quick Links': 'Snabblänkar',
        'About Us': 'Om oss',
        'FAQ': 'FAQ',
        'Legal': 'Juridisk',
        'Legal Notice': 'Juridisk meddelande',
        'Privacy Policy': 'Integritetspolicy',
        'Accept': 'Acceptera',
        'Learn more': 'Läs mer',
        'All rights reserved.': 'Alla rättigheter förbehållna.',
        'Site Name': 'Webbplatsnamn',
        'Tagline': 'Slogan',
        'Email': 'E-post',
        'Phone': 'Telefon',
        'Address': 'Adress',
        'Business Hours': 'Öppettider',
        'About Text': 'Om text',
        'Terms of Service': 'Användarvillkor',
        'Site Settings': 'Webbplatsinställningar',
        'Contact Info': 'Kontaktinfo',
        'natural medical products, cannabis, CBD, hemp, organic medicine, herbal remedies': 'naturliga medicinska produkter, cannabis, CBD, hampa, ekologisk medicin, örtmedicin',
        'We use cookies to improve your experience. By continuing to use our site, you accept our use of cookies.': 'Vi använder cookies för att förbättra din upplevelse. Genom att fortsätta använda vår webbplats accepterar du vår användning av cookies.',
        'Medical Disclaimer:': 'Medicinsk ansvarsfriskrivning:',
        'The information provided is for educational purposes only and should not replace professional medical advice.': 'Informationen som tillhandahålls är endast för utbildningsändamål och bör inte ersätta professionell medicinsk rådgivning.'
    }
}

def update_po_file(language_code, translations):
    """Update a .po file with translations"""
    po_file_path = f'locale/{language_code}/LC_MESSAGES/django.po'
    
    if not os.path.exists(po_file_path):
        print(f"Warning: {po_file_path} does not exist")
        return
    
    # Read the current file
    with open(po_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update translations
    for english_text, translated_text in translations.items():
        # Look for the msgid and update the corresponding msgstr
        msgid_pattern = f'msgid "{english_text}"'
        if msgid_pattern in content:
            # Find the msgstr line that follows
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip() == f'msgid "{english_text}"':
                    # Check if the next line is msgstr
                    if i + 1 < len(lines) and lines[i + 1].strip().startswith('msgstr'):
                        lines[i + 1] = f'msgstr "{translated_text}"'
                        break
            content = '\n'.join(lines)
    
    # Write the updated content back
    with open(po_file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated translations for {language_code}")

def main():
    """Main function to update all translation files"""
    for lang_code, translations in TRANSLATIONS.items():
        update_po_file(lang_code, translations)
    
    print("Translation update complete!")
    print("Run 'python manage.py compilemessages' to compile the translations.")

if __name__ == '__main__':
    main()