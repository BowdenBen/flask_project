from flask import Flask

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/convert/<celsius>')
def convert_celsius(celsius):
    """Convert Celsius to Fahrenheit via URL."""
    try:
        # Convert the URL parameter from string to float
        celsius = float(celsius)
        # Call the conversion function
        fahrenheit = celsius_to_fahrenheit(celsius)
        # Return a useful response
        return f"<h1>{celsius:.2f}°C is {fahrenheit:.2f}°F</h1>"
    except ValueError:
        # Handle invalid input
        return "<h1>Invalid Celsius value. Please provide a numeric input.</h1>"


if __name__ == '__main__':
    app.run()
