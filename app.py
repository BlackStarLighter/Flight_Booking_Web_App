from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Flight
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here' # Needed to flash messages

db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    flights = Flight.query.all()
    return render_template('index.html', flight=flights)

@app.route('/add', methods=['GET', 'POST'])
def add_flight():
    if request.method == 'POST':
        flight_number = request.form['flight_number']
        origin = request.form['origin']
        destination = request.form['destination']
        departure_time =request.form['departure_time']
        arrival_time = request.form['arrival_time']

        # Input validation can be added here

        new_flight = Flight(
            flight_number=flight_number,
            origin=origin,
            destination=destination,
            departure_time=datetime.strptime(departure_time, '%Y-%m-%dT%H:%M'),
            arrival_time=datetime.strptime(arrival_time, '%Y-%m-%dT%H:%M')
        )
        db.session.add(new_flight)
        db.session.commit()
        flash('Flight added successfully!', 'succes')
        return redirect(url_for('index'))
    return render_template('add_flight.html')

@app.route('/edit/<int:flight_id>', methods=['GET', 'POST'])
def edit_flight(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    if request.method == 'POST':
        flight.flight_number = request.form['flight_number']
        flight.origin = request.form['origin']
        flight.destination = request.form['destination']
        flight.departure_time = datetime.strptime(request.form['departure_time'], '%Y-%m-%dT%H:%M')
        flight.arrival_time = datetime.strptime(request.form['arrival_time'], '%Y-%m-%dT%H:%M')

        db.session.commit()
        flash('Flight updated successufully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_flight.html', fligh=flight)

@app.route('/delete/<int:flight_id>', methods=['POST'])
def delete_flight(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    db.session.delete(flight)
    db.session.commit()
    flash('Flight deleted successufully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    