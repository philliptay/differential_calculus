from math import *

def main() :
     print("Welcome to the Program of Differential Calculus. Begin typing your function:\n")
     function = input("f(x) = ")
     f = function_input(function)
     exponential = False
     logOrSqrt = False
     leftDomain = float(input("Enter a minimum domain value: "))
     rightDomain = float(input("Enter a maximum domain value: "))
     critValList = criticalPoint(f, leftDomain, rightDomain)

     if critValList == [] :
          print("No Critical Values.")
     else :
          for i in range(len(critValList)) :
               print("Critical Value At: ("+ str(round(critValList[i][0], 2)) + ", " + str(round(critValList[i][1], 2)) + ")")
               
     maximaEtMinima(f, leftDomain, rightDomain)
     
     inflectPointList = inflection(f, leftDomain, rightDomain)
     if inflectPointList == [] :
          print("No Inflection Points.")
     else :
          for i in range(len(inflectPointList)) :
               print("Inflection Point At: ("+ str(round(inflectPointList[i][0], 5)) + ", " + str(round(inflectPointList[i][1], 5)) + ")")

               
     
     increasingValues = increasing(f, leftDomain, rightDomain)
     print("Increasing: " + increasingValues[0])
     print("Decreasing: " + increasingValues[1])
     
               
     concaveValues = concavity(f, leftDomain, rightDomain)
     print("Concave Up: " + concaveValues[0])
     print("Concave Down: " + concaveValues[1])

          
     
def function_input(prompt) :
    user_input = prompt
    user_input = user_input.replace("^", "**")
    user_input = user_input.replace("0x", "0*x")
    user_input = user_input.replace("1x", "1*x")
    user_input = user_input.replace("2x", "2*x")
    user_input = user_input.replace("3x", "3*x")
    user_input = user_input.replace("4x", "5*x")
    user_input = user_input.replace("5x", "5*x")
    user_input = user_input.replace("6x", "6*x")
    user_input = user_input.replace("7x", "7*x")
    user_input = user_input.replace("8x", "8*x")
    user_input = user_input.replace("9x", "9*x")
    user_input = user_input.replace(")(", ")*(")
    user_input = user_input.replace(")x", ")*x")
    user_input = user_input.replace("x(", "x*(")                                   
    return lambda x: eval(user_input)

def criticalPoint(f, leftDomain, rightDomain) :
     critValList = []
     x = leftDomain
     criticalValues = False
     firstIteration = True
     while x >= leftDomain and x <= rightDomain :
          critValPos = x
          fDoublePrime = round(secondDeriv(f, critValPos), 3)         
               
          if fDoublePrime != 0 :
               while abs(deriv(f, critValPos)) > 0.00001 :
                    critValPos = critValPos - deriv(f, critValPos)/secondDeriv(f, critValPos)
                    
               if firstIteration :
                    oldCritValPos = critValPos
                    if critValPos >= leftDomain and critValPos <= rightDomain :
                         critVal = f(critValPos)                             
                         critValList.append([round(critValPos, 5), round(critVal, 5)])
                         criticalValues = True
                         firstIteration = False
                         
               if abs(critValPos - oldCritValPos) > 0.1 and critValPos >= leftDomain and critValPos <= rightDomain :
                    critVal = f(round(critValPos, 5))
                    oldCritValPos = critValPos
                    if [round(critValPos, 5), round(critVal, 5)] not in critValList :
                         critValList.append([round(critValPos, 5), round(critVal, 5)])
                    
          x += 1
   
     return sorted(critValList)

def maximaEtMinima(f, leftDomain, rightDomain):
     critValList = criticalPoint(f, leftDomain, rightDomain)
     for i in range(len(critValList)) :
          if secondDeriv(f, round(critValList[i][0], 2)) < 0 :
               print("Maximum: (" + str(critValList[i][0]) + ", " + str(round(f(critValList[i][0]), 5)) + ")")
          elif secondDeriv(f, round(critValList[i][0], 2)) > 0 :
               print("Minimum: (" + str(critValList[i][0]) + ", " + str(round(f(critValList[i][0]), 5)) + ")")
     if critValList == [] :
          print("No Minima Or Maxima Over Domain.")


