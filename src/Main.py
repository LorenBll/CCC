import os

try:
    import pytube
except:
    print("You need to install the pytube module to use this program.")
    print("Run the command 'pip install pytube' to install it.")
    exit()

try :
    import zipfile
except:
    print("You need to install the zipfile module to use this program.")
    print("Run the command 'pip install zipfile' to install it.")
    exit()



def isLinkValid ( link ) :
    # check if the link is a valid yotube video or playlist link
    
    try :
        yt = pytube.YouTube(link)
        return True
    except:
        return False
    
    

def main ():
    pass
    


if __name__ == "__main__":
    main()