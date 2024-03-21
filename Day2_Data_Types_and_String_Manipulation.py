# String
firstName = 'Shubham'
middleName = "Kumar"
lastName = 'Gupta'
print(firstName, middleName, lastName)
print(type(firstName))
print(firstName[0])
print(firstName[-1])
# string concatenation
print('123' + '345')
print('123'+firstName)

# Integer
rollNo = 101
print(rollNo)
print(type(rollNo))
# cool trick : using _ with int
print(123_456_789)

# Float
rate = 120.45
print(rate)
print(type(rate))
# print(120.45_120.45_120.45)
# Note: using _ doesn't work with float

# Boolean
print(True)
print(type(True))
print(False)
print(type(False))

# Quiz 2 : Data Types Quiz

mystery = 734_529.678
print(mystery)
print(type(mystery))

street_name = 'Abbey Road'
print(street_name[4] + street_name[7])

# type()
num_char = len(input('Enter Your Name: '))
# type checking
print(type(num_char))

# type conversion
# int -> str
new_num_char = str(num_char)
print('Your Name has ' + new_num_char + ' characters.')

a = '120'
print(type(a))
b = int(a)
print(type(b))
print(str(70) + str(100))
print(int('70') + int('100'))
print(float('70.1') + float('100.5'))
