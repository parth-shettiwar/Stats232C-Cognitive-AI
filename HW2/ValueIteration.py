class ValueIteration(object):
	def __init__(self, transitionTable, rewardTable, valueTable, convergenceTolerance, gamma):
		self.transitionTable = transitionTable
		self.rewardTable  = rewardTable
		self.valueTable = valueTable
		self.convergenceTolerance = convergenceTolerance
		self.gamma = gamma

	def __call__(self):

        #######################################
        ########## YOUR CODE HERE #############
        #######################################
		all_states = []
		policyTable = {}
		actions = [(0,1),(1,0),(0,-1),(-1,0)]
		for keys,values in self.transitionTable.items():
			all_states.append(keys)
		delta = 1e10

		while(delta>=self.convergenceTolerance):
			delta = 0
			s = len(self.transitionTable)
			self.valueTable2 = self.valueTable.copy()
			for i in range(s):
				v = self.valueTable[all_states[i]]
				maxx = -1e10
				for j in range(len(actions)):
					next_state = list(self.transitionTable[all_states[i]][actions[j]])
					summ = 0
					for kk in range(len(next_state)):

						prob = self.transitionTable[all_states[i]][actions[j]][next_state[kk]]
						exp_reward = (self.valueTable[next_state[kk]]*self.gamma + self.rewardTable[all_states[i]][actions[j]][next_state[kk]])
						summ += (prob*exp_reward)
					maxx = max(maxx,summ)
				self.valueTable2[all_states[i]] = maxx	
				delta =	max(delta,abs(v-maxx))
			self.valueTable = self.valueTable2.copy()	
		stateValues = self.valueTable
		for i in range(s):
				val = []
				for j in range(len(actions)):
					next_state = list(self.transitionTable[all_states[i]][actions[j]])
					summ = 0
					for kk in range(len(next_state)):
				
						prob = self.transitionTable[all_states[i]][actions[j]][next_state[kk]]
						exp_reward = (self.valueTable[next_state[kk]]*self.gamma + self.rewardTable[all_states[i]][actions[j]][next_state[kk]])
						summ += (prob*exp_reward)
					val.append(summ)
				maxx = max(val)
				count = val.count(maxx)
				for j in range(len(actions)):
					if(all_states[i] not in policyTable):
						if(val[j]==maxx):
							policyTable[all_states[i]] = {actions[j]:1/count}
					else:
						if(actions[j] not in policyTable):
							if(val[j]==maxx):
								policyTable[all_states[i]][actions[j]] = 1/count
						

		return([stateValues, policyTable])


def viewDictionaryStructure(d, levels, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(levels[indent]) + ": "+ str(key))
        if isinstance(value, dict):
            viewDictionaryStructure(value, levels, indent+1)
        else:
            print('\t' * (indent+1) + str(levels[indent+1])+ ": " + str(value))



