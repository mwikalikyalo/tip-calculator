def main():
  print("Thanks for coming to Eateries.")
#   welcome and ask if ready to pay
  prompt1 = input('Ready to pay? ')
  prompt1 = prompt1.capitalize()
  print(prompt1)
  if prompt1== 'Yes':
      print('Do you want to tip?')
  elif prompt1== 'No':
        print('We will give you a minute')
  else:
        print('Your input was invalid.')

if __name__ == '__main__':
    main()