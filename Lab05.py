# define a function to count vowels
def countv(word):
    
    count = 0
    #make a list of vowels
    vowel = ['a','e','i','o','u']
    # use for loop to count number of vowels
    for letters in word:
        #to count ,we need to check whether letter  is a vowel or not using conditional statement
        if letters in vowel:
            #increment of count 
            count=count+1
            print(count)
            print(letters,end=',')
    print("\nNo of vowels: ",count)
    # returning count so that it can be used further 
    return count
word=input("Enter words").lower()
print(word)
#calling function 
count=countv(word)

#define a function to calculate and print percentage
def percent(word,count):
     #make a formula to find percentage
    per=(count/len(word))*100
    print(per)
#calling function 
percent(word,count)