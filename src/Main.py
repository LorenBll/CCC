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


#! FUNCTIONS RELATED TO THE STARTUP DATA
def read_startupData () :
    # read the startup data from startupData.txt
    
    try:
        with open("./data/startupData.txt", "r") as file :
            data = file.read()        
        return data
    
    except:
        return None
        
def write_startupData ( data ) :
    # write the startup data to startupData.txt
    
    with open("./data/startupData.txt", "w") as file :
        file.write(data)
        
def get_startupData () :
    # set the startup data
    
    #. if the program is not run for the first time, read the data from the file
    data = read_startupData()
    if data != None:
        downloadPath = data.split("\n")[0]
        #tocheck : potrebbero esserci altri dati da leggere, ma al momento non sappiamo quali saranno
        return [downloadPath , ]
    
    
    
    #. if the program is run for the first time, ask the user to input the startup data
    while True:
        downloadPath = input("Enter the destination folder: ")
        if downloadPath != "" and os.path.exists(downloadPath):
            break
        
        print("Invalid folder. Please try again.")
    
    write_startupData( [downloadPath , ] )
    return [downloadPath , ]



#! FUNCTIONS RELATED TO THE ALREADY DOWNLOADED VIDEOS
def read_downloadedVideos () :
    # read the data of the already downloaded videos from downloadedVideos.txt
    
    try:
        with open("./data/downloadedVideos.txt", "r") as file :
            data = file.read()        
        return data
    
    except:
        return None

def get_downloadedVideos () :
    # set the data of the already downloaded videos
    
    #. if the program is not run for the first time, read the data from the file
    # note: the file is a sort of table, where each row is a video and each column is a piece of information about what has been downloaded in the order "playlist/video" , "URL", "download title"
    data = read_downloadedVideos()
    if data != None:
        
        data = data.split("\n")
        for i in range( len(data) ):
            data[i] = data[i].split(" ")
            
        return data        
    
    return []
    
    
def main () :
    
    print("Welcome to Cancel Cancel Culture!")
    print("Read the README file for instructions on how to use this program.")
    print("")
    
    startupData = get_startupData()
    downloadPath = startupData[0]
    #tocheck : potrebbero esserci altri dati da leggere, ma al momento non sappiamo quali saranno
    
    dataOf_downloadedVideos = get_downloadedVideos()
    
    
    
        
    

if __name__ == "__main__" :
    main()