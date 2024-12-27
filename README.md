# Flight Booking Web Application

A simple web application for managing flight bookings, built with Flask. This app allows users to **add**, **edit**, **delete**, and **view** flights. It uses **SQLite** as the database and includes dynamic HTML templates for a seamless user experience.

## Features

- Add new flights with details like flight number, origin, destination, departure, and arrival times.
- Edit existing flights to update their details.
- Delete flights from the database.
- View a list of all flights.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Bootstrap for styling), Jinja2 templating
- **Database**: SQLite
- **Tools**: SQLAlchemy for ORM

## Installation

Follow these steps to set up the application on your local machine:

### Prerequisites

- Python 3.7+ installed.
- `pip` package manager.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/flight-booking-app.git
   cd flight-booking-app
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**

   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. **Run the Application**

   ```bash
   python app.py
   ```

6. **Open in Browser**

   Navigate to `http://127.0.0.1:5000` in your web browser.

## Project Structure

```
flight_booking_app/
│
├── templates/              # HTML templates
│   ├── base.html           # Base layout
│   ├── index.html          # Home page
│   ├── add_flight.html     # Add flight form
│   └── edit_flight.html    # Edit flight form
│
├── app.py                  # Main application
├── models.py               # Database models
├── requirements.txt        # Dependencies
└── flights.db              # SQLite database (generated after running the app)
```

## Usage

1. **Home Page**: Displays all available flights.
2. **Add Flight**: Use the "Add Flight" button to add new flights.
3. **Edit Flight**: Click "Edit" next to a flight to update its details.
4. **Delete Flight**: Click "Delete" next to a flight to remove it.

## Screenshots

### Home Page
![Home Page](https://via.placeholder.com/800x400.png?text=Home+Page)

### Add Flight
![Add Flight](https://via.placeholder.com/800x400.png?text=Add+Flight+Page)

### Edit Flight
![Edit Flight](https://via.placeholder.com/800x400.png?text=Edit+Flight+Page)

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add some feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Jinja2 Templating](https://jinja.palletsprojects.com/)

---

Enjoy managing your flight bookings with this simple and intuitive app! 😊
