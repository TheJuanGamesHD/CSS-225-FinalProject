import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

def MainGame():
    print("==> Combat Medic Game <==")
    print("Story genre: War/Military")
    print("Character background (player): You are a military doctor and you want to help everyone in the fastest and safest way.")
    print("Game Objective/Actions: You will have to heal comrades fallen in combat using all methods to reach them.")
    print("==========================================")
    chapter = 1
    

    #this variants and statement are for complete and start in false and change depeding of the choices of the user or player 
    equipments = False 
    fought = False
    medic = False
    climbed = False
    angel = False
   

    #some chapters have and implement a variable or statement for reinforce the selection for the options and final
    while chapter:
        if chapter == 1:
            chapter,equipments = chapter1.IntroChapter(equipments)
        elif chapter == 2:
            chapter, fought, medic = chapter2.AmbushChapter()
        elif chapter == 3:
            chapter, climbed = chapter3.AftermathChapter(fought)
        elif chapter == 4:
            chapter,angel = chapter4.MedicChapter()
        elif chapter == 5:
            chapter = chapter5.HomeChapter(fought, medic, climbed, angel)

if __name__ == "__main__":
    MainGame()
