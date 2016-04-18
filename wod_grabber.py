#!/Users/jonmiller/.virtualenvs/wod_grab/bin/python3
from lxml import html
import requests
from datetime import date


def main():
    print("Today is " + str(date.today()))
    today = date.today().strftime("%B-%d-%Y")
    page = requests.get('https://www.crossfitinvictus.com/wod/' + today)
    tree = html.fromstring(page.content)
    workout_list = tree.xpath('//div[@class="entry-content"]/p')
    for workout in workout_list:
        print(workout.text_content())

if __name__ == "__main__":
    main()