def increasing(f, leftDomain, rightDomain) :
     decreasingStr = ""
     increasingStr = ""
     critValList = criticalPoint(f, leftDomain, rightDomain)
     if deriv(f, leftDomain) < 0 :
          sign = -1
          decreasingStr += "(" + str(leftDomain) + ", "

     elif deriv(f, leftDomain) > 0 :
          sign = 1
          increasingStr = "(" + str(leftDomain) + ", "
                    
     for i in range(len(critValList)) :
               if sign < 0 and deriv(f, critValList[i][0] + 0.1) > 0 :
                    sign = 1
                    decreasingStr += str(critValList[i][0]) + "], "
                    increasingStr += "[" + str(critValList[i][0]) + ", "
                         
               if sign > 0 and deriv(f, critValList[i][0] + 0.1) < 0 :
                    sign = -1 
                    decreasingStr += "[" + str(critValList[i][0]) + ", "
                    increasingStr += str(critValList[i][0]) + "], "
                    
     if deriv(f, rightDomain) < 0 :
          decreasingStr += str(rightDomain) + ")"
                    
     elif deriv(f, rightDomain) > 0 :
          increasingStr += str(rightDomain) + ")"

     increasingStr = increasingStr.rstrip(", ")
     decreasingStr = decreasingStr.rstrip(", ")

     if increasingStr == "" :
          increasingStr = "Function Not Increasing Over Domain."
     if decreasingStr == "" :
          decreasingStr = "Function Not Decreasing Over Domain."
 
     return [increasingStr, decreasingStr]


def inflection(f, leftDomain, rightDomain) :
     inflectValList = []
     x = leftDomain
     inflectValues = False
     firstIteration = True
     while x >= leftDomain and x <= rightDomain :
          inflectValPos = x
          fTriplePrime = round(thirdDeriv(f, inflectValPos), 3)         
               
          if fTriplePrime != 0 :
               while abs(secondDeriv(f, inflectValPos)) > 0.00001 :
                    inflectValPos = inflectValPos - secondDeriv(f, inflectValPos)/thirdDeriv(f, inflectValPos)
                    
               if firstIteration :
                    oldInflectValPos = inflectValPos
                    if inflectValPos >= leftDomain and inflectValPos <= rightDomain :
                         inflectVal = f(inflectValPos)
                         inflectValList.append((round(inflectValPos, 5), round(inflectVal, 5)))
                         inflectValues = True
                         firstIteration = False
                         
               if abs(inflectValPos - oldInflectValPos) > 0.01 and inflectValPos >= leftDomain and inflectValPos <= rightDomain :
                    inflectVal = f(inflectValPos)
                    oldInflectValPos = inflectValPos
                    if (round(inflectValPos, 5), round(inflectVal, 5)) not in inflectValList :
                         inflectValList.append((round(inflectValPos, 5), round(inflectVal, 5)))
          x += 1
     
     return sorted(inflectValList)


def concavity(f, leftDomain, rightDomain) :
     concaveDownStr = ""
     concaveUpStr = ""
     inflectPointList = inflection(f, leftDomain, rightDomain)
     if secondDeriv(f, leftDomain) < 0 :
          sign = -1
          concaveDownStr += "(" + str(leftDomain) + ", "

     elif secondDeriv(f, leftDomain) > 0 :
          sign = 1
          concaveUpStr = "(" + str(leftDomain) + ", "
                    
     for i in range(len(inflectPointList)) :
               if sign < 0 and secondDeriv(f, inflectPointList[i][0] + 0.1) > 0 :
                    sign = 1
                    concaveDownStr += str(round(inflectPointList[i][0], 5)) + "], "
                    concaveUpStr += "[" + str(round(inflectPointList[i][0], 5)) + ", "
                         
               if sign > 0 and secondDeriv(f, inflectPointList[i][0] + 0.1) < 0 :
                    sign = -1 
                    concaveDownStr += "[" + str(round(inflectPointList[i][0], 5)) + ", "
                    concaveUpStr += str(round(inflectPointList[i][0], 5)) + "], "
                    
     if secondDeriv(f, rightDomain) < 0 :
          concaveDownStr += str(rightDomain) + ")"
                    
     elif secondDeriv(f, rightDomain) > 0 :
          concaveUpStr += str(rightDomain) + ")"

     concaveUpStr = concaveUpStr.rstrip(", ")
     concaveDownStr = concaveDownStr.rstrip(", ")

     if concaveUpStr == "" :
          concaveUpStr = "Function Not Concave Up Over Domain."
     if concaveDownStr == "" :
          concaveDownStr = "Function Not Concave Down Over Domain."
 
     return [concaveUpStr, concaveDownStr]

     
def deriv(f, x) :
     h = 0.001
     dy = f(x+h) - f(x-h)    
     dx = 2*h
     return dy/dx
     
def secondDeriv(f, x) :
     h = 0.01
     y2 = deriv(f, x+h)
     y1 = deriv(f, x-h)
     return (y2 - y1)/(2*h)

def thirdDeriv(f, x) :
     h = 0.001
     y2 = secondDeriv(f, x+h)
     y1 = secondDeriv(f, x-h)
     return (y2 - y1)/(2*h)
         
              
main()


         
         
         
