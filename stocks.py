import praw
import re

reddit = praw.Reddit(
        client_id="AdSw7bvhSVSVmg",
        client_secret="Gmwx7PI0P-AdQb-EGZwGME0YGd4T4A",
        username="jujutsuGojo",
        password="redditbot",
        user_agent="redditscrape")

def day(stock_ticker, company):
    subs_list = ["stocks", "investing", "wallstreetbets",
                 "options", "StockMarket", "pennystocks",
                 "thetagang", "smallstreetbets"]
    day_count = 0
    for i in subs_list:
        subreddit = reddit.subreddit(i)
        top_python = subreddit.top("day", limit=100)  # 1000 is limit
        day_count += counter(top_python, stock_ticker, company)
    return day_count


def week(stock_ticker, company):
    subs_list = ["stocks", "investing", "wallstreetbets",
                 "options", "StockMarket", "pennystocks",
                 "thetagang", "smallstreetbets"]
    week_count = 0
    for i in subs_list:
        subreddit = reddit.subreddit(i)
        top_python = subreddit.top("week", limit=100)  # 1000 is limit
        week_count += counter(top_python, stock_ticker, company)
    return week_count


def month(stock_ticker, company):
    subs_list = ["stocks", "investing", "wallstreetbets",
                 "options", "StockMarket", "pennystocks",
                 "thetagang", "smallstreetbets"]
    month_count = 0
    for i in subs_list:
        subreddit = reddit.subreddit(i)
        top_python = subreddit.top("month", limit=100)  # 1000 is limit
        month_count += counter(top_python, stock_ticker, company)
    return month_count

def counter(time_filter, stock_ticker, company):
    count = 0
    for submission in time_filter:
        post = submission.title.lower()  # get post titles
        # print(post)
        """
        re.search function returns None when search does not find matching,
        does not return true if ticker is found, so 'is not None' fixes this 
        """

        if re.search(stock_ticker, post) is not None:  # counting all matching mentions that are (not None) True
            count += 1
        elif re.search(company, post) is not None:  # counting all matching mentions that are (not None) True
            count += 1

    return count


stock_ticker = 'MSFT'.lower()

company = "Microsoft".lower()

flag_loading = False

day = day(stock_ticker, company)
week = week(stock_ticker, company)
month = month(stock_ticker, company)

flag_loading = True