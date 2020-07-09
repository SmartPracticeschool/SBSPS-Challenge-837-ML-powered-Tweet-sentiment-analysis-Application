from textblob import TextBlob
from tweepy import OAuthHandler
import sys,tweepy,csv,re
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, url_for
import string,csv
from collections import Counter
import GetOldTweets3 as got



import matplotlib.pyplot as plt

import os
app = Flask(__name__, template_folder='template')


class SentimentAnalysis:
	
	#def grph(graph):
			
   		#graph=os.system('python main.py')
   		#return graph

	def __init__(self):
		self.tweets = []
		self.tweetText = []
	
	def percentage(self,part, whole):
    		return 100* float(part)/float(whole)



	tweetText = []
	tweets = []
	piedata = []
	 

	def cleanTweet(self,tweet):
		# Remove Links, Special Characters etc from tweet
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())
	
	def DownloadData(self,keyword,tweet_no,piedata):
		
		piedata = []
		

		consumerKey = '5PbS87u5bnbPNnlOaru6ujWkK'
		consumerSecret = '1bQAMFQo9JpmdKtQJDP3FG250PtTN6PDQin4XcKoh5i3mh8u3T'
		accessToken = '945854006-vR8THk6iw5fNy89IZlAbiK2N1LF6zx5TvlDM1t1L'
		accessTokenSecret = 'neFUetVcoNwA33Mnmw55ndywcXd8RZXIgsfjlXWqz5NB9'
		auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
		auth.set_access_token(accessToken, accessTokenSecret)
		#api = tweepy.API(auth)
		api = tweepy.API(auth, wait_on_rate_limit=True)
		searchTerm = keyword
		noOfSearchTerms = int(tweet_no)

		self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(noOfSearchTerms)
		# Open/create a file to append data to
		csvFile = open('result.csv','a')
		#import main


		# Use csv writer
		csvWriter = csv.writer(csvFile)
		polarity = 0
		positive = 0
		wpositive = 0
		spositive = 0
		negative = 0
		wnegative = 0
		snegative = 0
		neutral = 0
		
		for tweet in self.tweets:
			#Append to temp so that we can store in csv later. I use encode UTF-8
			self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
			analysis = TextBlob(tweet.text)
			polarity += analysis.sentiment.polarity
			if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
				neutral += 1
			elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
				wpositive += 1
			elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
				positive += 1
			elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
				spositive += 1
			elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
				wnegative += 1
			elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
				negative += 1
			elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
				snegative += 1

		


		#Write to csv and close csv file
		csvWriter.writerow(self.tweetText)
		csvFile.close()

		
		import main
		#os.system('python main.py')
		

        
		positive = self.percentage(positive, noOfSearchTerms)
		wpositive = self.percentage(wpositive,noOfSearchTerms)
		spositive = self.percentage(spositive,noOfSearchTerms)
		negative = self.percentage(negative,noOfSearchTerms)
		wnegative = self.percentage(wnegative,noOfSearchTerms)
		snegative = self.percentage(snegative,noOfSearchTerms)
		neutral = self.percentage(neutral,noOfSearchTerms)

		polarity = polarity / noOfSearchTerms

		positive = format(positive, '.2f')
		wpositive = format(wpositive, '.2f')
		spositive = format(spositive, '.2f')
		snegative = format(snegative, '.2f')
		wnegative = format(wnegative, '.2f')
		negative = format(negative, '.2f')
		neutral = format(neutral, '.2f')
		print("How people are reacting on " + searchTerm + " by analyzing   " + str(noOfSearchTerms) + " tweets.")
		
		

		print()
		print("Detailed Report: ")
		print(str(positive) + "% people thought it was positive")
		print(str(wpositive) + "% people thought it was weakly positive")
		print(str(spositive) + "% people thought it was strongly positive")
		print(str(negative) + "% people thought it was negative")
		print(str(wnegative) + "% people thought it was weakly negative")
		print(str(snegative) + "% people thought it was strongly negative")
		print(str(neutral) + "% people thought it was neutral")
		
		piedata=[positive,negative,neutral,searchTerm,noOfSearchTerms,wpositive,spositive,wnegative,snegative]
		print(piedata[2])

		#import main


# reading text file
		text = open("result.csv", encoding="utf-8").read()

# converting to lowercase
		text = ""
		lower_case = text.lower()

# Removing punctuations
		cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
		tokenized_words = cleaned_text.split()

		stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself","yourselves", "he", "him", "his", 			"himself", "she", "her", "hers", "herself", "it", "its", "itself","they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", 			"that", "these","those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do","does", "did", "doing", "a", 			"an", "the", "and", "but", "if", "or", "because", "as", "until", "while","of", "at", "by", "for", "with", "about", "against", "between", "into", "through", 			"during", "before","after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again","further", "then", "once", 			"here", "there", "when", "where", "why", "how", "all", "any", "both", "each","few", "more", "most", "other", "some", "such", "no", "nor", "not", 			"only", "own", "same", "so", "than","too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
		final_words = []
		for word in tokenized_words:
    			if word not in stop_words:
        				final_words.append(word)

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

		emotion_list = []
		with open('emotions.txt', 'r') as file:
			for line in file:
        				clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        				word, emotion = clear_line.split(':')

        				if word in final_words:
            					emotion_list.append(emotion)

		#print(emotion_list)
		w = Counter(emotion_list)
		print(w)

# Plotting the emotions on the graph

		fig, ax1 = plt.subplots()
		ax1.bar(w.keys(), w.values())
		fig.autofmt_xdate()
		plt.savefig('bargraph.png')
		#plt.show()
		

		return piedata

		
		
		
		
 
		def plotPieChart(self, positive,negative,neutral, searchTerm, noOfSearchTerms):
			labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
			sizes = [positive,neutral,negative]
			colors = ['yellowgreen','gold','red']
			patches, texts = plt.pie(sizes, colors=colors, startangle=90)
			plt.legend(patches, labels, loc="best")
			plt.title('How people are reacting on abcdef ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
			plt.axis('equal')
			plt.tight_layout()
			#plt.show()
			plt.savefig('pie.png')
		


       

@app.route('/',methods=['GET','POST'])
def form():
	global piedata
	global tweets
	tweets=[]
			
	global labels
	labels=[]
	global sizes
	sizes=[]
	global colors
	colors=[]
	piedata = []
	
	
	if (request.method=='POST'):
		
		#piedata = []
		
		
		
		keyword = request.form.get('keyword')
		tweet_no = request.form.get('tweet_no')
		sa = SentimentAnalysis()
		piedata = sa.DownloadData(keyword,tweet_no,piedata)
		#results = [keyword,tweet_no,piedata]
		tweets=sa.DownloadData(keyword,tweet_no,piedata)
		#self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(noOfSearchTerms)
		#tweets=self.tweets
		

	return render_template('index.html',piedata=piedata,tweets=tweets)
	#else:
		#return render_template('index.html')


"""
@app.route('/tweets',methods=['GET','POST'])
def view():
	global tweets
	tweets=[]
	if request.method=='POST':
		keyword = request.form.get('keyword')
		tweet_no = request.form.get('tweet_no')
		sa = SentimentAnalysis()
		
		tweet=sa.DownloadData(keyword,tweet_no,piedata)
		
		self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(noOfSearchTerms)
		tweets=self.tweets

		return render_template('view.html',tweets=tweets)

"""	


if __name__ == "__main__":
	# calling main function
	app.run(debug=True)
	
	#import main
	#execfile("main.py 1")

app.run(debug=True)

#import main
#execfile("main.py 0")


