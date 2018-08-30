from selenium import webdriver

browser= webdriver.Chrome(executable_path="")
browser.get('https://old.reddit.com/user/CommonMisspellingBot/comments/?sort=top') # The top posts of the bot

pages = 40 #40 page iteration

# A stupid solution for not learning the csv module, and creating lists for what is supposed to be columns
subreddit =[]
misspell = []
correction = []
upvote = []

for i in range(pages):
    # Subreddits
    subreddits = browser.find_elements_by_class_name('subreddit')
    for sub in subreddits:
        subreddit.append(sub.text)

    # Post informations
    bold_letters = browser.find_elements_by_tag_name('strong')

    # There are three bold element in each comment, they are for -  misspelled word, correction, and hint
    
    imisspell, icorrection, ihint = 0, 1, 2 
    for i in range(int(len(bold_letters)/3)):
        misspell.append(bold_letters[imisspell].text)
        correction.append(bold_letters[icorrection].text)

        imisspell +=3
        icorrection +=3
        ihint +=3


    # Upvotes
    scores = browser.find_elements_by_class_name('likes')
    for upvotes in scores:
        upvote.append(upvotes.get_attribute("innerHTML"))

    next_button= browser.find_element_by_class_name('next-button')
    next_button.click()

# This outputs tuples which a copy, pasted in text editor and with a series of replacing chracters("'", " points", "(", ")" ) i have saved them as csv
for i in zip(subreddit,misspell,correction,upvote):
    print(i)
