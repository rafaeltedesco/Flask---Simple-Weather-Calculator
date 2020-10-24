from flask import Flask
import weather


app = Flask(__name__)


@app.route('/celsius_to_fahrenheit/<float:celsius>')
def celsius_to_fahrenheit(celsius):
  fahrenheit = weather.celsius_to_fahrenheit(celsius)
  return f'{celsius}ºC = {fahrenheit} ºF'

@app.route('/celsius_to_kelvin/<float:celsius>')
def celsius_to_kelvin(celsius):
  kelvin = weather.celsius_to_kelvin(celsius)
  return f'{celsius}ºC = {kelvin}K'


app.run(debug=True, host='0.0.0.0', port='3003')