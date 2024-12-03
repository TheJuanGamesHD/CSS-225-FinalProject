def AmbushChapter():

    print("\nChapter 2:")
    print("“In a convoy of armed vehicles, suddenly a whistling sound is heard nearby. It's an ambush, bullets are flying very close”.")
    print("Scene 2:")
    print("The player is under an enemy ambush.")
    
    print("\nOptions:")
    print("1. go back to base (back to Chapter 1, all team die)")
    print("2. run, leave all your comrades and climb a mountain (moves to Chapter 3)")
    print("3. grab the rifle and counterattack the ambush (move to Chapter 3 but many of your teammates die)")
    print("4. take out medical supplies and help the wounded (move to Chapter 3; the more allies you heal; the more allies you receive)")
    
    choice = input("\nChoose an action (1-4): ")
    
    print("=> ACTION RESPOND <=")

    if choice == '1': #leave all
        print("You were afraid, you didn't know what else to do, you were nervous, now you have to live with the burden that you left behind to your comrades.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 1,False, False #we have more variant that why two false
    
    elif choice == '2':
        print("You were scared, disoriented, and decided to follow your instincts so you climbed to a high place.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 3,False, False #almost like the first one but this change
    
    elif choice == '3':
        print("Adrenaline rises and you decide to FIGHT with honor even though others fall.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 3,True, False #depeding of the choice this can change to different final
    
    elif choice == '4':
        print("Your instinct and practice are put to the test, even though everything is chaos you decide to be an angel in hell.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 3,False, True #this is the best selection
