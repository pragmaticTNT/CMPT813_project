import itertools
import math
import random
import sys
import Tkinter

import visualize

## RETURN: (LIST) n-partition of 2*PI
def GenNPartition( n ):
    numParts = n-1
    parts = [ random.random() for i in range(numParts) ]
    parts.sort()
    theta = [ parts[0] ] + [ parts[i]-parts[i-1] for i in range(1,numParts) ] + [ 1-parts[numParts-1] ]
    theta = [ 2*math.pi*i for i in theta ]
    return theta

## RETURN: (LIST) list of n integers [a_1,...a_n] such that 1 <= a_i <= maxVal
def GenNLengths( n, maxVal ):
    return [ int(random.random()*maxVal)+1 for i in range(n) ]

## RETURN: (LIST, LIST, LIST)
##    - theta: randomly generated n-partition of 2PI
##    - maxPrm: permutation which generates maximum area umbrella
##    - minPrm: permutation which generates minimum area umbrella
def FindPermutation( n, maxVal, theta=None, L=None ):
    maxSum = 0
    maxPrm = ()
    minSum = sys.maxint
    minPrm = ()

    if theta is None:
        theta = GenNPartition( n )
    if L is None:
        L = GenNLengths( n, maxVal )
    sinTheta = [ math.sin(i) for i in theta ]
    permutations = itertools.permutations( L )

    print "==>> Starting trial ..."
    print "==   Theta: ", [math.trunc(math.degrees(angleR)) for angleR in theta]
    print "==   sinTheta: ", ["{0:.3f}".format(sinAngle) for sinAngle in sinTheta]
    print "==   Lngth: ", L
    print "==>> Permuting ..."
    for p in permutations:
        area = (1.0/2)*sum( [p[i]*p[i+1]*sinTheta[i] for i in range(n-1)] + [p[n-1]*p[0]*sinTheta[n-1]] )
        if maxSum < area:
            maxSum = area
            maxPrm = p
        if minSum > area:
            minSum = area
            minPrm = p
    print "==>> Best Permutation: ", maxPrm
    print "==   value: ", maxSum
    print "==>> Wort Permutation: ", minPrm
    print "==   Value: ", minSum
    return [theta, maxPrm, minPrm]

def Trail( parts, maxVal, scale, dim, theta=None, L=None ):
    theta, maxPrm, minPrm = FindPermutation(parts, maxVal, theta, L)
    for i in range(1, parts):
        theta[i] = theta[i]+theta[i-1]
    # print "Sumed Theta:", ["{0:.4f}".format(i) for i in theta]

    root = Tkinter.Tk()
    bz = visualize.Visual(root, scale, dim, theta, maxPrm, minPrm)
    root.geometry(str(dim[0])+'x'+str(dim[1])+'+0+0')
    root.mainloop()

def main():
    ## theta = GenNPartition(5)
    ## print "Theta: ", theta, " Total: ", sum(theta)
    ## Trial( 1, 7, 10 )
    PARTS   = 8
    MAXVAL  = 10
    SCALE   = 30
    DIM     = [1200, 600]   # [WIDTH, HEIGHT]

    # => RANDOM n-partition and segment lengths
    Trail(PARTS, MAXVAL, SCALE, DIM)
    # => FIXED n-partition and segment lengths
    # theta   = [math.pi/2, math.pi/6, math.pi/3, math.pi]
    # L       = [1, 2, 3, 4]
    # Trail(len(theta), 0, SCALE, DIM, theta, L)

if __name__ == '__main__':
    main()
