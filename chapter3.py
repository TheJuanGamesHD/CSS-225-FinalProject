def AftermathChapter(fought):
    
    print("\nChapter 3:")
    print("“The bullets are getting fewer and fewer, only a sound like a drum can be heard. It is the heart of the survivors that can be heard”.")
    print("Scene 3:")
    print("The player must choose what is best for his team.")
    
    print("\nOptions:")
    if fought:
        print("1. collect ID tags (only if the player fought)") #only if you fight 
    else:
        print("OPTION NOT available 1. collect ID tags (only if the player fought) ") #if you dont fight you comrades are alive
    print("2. continue with the mission (another ambush and they die)")
    print("3. climb the mountain (team regrouping)")
    print("4. return to base (Chapter 2 if he left the team; Chapter 1 if he fight)")
    
    choice = input("\nChoose an action (1-4): ")
    
    print("=> ACTION RESPOND <=")

    if choice == '1' and fought:
        if fought:
            print("You have and will collect the military IDs of your fallen comrades, because even though you fought, you abandoned your responsibilities.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return 3, False #this is choice if you select being a fighter instead a medic
        else:
            print("Since you didn't fight and fulfilled your responsibilities, there were no casualties but it's not over yet.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return 2, False #this is choice if you select being a medic instead a figher
    
    elif choice == '2':
        print("You are DEAD. GAME OVER.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 0 #you are dead
    
    elif choice == '3':
        print("You decided to climb the mountain with your comrades who are disoriented and fearful that there might be another fight.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return 4, True #this choice is as a leader
    
    elif choice == '4':
        if fought:
            print("1. Fight with honor and die with glory You decided to fight and try to return to base, although many of your comrades die along the way.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return 1, False #this is ignorin medic
        else:
            print("2. If you decided to go down the mountain you still have time, help your comrades or watch from afar as they are massacred and slowly lose their lives.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return 2, False #fight but ignoring variant medicthis is when you already run but you decide to go down
        
        
