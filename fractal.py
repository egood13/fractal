
import colorsys
import numpy as np
from PIL import Image
from datetime import datetime

def main():
    start = datetime.now()

    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    x_limits = [-.75,-.65]
    y_limits = [-.5,-.4]
    fractal_array = []

    
    fractal_array = create_array(SCREEN_WIDTH, SCREEN_HEIGHT, x_limits, y_limits)
    filename = f"fractal/fractal_({x_limits[0]},{y_limits[0]})-({x_limits[1]},{y_limits[1]}).png"
    fractal_img(filename, fractal_array)
    print(f"Script ran in {datetime.now() - start}.")

def fractal_img(output, fractal_array):

    array = np.array(fractal_array, dtype=np.uint8)
    img = Image.fromarray(array)
    img.save(output)

def create_array(width_length, height_length, x_limits, y_limits):
    '''
    width_lenght, height_length - (int) set number of points in x, y axis
    x_limits, y_limits - (list) set beginning and end points for x,y axis
    '''
    
    fractal_array = []
    x_initial = x_limits[0]
    x_final = x_limits[1]
    y_initial = y_limits[0]
    y_final = y_limits[1]

    x = x_initial
    y = y_initial
    for i in range(height_length + 1):
        y = y_initial + (i*(y_final - y_initial)/height_length)
        row_vals = []
        for j in range(width_length):
            x = x_initial + (j*(x_final - x_initial)/width_length)
            row_vals.append(iterate_z(50, complex(x, y), 0))
        fractal_array.append(row_vals)

    return(fractal_array)

def iterate_z(max_iterations, c, z=0):
    ''' Iterate z_n number of iterations for value c '''
    rgb = ()
    i = 0
    while i <= max_iterations and abs(z) <= 2.0:
        z = z**2 + c
        i += 1
        
    if abs(z) >= 2.0:
        rgb = tuple(round(255*h) for h in colorsys.hsv_to_rgb((240-(i/max_iterations)*80)/360,0.5,1.0))
        
    else: rgb = (0,0,0)
    return(rgb) # return magnitude of complex number


if __name__ == "__main__":
    main()