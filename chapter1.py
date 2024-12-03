def IntroChapter(equipments):
    
    print("\nChapter 1:")
    print("“After training and bootcamp you arrive at a military base in a place you've never heard of before, it's hot, you can't lift your head because of the scorching sun”.")
    print("Scene 1:")
    print("The player leaves his stuff in the tent he shares and heads to the command post; he is informed that he is the only military medic on duty and has to prepare for the worst.")
    
    print("\nOptions:")
    print("1. Go to the armory (supplies/equip yourself)")
    print("2. Talk to comrades (information/mental preparation)")
    print("3. Write a letter for family (tell them you love them)")
    print("4. Rest (go to Chapter 2)")
    
    choice = input("\nChoose an action (1-4): ")

    print("=> ACTION RESPOND <=")
   
    if choice == '4': #no pass if dont have the basics
        if equipments:
            print("SUPERIOR: You've equipped yourself well, I think you're ready.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return 2, equipments  # Proceed to Chapter 2
        else:
            print("SUPERIOR: You think that outside is a peaceful place, if you don't equip yourself well, you will come back in a black bag.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return 1, equipments  # Stay in Chapter 1

    elif choice == '3':
        letter1 = input("Letter for?: ")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 1,equipments #a letter to your family or friends how is going
    
    elif choice == '2': #stories about the war and how is being active
        print("User: What is being in a active zone?")
        print("Solider 1: You are going to cry, kid")
        print("Solider 2: It's like hell in person")
        print("Solider 3: If you don't make the right decisions you will come back in a black bag")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 1,equipments 
     
    elif choice == '1': #basic equipment for going outside
        print("You Take a M4A1, 210 rounds, and big MedKit")
        equipments = True

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 1,equipments
    