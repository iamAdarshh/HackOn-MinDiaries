import requests

anxeity_questions = {'Anxious mood': {'des': 'Worries, anticipation of the worst, fearful anticipation, irritability.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']},
        'Tension': {'des': 'Feelings of tension, fatigability, startle response, moved to tears easily, trembling, feelings of restlessness, inability to relax.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']}, 
        'Fears': {'des': 'Of dark, of strangers, of being left alone, of animals, of traffic, of crowds.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']}, 
        'Insomnia': {'des': 'Difficulty in falling asleep, broken sleep, unsatisfying sleep and fatigue on waking, dreams, nightmares, night terrors.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']},
        'Intellectual': {'des': 'Difficulty in concentration, poor memory.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']},
        'Depressed mood': {'des': 'Loss of interest, lack of pleasure in hobbies, depression, early waking, diurnal swing.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']},
        'Somatic (muscular)': {'des': 'Pains and aches, twitching, stiffness, myoclonic jerks, grinding of teeth, unsteady voice, increased muscular tone.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']},
        'Somatic (sensory)': {'des': 'Tinnitus, blurring of vision, hot and cold flushes, feelings of weakness, pricking sensation.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']}, 
        'Cardiovascular symptoms': {'des': 'Tachycardia, palpitations, pain in chest, throbbing of vessels, fainting feelings, missing beat.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']}, 
        'Respiratory symptoms': {'des': 'Pressure or constriction in chest, choking feelings, sighing, dyspnea.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']},
        'Gastrointestinal symptoms': {'des': 'Difficulty in swallowing, wind abdominal pain, burning sensations, abdominal fullness, nausea, vomiting, borborygmi, looseness of bowels, loss of weight, constipation.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']}, 
        'Genitourinary symptoms': {'des': 'Frequency of micturition, urgency of micturition, amenorrhea, menorrhagia, development of frigidity, premature ejaculation, loss of libido, impotence.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']},
        'Autonomic symptoms': {'des': 'Dry mouth, flushing, pallor, tendency to sweat, giddiness, tension headache, raising of hair.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']},
        'Behavior at interview': {'des': 'Fidgeting, restlessness or pacing, tremor of hands, furrowed brow, strained face, sighing or rapid respiration, facial pallor, swallowing, etc.', 'options': ['Not present', 'Mild', 'Moderate', 'Severe', 'Very Severe']}
        }

def getIndiaData():
        url = "https://coronavirus-smartable.p.rapidapi.com/stats/v1/IN/"

        headers = {
                'x-rapidapi-key': "1462e1f3f4msh27f76a4b837890ep16cf77jsne70d94f8cd76",
                'x-rapidapi-host': "coronavirus-smartable.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        response = response.json()

        data = {
                'location': response["location"],
                'totalConfirmedCases': response["stats"]["totalConfirmedCases"],
                'newlyConfirmedCases': response["stats"]["newlyConfirmedCases"],
                'totalDeaths': response["stats"]["totalDeaths"],
                'newlyDeaths': response["stats"]["newDeaths"],
                'totalRecovedCases': response["stats"]["totalRecoveredCases"],
                'newlyRecovedCases': response["stats"]["newlyRecoveredCases"],
                'lastUpdated': response["updatedDateTime"]
        }

        return data

def getGlobalCovidData(country=None):
        content = {}

        url = "https://coronavirus-smartable.p.rapidapi.com/stats/v1/global/"

        headers = {
                'x-rapidapi-key': "1462e1f3f4msh27f76a4b837890ep16cf77jsne70d94f8cd76",
                'x-rapidapi-host': "coronavirus-smartable.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        response = response.json()

        content["lastUpdated"] = response["updatedDateTime"]

        if country == None:
                for data in response["stats"]["breakdowns"]:
                        content[data["location"]["countryOrRegion"]] = {
                                'totalConfirmedCases' : data["totalConfirmedCases"],
                                'newlyConfirmedCases': data["newlyConfirmedCases"],
                                'totalDeaths': data["totalDeaths"],
                                'newlyDeaths': data["newDeaths"],
                                'totalRecovedCases': data["totalRecoveredCases"],
                                'newlyRecovedCases': data["newlyRecoveredCases"]
                        }
        else:
                data_found = False
                for data in response["stats"]["breakdowns"]:
                        if data["location"]["countryOrRegion"].lower() == country.lower():
                                content[data["location"]["countryOrRegion"]] = {
                                        'totalConfirmedCases' : data["totalConfirmedCases"],
                                        'newlyConfirmedCases': data["newlyConfirmedCases"],
                                        'totalDeaths': data["totalDeaths"],
                                        'newlyDeaths': data["newDeaths"],
                                        'totalRecovedCases': data["totalRecoveredCases"],
                                        'newlyRecovedCases': data["newlyRecoveredCases"]
                                }
                                data_found = True
                
                if data_found == False:
                        content["Error"] = "Not Found"
        
        return content
                        
