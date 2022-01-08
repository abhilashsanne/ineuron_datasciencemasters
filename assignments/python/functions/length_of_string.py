
def string_length(a:str):
  """
  This method calculates and returns the length of the given input string 'a'
  """
    length = 0
    for i in a:
      length += 1
    return length

a = str(input('Enter your string: '))

print(f"Length of '{a}' is {string_length(a)}")
