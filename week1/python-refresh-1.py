print(2+2)

print(50-5*6)

print(8/5) #division
print(8//5) #floor division removes the fractional part
print(8%5) #returns the remainder of the division

print (5**2) #Power operator: 5 squared
print (2**7) #Power operator: 2 to the power of 7


width = 20
height = 5*9
print (width*height)

tax = 12.5 / 100
price = 100.50
tax_amount = price * tax
print(tax_amount)

total = price + tax_amount
print(total )

print(round(total, 2))

#TEXT
print('eggs')

print("\"yes,\" They said")

print("She just said \"Hello\" to us")

s = 'First line.\nSecond line.'
print(s)

print('Hello \nHello to you')

#If you don’t want characters prefaced by \ to be interpreted 
#as special characters, you can use raw strings 
#by adding an r before the first quote:'

print('''\
    Usage
    -h
    -H
    ''')

print('mi'+'ni'+'mum')
print('mi'*2)

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

word = 'python'
word[-6]  #y

word[2:5] # from 2 (included) to 5 (excluded)

word[1:] #ython
word[:3] #pyt

word[:2]+ word[2:]

#Python strings cannot be changed
#They are immutable.

'Un ' + word[2]+word[4]+word[5] + 'ton'
len(word)