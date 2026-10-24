"""Use the unit_converter module and the standard library datetime module."""

from datetime import datetime
from unit_converter import km_to_miles, kg_to_pounds, celsius_to_fahrenheit

print("Run at:", datetime.now().strftime("%Y-%m-%d %H:%M"))
print(f"10 km = {km_to_miles(10):.2f} miles")
print(f"70 kg = {kg_to_pounds(70):.2f} pounds")
print(f"30 C = {celsius_to_fahrenheit(30):.1f} F")
