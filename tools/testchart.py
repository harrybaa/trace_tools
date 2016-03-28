# import plotly.plotly as py
# import plotly.graph_objs as go

# # Create random data with numpy
# import numpy as np

# N = 500
# random_x = np.linspace(0, 1, N)
# random_y = np.random.randn(N)

# # Create a trace
# trace = go.Scatter(
#     x = random_x,
#     y = random_y
# )

# data = [trace]

# # Plot and embed in ipython notebook!
# py.iplot(data, filename='basic-line')

# # or plot with: plot_url = py.plot(data, filename='basic-line')

import plotly
print plotly.__version__  # version >1.9.4 required
from plotly.graph_objs import Scatter, Layout

# Create random data with numpy
import numpy as np
import plotly.graph_objs as go

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]


plotly.offline.plot({
"data": data,
"layout": Layout(
    title="hello world"
)
})