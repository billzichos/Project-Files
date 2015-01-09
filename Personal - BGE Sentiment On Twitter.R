install.packages("twitteR")
install.packages("plyr")
install.packages("stringr")
install.packages("ggplot2")

library(twitteR)		# provides an interface to the twitter api
library(ROAuth)		# allows users to authenticate via OAuth to the server of their choise
library(plyr)		# tools for splitting, applying and combining data
library(stringr)		# makes it easier to work with strings
library(ggplot2)		# an implementation of the grammar of graphics

load("C:\\Users\\Bill\\SkyDrive\\Documents\\R Code\\Authentication\\twitter_authentication.RData")
registerTwitterOAuth(Cred)

bge.list <- searchTwitter('@MyBGE', n=1000, cainfo="cacert.pem")
bge.df <- twListToDF(bge.list)
write.csv(bge.df, file="C:\\Users\\Bill\\SkyDrive\\Documents\\R Code\\temp\\BGEtweets.csv", row.names=F)

str(bge.df)

score.sentiment = function(sentences, pos.words, neg.words, .progress='no) {
	require(plyr)
	require(stringr)

	scores = laply(sentences, function(sentence, pos.words, neg.words) {
	
	
	}
}

help(twitteR)

??TwitteR

availableTrendLocations()
dmGet(n=25)