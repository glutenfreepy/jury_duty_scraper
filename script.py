import requests
from bs4 import BeautifulSoup

JURY_DUTY_URL = "https://www.ventura.courts.ca.gov/JuryService/"


def parse_webpage(url=JURY_DUTY_URL):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    reporting = soup.find_all("div", {"id": "reporting"})
    reporting_text = reporting[0].text.strip()
    return reporting_text


def send_notification(jury_info):
    requests.post("https://ntfy.sh/ventura_jury_duty",
                  data=jury_info.encode(encoding='utf-8'))


if __name__ == "__main__":
    jury_info = parse_webpage()
    send_notification(jury_info)
