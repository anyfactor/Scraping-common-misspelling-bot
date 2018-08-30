# Scraping of the commonly misspelled bot on reddit

Scraping of the [Common misspelling bot](https://www.reddit.com/user/CommonMisspellingBot), using selenium and MS excel.

I have scraped about 884 comments of the bot. Four information I have extracted from each comments-

* Misspelled word
* Correction
* Upvotes
* Respective subreddits

I have probably forgot to adjust each upvote, by deducting one vote from each of them. 

I have outputted the results in tuples using pythons zip function, rather than outputting them in CSV (I haven't learned it yet). Then after a series of deletion of some characters I have saved it as CSV, then used Microsoft excel for further analysis and visualization.
