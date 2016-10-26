import matplotlib.pyplot

# de coordinaten per punt
x_coords = [0,1,2,3,4,5]
y_coords = [0,1,4,9,16,25]

# plot punten (y tegen x) met groene rondjes
matplotlib.pyplot.plot(x_coords, y_coords, 'go')
matplotlib.pyplot.show()