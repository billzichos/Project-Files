wordSentiment = {'affordable': 'Positive',
                 'amazing': 'Positive',
                 'angry': 'Negative',
		 'appreciate': 'Positive',
                 'awesome': 'Positive',
                 'best': 'Positive',
		 'bitch': 'Negative',
                 'bitter': 'Negative',
                 'cheap': 'Negative',
                 'crap': 'Negative',
                 'exceptional': 'Positive',
                 'excite': 'Positive',
		 'excited': 'Positive',
                 'fabulous': 'Positive',
		 'fail': 'Negative',
                 'failure': 'Negative',
                 'friend': 'Positive',
		 'friendly': 'Positive',
                 'glamorous': 'Positive',
		 'good': 'Positive',
                 'great': 'Positive',
                 'gross': 'Negative',
                 'handsome': 'Positive',
                 'happy': 'Positive',
                 'hate': 'Negative',
		 'hell': 'Negative',
                 'impress': 'Positive',
                 'inconvenience': 'Negative',
                 'kill': 'Negative',
                 'kind': 'Positive',
		 'lose': 'Negative',
                 'loser': 'Negative',
                 'love': 'Positive',
                 'lovely': 'Positive',
                 'mad': 'Negative',
		 'never': 'Negative',
                 'nice': 'Positive',
		 'notfriendly': 'Negative',
		 'nothappy': 'Negative',
		 'notnice': 'Negative',
		 'pretty': 'Positive',
                 'sexy': 'Positive',
                 'shit': 'Negative',
		 'shitty': 'Negative',
		 'sour': 'Negative',
                 'stoked': 'Positive',
                 'strange': 'Negative',
		 'stupid': 'Negative',
		 'suck': 'Negative',
                 'super': 'Positive',
		 'superior': 'Positive',
		 'sweet': 'Positive',
                 'terrible': 'Negative',
                 'threat': 'Negative',
		 'ugly': 'Negative',
                 'unhappy': 'Negative',
                 'wait': 'Negative',
                 'win': 'Positive',
                 'wonderful': 'Positive',
                 'worse': 'Negative',
		 'worst': 'Negative',
		 'wow': 'Positive'}

print(len(set(wordSentiment.values())))

text = 'I love the new soccer ball I received for Christmas.'

import nltk

words = nltk.word_tokenize(text)

sentimentAnalysis = [wordSentiment.setdefault(word, "UNK") for word in words]

print(sentimentAnalysis)
