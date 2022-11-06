def displayMessage(message:str,style:int=0):
    pointer=""

    if style is 0:
        pointer="-"

    elif style is 1:
        pointer="*"
        
    else:
        pointer=" "
    
    print(f"[{pointer}] {message}")

def getLogo():
    with open("art.txt","r") as f:
        logo=f.read()
        f.close()

    return logo
