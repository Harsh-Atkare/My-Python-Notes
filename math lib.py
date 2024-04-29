# if you write only import then you can use all feature of library
import math

# if you wanna use only few or one feature of library you can use form keyward
from math import sqrt, pi
result=math.sqrt(36)
print(result)
# imported pi from math library and print its value
print(pi)

# if you wanna use short from of library or freature you can use as keyward

from math import sqrt as s
print(s(81))
import math as m

# dir funtion use to print all the keywords or functions that libraries provides
print(dir(math))