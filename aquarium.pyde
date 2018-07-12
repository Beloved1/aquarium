xCoord = 500
yCoord = 100
Width = 70
Length = 40
rectlength = 600

def setup():
    size (500, 500)
    background(255, 108, 0)
    fill(255, 108, 0)
    
def fish(xCoord, yCoord, Width, Length):
    fill(0, 255, 255)
    rect(0, 0, rectlength, rectlength)
    noStroke()
    fill(0,128,128)
    ellipse(xCoord, yCoord, Width, Length)
    #curve(5, 26, 30, 85, 30, 117, 5, 160)
    triangle(xCoord+25, yCoord, xCoord+40, yCoord-30, xCoord+40, yCoord+25)
    fill(0)
    ellipse(xCoord-25, yCoord-10, Width/10, Length/10)
    
    
def draw():
    global xCoord, yCoord, Width, Length, rectlength
    fill(0,128,128)
    rect(0, 0, rectlength, rectlength)
    
    fish(xCoord, yCoord, Width, Length)
    xCoord  -= .3
    yCoord += .1
    

    
