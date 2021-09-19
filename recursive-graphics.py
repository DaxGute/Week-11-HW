from graphics import *
def setUpWindow():
    win = GraphWin("Recursive Graphics", 500, 500)
    win.setCoords(0, 0, 500, 500)
    return win

def drawCircles(numLoop, center, radius, win):
    if numLoop != 0:
        currentCircle = Circle(center, radius)
        currentCircle.setFill("yellow")
        currentCircle.draw(win)

        newRadius = int(radius/2)
        centerX = center.getX()
        centerY = center.getY()
        newTopCenter = Point(centerX, centerY + radius + newRadius)
        newRightCenter = Point(centerX + radius + newRadius, centerY)
        drawCircles(numLoop-1, newTopCenter, newRadius, win)
        drawCircles(numLoop-1, newRightCenter, newRadius, win)

def main():
    numLoops = int(input("How many layers deep would you like: "))
    win = setUpWindow()
    drawCircles(numLoops, Point(125, 125), 125, win)

    win.getMouse()
    win.close()


main()