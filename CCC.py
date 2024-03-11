import pytube
import os
import zipfile



def remove_illegalCharacters_fromString ( string ):
    # remove illegal characters from the string
    
    illegalCharacters = ["/" , "\\" , ":" , "*" , "?" , "\"" , "<" , ">" , "|"]
    
    for character in illegalCharacters:
        string = string.replace(character, "")
    
    return string



def instance_ytObject ( url ):
    # instance the object yt from the URL
    
    if "watch" in url:
        yt = pytube.YouTube(url)
        return yt
    elif "playlist" in url:
        yt = pytube.Playlist(url)
        return yt
    elif "channel" in url:
        yt = pytube.Channel(url)
        return yt
    
    return None



def download ( yt , pathOf_download , zipFile ):
    # download the video, playlist or channel
    
    # download of one video
    if isinstance(yt, pytube.YouTube):
        yt.title = remove_illegalCharacters_fromString(yt.title)
        
        yt.streams.get_highest_resolution().download( output_path=pathOf_download , filename=(yt.title+".mp4") )
        
        return
    
    # download of a playlist or channel
    for video in yt.videos:
        video.title = remove_illegalCharacters_fromString(video.title)
        
        video.streams.get_highest_resolution().download( output_path=pathOf_download , filename=(video.title+".mp4") )
        
        # add the video to the zip file and remove the video from output_path
        zipFile.write(video.title+".mp4")
        os.remove(video.title+".mp4")
    
    zipFile.close()
        
                

def main ():
    
    print("Welcome to Cancel Cancel Culture!")
    print("Read the README file for instructions on how to use this program.")
    
    print("")
    
    
    
    #. input of URL
    while True:
        url = input("Enter the URL of the video, playlist or channel you want to download: ")

        try:
            yt = instance_ytObject(url)
            if yt != None:
                break
            
            print("Invalid URL. Please try again.")
        except:
            print("Invalid URL. Please try again.")
    
    
    
    print("")
    
    
        
    #. input destination folder
    while True:
        pathOf_download = input("Enter the destination folder: ")
        
        if os.path.exists(pathOf_download):
            break
        
        print("Invalid folder. Please try again.")
    os.chdir(pathOf_download)
    
    
    
    print("")


    
    #. input of zip file name
    zipFile = None
    if not isinstance(yt, pytube.YouTube): 
        while True:
            nameOf_zipFile = input("Enter the name of the zip file: ")
            
            if nameOf_zipFile != "":
                
                if ".zip" not in nameOf_zipFile:
                    nameOf_zipFile += ".zip"
                
                zipFile = zipfile.ZipFile(nameOf_zipFile, "w")
                
                break
            
            print("Invalid name. Please try again.")
        
        
        
    #. download
    download( yt , pathOf_download , zipFile )
    

            
    print("Thank you for using Cancel Cancel Culture!")
    
    
    
if __name__ == "__main__":
    main()
