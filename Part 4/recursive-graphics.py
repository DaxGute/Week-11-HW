from graphics import *

"""
Description: For Part 4, this program draws a circle recursively. Its main function
sets up the graphics window and then call a recursive function to draw the objects. 
From the recursive drawing a tree of recursively smaller yellow circles are drawn.
Name: Daxton Gutekunst
Date: Sep. 25 2021
"""

def drawCircles(numLoop, center, radius, win):
    """
    Purpose: This program both draws a circle and (provided it hasn't reached the end
    of its recursion) sets up the next two circles to be drawn to the top and right of
    the original one. This continues on and on until the numloop iterator reaches 0 where
    the recursive loop stops
    Parameters: an iterator that keeps track of the number of levels deep the function goes, 
                the center of the next circle, the radius of the next circle, the window that
                they will be drawn on
    Return Val: None (just draws the circles)
    """
    if numLoop != 0:
        # This draws the circle 
        currentCircle = Circle(center, radius)
        currentCircle.setFill("yellow")
        currentCircle.draw(win)

        #this sets up the next circle 
        newRadius = int(radius/2)
        centerX = center.getX()
        centerY = center.getY()
        newTopCenter = Point(centerX, centerY + radius + newRadius)
        newRightCenter = Point(centerX + radius + newRadius, centerY)
        drawCircles(numLoop-1, newTopCenter, newRadius, win)
        drawCircles(numLoop-1, newRightCenter, newRadius, win)


def main():
    numLoops = int(input("How many layers deep would you like: "))

    win = GraphWin("Recursive Graphics", 500, 500)
    win.setCoords(0, 0, 500, 500)
    win.getMouse()

    drawCircles(numLoops, Point(125, 125), 125, win)

    win.getMouse()
    win.close()
main()