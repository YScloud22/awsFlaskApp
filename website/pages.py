from flask import Blueprint, render_template, request, flash, redirect
import sys
import praw
import re
# import stocks.py


pages = Blueprint('pages', __name__)



@pages.route('/newloading', methods = ['GET','POST'])
def newloadingPage():
    return render_template("newloading.html")

@pages.route('/loading', methods = ['GET','POST'])
def loadingPage():
    return render_template("loading_page.html")

@pages.route('/data', methods = ['GET','POST'])
def data():

    stock_ticker = request.form.get("stock_ticker").lower()
    company = request.form.get("stock_name").lower()

    reddit = praw.Reddit(
        client_id="AdSw7bvhSVSVmg",
        client_secret="Gmwx7PI0P-AdQb-EGZwGME0YGd4T4A",
        username="jujutsuGojo",
        password="redditbot",
        user_agent="redditscrape")

    subs_list = ["stocks"]

    def day(stock_ticker, company, subs_list = subs_list):
        
        day_count = 0
    
        for i in subs_list:
            subreddit = reddit.subreddit(i)
            top_python = subreddit.top("day", limit=1000)  # 1000 is limit
            day_count += counter(top_python, stock_ticker, company)
        return day_count
    def week(stock_ticker, company,subs_list = subs_list):
       
        week_count = 0
        for i in subs_list:
            subreddit = reddit.subreddit(i)
            top_python = subreddit.top("week", limit=1000)  # 1000 is limit
            week_count += counter(top_python, stock_ticker, company)
        return week_count
    def month(stock_ticker, company, subs_list = subs_list):
        month_count = 0
        for i in subs_list:
            subreddit = reddit.subreddit(i)
            top_python = subreddit.top("month", limit=1000)  # 1000 is limit
            month_count += counter(top_python, stock_ticker, company)
        return month_count
    def counter(time_filter, stock_ticker, company):
        count = 0
        for submission in time_filter:
            post = submission.title.lower()
            if re.search(stock_ticker, post) is not None:  # counting all matching mentions that are (not None) True
                count += 1
            elif re.search(company, post) is not None:  # counting all matching mentions that are (not None) True
                count += 1
        return count

    day = day(stock_ticker, company)
    week = week(stock_ticker, company)
    month = month(stock_ticker, company)


    data = [("day",day), ("week",week), ("month",month)] #change numbers to actual mentions later
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    

    return render_template("data.html", 
    stock_ticker = stock_ticker, 
    company = company,
    day = day, 
    week = week, 
    month = month, 
    labels = labels, 
    values = values
    )

@pages.route('/', methods=['GET','POST'])
def home():
    list 
    stock_ticker = 'xxxx'
    company = 'xxxx'
    if request.method == 'POST':
        stock_ticker = request.form.get("stock_ticker")
        company = request.form.get("stock_name")
        if len(stock_ticker) == 0: 
            return render_template("base.html")
        if len(company) == 0: 
            return render_template("base.html")
        else:
            return data()
    return render_template("base.html")

@pages.route('/graph', methods = ['GET', 'POST'])
def graph(): 
    data = [("day",10), ("week",20), ("month",15)] #change numbers to actual mentions later
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("graph.html", labels=labels, values=values)

