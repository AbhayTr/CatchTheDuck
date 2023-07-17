# Catch the Duck Hand Game
An AI Based Game in which the player can move the in-game hand by moving their actual hand in front of a camera, and then close their hand in front of the camera when their in-game hand is above the duck, to catch the duck and score a point.

## Demo Video

Below is the video demonstrating the game:

%VIDEO%

## Prerequisites to deploy and use the Web App
  - **Python** should be installed on the system to run the game.
  - **Pip** should be installed on the system to install dependencies of the game.
  - The following packages should be installed by using pip on the system (run the following commands in Command Prompt/Terminal after installing python and pip to install them):
    
    ```bash
    pip install tk
    pip install opencv-python
    pip install numpy
    pip install Pillow
    pip install mediapipe
    pip install tensorflow
    pip install pygame
    ```

## Instructions to play the game
  - Donwload the project and extract the files in any folder.
  - Open Command Prompt/Terminal and navigate to the **project** folder.
  - In the **project** folder, run the **"game.py"** file to start the Game by running the following command:
    
    ```bash
    python game.py
    ```
    
  - Done! The game will start.
  - First it will ask your username, so that it can save your High Score.
  - Then, the actual game will start where you have to move your hand in front of your camera to play the game. When your hand is above the duck, you have to close your hand to catch the duck, and hence score a point.

Enjoy the game!