from rgbmatrix import RGBMatrix, RGBMatrixOptions
from renderer import MainRenderer

matrixOptions = RGBMatrixOptions()
matrixOptions.rows = 32
matrixOptions.cols = 64
matrixOptions.gpio_slowdown = 2
matrixOptions.brightness = 50

matrix = RGBMatrix(options = matrixOptions)

MainRenderer(matrix).render()