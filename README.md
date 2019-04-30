# Medical-Information-Notification-Chatbot

Chatbot Service Development with Python

If you have any aches and pains, tell the chatbot where you're sick<br>
Then, chatbot will diagnose you for what kind of disease you have. Also chatbot will tell you a dietary regime and prevention for diseases.

You can search for curious diseases.

### Stack
- FrontEnd : html, css, bootstrap
- BackEnd : python - django
- DataBase : sqlite3
- Crawling : python - BeautifulSoup4

## Tutorial


## Progress

We got medical data such as definition, cause, and symptoms of disease from Naver Encyclopedia by crawling<br>
And each item was put into the database.

![DB](https://user-images.githubusercontent.com/41745717/56972604-3df94400-6ba6-11e9-930b-3a112187e267.png)


### How to use BeautifulSoup4
```
import bs4
    main_url = "https://terms.naver.com/list.nhn?cid=51007&categoryId=51007" + "&page=" + str(page_num)
    main_html = urlopen(main_url)

    bs_obj = bs4.BeautifulSoup(main_html, "html.parser")
```
We can get data on each Naver Encyclopedia page in the above way.


## To Do

- We will make a chatbot using Kakaotalk API.

- We will present symptoms of each disease as a set of specific words. (Example : cold - ["a fever", "cough", "phlegm", ])
- We will map the sentences you enter to each symptom.
- We will select several diseases that have same symptom that users suffer
- Chatbot will ask a few questions through some selected diseases that have symptoms
- Chatbot will inform  you of suspected diseases and information about them.
