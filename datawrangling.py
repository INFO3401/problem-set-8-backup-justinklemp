#Justin Klemperer
#INFO3401
#Problem Set 8
#28 October 2018

#Collabortators: Steven, Luke, Harold, Zach, Marissa

import pandas as pd

import re

import csv


#Function which takes .csv as inputs and uses cleaned data for outputs

def generateCleanFile(input_file, output_file):
    
    df = pd.read_csv(input_file, encoding = "latin1", low_memory = False)


#1. Remove spam: Some comments on social media contain spam and aren't useful for our analysis. We can determine comments that are spam by removing any comments containing a web address or any of the following keywords: App, FREE, %20, Check out my page. Note that these keywords are NOT case sensitive (e.g., you should remove comments containing APP, app, App, APp, etc.). Also, don't worry about the capitalization of the output file. If it says "R.I.P. Colby" in the input file and "r.i.p. colby" in the output file, that's okay.

df['comment_msg'] = df['comment_msg'].apply(lambda x: x.lower())

spam_gone = ['app', 'free', '%20', 'check out my page', 'http://', 'www.', '.com']

df = df[df.comment_msg.str.contains('|'.join(spam_gone)) == False]


#2. Remove HTML Tags: Since this data has been scraped from the web, it contains a number of HTML tags that indicate components of the DOM but aren't useful for analysis. Remove any HTML tags, but keep the contents of the comment. For example, Hi, Mike! will become Hi, Mike!

df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'<.*?>',"",str(x)))

df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'\r*',"", str(x)))

df['comment_msg'] = df['comment_msg'].apply(lambda x: str(x).lstrip())


#3. Remove Missing Data: The data collection script used to scrape MySpace inserted null values in cases where the data collection was unable to process meaningful content. Remove all rows where the message is null.

df = df[df['comment_msg'] != "null"]


df = df[df['comment_msg'] != ""]


df = df[df['comment_msg'] != "nan"]


#To export:

df.to_csv(output_file)


generateCleanFile("dd-comment-profile.csv", "dd-comment-profile-revised-clean.csv")
