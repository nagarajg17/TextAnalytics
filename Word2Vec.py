import numpy as np
class Vocabulary:
	def __init__(self,filename,window_size):
		self.window_size = window_size
		self.sentences = []
		self.sentence_end = []
		with open(filename,"r") as f:
			for line in f:
				sentence = []
				line = line.split(" ")
				for word in line:
					if(word not in sentence):
						sentence.append(word)
				self.sentences.append(sentence)
				self.sentence_end.append(len(sentence))
		self.vocabulary_size = max(self.sentence_end)
		self.generatePair()

	def generatePair(self):
		self.word_target = []
		for sentence in self.sentences:
			curSentence_target = []
			index_sentence = self.sentences.index(sentence)
			for word in sentence:
				curWord_target = []
				index_word = sentence.index(word)
				i = index_word
				max_traverse = index_word+self.window_size
				while(i<self.sentence_end[index_sentence]-1 and i<max_traverse):
					i+=1
					curWord_target.append((index_word,i))
				i = index_word
				max_traverse = index_word-self.window_size
				while(i>0 and i>max_traverse):
					i-=1
					curWord_target.append((index_word,i))
				curSentence_target.append(curWord_target)
			self.word_target.append(curSentence_target)

	def oneHotEncoding(self,sentence_no,word_no):
		self.encoded_word = []
		index = self.word_target[sentence_no][word_no]
		x = np.array([np.zeros(self.vocabulary_size)])
		x[0][word_no] = 1
		self.encoded_word.append(x)
		for i,j in index:
			x = np.zeros(self.vocabulary_size)
			x[j] = 1
			self.encoded_word.append(x)

class SkipGramModel(Vocabulary):
	def __init__(self,filename,window_size,epocs,learning_rate,no_of_hiddenNeurons):
		Vocabulary.__init__(self,filename,window_size)
		self.no_of_runs = epocs
		self.learning_rate = learning_rate
		self.no_of_features = no_of_hiddenNeurons
		self.prev_error = 100.0
		self.prob = []
		self.vector_representation = []

	def train(self,sentence_no):
		self.input2hiddenWeights = self.generateWeights(self.vocabulary_size,self.no_of_features)
		self.hidden2outputWeights = self.generateWeights(self.no_of_features,self.vocabulary_size)
		for epoc in range(self.no_of_runs):
			sentence_sample = self.word_target[sentence_no]
			for word_context in sentence_sample:
				word_no = word_context[0][0]
				self.forward_backwardPropagation(sentence_no,word_no,word_context)

	def generateWeights(self,no_of_rows,no_of_cols):
		 return(np.random.uniform(low = 0,high = 1,size = (no_of_rows,no_of_cols)))

	def softmax(self,output_activation):
		return np.exp(output_activation)/np.sum(np.exp(output_activation),axis = 0)


	def forward_backwardPropagation(self,sentence_no,word_no,word_context):
		#forward propagation
		self.oneHotEncoding(sentence_no,word_no)
		#print self.word_target
		input_vector = self.encoded_word[0]
		input_vector = input_vector.transpose()
		hidden_activation = np.dot(self.input2hiddenWeights.transpose(),input_vector)
		output_activation = np.dot(self.hidden2outputWeights.transpose(),hidden_activation)
		softmax_probabilities = self.softmax(output_activation).transpose()
		errors = []
		error_sum = 0.0
		for vector in self.encoded_word[1:]:
			error = softmax_probabilities - vector
			errors.append(error)
		sum_of_errors = np.sum(errors,axis = 0)
		error_sum=np.sum(sum_of_errors**2,axis=1)
		print error_sum
		#backward propagation
		if(error_sum<=self.prev_error):
			self.hidden2outputWeights = self.hidden2outputWeights - self.learning_rate*np.dot(hidden_activation,sum_of_errors)
			self.input2hiddenWeights = self.input2hiddenWeights - self.learning_rate*np.dot(input_vector,np.dot(self.hidden2outputWeights,sum_of_errors.transpose()).transpose())
		self.prev_error = error_sum
		self.prob = softmax_probabilities

	def trainSentences(self):
		for sentence_index in range(self.sentences):
			self.train(sentence_index)
			self.vector_representation.append(self.input2hiddenWeights)






obj = SkipGramModel("ProcessedData1.txt",2,250,0.1,5)
obj.train(3)
#print obj.input2hiddenWeights
print obj.prev_error
print obj.prob
#obj.forward_backwardPropagation(0,3, [(3, 4), (3, 5), (3, 2), (3, 1)])



		