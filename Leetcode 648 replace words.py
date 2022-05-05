class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
            for counter, element in enumerate(dictionary): #use enumerate to get a counter for every element, to pair the root and successor, we found word in dictionary shorter than word in sentence then replace like "cattle" to "cat"
                for i in dictionary:
                    if i == element[0:len(i)]:
                        dictionary[counter] = i
                        
                        split_sentence = sentence.split() # split word in sentence

                        
            for counter, word in enumerate(split_sentence): #if word in splited sentences matches dictionary
                
                for i in dictionary:
                    if i == word[0:len(i)]: #count length of sentence
                        split_sentence[counter] = i
                    
            return ' '.join(split_sentence) #return concatenated splited sentence 
