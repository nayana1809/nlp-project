
def review(sentence, word1,word2,word3,word4):
    s = sentence.split(" ")
 
    for i in s:
        if (i == word1):
            return True
        elif (i==word2):
            return True
        elif (i==word3):
            return True
        elif (i==word4):
            return True
    return False
    

s = "the product was not usable"
word1 = "not"
word2="bad"
word3="didn't"
word4="un"
 
if (review(s, word1,word2,word3,word4)):
    print("the customer had negative feed back")

else:
    print("the costumer had positive feedback")
