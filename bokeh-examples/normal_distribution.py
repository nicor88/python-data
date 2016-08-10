import numpy as np
from scipy.stats import norm
from bokeh.plotting import figure, output_file, show
import matplotlib.mlab as mlab

output_file("normlDistribution.html")
mu = 50  # center of pdf
sigma1 = 4
sigma2 = 20
x = np.linspace(0, 99, 100)
multiple_x_axis = []
multiple_distributions = []
for i in range(10):
    multiple_x_axis.append(x)
    multiple_distributions.append(norm.pdf(x, mu, i))
    #print(i)

p = figure(plot_width=800, plot_height=500)
p.multi_line(multiple_x_axis, multiple_distributions)
show(p)

# normal_distr1 = norm.pdf(x_axis, mu, sigma1)
# normal_distr2 = norm.pdf(x_axis, mu, sigma2)
# p = figure(plot_width=600, plot_height=500)
# p.multi_line([x_axis,x_axis],[normal_distr1,normal_distr2],color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=4)
# show(p)
