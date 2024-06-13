import requests

from bs4 import BeautifulSoup

JURY_DUTY_URL = "https://www.ventura.courts.ca.gov/JuryService/"

response = requests.get(JURY_DUTY_URL)
soup = BeautifulSoup(response.text, "html.parser")
# soup.find_all("div", {"id": "reporting"})
# left off at 16:20 here https://pybites.circle.so/c/pybites-coaching-calls/sections/117462/lessons/394745
breakpoint()