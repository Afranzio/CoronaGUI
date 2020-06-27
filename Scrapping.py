#Country Value get from source file
def count(Country):

    #Import Required Modules to Use..
    import matplotlib.pyplot as plt
    import requests
    import json
    import os
    from pathlib import Path
    
    #Set This Path As OS Path
    my_file = Path("./pythonjseel/web/img.png")

    if os.path.exists(my_file):  #Check if the file exists and remove it
        os.remove(my_file)

    #API Section
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "3a498859c5msh412bbfd36004dbcp1acc62jsne99b7a2663fb"
        }

    response = requests.request("GET", url, headers=headers)

    #Getting Value Of Global Status
    world_data = json.loads(response.text)["world_total"]

    #Getting Value Of Every Country Status
    whole_data = json.loads(response.text)["countries_stat"]

    country_data = dict

    #Check If Input Country is empty string or not....
    if Country == "" :
        
        #Extract individual data from API
        Total_Cases = str(world_data["total_cases"])
        Total_Deaths = str(world_data["total_deaths"])
        Total_Recovered = str(world_data["total_recovered"])
        New_Cases = str(world_data["new_cases"])
        New_Deaths = str(world_data["new_deaths"])
        Serious_Critical = str(world_data["serious_critical"])
        # Total_Active = int(Total_Cases.replace(",","")) - int(Total_Deaths.replace(",","")) - int(Total_Recovered.replace(",",""))

        #Convert the string data to an integer  to use the data
        plot_Cases = Total_Cases.replace(",","")
        plot_Recovered = int(Total_Recovered.replace(",",""))
        plot_Deaths = int(Total_Deaths.replace(",",""))

        #List those data into a variable
        data = [plot_Cases,plot_Recovered,plot_Deaths]
        label=['Cases,''Recovered','Deaths']
        color = ['royal blue,'"#62D726","red"]
        
        #Pie Plot the Data
        plt.pie(x=data,startangle=90,labels=label,radius=2,counterclock=False,colors=color,shadow = True)

        #Save the Plot
        plt.savefig(r"C:\\Users\\Afranzio\\Python\\pythonjseel\\web\\ img.png" ,transparent=True,bbox_inches='tight')

        #Clear the previous plot
        plt.clf()
        
        return("Starts_Over = " + "Global Status",
            "\nTotal_Cases = " + Total_Cases,   
            # "\nTotal_Active = " + str(Total_Active),
            "\nTotal_Deaths = " + Total_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nNew_Cases = " + New_Cases,
            "\nNew_Deaths = " + New_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nSerious_Critical = "+ Serious_Critical)
        
        
    else:

        #Get the exact country data from all country data
        for data in whole_data:
            if data["country_name"] == Country :
                country_data = data

        #Extract individual data from API
        Country_Name = country_data["country_name"]
        Total_Cases = str(country_data["cases"])
        Total_Active = str(country_data["active_cases"])
        Total_Deaths = str(country_data["deaths"])
        Total_Recovered = str(country_data["total_recovered"])
        New_Cases = str(country_data["new_cases"])
        New_Deaths = str(country_data["new_deaths"])
        Total_test = str(country_data["total_tests"])

        #Convert the string data to an integer  to use the data
        plot_Active = int(Total_Active.replace(",",""))
        plot_Recovered = int(Total_Recovered.replace(",",""))
        plot_Deaths = int(Total_Deaths.replace(",",""))

        #List those data into a variable
        data = [plot_Active,plot_Recovered,plot_Deaths]
        label=['Active','Recovered','Deaths']
        color = ["royalblue","#62D726","red"]

        #Plot the Data
        plt.pie(x=data,startangle=90,labels=label,radius=2,explode=[0,0,1],counterclock=False,colors=color,shadow = True,autopct='%1.f%%')

        #Save the plot
        plt.savefig(r"C:\\Users\\Afranzio\\Python\\pythonjseel\\web\\img.png" ,transparent=True, bbox_inches='tight')

        #Clear the plot.
        plt.clf()

        return("Country = " + Country_Name,
            "\nTotal_Cases = " + Total_Cases,
            "\nTotal_Active = " + Total_Active,
            "\nTotal_Deaths = " + Total_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nNew_Cases = " + New_Cases,
            "\nNew_Deaths = " + New_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nTotal_Test = "+Total_test)