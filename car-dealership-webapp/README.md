# Car Dealership WebApp

A Django-based web application for managing a car dealership inventory with user authentication, CRUD operations, and OpenAI integration.

## 🚗 Features

- **Car Inventory Management**: Complete CRUD operations for managing car listings
- **Brand Management**: Organize cars by brand with foreign key relationships
- **User Authentication**: Secure login/logout system with protected views
- **Image Upload**: Photo upload functionality for car listings
- **Search Functionality**: Search cars by model name
- **Inventory Tracking**: Track total car count and inventory value
- **AI Integration**: OpenAI API client for potential AI-powered features
- **PostgreSQL Database**: Production-ready database with SQLite fallback for testing
- **Responsive Design**: Clean, user-friendly interface

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4
- **Database**: PostgreSQL (with SQLite for testing)
- **Frontend**: HTML Templates with Django Template Engine
- **Image Processing**: Pillow
- **AI Integration**: OpenAI API (v1.106.1)
- **Configuration**: python-dotenv for environment variables
- **Deployment**: uWSGI configuration included

## 📋 Prerequisites

- Python 3.13.5+
- PostgreSQL
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rodsantis/car-dealership-webapp.git
   cd car-dealership-webapp
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   USER_PSQL=your_postgresql_username
   PASSWORD_PSQL=your_postgresql_password
   OPENAI_API_KEY=your_openai_api_key  # Optional
   ```

5. **Set up PostgreSQL database**
   ```bash
   createdb cars
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
car-dealership-webapp/
├── core/                   # Main Django project settings
│   ├── settings.py        # Django configuration
│   ├── urls.py           # URL routing
│   └── templates/        # Base templates
├── cars/                  # Cars app
│   ├── models.py         # Car, Brand, and CarInventory models
│   ├── views.py          # Class-based views for CRUD operations
│   ├── forms.py          # Django forms
│   ├── admin.py          # Admin interface configuration
│   ├── signals.py        # Django signals for inventory tracking
│   ├── templates/        # Car-specific templates
│   └── tests.py          # Unit tests
├── accounts/              # User authentication app
│   ├── views.py          # Login/logout views
│   ├── templates/        # Authentication templates
│   └── tests.py          # Authentication tests
├── openai_api/           # OpenAI integration
│   ├── client.py         # OpenAI API client
│   └── tests.py          # API tests
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── cars_uwsgi.ini        # uWSGI configuration for deployment
```

## 🎯 Usage

### Adding Cars

1. Login to the application
2. Navigate to "Add New Car"
3. Fill in car details:
   - Model name
   - Brand (select from existing or add new)
   - Factory year
   - Model year
   - License plate
   - Value
   - Photo upload
   - Description/bio

### Managing Inventory

- View all cars in the main cars list
- Use the search functionality to find specific models
- Click on any car to view detailed information
- Edit or delete cars (requires authentication)
- Track inventory statistics automatically

### User Management

- Register new accounts through the admin interface
- Login/logout functionality
- Protected views for car management operations

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

The project includes comprehensive tests for:
- Car CRUD operations
- User authentication
- Model relationships
- OpenAI API integration

## 🚀 Deployment

The project includes uWSGI configuration for production deployment:

1. **Configure uWSGI**
   ```bash
   uwsgi --ini cars_uwsgi.ini
   ```

2. **Set up static files**
   ```bash
   python manage.py collectstatic
   ```

3. **Configure your web server** (Nginx/Apache) to serve static files and proxy to uWSGI

## 🔧 Configuration

### Database Configuration

- **Development**: PostgreSQL (configured in settings.py)
- **Testing**: SQLite in-memory database
- **Environment variables**: Database credentials via .env file

### Security Features

- CSRF protection enabled
- User authentication required for car management
- Secure file upload handling
- Environment-based configuration

## 📝 API Integration

The project includes OpenAI API integration setup for potential AI features:
- Client configuration in `openai_api/client.py`
- Environment-based API key management
- Test coverage for API integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Rodrigo De Santis**
- GitHub: [@rodsantis](https://github.com/rodsantis)

## 🆘 Support

If you encounter any issues or have questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

---

**Happy coding! 🚗💨**
