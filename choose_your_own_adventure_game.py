
print('''"
     \\XXXXXX//
      XXXXXXXX
     //XXXXXX\\                      OOOOOOOOOOOOOOOOOOOO
    ////XXXX\\\\                     OOOOOOOOOOOOOOOOOOOO
   //////XX\\\\\\     |||||||||||||||OOOOOOOOOOOOOOOVVVVVVVVVVVVV
  ////////\\\\\\\\    |!!!|||||||||||OOOOOOOOOOOOOOOOVVVVVVVVVVV'
 ////////  \\\\\\\\ .d88888b|||||||||OOOOOOOOOOOOOOOOOVVVVVVVVV'
////////    \\\\\\\d888888888b||||||||||||            'VVVVVVV'
///////      \\\\\\88888888888||||||||||||             'VVVVV'
//////        \\\\\Y888888888Y||||||||||||              'VVV'
/////          \\\\\\Y88888Y|||||||||||||| .             'V'
////            \\\\\\|iii|||||||||||||||!:::.            '
///              \\\\\\||||||||||||||||!:::::::.
//                \\\\\\\\           .:::::::::::.
/                  \\\\\\\\        .:::::::::::::::.
                    \\\\\\\\     .:::::::::::::::::::.
''')


print("welcome to treasure island")
print("your mission is to find the treasure")
cross_road = input('your at a cross road where do you want to go? "left" or "right":\n ').lower()
door = 0
if cross_road == "right":
    cross_road.lower()
    print("fell into a hole. Game over")
elif cross_road == "left":
    swim_or_wait = input('you are at a lake, there is an island at the middle. would you want to "wait" for a boat or "swim" across?:\n').lower()
    if swim_or_wait == "swim":
        print("ops!! you gote swallowed by a shack.Game Over")
    elif swim_or_wait == "wait":
        swim_or_wait.lower()
        door = input('you arrived at the island unharmed. There is a house with 3 doors. One "red", one "yellow", and one "blue". which color do you choose?\n').lower()
    if door == "blue":
        print("that room was filled with magma.Game over")
    if door == "red":
        print("you entered a room filled with snakes. Game over")
    if door == "yellow":
        print("you succeeded in getting the treasure. you win")
else:
    print("you probably have a typo or did not input anything  ")