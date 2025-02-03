import  os
import  sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './temperatures')))

from calvin import Calvin
from celcius import Celcius
from farheinheit import  Farheinheit
from orange import Orange
from temperature_converter import TemperatureConverter

class Application:
    def run(self):
        calvin = Calvin()
        celcius = Celcius()
        farheinheit = Farheinheit()
        orange = Orange()

        amount = 32

        conv = TemperatureConverter(farheinheit, celcius)
        result = conv.convert(amount)
        print(f'{amount} Celcius to calvin: {result}')

