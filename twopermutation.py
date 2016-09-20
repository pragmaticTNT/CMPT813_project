import itertools
import math
import random

## RETURN: (LIST) list of n integers [a_1,...a_n] such that 1 <= a_i <= maxVal
def GenNLengths( n, maxVal ):
    ## return [ int(random.random()*maxVal)+1 for i in range(n) ]
    return random.sample( range(1, maxVal), n )

## RETURN: (LIST, LIST, LIST)
##    - theta: randomly generated n-partition of 2PI
##    - maxPrm: permutation which generates maximum area umbrella
##    - minPrm: permutation which generates minimum area umbrella
def BestPermutation( A, B ):
    permutations = [ p for p in itertools.permutations( A ) ]
    values = [ permval( p, B ) for p in permutations ]
    perm_val = zip( permutations, values ) 
    return max( perm_val, key=lambda x: x[1] )

def permval( A, B ):
    n = len(A)
    return sum( [ A[(i+1)%n]*A[i]*B[i] for i in range(n)] )

def Trial( n, maxVal, rodTrials ):
    B = GenNLengths( n, maxVal )
    A_index = [ i+1 for i in range(n) ]
    order = [ i-1 for i in BestPermutation( A_index, B )[0] ]

    print "==> Starting Trial..."
    print "==  B:    ", B
    print "==  Order:", order

    for i in range( rodTrials ):
        A = GenNLengths( n, maxVal )
        bestPerm =  BestPermutation( A, B )
        A.sort()
        A_ordered = map(lambda i: A[i], order)
        orderedVal = permval( A_ordered, B )
        if orderedVal < bestPerm[1]:
            print "\n==  B:       ", B
            print "==  Order:", order
            print "==  [ERR] Best:", bestPerm[0], "Ordered:", A_ordered
            print "==  BestVal:", bestPerm[1], "OrderedVal:", orderedVal
            return False
        print "==  Best A:", bestPerm[0], "ok."

    return True 

def main():
    n           = 4
    MAXVAL      = 10
    NUMTRIALS   = 1
    RODTRIALS   = 20

    for i in range( NUMTRIALS ):
        if not Trial( n, MAXVAL, RODTRIALS ):
            print "XXXXXXXXXX GAME OVER! XXXXXXXXXX"
            break
        print "\n"

if __name__ == '__main__':
    main()
