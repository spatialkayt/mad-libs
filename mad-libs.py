import random

########### MAD MAD MAD MAD LIBS ###########

import random  # to get the .choice method

noun_list = ["dog", "horse", "yoga block", "crock pot", "can of beans", "couch", "phone",
             "carpet", "foot", "boots", "apron", "art", "ceiling fan"]

verb_list = ["admired", "boiled", "calculated", "decorated", "expanded", "floated", "glowed",
             "hammered", "influenced", "judged", "knocked", "launched", "meddled", "pinched"]


class GenerateMaddness(object):
    def __init__(self, noun, verb):

        self.noun = noun  # TODO fix this bug -- why is it a bug???
        self.verb = verb  # TODO fix this bug -- why is it a bug???
        self.madlibs = ["How did it feel when you {} my {}, you rotten scumbag?",  # TODO -- what is this {} nonsense?!
                        "What kind of rotten eejit would have {} my {}????",
                        "You claim to be humane after you {} my precious {}??",
                        "Only a miscreant would have {} my sacred {} without asking!!!"]

    def get_random_word_from_list(self, word_list):
        len_word_list = len(word_list)
        random_word_index = random.randint(0, len_word_list-1)
        return word_list[random_word_index]

    def generate_noun(self):
        # len_nouns = len(self.noun) - 1
        # random_noun = randint(0, len_nouns)
        # self.noun = self.noun[random_noun]
        self.noun = self.get_random_word_from_list(self.noun)    # TODO: ugly bug here

    def generate_verb(self):
        # len_verbs = len(self.verb) - 1
        # random_verb = randint(0, len_verbs)
        # self.verb = self.verb[random_verb]
        self.verb = self.get_random_word_from_list(self.verb)    # TODO: ugly bug here


    def generate_mad_libs(self):
        self.generate_noun()
        self.generate_verb()
        print "How did it feel when you %s my %s?" % (self.verb, self.noun)

        
        print self.generate_madlib(self.verb, self.noun)
        print "\nBut.. but... Why does THIS work every time????:"
        print self.generate_madlib(random.choice(verb_list), random.choice(noun_list))



mad_libs = GenerateMaddness(noun_list, verb_list)

print "\nFirst call to generate_mad_libs():...\n"
mad_libs.generate_mad_libs()


print "\nNow try a second time...\n"
mad_libs.generate_mad_libs()  # TODO -- W T F ? ? ?  Why doesn't this work a second time????


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

# generate_madness(noun_list, verb_list)
