def to_camel_case(text):
  '''
  Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
  The first word within the output should be capitalized only if the original word was capitalized 
  (known as Upper Camel Case, also often referred to as Pascal case).
  >>> to_camel_case("the-stealth-warrior")
  "theStealthWarrior"
  >>> to_camel_case("The_Stealth_Warrior")
  "TheStealthWarrior"
  '''
  ans = ''
  for i, element in enumerate(text.title()):i
      if i == 0:
          ans += text[0]
      elif element.isalpha():
          ans += element
  return ans
