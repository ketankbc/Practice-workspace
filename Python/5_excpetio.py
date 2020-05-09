def get_number():
  try:
    number1 =input('Enter a number. I will square...')
  except:
    print('please input a number')
  else:
    print('suare='+number1**2)
  finally:
    print("End of Program... Thank you..")
