def HomeChapter(fought, medic, climbed, angel):
    
    print("\nChapter 5: A helicopter appears in the sky. You’re going home.")
    print("“You can hear a throbbing sound that resonates, everyone is ready, something can be seen in the sky. It's a helicopter, we're going home”.")
    print("Scene 5:")
    print("The player returned to base.")
   
    print("\nOptions:")
    print("1. Go to the armory (supplies/equip yourself)")
    print("2. Talk to comrades (information/mental preparation)")
    print("3. Write a letter for family (tell them you love them)")
    print("0. Close the Game")
    print("4. Play Again")

    print("\nCONGRATULATIONS you have completed the game, but you can find out what your result was by talking to your comrades")

    choice = input("\nChoose an action: ")
    
    print("=> ACTION RESPOND <=")

    if choice == '3':
        letter2 = input("Letter to the family, tells what happened, I am a hero: ")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 5
    
    elif choice == '2': #depending what choice you have taken the respond is going to be different
        if fought and climbed and not angel:
            print("When you go to talk to your comrades, Your comrades see you as a COWARD who left men behind, forgetting his responsibilities.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return 5
        elif medic and climbed and angel:
            print("When you go to talk to your comrades, Your comrades see you and tell you that you are an ANGEL who protected them during a disaster.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return 5
        else:
            print("When you go to talk to your comrades, Your comrades see you as a coward who backed out at the last minute, and they don't trust you either.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return 5

    elif choice == '1': #this is for drama
        print("You are like an angel in hell that continues to fight, take the equipment; B&T APC9 Pro-K as gun, Medical equipment: Fluid Resuscitation Hemorrhage (blood loss) Control Airway Management Assorted Equipment Personal Protection Triage Systems Diagnostic Equipment Casualty Management Hypothermia Prevention Battlefield Medicine Also, you also star praying to go to the ballata")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 5

    elif choice == '0': #this end and close the game
        print("----> Thanks for playing my game <----")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 0
    
    elif choice == '4': #this start de game again for different final
        print("You decided to change the future")
        print("Let the party begin again")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 1
    
