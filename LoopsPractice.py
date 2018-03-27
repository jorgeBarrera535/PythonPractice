# Do Now Round 1
condition = True
while condition:
  print "Hey we looped!"
  condition = False
  
  x = 0
while x < 4:
  print "Loop: %d" % (x)
  x += 1
  
  # Do Now Round 2
count = 0
while True:
  print "We're looping! Count: %d" % (count)
  count += 1
  if count == 10:
    break
  
  
  import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win the lottery!"
  
#"for loop" example 1
my_string = "hello"
for letter in my_string:
  if letter in ["a", "e", "i", "o", "u"]:
    print "x"
    continue
  print letter

#Do Now Round 4 (write your code below)

# Do Now Round 5
fruits_dictionary = {'b': 'berry','a': 'apple', 'c': 'cherry'}
for key, value in fruits_dictionary.iteritems():
  if value == "apple":
    print "found apple!"
  else:
    print "not an apple"

