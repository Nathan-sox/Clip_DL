  # Clip_DL
    #### Video Demo:  https://youtu.be/N_XggS_HnmI
    #### Description:
    This is a simple Youtube Donwloader with using a CLI interface for interactions with the user.
    I'll explain the project using each each project file as a paragraph I think
    
    ### Project files: 
    1.Reformatting.py
    2.project.py
    3.downloader.py
    4.history.py
    5.test_project.py

    ## 1. Reformatting.py
    This file was just used to add headers to another file I made by checking if the first character is a *.
    If the first character is a * it formats it adds 3 "===" to each side using the str.center() method

    ## 2. Project.py
    This is the main file. I was advised by chatGPT while planning to modularize and split the functionality of the code into different files.
    This file handles showing the menu and processing user input so it can be passed into other functions from other modules
    It firsts prompts the user for a Youtube link
    Then asks the user in which format they would like to download it:
    i. video 
    ii.audio 
    iii. a clip from the video

    ### i and iii
    If the user chooses video or clip from video: It then prompts them with them with the available qualities of that video and a menu to choose what quality to download the video in

    Specifically for the clip from video: It prompts the user for a start time and end time they want to download while checking if the start time/ end time is a valid range.
    #### Note: I didnt add any sort of Retry for this program if at any point the user chooses a wrong option it quits with an error message.
    I chose this design choice because it would have taken longer to implement a retry for each menu phase. I have plans of adding in the future if i come back to this project

    ### ii
    If the user chooses a audio format. It just downloads the audio in an m4a format.
    Design choice: I didnt implement a choosing quality/format option like in the video because the main purpose of the project was for the clipping and i thought this would be a fun add-on.

    ## downloader.py
    This is the download module that simplifies downloading files by giving simple functions to call in the main(project.py) file.
    It also has some extra functions that that simplifies processes in the main like:
    i. get_video_format
    ii. display_video_metadata

    ### i and ii
    Both of these functions have a side effect of displaying whatever relevant information specific to them
    
    Design choice: I chose this so that displaying the information would be easier and linking them back to the function to use would also be easier.

    ## histroy.py
    history.py is a simple program that tracks the download history of videos you download using a json file.
    The file stores a the the videos URL, videos title, and the time the video was downloadeded.
    All of this is stored in the history.json file

    ## test_project.py
    Sadly I didnt write the tests in this file but i can explain what it tests.
    The tests just test whether the the file saves the history and loads it correctly.
    The tests also test an add_basic_configuration function i wrote in the main fiel(project.py). it checks whether it adds the data to the file appropriately
    These are the only two tests that can be simply tested without further configuration or input from the use


# Thank you Mr Malan and the team at CS50P for this amazing course.🙇
