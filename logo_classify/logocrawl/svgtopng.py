#cairosvg.svg2png(#url="/path/to/input.svg", write_to="/tmp/output.png")
import cairosvg
import numpy as np
path = "../res/"
file_name = "google-play-store"
cairosvg.svg2png(url=path+file_name+".svg", 
                 write_to=path+file_name+".png", 
                 dpi = 100
                )