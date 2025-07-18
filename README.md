# MedicalStore - Professional Medical Products Platform

A complete responsive e-commerce-style medical product platform built with Django and Tailwind CSS, featuring comprehensive product information including composition, usage instructions, creation methods, and health benefits.

## 🚀 Features

### Core Functionality
- **Product Management**: Complete CRUD operations for medical products and categories
- **Session-based Cart**: Add/remove items, quantity management, total calculation
- **Order Processing**: Checkout system with order confirmation and history
- **User Authentication**: Registration, login, profile management (optional at checkout)
- **Search & Filtering**: Product search by name, category, benefits, and price range
- **Responsive Design**: Mobile-first design with Tailwind CSS

### Medical Product Information
Each product includes:
- **Composition**: Detailed ingredients and active compounds
- **Usage Instructions**: Professional guidance on proper usage
- **Creation Method**: Manufacturing and formulation processes
- **Health Benefits**: Comprehensive benefit information
- **Scientific Accuracy**: All information reviewed by healthcare professionals

### Security & Compliance
- **GDPR Compliance**: Cookie consent and privacy controls
- **Medical Disclaimers**: Appropriate medical disclaimers throughout
- **CSRF Protection**: All forms protected with CSRF tokens
- **Secure Forms**: Input validation and sanitization
- **Data Privacy**: Secure handling of personal and medical information

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: Django Templates + Tailwind CSS
- **Styling**: Tailwind CSS with custom medical theme
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)

## 📁 Project Structure

```
medicalstore/
├── medicalstore/           # Main project settings
├── products/              # Product and category management
├── cart/                  # Session-based shopping cart
├── orders/                # Order processing and history
├── accounts/              # User authentication and profiles
├── pages/                 # Static pages (FAQ, About, Contact, Legal)
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploaded files
└── requirements.txt       # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd medicalstore
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate with sample data**
   ```bash
   python manage.py populate_db
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin

## 📊 Sample Data

The `populate_db` management command creates:
- **5 Categories**: Pain Relief, Cardiovascular Health, Digestive Health, Immune Support, Respiratory Care
- **10 Products**: Complete medical products with all required information
- **Realistic Data**: Professional medical product descriptions and compositions

## 🎨 Design Features

### Color Scheme
- **Primary**: Medical Blue (#3B82F6)
- **Secondary**: Light Blue (#EBF8FF)
- **Accent**: Dark Blue (#1E40AF)
- **Background**: Light Gray (#F9FAFB)

### Typography
- **Primary Font**: Inter (Google Fonts)
- **Headings**: Bold weights (600-700)
- **Body**: Regular weight (400)

### Components
- **Cards**: Rounded corners with subtle shadows
- **Buttons**: Consistent styling with hover effects
- **Forms**: Clean input fields with focus states
- **Navigation**: Sticky header with search functionality

## 🔧 Configuration

### Environment Variables
Create a `.env` file for production:
```env
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Database Configuration
For PostgreSQL production setup:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'medicalstore',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🚀 Deployment

### Render.com Deployment

1. **Create render.yaml**
   ```yaml
   services:
     - type: web
       name: medicalstore
       env: python
       buildCommand: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
       startCommand: gunicorn medicalstore.wsgi:application
       envVars:
         - key: DEBUG
           value: False
         - key: SECRET_KEY
           generateValue: true
         - key: DATABASE_URL
           fromDatabase:
             name: medicalstore-db
             property: connectionString
   
   databases:
     - name: medicalstore-db
       databaseName: medicalstore
       user: medicalstore_user
   ```

2. **Update settings for production**
   ```python
   import os
   import dj_database_url
   
   DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
   SECRET_KEY = os.environ.get('SECRET_KEY')
   ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
   
   if 'DATABASE_URL' in os.environ:
       DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'])
   ```

### Railway Deployment

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Deploy**
   ```bash
   railway login
   railway init
   railway up
   ```

### VPS Deployment

1. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx postgresql
   ```

2. **Setup application**
   ```bash
   git clone <repository-url>
   cd medicalstore
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt gunicorn
   ```

3. **Configure Nginx**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
       
       location /static/ {
           alias /path/to/medicalstore/static/;
       }
       
       location /media/ {
           alias /path/to/medicalstore/media/;
       }
   }
   ```

## 🧪 Testing

### Manual Testing Checklist
- [ ] Homepage loads with categories and featured products
- [ ] Product listing with search and filters
- [ ] Product detail pages with all tabs
- [ ] Add to cart functionality
- [ ] Cart management (add/remove/update quantities)
- [ ] Checkout process
- [ ] Order confirmation
- [ ] User registration and login
- [ ] Admin panel access
- [ ] Responsive design on mobile devices

### Running Tests
```bash
python manage.py test
```

## 🔒 Security Features

- **CSRF Protection**: All forms include CSRF tokens
- **Input Validation**: Server-side validation for all user inputs
- **SQL Injection Prevention**: Django ORM prevents SQL injection
- **XSS Protection**: Template auto-escaping enabled
- **Secure Headers**: Security middleware configured
- **Medical Disclaimers**: Appropriate disclaimers throughout the site

## 🌐 Internationalization

The platform is structured for future multilingual support:
- Template structure supports translation tags
- Model fields can be extended for multiple languages
- URL patterns ready for language prefixes

## 📱 Mobile Responsiveness

- **Mobile-first Design**: Optimized for mobile devices
- **Responsive Grid**: Adapts to different screen sizes
- **Touch-friendly**: Large buttons and touch targets
- **Fast Loading**: Optimized images and minimal JavaScript

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Medical Disclaimer

This platform provides information for educational purposes only and should not replace professional medical advice. Users should consult healthcare providers before using any medical products.

## 📞 Support

For support and questions:
- Email: support@medicalstore.com
- Documentation: [Link to docs]
- Issues: [GitHub Issues]

## 🔄 Version History

- **v1.0.0**: Initial release with core functionality
- Complete e-commerce platform
- Medical product information system
- Responsive design with Tailwind CSS
- User authentication and order management

---

Built with ❤️ for healthcare professionals and medical product education.