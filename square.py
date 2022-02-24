def square(n):
  return n * n
numbers = [2,3,4,5,6,7,8,9]
print("Original List: ",numbers)
output = map(square, numbers)
print("Square of the elements of the given list using map():")
print(list(output))