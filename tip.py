def main():
  print("Thanks for coming to Eateries.")
  # welcome and ask if ready to pay
  prompt1 = input('Ready to pay? ').strip().capitalize()
  
  print(prompt1)
  if prompt1== 'Yes':
      print('Let us calculate the tip.')
      prompt2= int(input("What is your bill? "))   
      if prompt2>= 0:
        print(prompt2)  
           
  elif prompt1== 'No':
      print('We will give you a minute')
  else:
      print('Your input was invalid.')

if __name__ == '__main__':
    main()