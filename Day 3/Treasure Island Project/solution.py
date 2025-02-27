#print an ASCII Art
print('''
     %           %
         %           %
            %           %
               %          %
                 %          %
                   %          %                   :::
                    %          %                ::::::
                 %%%%%%  %%%%%%%%%            ::::::::
              %%%%%ZZZZ%%%%%%   %%%ZZZZ     ::::::::::         ::::::
             %%%ZZZZZ%%%%%%%%%%%%%%ZZZZZZ  :::::::::::    :::::::::::::::::
             ZZZ%ZZZ%%%%%%%%%%%%%%%ZZZZZZZ::::::::::***:::::::::::::::::::::
          ZZZ%ZZZZZZ%%%%%%%%%%%%%%ZZZZZZZZZ::::::***:::::::::::::::::::::::
        ZZZ%ZZZZZZZZZZ%%%%%%%%%%ZZZZZZ%ZZZZ:::***:::::::::::::::::::::::
       ZZ%ZZZZZZZZZZZZZZZZZZZZZZZ%%%%% %ZZZ:**::::::::::::::::::::::
      ZZ%ZZZZZZZZZZZZZZZZZZZ%%%%% | | %ZZZ *:::::::::::::::::::
      Z%ZZZZZZZZZZZZZZZ%%%%%%%%%%%%%%%ZZZ::::::::::::::::::::::::::
       ZZZZZZZZZZZ%%%%%ZZZZZZZZZZZZZZZZZ%%%%:::ZZZZ:::::::::::::::::
         ZZZZ%%%%%ZZZZZZZZZZZZZZZZZZ%%%%%ZZZ%%ZZZ%ZZ%%*:::::::::::
            ZZZZZZZZZZZZZZZZZZ%%%%%%%%%ZZZZZZZZZZ%ZZ%:::*:::::::
            *:::%%%%%%%%%%%%%%%%%%%%%%%ZZZZZZZZZZ%%%*::::*::::
          *:::::::%%%%%%%%%%%%%%%%%%%%%%%ZZZZZ%%      *:::Z
         **:ZZZZ:::%%%%%%%%%%%%%%%%%%%%%%%%%%%ZZ      ZZZZZ
        *:ZZZZZZZ       %%%%%%%%%%%%%%%%%%%%%ZZZZ    ZZZZZZZ
       *::::ZZZZZZ         %%%%%%%%%%%%%%%ZZZZZZZ      ZZZ
        *::ZZZZZZ           Z%%%%%%%%%%%ZZZZZZZ%%
          ZZZZ              ZZZZZZZZZZZZZZZZ%%%%%
                           %%%ZZZZZZZZZZZ%%%%%%%%
                          Z%%%%%%%%%%%%%%%%%%%%%
                          ZZ%%%%%%%%%%%%%%%%%%%
                          %ZZZZZZZZZZZZZZZZZZZ
                          %%ZZZZZZZZZZZZZZZZZ
                           %%%%%%%%%%%%%%%%
                            %%%%%%%%%%%%%
                             %%%%%%%%%
                              ZZZZ
                              ZZZ
                             ZZ
                            Z

'''
)
print("Welcome to the Beehive")
print('''
                                   ...vvvv)))))).
       /~~\               ,,,c(((((((((((((((((/
      /~~c \.         .vv)))))))))))))))))))\``
          G_G__   ,,(((KKKK//////////////'
        ,Z~__ '@,gW@@AKXX~MW,gmmmz==m_.
       iP,dW@!,A@@@@@@@@@@@@@@@A` ,W@@A\c
       ]b_.__zf !P~@@@@@*P~b.~+=m@@@*~ g@Ws.
          ~`    ,2W2m. '\[ ['~~c'M7 _gW@@A`'s
            v=XX)====Y-  [ [    \c/*@@@*~ g@@i
           /v~           !.!.     '\c7+sg@@@@@s.
          //              'c'c       '\c7*X7~~~~
         ]/                 ~=Xm_       '~=(Gm_.
''')
print("Your mission is to find the treasure by escaping a bee sting")

#Determine to continue or end the game based on the users choosen direction
Level1 = input("Where do you want to turn? Left or Right: ")
if Level1 == "Left":

    Level2 = input("What do you want to do next? Swim or Wait: ")
    if Level2 == "Wait":

        Level3 = input("Which door do you want to go into? Blue, Yellow or Red: ")
        if Level3 == "Yellow":
            print("You won!")
        elif Level3 == "Blue": 
            print("Eaten by a Beastly Bee, GAME OVER!!")
        else: 
            print("Burned by fired belly Dragon Bee, GAME OVER!!")
    else:
        print("You are being attacked by a Bumble Bee: Game Over!!")
else:
    print("You've been stung by a baby Bee: GAME OVER!!")



