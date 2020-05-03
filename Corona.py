import eel

eel.init("web")

@eel.expose

def finder(data):

    find = data

    import requests,json

    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

    headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "3a498859c5msh412bbfd36004dbcp1acc62jsne99b7a2663fb"
    }

    response = requests.request("GET", url, headers=headers)

    whole_data = json.loads(response.text)["countries_stat"]

    country_data = dict

    world_data = json.loads(response.text)["world_total"]
    

    if find == "" :
        
        print("Please Enter Valid Country..")
        
        Total_Cases = str(world_data["total_cases"])
        Total_Deaths = str(world_data["total_deaths"])
        Total_Recovered = str(world_data["total_recovered"])
        New_Cases = str(world_data["new_cases"])
        New_Deaths = str(world_data["new_deaths"])
        Serious_Critical = str(world_data["serious_critical"])
        #Total_Active = Total_Cases.replace(",","") - Total_Deaths.replace(",","") - Total_Recovered.replace(",","")
        
        return("Starts_Over = " + "Global Status",
            "\nTotal_Cases = " + Total_Cases,
            "\nTotal_Deaths = " + Total_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nNew_Cases = " + New_Cases,
            "\nNew_Deaths = " + New_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nSerious_Critical = "+ Serious_Critical)
        
        
    else:
        for datas in whole_data:
            if datas["country_name"]==find:
                country_data = datas
                
        Country_Name = country_data["country_name"]
        Total_Cases = str(country_data["cases"])
        Total_Active = str(country_data["active_cases"])
        Total_Deaths = str(country_data["deaths"])
        Total_Recovered = str(country_data["total_recovered"])
        New_Cases = str(country_data["new_cases"])
        New_Deaths = str(country_data["new_deaths"])
        Total_test = str(country_data["total_tests"])
        
        
        return("Country = " + Country_Name,
            "\nTotal_Cases = " + Total_Cases,
            "\nTotal_Active = " + Total_Active,
            "\nTotal_Deaths = " + Total_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nNew_Cases = " + New_Cases,
            "\nNew_Deaths = " + New_Deaths,
            "\nTotal_Recovered = " + Total_Recovered,
            "\nTotal_Test = "+Total_test)


eel.start('index.html',size=(1200,700))