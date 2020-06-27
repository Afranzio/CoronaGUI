from Scrapping import  count
import eel

##Select The Folder of FrontEnd File
eel.init("web")

@eel.expose

def get(inputs):

    #customize the Inputs

    if len(inputs)<=3:
        inputs = inputs.upper()  #For countries like USA,UAE
        
    else:
        inputs = inputs.title()  #Others in Title

    Country = inputs
    
    ##Pass Country name to the defined function!!

    return (count(Country))

eel.start('index.html',size = (1024,500),cmdline_args=['--start-fullscreen'])