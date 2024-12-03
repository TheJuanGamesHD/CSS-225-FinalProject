def MedicChapter():

    print("\nChapter 4:")
    print("“The adrenaline is wearing off, watching your surroundings waiting for another whistle, fear is present”.")
    print("Scene 4:")
    print("The player is on top of a mountain.")
    
    print("\nOptions:")
    print("1. Be a military medic (the player gives first aid to the survivors; makes a perimeter; asks for extraction if he helped during the ambush; continues to Chapter 5)")
    print("2. Go down the mountain (return to Chapter 3)")
    print("3. You are tired so you decide to sleep.")
    
    choice = input("\nChoose an action (1-3): ")
    
    print("=> ACTION RESPOND <=")
    
    if choice == '1':
        print("You decide to be a light in such a difficult time and although you are also afraid, everyone trusts and depends on you to survive, you are respected by many.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 5, True #best choice and you can get a Rank
    
    elif choice == '2':
        print("You are not sure what you have done so you make the decision to go down the mountain with your unit.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 3, False #this is for changing final but doesnt help much instead this affect the final
    
    elif choice =='3':
        print("All the fear finally caught up with you and you let many suffer")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 5, False #this choice was added for drama
