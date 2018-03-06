import string
#To remove stop words for better processing
class DataProcessing1():
	def __init__(self,file_name):
		self.stopwords=['ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some',
				'for','do','its','yours','such','into','of','most','itself','other','off','is','s','am','or','who','as','from','him','each','the','themselves','until','below',
				'are','we','these','your','his','through','don','nor','me','were','her','more','himself','this','down','should','our','their','while','above','both','up','to',
				'ours','had','she','all','no','when','at','any','before','them','same','and','been','have','in','will','on','does','yourselves','then','that','because','what',
				'over','why','so','can','did','just','where','too','only','myself','which','those','i','after','few','whom','t','being','if','theirs','my','against','a','by','doing',
				'it','how','further','was','here','than','0','1','2','3','4','5','6','7','8','9','@','#','$',':','.',';','?','-']

		self.processed_lines=[]
		self.punctuation = string.punctuation
		self.extraSpaces = ["\n","\t"]
		self.removeStopWords(file_name)


	def removeStopWords(self,file_name):
		with open(file_name,"r") as f:
			for line in f:
				line = line.lower()
				line = line.split(" ")
				self.processed_lines.append([word for word in line if word not in self.stopwords]) 
		self.removePunctuation()		
		with open("ProcessedData.txt","w") as f:
			for line in self.processed_lines:
				for i in range(len(line)-1):
					f.write(line[i]+" ")

				f.write(line[len(line)-1])
				f.write("\n")
	def removePunctuation(self):
		for i in range(len(self.processed_lines)):
			for j in range(len(self.processed_lines[i])):
				self.processed_lines[i][j] = "".join(char for char in self.processed_lines[i][j] if char not in self.punctuation and char not in self.extraSpaces)

		
				
								
										

								
obj = DataProcessing1("F://AI Project//Dataset//trainingdata.txt")
#obj = DataProcessing1("text.txt")


