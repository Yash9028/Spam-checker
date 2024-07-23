data =None
try:
  with open('keywords.txt','r') as f:
    # print(f.read())
    data = f.read()

except FileNotFoundError:
  print("file not found!")

# print(data)

def spam_check(sentense, spam_list):
  for word in spam_list:
    if word in sentense:
      print('marked as spam!')
      return True

  print('The given sentense is safe')
  return False      
x = spam_check('Hey there I am playing rummy',data.split(', '))
print(x)