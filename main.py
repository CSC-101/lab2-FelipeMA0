# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("fmendo08@calpoly.edu")
print(message)


def smallest(n: float, m: float) -> float:
   if n < m:
      return n  # The statement is evaluated for neither of the calls as the first value is smaller for both calls
   else:
      return m


first = smallest(3, 2)  # The value of first is 2
second = smallest(2, 2)  # The value of second is 2, which is not reasonable as 2 is not smaller than 2.
print()



def function2(a: int, b: int, c: int) -> int:
   if a > b and a > c:
      return a - b  # A call to this function will evaluate this statement only when a is the largest value
   elif b > c:
      return b + c  # A call to this function will evaluate this statement when b is the largest value
   else:
      return 2 * c  # A call to this function will only evaluate this statement only when c is the largest value


answer1 = function2(3, 2, 1)  # The value of answer1 is 1
answer2 = function2(2, 3, 1)  # The value of answer2 is 4
answer3 = function2(2, 1, 3)  # The value of answer3 is 6
print()




from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # The value of test is true if the index exists in the list, and false if it doesn't
    if test:                            # The check is preventing you from searching for an index that doesn't exist
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # The value of first is none
second = checked_access([1, 0, 1], 2)    # The value of second is 1
print()




def length_sum(L: list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])  # This statement is evaluated for the call "first" and the values 4, 2 and 3 are being added.
   elif len(L) > 1:
      result = len(L[0]) + len(L[1])  # This statement is being evaluated for call "third", and the values 7 and 4 are being added
   elif len(L) > 0:
      result = len(L[0])  # This statement is being evaluated for call "second", and the value 11 is being added
   else:
      result = 0
   return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()




def surprising(L: list[str], other: str) -> list[str]:
   L.append(other.upper())
   return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# The value of words is "this is confusing code" at this point.
# The value of first is "this is confusing code.AVOID", and the value of second is "this is confusing code.AVOID SUCH."
# The function added "avoid" and "such" at the end of the list in all caps
print()