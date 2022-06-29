my_tuple = (7, 25, 36, 9, 6, 8)

print("The tuple is : ")
print(my_tuple)

K = 2
print("The value of K has been initialized to ")
print(K)
my_result = []
my_tuple = list(my_tuple)
temp = sorted(my_tuple)

for idx, val in enumerate(temp):
   if idx < K or idx >= len(temp) - K:
      my_result.append(val)
my_result = tuple(my_result)

print("The result is : " )
print(my_result)
