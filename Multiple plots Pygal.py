import pygal
import random

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

chart = pygal.line()
chart.force_uri_protocol = ('http')
chart.title = ("Squares and Cubes")
chart.x_labels = x_values

chart.add('Squares',squares)
chart.add('Cubes',cubes)
chart.render_to_file('Squares_cubes.svg')
chart = pygal.Line(fill=True, zero=0)
