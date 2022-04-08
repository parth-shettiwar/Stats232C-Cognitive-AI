

def getPosterior(priorOfA, priorOfB, likelihood):
	
##################################################
#		Your code here
##################################################
    data_prior = 0
    marginalOfA = {}
    marginalOfB = {}
    for k,v in priorOfA.items():
        tem = 0
        for k2,v2 in priorOfB.items():
            tt = (k,k2)
            data_prior += likelihood[tt]*v*v2
            tem += likelihood[tt]*v2
        marginalOfA[k] = tem*v 
    for k,v in marginalOfA.items():
        marginalOfA[k] = (marginalOfA[k]/data_prior)

    data_prior = 0    
    for k,v in priorOfB.items():
        tem = 0
        for k2,v2 in priorOfA.items():
            tt = (k2,k)
            data_prior += likelihood[tt]*v*v2
            tem += likelihood[tt]*v2
        marginalOfB[k] = tem*v
    for k,v in marginalOfB.items():
        marginalOfB[k] = marginalOfB[k]/data_prior  


    return([marginalOfA, marginalOfB])



def main():
    exampleOnePriorofA = {'a0': .5, 'a1': .5}
    exampleOnePriorofB = {'b0': .25, 'b1': .75}
    exampleOneLikelihood = {('a0', 'b0'): 0.42, ('a0', 'b1'): 0.12, ('a1', 'b0'): 0.07, ('a1', 'b1'): 0.02}
    print(getPosterior(exampleOnePriorofA, exampleOnePriorofB, exampleOneLikelihood))

    exampleTwoPriorofA = {'red': 1/10 , 'blue': 4/10, 'green': 2/10, 'purple': 3/10}
    exampleTwoPriorofB = {'x': 1/5, 'y': 2/5, 'z': 2/5}
    exampleTwoLikelihood = {('red', 'x'): 0.2, ('red', 'y'): 0.3, ('red', 'z'): 0.4, ('blue', 'x'): 0.08, ('blue', 'y'): 0.12, ('blue', 'z'): 0.16, ('green', 'x'): 0.24, ('green', 'y'): 0.36, ('green', 'z'): 0.48, ('purple', 'x'): 0.32, ('purple', 'y'): 0.48, ('purple', 'z'): 0.64}
    print(getPosterior(exampleTwoPriorofA, exampleTwoPriorofB, exampleTwoLikelihood))




if __name__ == '__main__':
    main()
