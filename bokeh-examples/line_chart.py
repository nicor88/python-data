__author__ = 'nicor88'

import numpy as np
from bokeh.plotting import figure, output_file, show
output_file("lineChart.html")
x_axis = np.linspace(1, 10, 10, endpoint=True)
print(x_axis)
y_axix = np.random.randint(2,40,10)
print(y_axix)
p = figure()
p.line(x_axis, y_axix, line_width=3,color="blue")
show(p)