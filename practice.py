# python generators

def squaregen(n):
	for i in range(n):
		yield i**2

for num in squaregen(10):
	print(num)




import random 

def rand(low,high,n):
	for i in range(n):
		yield random.randint(low,high)

for num in rand(1,10,8):
    print(num)




s = "hello"

i = iter(s)
print(next(i))
print(next(i))
print(next(i))





#python statements

st = 'Print only the words that start with s in this sentence'

for word in st.split():
	if word[0] == "s":
		print(word)




for num in range(0,10):
	if num%2 == 0:
		print(num)



lst = [x for x in range(1,51) if x%3 == 0]
print(lst)



st = 'Print every word in this sentence that has an even number of letters'

for w in st.split():
	if len(w)%2 == 0:
		print(w+ " has even length")



for i in range(1,100):
	if i%3 == 0 and i%5 == 0:
		print("FizzBuzz")
	elif i%5 == 0:
		print("Buzz")
	elif i%3 == 0:
		print("Fizz")
	else:
		print(i)



st = 'Create a list of the first letters of every word in this string'
lst = [word[0] for word in st.split()]
print(lst)









# function practice exercise

def lesser_of_two(a,b):
	if a%2 == 0 and b%2 == 0:
		return min(a,b)
	else:
		return max(a,b)

print(lesser_of_two(2,4))
print(lesser_of_two(2,5))




def animal_crackers(text):
	two_word = text.split()
	if two_word[0][0] == two_word[1][0]:
		return True 
	else:
		return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))




def makes_twenty(n1,n2):
	if (n1+n2) == 20 or n1 == 20 or n2 == 20:
		return True 
	else:
		return False
	
print(makes_twenty(20,10))
print(makes_twenty(2,3))
print(makes_twenty(8,12))



def old_mac(name):
	word = name
	return (word[0].capitalize()+word[1:3]+word[3].capitalize()+word[4:])

print(old_mac('macdonald'))



def master_yoda(text):
	return " ".join(text.split()[::-1])

print(master_yoda('I am home'))



def almost_there(n):
	if (n>=90 and n<=110) or (n>=190 and n<=210):
		return True
	else:
		return False

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


# Level 2 Problems
def has_33(nums):
	for n in range(0,len(nums)-1):
	#in the above code len(nums)-1 because counting starts from 0.so,if there are 3 elemets in a list then
	#counting will only go upto 2 eg.[0,1,2]
		if nums[n:n+2] == [3,3]:
			return True 
	else:
		return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))



# PAPER DOLL
def paper_doll(text):
	result = " "
	for char in text:
		result += char*3
	return result
        
print(paper_doll("hello"))



# BLACKJACK
def blackajack(a,b,c):
	sum = a+b+c
	if sum <= 21:
		return sum
	elif sum > 21 and int(11) in (a,b,c):
		return sum-10
	else:
		return "bust"

print(blackajack(5,6,7))
print(blackajack(9,9,9))
print(blackajack(9,9,11))



# SUMMER OF '69'







		
	




















	

	
















