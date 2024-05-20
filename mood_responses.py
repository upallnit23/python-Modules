def responses(mood):
    response = ["happy", "sad", "peaceful", "angry", "joyful", "worried"]
    if mood in response:
        if mood is "happy" or "joyful":
            return "Have a nice day!"
        if mood is "sad" or "worried":
            print(f"It's a beautiful day to go for a walk and visit the cafe with friends.")
        if mood is "peaceful":
            print(f"Let's catch up on our work and emails!")
        if mood is "angry":
            print(f"Let's go to the gym and expel some of that energy!")
        else:
            print(f"Let's make some tea and grind out our work today!")
        