def main():
	"""
	Example 1: Deterministic Transition
	When transitions are deterministic, the optimal policy is always to take the action or actions that move you closer to the goal state while avoiding the trap.
	"""
	    
	transitionTableDet = {(0, 0): {(1, 0): {(1, 0): 1},(0, 1): {(0, 1): 1},(-1, 0): {(0, 0): 1},(0, -1): {(0, 0): 1}},(0, 1): {(1, 0): {(1, 1): 1},(0, 1): {(0, 2): 1},(-1, 0): {(0, 1): 1},(0, -1): {(0, 0): 1}},(0, 2): {(1, 0): {(1, 2): 1},(0, 1): {(0, 3): 1},(-1, 0): {(0, 2): 1},(0, -1): {(0, 1): 1}},(0, 3): {(1, 0): {(1, 3): 1},(0, 1): {(0, 4): 1},(-1, 0): {(0, 3): 1},(0, -1): {(0, 2): 1}},(0, 4): {(1, 0): {(1, 4): 1},(0, 1): {(0, 4): 1},(-1, 0): {(0, 4): 1},(0, -1): {(0, 3): 1}},(1, 0): {(1, 0): {(2, 0): 1},(0, 1): {(1, 1): 1},(-1, 0): {(0, 0): 1},(0, -1): {(1, 0): 1}},(1, 1): {(1, 0): {(2, 1): 1},(0, 1): {(1, 2): 1},(-1, 0): {(0, 1): 1},(0, -1): {(1, 0): 1}},(1, 2): {(1, 0): {(2, 2): 1},(0, 1): {(1, 3): 1},(-1, 0): {(0, 2): 1},(0, -1): {(1, 1): 1}},(1, 3): {(1, 0): {(2, 3): 1},(0, 1): {(1, 4): 1},(-1, 0): {(0, 3): 1},(0, -1): {(1, 2): 1}},(1, 4): {(1, 0): {(2, 4): 1},(0, 1): {(1, 4): 1},(-1, 0): {(0, 4): 1},(0, -1): {(1, 3): 1}},(2, 0): {(1, 0): {(2, 0): 1},(0, 1): {(2, 1): 1},(-1, 0): {(1, 0): 1},(0, -1): {(2, 0): 1}},(2, 1): {(1, 0): {(2, 1): 1},(0, 1): {(2, 2): 1},(-1, 0): {(1, 1): 1},(0, -1): {(2, 0): 1}},(2, 2): {(1, 0): {(2, 2): 1},(0, 1): {(2, 3): 1},(-1, 0): {(1, 2): 1},(0, -1): {(2, 1): 1}},(2, 3): {(1, 0): {(2, 3): 1},(0, 1): {(2, 4): 1},(-1, 0): {(1, 3): 1},(0, -1): {(2, 2): 1}},(2, 4): {(1, 0): {(2, 4): 1},(0, 1): {(2, 4): 1},(-1, 0): {(1, 4): 1},(0, -1): {(2, 3): 1}}}
	rewardTableDet = {(0, 0): {(1, 0): {(1, 0): -1},(0, 1): {(0, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(0, 0): -1}},(0, 1): {(1, 0): {(1, 1): -1},(0, 1): {(0, 2): -1},(-1, 0): {(0, 1): -1},(0, -1): {(0, 0): -1}},(0, 2): {(1, 0): {(1, 2): -1},(0, 1): {(0, 3): -1},(-1, 0): {(0, 2): -1},(0, -1): {(0, 1): -1}},(0, 3): {(1, 0): {(1, 3): -1},(0, 1): {(0, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(0, 2): -1}},(0, 4): {(1, 0): {(1, 4): -1},(0, 1): {(0, 4): -1},(-1, 0): {(0, 4): -1},(0, -1): {(0, 3): -1}},(1, 0): {(1, 0): {(2, 0): -1},(0, 1): {(1, 1): -1},(-1, 0): {(0, 0): -1},(0, -1): {(1, 0): -1}},(1, 1): {(1, 0): {(2, 1): 10},(0, 1): {(1, 2): 10},(-1, 0): {(0, 1): 10},(0, -1): {(1, 0): 10}},(1, 2): {(1, 0): {(2, 2): -100},(0, 1): {(1, 3): -100},(-1, 0): {(0, 2): -100},(0, -1): {(1, 1): -100}},(1, 3): {(1, 0): {(2, 3): -1},(0, 1): {(1, 4): -1},(-1, 0): {(0, 3): -1},(0, -1): {(1, 2): -1}},(1, 4): {(1, 0): {(2, 4): -1},(0, 1): {(1, 4): -1},(-1, 0): {(0, 4): -1},(0, -1): {(1, 3): -1}},(2, 0): {(1, 0): {(2, 0): -1},(0, 1): {(2, 1): -1},(-1, 0): {(1, 0): -1},(0, -1): {(2, 0): -1}},(2, 1): {(1, 0): {(2, 1): -1},(0, 1): {(2, 2): -1},(-1, 0): {(1, 1): -1},(0, -1): {(2, 0): -1}},(2, 2): {(1, 0): {(2, 2): -1},(0, 1): {(2, 3): -1},(-1, 0): {(1, 2): -1},(0, -1): {(2, 1): -1}},(2, 3): {(1, 0): {(2, 3): -1},(0, 1): {(2, 4): -1},(-1, 0): {(1, 3): -1},(0, -1): {(2, 2): -1}},(2, 4): {(1, 0): {(2, 4): -1},(0, 1): {(2, 4): -1},(-1, 0): {(1, 4): -1},(0, -1): {(2, 3): -1}}}
	valueTableDet = {(0, 0): 0,(0, 1): 0,(0, 2): 0,(0, 3): 0,(0, 4): 0,(1, 0): 0,(1, 1): 0,(1, 2): 0,(1, 3): 0,(1, 4): 0,(2, 0): 0,(2, 1): 0,(2, 2): 0,(2, 3): 0,(2, 4): 0}
	convergenceTolerance = 10e-7
	gamma = .9


	"""
	Example 2: Probabilistic Transition

	"""
	transitionTable = {(0, 0): {(1, 0): {(1, 0): 0.7, (0, 1): 0.2, (0, 0): 0.1},(0, 1): {(0, 1): 0.7999999999999999, (1, 0): 0.2},(-1, 0): {(0, 0): 0.7, (1, 0): 0.2, (0, 1): 0.1},(0, -1): {(0, 0): 0.7, (1, 0): 0.1, (0, 1): 0.2}},(0, 1): {(1, 0): {(1, 1): 0.7999999999999999, (0, 1): 0.1, (0, 2): 0.1},(0, 1): {(0, 2): 0.7999999999999999, (0, 0): 0.2},(-1, 0): {(0, 1): 0.8999999999999999, (0, 0): 0.1},(0, -1): {(0, 0): 0.7999999999999999, (0, 2): 0.1, (0, 1): 0.1}},(0, 2): {(1, 0): {(1, 2): 0.7999999999999999, (0, 1): 0.2},(0, 1): {(0, 3): 0.7999999999999999, (0, 1): 0.1, (1, 2): 0.1},(-1, 0): {(0, 2): 0.7, (0, 1): 0.1, (1, 2): 0.1, (0, 3): 0.1},(0, -1): {(0, 1): 0.8999999999999999, (0, 3): 0.1}},(0, 3): {(1, 0): {(1, 3): 0.8999999999999999, (0, 2): 0.1},(0, 1): {(0, 3): 0.9999999999999999},(-1, 0): {(0, 3): 0.7999999999999999, (0, 2): 0.1, (1, 3): 0.1},(0, -1): {(0, 2): 0.7999999999999999, (0, 3): 0.2}},(1, 0): {(1, 0): {(2, 0): 0.8999999999999999, (1, 1): 0.1},(0, 1): {(1, 1): 0.8999999999999999, (1, 0): 0.1},(-1, 0): {(0, 0): 0.7, (1, 1): 0.2, (2, 0): 0.1},(0, -1): {(1, 0): 0.7999999999999999, (0, 0): 0.2}},(1, 1): {(1, 0): {(2, 1): 0.7999999999999999, (1, 0): 0.1, (0, 1): 0.1},(0, 1): {(1, 2): 0.7, (2, 1): 0.30000000000000004},(-1, 0): {(0, 1): 0.7, (2, 1): 0.1, (1, 0): 0.2},(0, -1): {(1, 0): 0.7999999999999999, (0, 1): 0.1, (2, 1): 0.1}},(1, 2): {(1, 0): {(2, 2): 0.7999999999999999, (1, 3): 0.1, (1, 1): 0.1},(0, 1): {(1, 3): 0.8999999999999999, (2, 2): 0.1},(-1, 0): {(0, 2): 0.8999999999999999, (1, 1): 0.1},(0, -1): {(1, 1): 0.7999999999999999, (2, 2): 0.1, (0, 2): 0.1}},(1, 3): {(1, 0): {(2, 3): 0.7999999999999999, (1, 3): 0.2},(0, 1): {(1, 3): 0.7999999999999999, (2, 3): 0.1, (0, 3): 0.1},(-1, 0): {(0, 3): 0.7, (2, 3): 0.1, (1, 2): 0.2},(0, -1): {(1, 2): 0.7999999999999999, (0, 3): 0.2}},(2, 0): {(1, 0): {(3, 0): 0.8999999999999999, (2, 0): 0.1},(0, 1): {(2, 1): 0.7999999999999999, (3, 0): 0.1, (1, 0): 0.1},(-1, 0): {(1, 0): 0.7, (2, 0): 0.2, (2, 1): 0.1},(0, -1): {(2, 0): 0.7, (2, 1): 0.2, (1, 0): 0.1}},(2, 1): {(1, 0): {(3, 1): 0.7999999999999999, (1, 1): 0.2},(0, 1): {(2, 2): 0.7, (1, 1): 0.1, (3, 1): 0.2},(-1, 0): {(1, 1): 0.7, (2, 0): 0.1, (2, 2): 0.1, (3, 1): 0.1},(0, -1): {(2, 0): 0.7, (1, 1): 0.2, (3, 1): 0.1}},(2, 2): {(1, 0): {(3, 2): 0.7, (1, 2): 0.1, (2, 1): 0.2},(0, 1): {(2, 3): 0.7999999999999999, (2, 1): 0.2},(-1, 0): {(1, 2): 0.7999999999999999, (2, 1): 0.1, (3, 2): 0.1},(0, -1): {(2, 1): 0.7999999999999999, (1, 2): 0.1, (3, 2): 0.1}},(2, 3): {(1, 0): {(3, 3): 0.7, (2, 3): 0.2, (2, 2): 0.1},(0, 1): {(2, 3): 0.7999999999999999, (2, 2): 0.1, (3, 3): 0.1},(-1, 0): {(1, 3): 0.8999999999999999, (2, 3): 0.1},(0, -1): {(2, 2): 0.7, (3, 3): 0.1, (1, 3): 0.1, (2, 3): 0.1}},(3, 0): {(1, 0): {(3, 0): 0.7, (3, 1): 0.1, (2, 0): 0.2},(0, 1): {(3, 1): 0.7999999999999999, (2, 0): 0.2},(-1, 0): {(2, 0): 0.7999999999999999, (3, 0): 0.2},(0, -1): {(3, 0): 0.7999999999999999, (2, 0): 0.1, (3, 1): 0.1}},(3, 1): {(1, 0): {(3, 1): 0.8999999999999999, (3, 2): 0.1},(0, 1): {(3, 2): 0.7, (2, 1): 0.2, (3, 0): 0.1},(-1, 0): {(2, 1): 0.7999999999999999, (3, 0): 0.1, (3, 1): 0.1},(0, -1): {(3, 0): 0.7999999999999999, (2, 1): 0.2}},(3, 2): {(1, 0): {(3, 2): 0.7999999999999999, (3, 1): 0.1, (2, 2): 0.1},(0, 1): {(3, 3): 0.7, (3, 2): 0.2, (2, 2): 0.1},(-1, 0): {(2, 2): 0.9999999999999999},(0, -1): {(3, 1): 0.7999999999999999, (3, 3): 0.1, (3, 2): 0.1}},(3, 3): {(1, 0): {(3, 3): 0.7999999999999999, (3, 2): 0.2},(0, 1): {(3, 3): 0.7999999999999999, (3, 2): 0.2},(-1, 0): {(2, 3): 0.7999999999999999, (3, 2): 0.1, (3, 3): 0.1},(0, -1): {(3, 2): 0.7999999999999999, (2, 3): 0.2}}}
	rewardTable = {(0, 0): {(1, 0): {(1, 0): -1, (0, 1): -1, (0, 0): -1},(0, 1): {(0, 1): -1, (1, 0): -1},(-1, 0): {(0, 0): -1, (1, 0): -1, (0, 1): -1},(0, -1): {(0, 0): -1, (1, 0): -1, (0, 1): -1}},(0, 1): {(1, 0): {(1, 1): -1, (0, 1): -1, (0, 2): -1},(0, 1): {(0, 2): -1, (0, 0): -1},(-1, 0): {(0, 1): -1, (0, 0): -1},(0, -1): {(0, 0): -1, (0, 2): -1, (0, 1): -1}},(0, 2): {(1, 0): {(1, 2): -1, (0, 1): -1},(0, 1): {(0, 3): -1, (0, 1): -1, (1, 2): -1},(-1, 0): {(0, 2): -1, (0, 1): -1, (1, 2): -1, (0, 3): -1},(0, -1): {(0, 1): -1, (0, 3): -1}},(0, 3): {(1, 0): {(1, 3): -1, (0, 2): -1},(0, 1): {(0, 3): -1},(-1, 0): {(0, 3): -1, (0, 2): -1, (1, 3): -1},(0, -1): {(0, 2): -1, (0, 3): -1}},(1, 0): {(1, 0): {(2, 0): -1, (1, 1): -1},(0, 1): {(1, 1): -1, (1, 0): -1},(-1, 0): {(0, 0): -1, (1, 1): -1, (2, 0): -1},(0, -1): {(1, 0): -1, (0, 0): -1}},(1, 1): {(1, 0): {(2, 1): -100, (1, 0): -100, (0, 1): -100},(0, 1): {(1, 2): -100, (2, 1): -100},(-1, 0): {(0, 1): -100, (2, 1): -100, (1, 0): -100},(0, -1): {(1, 0): -100, (0, 1): -100, (2, 1): -100}},(1, 2): {(1, 0): {(2, 2): -1, (1, 3): -1, (1, 1): -1},(0, 1): {(1, 3): -1, (2, 2): -1},(-1, 0): {(0, 2): -1, (1, 1): -1},(0, -1): {(1, 1): -1, (2, 2): -1, (0, 2): -1}},(1, 3): {(1, 0): {(2, 3): -1, (1, 3): -1},(0, 1): {(1, 3): -1, (2, 3): -1, (0, 3): -1},(-1, 0): {(0, 3): -1, (2, 3): -1, (1, 2): -1},(0, -1): {(1, 2): -1, (0, 3): -1}},(2, 0): {(1, 0): {(3, 0): -1, (2, 0): -1},(0, 1): {(2, 1): -1, (3, 0): -1, (1, 0): -1},(-1, 0): {(1, 0): -1, (2, 0): -1, (2, 1): -1},(0, -1): {(2, 0): -1, (2, 1): -1, (1, 0): -1}},(2, 1): {(1, 0): {(3, 1): -1, (1, 1): -1},(0, 1): {(2, 2): -1, (1, 1): -1, (3, 1): -1},(-1, 0): {(1, 1): -1, (2, 0): -1, (2, 2): -1, (3, 1): -1},(0, -1): {(2, 0): -1, (1, 1): -1, (3, 1): -1}},(2, 2): {(1, 0): {(3, 2): -1, (1, 2): -1, (2, 1): -1},(0, 1): {(2, 3): -1, (2, 1): -1},(-1, 0): {(1, 2): -1, (2, 1): -1, (3, 2): -1},(0, -1): {(2, 1): -1, (1, 2): -1, (3, 2): -1}},(2, 3): {(1, 0): {(3, 3): -1, (2, 3): -1, (2, 2): -1},(0, 1): {(2, 3): -1, (2, 2): -1, (3, 3): -1},(-1, 0): {(1, 3): -1, (2, 3): -1},(0, -1): {(2, 2): -1, (3, 3): -1, (1, 3): -1, (2, 3): -1}},(3, 0): {(1, 0): {(3, 0): -1, (3, 1): -1, (2, 0): -1},(0, 1): {(3, 1): -1, (2, 0): -1},(-1, 0): {(2, 0): -1, (3, 0): -1},(0, -1): {(3, 0): -1, (2, 0): -1, (3, 1): -1}},(3, 1): {(1, 0): {(3, 1): -1, (3, 2): 10},(0, 1): {(3, 2): 10, (2, 1): 10, (3, 0): 10},(-1, 0): {(2, 1): 10, (3, 0): 10, (3, 1): -1},(0, -1): {(3, 0): 10, (2, 1): 10}},(3, 2): {(1, 0): {(3, 2): -1, (3, 1): -1, (2, 2): -1},(0, 1): {(3, 3): -1, (3, 2): -1, (2, 2): -1},(-1, 0): {(2, 2): -1},(0, -1): {(3, 1): -1, (3, 3): -1, (3, 2): -1}},(3, 3): {(1, 0): {(3, 3): -1, (3, 2): -1},(0, 1): {(3, 3): -1, (3, 2): -1},(-1, 0): {(2, 3): -1, (3, 2): -1, (3, 3): -1},(0, -1): {(3, 2): -1, (2, 3): -1}}}
	valueTable = {(0, 0): 0,(0, 1): 0,(0, 2): 0,(0, 3): 0,(1, 0): 0,(1, 1): 0,(1, 2): 0,(1, 3): 0,(2, 0): 0,(2, 1): 0,(2, 2): 0,(2, 3): 0,(3, 0): 0,(3, 1): 0,(3, 2): 0,(3, 3): 0}
	convergenceTolerance = 10e-7
	gamma = .9


	
	# Uncomment to view transition or reward structure in a readable format

	# levelsReward  = ["state", "action", "next state", "reward"]
	# levelsTransition  = ["state", "action", "next state", "probability"]

	# viewDictionaryStructure(transitionTableDet, levelsTransition)
	# viewDictionaryStructure(rewardTableDet, levelsReward)
	

	performValueIteration = ValueIteration(transitionTableDet, rewardTableDet, valueTableDet, convergenceTolerance, gamma)
	optimalValuesDeterminsitic, policyTableDet = performValueIteration()
	print(optimalValuesDeterminsitic)
	print(policyTableDet)


	performValueIteration = ValueIteration(transitionTable, rewardTable, valueTable, convergenceTolerance, gamma)
	optimalValuesDeterminsitic, policyTable = performValueIteration()
	print(optimalValuesDeterminsitic)
	print(policyTable)
	

if __name__ == '__main__':
	main()