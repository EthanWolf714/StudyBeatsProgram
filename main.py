import webbrowser
import sys
import random
import datetime

# main youtube url
url = "https://www.youtube.com/watch?v="
# Nested list for video url codes
vid_IDs = [
    ["jfKfPfyJRdk", "1fueZCTYkpA&list=PL6NdkXsPL07KN01gH2vucrHCEyyNmVEx4&index=9", "_tV5LEBDs7w&list=PL6NdkXsPL07KN01gH2vucrHCEyyNmVEx4&index=14", "l98w9OSKVNA&list=PL6NdkXsPL07KN01gH2vucrHCEyyNmVEx4&index=10"],
    ["TlWYgGyNnJo&list=PL6NdkXsPL07KN01gH2vucrHCEyyNmVEx4&index=4", "Z-_TTyZUOLk&list=PL6NdkXsPL07KN01gH2vucrHCEyyNmVEx4&index=1"],
    ["NJuSStkIZBg&t=2500s","MYPVQccHhAQ", "zr5JjgOMXeQ"],
    ["Uf9vubG4BnY"],
    ["wa_j8DgTtUE"],
    ["_tV5LEBDs7w&t=228s","b6_XsMcUojM"]
]
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def main():
    print("-------------------------------------------------------------------------")
    print(""""Welcome to lofi-beats, browser through what genre you want to listen to!
        Library:
        0.Lofi-Girl
        1.Lofi-Boy
        2.Coffee Shop Beats
        3.Starfield
        4.Spooky
        5.Christmas/Winter
        """)
    print("-------------------------------------------------------------------------")
    
    open_video()
    
    


   
#get_input chooses link code based on user input
def get_input():
     current_date = datetime.datetime.now()
     current_Month = current_date.month
     genreInpt = int(input("Pick a genre: "))
     vidList = ', '.join(map(str, vid_IDs[genreInpt]))
     if(genreInpt == 4):
         if(current_Month == 10):
             print("Its spooky season, spooky playlist avaiable")
         else: print("Not spooky season")
     elif(genreInpt == 5):
         if(current_Month == 12):
             print("It winter time! Holiday playlist avaiable")
         else: print("Its not winter time")
            
     
     
     print("Now choose an option from this list: " + vidList)     
     vid_Choice = int(input("Enter your music option: "))
     found_id = None
     for index, vidID in enumerate(vid_IDs[genreInpt]):
        if index == vid_Choice:
            found_id = vidID
            return vidID 
      
    
#assembles the final url to input into search query        
def open_video():
    final_url = url + str(get_input())
    print(final_url)
    webbrowser.get(chrome_path).open(final_url)
    


    
    


main()
