import numpy as np
from bokeh.plotting import figure, show, output_file

# some pseudo data
xs = np.linspace(0, 2*np.pi, 25)
yerrs = np.random.uniform(0.1, 0.3, xs.shape)
ys = np.sin(xs) + np.random.normal(0, yerrs, xs.shape)

output_file('bokehErrorbars.html')

# plot the points
p = figure(title='errorbars with bokeh', width=800, height=400)

p.xaxis.axis_label = 'x'
p.yaxis.axis_label = 'y'


p.circle(xs, ys, color='red', size=5, line_alpha=0)


# create the coordinates for the errorbars
err_xs = []
err_ys = []

for x, y, yerr in zip(xs, ys, yerrs):
    err_xs.append((x, x))
    err_ys.append((y - yerr, y + yerr))

# plot them
p.multi_line(err_xs, err_ys, color='red')

show(p)