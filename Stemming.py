class Stemmer():
	def __init__(self,file_name):
		self.processed_lines = []
		with open(file_name,'r') as f:
			for line in f:
				line = line.lower()
				line = line.split(" ")
				line_process=[]
				for word in line:
					line_process.append(self.stem(word))
				self.processed_lines.append(line_process)

		with open("ProcessedData1.txt","w") as f:
			for line in self.processed_lines:
				for i in range(len(line)-1):
					f.write(line[i]+" ")

				f.write(line[len(line)-1])

	def isVowel(self,char):
		if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
			return True
		else:
			return False
	#*v*
	def containsVowel(self,word):
		for i in range(len(word)):
			if self.isVowel(word[i]):
				return True
			elif(i!=0 and word[i] == 'y' and not self.isVowel(word[i-1])):
				return True
			
		return False

	def containsConsonant(self,word,i):
		if(not self.isVowel(word[i])):
			if(i!=0 and word[i] == 'y' and self.isVowel(word[i-1])):
				return True
			else:
				return False
		else:
			return False
	
	#*d
	def doubleConsonant(self,word):
		if(len(word)>=2 and self.isConsonant(word[-1]) and self.isConsonant(word[-2])):
			return True
		else:
			return False

	def isConsonant(self,char):
		if(not self.isVowel(char)):
			return True
		else:
			return False

	#*S
	def endsWith(self,word,char):
		if word.endswith(char):
			return True
		else:
			return False
	#*o
	def cvc(self,word):
		if(len(word)>=3):
			if(self.isConsonant(word[-3]) and self.isVowel(word[-2]) and self.isConsonant(word[-1])):
				if(word[-1]!='w' and word[-1]!='x' and word[-1]!='y'):
					return True
				else:
					return False
			else:
				return False
		else:
			return False

	#m
	def getM(self,word):
		form = []
		formstr =""
		for i in word:
			if(self.isConsonant(i)):
				form.append('c')
			else:
				form.append('v')
		formstr = "".join(form)
		return formstr.count('vc')

	def replace(self,word,pattern,replace):
		index = word.rfind(pattern)
		new_str = word[0:index]
		return(new_str+replace)

	def replace1(self,word,pattern,replace):
		index = word.rfind(pattern)
		new_str = word[0:index]
		if(self.getM(new_str)>0):
			word = new_str+replace
			return word
		else:
			return word

	def replace2(self,word,pattern,replace):
		index = word.rfind(pattern)
		new_str = word[0:index]
		if(self.getM(new_str)>1):
			word = new_str+replace
			return word
		else:
			return word
	

	def step1a(self,word):
		if word.endswith('sses'):
			self.replace(word,'sses','ss')
		elif word.endswith('ies'):
			self.replace(word,'ies','i')
		elif word.endswith('ss'):
			self.replace(word,'ss','ss')
		elif word.endswith('s'):
			self.replace(word,'s','')
		return word

	def step1b(self,word):
		flag = False
		if(word.endswith('eed')):
			index = word.rfind('eed')
			new_str = word[0:index]
			if(self.getM(new_str)>0):
				word = new_str+"ee"
		elif(word.endswith('ed')):
			index = word.rfind('ed')
			new_str = word[0:index]
			if(self.containsVowel(word)):
				word = new_str
				flag = True
		elif(word.endswith('ing')):
			index = word.rfind('ing')
			new_str = word[0:index]
			if(self.containsVowel(word)):
				word = new_str
				flag = True
		if(flag):
			if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
				word+='e'
			elif(self.doubleConsonant(word) and not self.endsWith(word,'l') and not self.endsWith(word,'s') and not self.endsWith(word,'z')):
				word = word[:-1]
			elif(self.getM(word) == 1 and self.cvc(word)):
				word+='e'

		return word

	def step2(self, word):
		if word.endswith('ational'):
			word = self.replace1(word, 'ational', 'ate')
		elif word.endswith('tional'):
			word = self.replace1(word, 'tional', 'tion')
		elif word.endswith('enci'):
			word = self.replace1(word, 'enci', 'ence')
		elif word.endswith('anci'):
			word = self.replace1(word, 'anci', 'ance')
		elif word.endswith('izer'):
			word = self.replace1(word, 'izer', 'ize')
		elif word.endswith('abli'):
			word = self.replace1(word, 'abli', 'able')
		elif word.endswith('alli'):
			word = self.replace1(word, 'alli', 'al')
		elif word.endswith('entli'):
			word = self.replace1(word, 'entli', 'ent')
		elif word.endswith('eli'):
			word = self.replace1(word, 'eli', 'e')
		elif word.endswith('ousli'):
			word = self.replace1(word, 'ousli', 'ous')
		elif word.endswith('ization'):
			word = self.replace1(word, 'ization', 'ize')
		elif word.endswith('ation'):
			word = self.replace1(word, 'ation', 'ate')
		elif word.endswith('ator'):
			word = self.replace1(word, 'ator', 'ate')
		elif word.endswith('alism'):
			word = self.replace1(word, 'alism', 'al')
		elif word.endswith('iveness'):
			word = self.replace1(word, 'iveness', 'ive')
		elif word.endswith('fulness'):
			word = self.replace1(word, 'fulness', 'ful')
		elif word.endswith('ousness'):
			word = self.replace1(word, 'ousness', 'ous')
		elif word.endswith('aliti'):
			word = self.replace1(word, 'aliti', 'al')
		elif word.endswith('iviti'):
			word = self.replace1(word, 'iviti', 'ive')
		elif word.endswith('biliti'):
			word = self.replace1(word, 'biliti', 'ble')
		return word

	def step3(self, word):
		if word.endswith('icate'):
			word = self.replace1(word, 'icate', 'ic')
		elif word.endswith('ative'):
			word = self.replace1(word, 'ative', '')
		elif word.endswith('alize'):
			word = self.replace1(word, 'alize', 'al')
		elif word.endswith('iciti'):
			word = self.replace1(word, 'iciti', 'ic')
		elif word.endswith('ful'):
			word = self.replace1(word, 'ful', '')
		elif word.endswith('ness'):
			word = self.replace1(word, 'ness', '')
		return word

	def step4(self, word):
		if word.endswith('al'):
			word = self.replace2(word, 'al', '')
		elif word.endswith('ance'):
			word = self.replace2(word, 'ance', '')
		elif word.endswith('ence'):
			word = self.replace2(word, 'ence', '')
		elif word.endswith('er'):
			word = self.replace2(word, 'er', '')
		elif word.endswith('ic'):
			word = self.replace2(word, 'ic', '')
		elif word.endswith('able'):
			word = self.replace2(word, 'able', '')
		elif word.endswith('ible'):
			word = self.replace2(word, 'ible', '')
		elif word.endswith('ant'):
			word = self.replace2(word, 'ant', '')
		elif word.endswith('ement'):
			word = self.replace2(word, 'ement', '')
		elif word.endswith('ment'):
			word = self.replace2(word, 'ment', '')
		elif word.endswith('ent'):
			word = self.replace2(word, 'ent', '')
		elif word.endswith('ou'):
			word = self.replace2(word, 'ou', '')
		elif word.endswith('ism'):
			word = self.replace2(word, 'ism', '')
		elif word.endswith('ate'):
			word = self.replace2(word, 'ate', '')
		elif word.endswith('iti'):
			word = self.replace2(word, 'iti', '')
		elif word.endswith('ous'):
			word = self.replace2(word, 'ous', '')
		elif word.endswith('ive'):
			word = self.replace2(word, 'ive', '')
		elif word.endswith('ize'):
			word = self.replace2(word, 'ize', '')
		elif word.endswith('ion'):
			result = word.rfind('ion')
			new_str = word[:result]
			if self.getM(new_str) > 1 and (self.endsWith(new_str, 's') or self.endsWith(new_str, 't')):
				word = new_str
			word = self.replace2(word, '', '')
		return word

	def step5a(self, word):
		if word.endswith('e'):
			new_str = word[:-1]
			if self.getM(new_str) > 1:
				word = new_str
			elif self.getM(new_str) == 1 and not self.cvc(new_str):
				word = new_str
		return word

	def step5b(self, word):
		if self.getM(word) > 1 and self.doubleConsonant(word) and self.endsWith(word, 'l'):
			word = word[:-1]
		return word

	def stem(self, word):
		word = self.step1a(word)
		word = self.step1b(word)
		word = self.step2(word)
		word = self.step3(word)
		word = self.step4(word)
		#word = self.step5a(word)
		word = self.step5b(word)
		return word


obj = Stemmer("ProcessedData.txt")





