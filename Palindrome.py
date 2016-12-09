message = input("input some word to check for palindrome bro \n")
num_length = len(message)-1
num_iter = int(num_length/2)
start_letter = 0
ispalindrome = False
while(num_iter != -1):
    if message[start_letter] == message[num_length]:
        start_letter+=1
        num_length-=1
        ispalindrome = True
    else:
        ispalindrome = False
        break

    num_iter-=1
        
if ispalindrome == False:
    print("bro that shit is not a palindrome")
elif ispalindrome == True:
    print("bro that shit is a palindrome, congrats")

    