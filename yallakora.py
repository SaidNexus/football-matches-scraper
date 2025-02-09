import requests
from bs4 import BeautifulSoup
import csv
import os

date = input("enter a Date in the follow format MM/DD/YYYY:")
page_center_maths = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")

def main(page):

    src = page.content
    soup = BeautifulSoup(src,"lxml")
    matches_details = []

    championships = soup.find_all("div",{'class' : 'matchCard'})
    
    def get_math_info(championships):

        championship_title = championships.find("h2").text.strip()
        all_matches = championships.find_all('div',{'class' : 'teamsData'})
        num_of_matches = len(all_matches)
        for i in range(num_of_matches):
            # get teams names
            team_A = all_matches[i].find('div',{"class":"teamA"}).text.strip()
            team_B = all_matches[i].find('div',{"class":"teamB"}).text.strip()
            # get score
            match_result = all_matches[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            score = f"{match_result[0].text.strip()}  {match_result[1].text.strip()}"

            # get time
            match_time = all_matches[i].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()

            # add match info to matches_detalis
            matches_details.append({"اسم البطوله":championship_title,"الفاريق الاول":team_A,"النتيجه":score,"الفاريق التاني":team_B,"ميعاد المباره":match_time})
    
    
    for i in range(len(championships)):
        get_math_info(championships[i])
    
    keys = matches_details[0].keys()
    #Get the dir of my location to save the new CSV
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    #Get the name for the new CSV
    name = input("enter file name : ").strip()

    #To merge the dir with the name of new CSV
    file_path = os.path.join(current_folder+"/outputs", f"{name}.csv")

    with open(f"{file_path}.csv",'w',encoding='utf-8') as output_file:
        dici_writer = csv.DictWriter(output_file,keys)
        dici_writer.writeheader()
        dici_writer.writerows(matches_details)
        print("file created")


main(page_center_maths)
