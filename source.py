from Scrapping import  count
import eel

eel.init("web")

@eel.expose

def get(inputs):

    #customize the Inputs

    if len(inputs)<=3:
        inputs = inputs.upper() # for countries like USA,UAE
        
    else:
        inputs = inputs.title() #Others in Title

    Country = inputs
    
    return (count(Country))

eel.start('index.html',size = (1024,500))