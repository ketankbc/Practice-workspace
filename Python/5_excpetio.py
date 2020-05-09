def get_number():
  try:
    number1 =input('Enter a number. I will square...')
  except:
    print('please input a number')
  else:
    print('suare='+number1**2)
  finally:
    print("End of Program... Thank you..")


#Handle the exception thrown by the code below by using try and except blocks.

try:
  for i in ['a','b','c']:
    print(i**2)

  x = 5
  y = 0

  z = x/y

except TypeError:
    print("This is a type error...please check values..")
except:
    print("Caught an exception... cannot devideby zero")
finally:
  print('all Done')

#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():    
      while True:
        try:
          number=int(input("Please input a number...") )
        except:
          print('Please re enter a number...')
        else:
          print('our number is '+str(number))
          break


ask()