"""
    Description: For Part 4, this program draws a circle recursively. Its main function
    sets up the graphics window and then call a recursive function to draw the objects.
    From the recursive drawing a tree of recursively smaller yellow circles are drawn.
    Author: Daxton Gutekunst
    Date: Sep. 25 2021
"""

from graphics import *

def drawSmiley(center, radius, win):
    """
    Purpose: This method draws a smiley face out of the given parameters, which vary the 
    position and size of said smiley. After creating this smiley, it is drawn on the window 
    Parameters: the center of the smiley to be drawn (Point object), the radius or how big
                the smiley will be drawn (int), the window (window object)
    Return Val: None (just draws the circles)
    """
    currentCircle = Circle(center, radius)
    currentCircle.setFill("yellow")
    currentCircle.draw(win)

    centerX = center.getX()
    centerY = center.getY()

    eyeYOffset = centerY + (radius/2)

    leftCenterX = centerX - (radius/2)
    leftEyeCenter = Point(leftCenterX, eyeYOffset)
    leftEye = Circle(leftEyeCenter, radius/4)
    leftEye.setFill("red")
    leftEye.draw(win)

    rightCenterX = centerX + (radius/2)
    rightEyeCenter = Point(rightCenterX, eyeYOffset)
    rightEye = Circle(rightEyeCenter, radius/4)
    rightEye.setFill("blue")
    rightEye.draw(win)

    lineYOffset = centerY - (radius/3)

    lineLeftX = centerX - (radius/2)
    leftLineCenter = Point(lineLeftX, lineYOffset)
    lineRightX = centerX + (radius/2)
    rightLineCenter = Point(lineRightX, lineYOffset)
    bottomLine = Line(leftLineCenter, rightLineCenter)
    bottomLine.draw(win)

def recursiveGraphs(numLoop, center, radius, win):
    """
    Purpose: This program calls a method to draw smileys and (provided it hasn't reached the end
    of its recursion) sets up the next two smileys to be drawn to the top and right of
    the original one. This continues on and on until the numloop iterator reaches 0 where
    the recursive loop stops
    Parameters: an iterator that keeps track of the number of levels deep the function goes (int),
                the center of the next circle (Point Object), the radius of the next circle (int),
                the window that they will be drawn on (Window Object)
    Return Val: None (just draws the circles)
    """
    if numLoop != 0:
        # This draws the circle
        drawSmiley(center, radius, win)

        #this sets up the next circle
        newRadius = int(radius/2)
        centerX = center.getX()
        centerY = center.getY()
        newTopCenter = Point(centerX, centerY + radius + newRadius)
        newRightCenter = Point(centerX + radius + newRadius, centerY)
        recursiveGraphs(numLoop-1, newTopCenter, newRadius, win)
        recursiveGraphs(numLoop-1, newRightCenter, newRadius, win)


def main():
    numLoops = int(input("How many layers deep would you like: "))

    win = GraphWin("Recursive Graphics", 500, 500)
    win.setCoords(0, 0, 500, 500)
    win.getMouse()

    recursiveGraphs(numLoops, Point(125, 125), 125, win)

    win.getMouse()
    win.close()
main()
