def count(Country):
    import matplotlib.pyplot as plt
    import pandas as pd
    import requests
    import json
    import os
    from pathlib import Path

    my_file = Path("./pythonjseel/web/img.png")

    if os.path.exists(my_file):
        os.remove(my_file)

    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "3a498859c5msh412bbfd36004dbcp1acc62jsne99b7a2663fb"
        }

    response = requests.request("GET", url, headers=headers)

    world_data = json.loads(response.text)["world_total"]

    whole_data = json.loads(response.text)["countries_stat"]

    country_data = dict

    if Country == "" :
        
        Total_Cases = str(world_data["total_cases"])
        Total_Deaths = str(world_data["total_deaths"])
        Total_Recovered = str(world_data["total_recovered"])
        New_Cases = str(world_data["new_cases"])
        New_Deaths = str(world_data["new_deaths"])
        Serious_Critical = str(world_data["serious_critical"])
        # Total_Active = int(Total_Cases.replace(",","")) - int(Total_Deaths.replace(",","")) - int(Total_Recovered.replace(",",""))

        plot_Cases = Total_Cases.replace(",","")
        plot_Recovered = int(Total_Recovered.replace(",",""))
        plot_Deaths = int(Total_Deaths.replace(",",""))

        data = [plot_Cases,plot_Recovered,plot_Deaths]
        label=['Cases,''Recovered','Deaths']
        color = ['royal blue,'"#62D726","red"]
        
        plt.pie(x=data,startangle=90,labels=label,radius=2,counterclock=False,colors=color,shadow = True)

        plt.savefig(r"C:\\Users\\Afranzio\\Python\\pythonjseel\\web\\"+Country +".png" ,transparent=True,bbox_inches='tight')
        
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
        for data in whole_data:
            if data["country_name"] == Country :
                country_data = data

        Country_Name = country_data["country_name"]
        Total_Cases = str(country_data["cases"])
        Total_Active = str(country_data["active_cases"])
        Total_Deaths = str(country_data["deaths"])
        Total_Recovered = str(country_data["total_recovered"])
        New_Cases = str(country_data["new_cases"])
        New_Deaths = str(country_data["new_deaths"])
        Total_test = str(country_data["total_tests"])

        plot_Active = int(Total_Active.replace(",",""))
        plot_Recovered = int(Total_Recovered.replace(",",""))
        plot_Deaths = int(Total_Deaths.replace(",",""))

        data = [plot_Active,plot_Recovered,plot_Deaths]
        label=['Active','Recovered','Deaths']
        color = ["royalblue","#62D726","red"]
        
        plt.pie(x=data,startangle=90,labels=label,radius=2,explode=[0,0,1],counterclock=False,colors=color,shadow = True,autopct='%1.f%%')

        plt.savefig(r"C:\\Users\\Afranzio\\Python\\pythonjseel\\web\\img.png" ,transparent=True, bbox_inches='tight', pad_inches=0.1)

        return("Country = " + Country_Name,
            "\nTotal_Cases = " + Total_Cases,
            "\nTotal_Active = " + Total_Active,
            "\nTotal_Deaths = " + Total_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nNew_Cases = " + New_Cases,
            "\nNew_Deaths = " + New_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nTotal_Test = "+Total_test)