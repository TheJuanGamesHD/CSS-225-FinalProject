# CSS-225-FinalProject

Technical Documentation for Combat Medic Game
 
Where the Code is Hosted
No Hosted in any place:
Update 1: GitHub

External Services
No external services are needed or required for this project because the game is own and runs locally on any compatible Python environments like VS Code.

Languages and Technologies
Programming Language: Python
Core Concepts: Functions, conditional statements (if-elif), loops (while), and modular programming to separate files for chapters and main game logic.

System Requirements and Supported Applications
Python Version: Python 3.6
Operating System: Any that supports Python
Required Applications:
Python interpreter: CPython
Any text editor or IDE for Python development: VSCode

Coding/Naming Conventions
File Naming: Each chapter is organized as a separate .py file and they follow an understandable order.
Function Naming: This represents the functions that are related to its name to know what is inside:
IntroChapter: Introduction choice for start
AmbushChapter: Ambush quick think choices
AftermathChapter: Aftermath choice logic
MedicChapter: Medic choices and actions
HomeChapter: Final chapter and game conclusion
Variable Naming:
Clear and descriptive names like equipments, fought, medic, climbed, and angel.
Boolean variables track key player decisions like those mentioned above and done in the past because it was a decision that was made and is not grouped.


How to Run/Build/Deploy the Program
Prerequisites:
Install Python 3.6 or higher from python.org.
The game files needs to import into the maingame.py and chapter files are in the same directory.
Run:
Open the terminal or command prompt.
Navigate to the directory containing the game files.
Execute the main file using the command:
python maingame.py
Deployment:
It is in a .py file but you can make an .exe although I haven't tried it.

An Overview of the Architecture
Main Game Loop (maingame.py):
Controls the overall flow and importation of chapters.
Tracks player decisions using variables like equipments, fought, medic, climbed, and angel.
Chapter Modules:
Chapter 1: The player must prepare for deployment by equipping himself with the essentials or having other options that help.
Chapter 2: The player chooses between fighting or helping his comrades change the future.
Chapter 3: The player must make the best decision to continue the game or game over.
Chapter 4: The player must make the decision of what to do since he is the person who helps.
Chapter 5: The player depending on his choices determines the player's perception among comrades for a better ending, he also has other options.

How to Start the Program (Start the Game)
To start the game:
Make sure Python is installed and configured on the machine. You can use the IDE or Visual Studio Code
Open a terminal/command prompt in the directory containing the files is only one.
Run the following command in the terminal/command prompt:
python maingame.py
Follow the on screen prompts to progress through the game by selecting numbered options and data info from the game.
