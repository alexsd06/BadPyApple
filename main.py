#!venv/bin/python
import frame_extractor
import to_ascii
import play_in_terminal
import sys
while True:
    print ("What do you want to do?")
    print ("1. Extract the frames from the mp4...")
    print ("2. Generate ascii art txt from extracted frames...")
    print ("3. Play ascii art in terminal...")
    print ("4. Exit...")
    option=int(input("Please enter option number: "))
    if option==1:
        frame_extractor.extract_frames()
    elif option==2:
        to_ascii.generate_ascii_txt()
    elif option==3:
        play_in_terminal.play_in_terminal()
    elif option==4:
        sys.exit(0)
    else:
        print ("Incorrect option selected... Please try again")