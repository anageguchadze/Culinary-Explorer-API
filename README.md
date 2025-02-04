# Culinary-Explorer-API 🍽️

A **Django REST Framework** project designed as a local culinary guide, allowing users to discover, share, and rate dishes. This API supports user registration, dish management, chef profiles, ingredient tracking, and personalized recommendations.

---

## 🚀 Features

- **Authentication:** JWT-based authentication system for secure access.
- **Dish Management:** Full CRUD operations for dishes with descriptions, preparation methods, and images.
- **Chef Profiles:** Manage chef profiles with culinary backgrounds and specialties.
- **Ingredients:** Associate ingredients with each dish.
- **Ratings:** Users can rate dishes on a 1-5 star scale.
- **Filtering:** Advanced filtering by dish name, chef, ingredients, and ratings.
- **Recommendations (Bonus):** Personalized dish suggestions based on user preferences.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (JSON Web Tokens)
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
- **Dependencies:** django-filter, djangorestframework-simplejwt

---

## 📦 Installation

1. **Clone the repository:**
   git clone https://github.com/anageguchadze/Culinary-Explorer-API.git
   cd Culinary-Explorer-API

2. **Create a virtual environment:**
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate    # For Windows

3. **Install dependencies:**
   pip install -r requirements.txt

4. **Apply migrations:**
   python manage.py makemigrations
   python manage.py migrate
 

5. **Run the server:**
   python manage.py runserver

---

## 🔑 API Endpoints

### **Authentication**
- `POST /api/token/` - Obtain JWT Token
- `POST /api/token/refresh/` - Refresh JWT Token

### **Dishes**
- `GET /api/dishes/` - List all dishes
- `POST /api/dishes/` - Create a new dish
- `GET /api/dishes/{id}/` - Retrieve dish details
- `PUT /api/dishes/{id}/` - Update a dish
- `DELETE /api/dishes/{id}/` - Delete a dish

### **Ratings**
- `POST /api/ratings/` - Add a rating (1-5 stars)
- `GET /api/ratings/` - View all ratings

### **Filtering Example:**
GET /api/dishes/?name=pasta&min_rating=4

---

## ⚙️ Configuration

- **JWT Settings:** Configured in `settings.py` using `rest_framework_simplejwt`.
- **Filtering:** Enabled via `django-filter`.
- **Custom User Model:** Extensible with `AbstractUser`.

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📫 Contact

For questions or suggestions:
- **Email:** anageguchadze22@gmail.com