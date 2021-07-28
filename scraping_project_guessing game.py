import requests
from bs4 import BeautifulSoup
import random


quotes_list=[]
n_url = "/page/1"
url = "http://quotes.toscrape.com"
while n_url:
    response= requests.get(f"{url}{n_url}")
    soup=BeautifulSoup(response.text,"html.parser")
    quotes=soup.select(".quote")

    for quote in quotes:
        q=quote.find(class_="text").get_text()
        name=quote.find(class_="author").get_text()
        about_url=url+quote.find("a")["href"]
        quotes_list.append([q,name,about_url])
    next_btn=soup.find(class_="next")
    n_url=next_btn.find("a")["href"] if next_btn else None



def play():
    quote=random.choice(quotes_list)
    print("\nHere's a quote:\n")
    print(quote[0])
    guess=4
    print(quote[1].lower())
    while guess>0:
        ans=input(f"\nWho said this? Guesses remaining: {guess}. ")
        if ans.lower()==quote[1].lower():
            print("You guessed correctly! Congratulations!")
            choice=input("\nWould you like to play again (y/n)?")
            while choice.lower() not in ('y','n','no','yes'):
                choice = input("\nWould you like to play again (y/n)?")
            if choice.lower()=='n' or choice.lower()=='no':
                print("Ok! See you next time!")
                exit()
            else:
                print("Great! Here we go again...")
                return play()

        else :
            guess-=1
            if guess==3:
                r = requests.get(quote[2])
                s = BeautifulSoup(r.text, "html.parser")
                date = s.find(class_="author-born-date").get_text()
                location = s.find(class_="author-born-location").get_text()
                print(f"Here's a hint: The author was born in {date} {location}.")
            elif guess==2:
                print(f"Here's a hint: The author's first name starts with {quote[1][0]}")
            elif guess==1:
                l=quote[1].split(' ')
                print(f"Here's a hint: The author's last name starts with {l[-1][0]}")

    print(f"Sorry, you've run out of guesses. The answer was {quote[1]}")
    choice = input("\nWould you like to play again (y/n)?")
    while choice.lower() not in ('y', 'n', 'no', 'yes'):
        choice = input("\nWould you like to play again (y/n)?")
    if choice.lower() == 'n' or choice.lower() == 'no':
        print("Ok! See you next time!")
        exit()
    else:
        print("Great! Here we go again...")
        return play()



play()