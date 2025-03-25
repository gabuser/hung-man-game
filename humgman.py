import random
word:list
value:str
yourinput :str
run = True
body= [" o","-|-","/ \\ "]
hung:object

with open("words.txt","r") as words: 
    word= words.read().split("\n")
    value= random.choice(word)

place = list(value)
show=["-"]*len(place)

class hunggame:

    def __init__(self,body:list,value:str):
        self.body = body
        self.value = value
        self.choosen =  sorted([c for c in self.value])
        #print(self.position)
        #print(sorted(self.choosen))
    
    def searchword(self,item:str) -> int:
        left = 0
        right = len(self.choosen) -1

        while(left <= right):
            half = (left+right) //2
            guess = self.choosen[half]

            if(guess == item):
                return half
            
            if(guess < item):
                left = half+1
            
            else:
                right = half-1
        return -1
    
    def checking(self, character:str):
        self.inputword = self.searchword(character)

        
        

hung= hunggame(body, value)
def main(run:bool):
    counting =0
    while(run):
        try:
            yourinput = input("\t")
            if(yourinput =="q"):
                run = False
            hung.checking(yourinput)

            if(show[0:-1] ==place[0:-1]):
                print("you win")
                print(f"word:{value}")
                run =False
    
        
            if( hung.inputword == -1):
                counting+=1
        
            if(counting > len(hung.body)):
                print("wrong answer :( ")
                print(f"you lost, the original word was:{value}")
                run = False

        
            try:
                v=place.index(yourinput)
                print(v)
            
                show[v]=yourinput
                print(show)
                
            except ValueError:        
                for c in hung.body:
                    print(c[0:counting])

        except KeyboardInterrupt:
            print("you left")
            run = False

main(run)