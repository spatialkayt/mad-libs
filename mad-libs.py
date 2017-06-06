########### MAD MAD MAD MAD LIBS ###########
noun_list = ["dog", "horse", "yoga block", "crock pot", "can of beans", "couch", "phone",
			"carpet", "foot", "boots", "apron", "art", "ceiling fan"]
			
verb_list = ["admired", "boiled", "calculated", "decorated", "expanded", "floated", "glowed",
			"hammered", "influenced", "judged", "knocked", "launched", "meddled", "pinched"]
	

class GenerateMaddness(object):
	def __init__(self, noun, verb):
		self.noun = noun
		self.verb = verb
		
	def generate_noun(self):
		len_nouns = len(self.noun) - 1
		random_noun = randint(0, len_nouns)
		self.noun = self.noun[random_noun]
		
	def generate_verb(self):
		len_verbs = len(self.verb) - 1
		random_verb = randint(0, len_verbs)
		self.verb = self.verb[random_verb]
		
	def generate_mad_libs(self):
		self.generate_noun()
		self.generate_verb()
		print "How did it feel when you %s my %s?" % (self.verb, self.noun)
		
mad_libs = GenerateMaddness(noun_list, verb_list)
mad_libs.generate_mad_libs()
		
	
	
########### the inspired function ###########
# def generate_madness(noun, verb):
# 	len_nouns = len(noun) - 1
# 	random_noun = randint(0, len_nouns)
# 	noun = noun[random_noun]
# 	
# 	len_verbs = len(verb) - 1
# 	random_verb = randint(0, len_verbs)
# 	verb = verb[random_verb]
# 	
# 	print "How did it feel when you %s my %s?" % (verb, noun)
	
#generate_madness(noun_list, verb_list)