import random

greetings = ["hi","is anyone there?", "hello", "good day","hello there"]
hyd = ["I'm doing great","I'm fine","superb","just fine","i am happy"]
bye = ["cya", "see you later","bye" ,"goodbye", "i am Leaving", "have a Good day"]
name = ["whats your name","what is your name","do you have any name","what should i call you","name"]
Machine_Learning = ["what is machine learning", "define machine learning", "tell me about machine learning","definition of machine learning"]
Types = ["types","types of machine learning","machine learning types"]
Supervised = ["supervised","what is supervised machine learning","supervised machine learning"]
Unsupervised = ["unsupervised","what is unsupervised machine learning","unsupervised machine learning"]
types_super = ["types of supervised learning","types of supervised ml","types of supervised"]
types_unsuper = ["types of unsupervised learning","types of unsupervised ml","types of unsupervised"]

print("\nThis chatbot is designed to tell you about Machine Learning and its basic concepts.")
print("Sample questions to ask from the bot are listed below:")
print("Definition of Machine Learning\nTypes of Machine_Learning\nwhat is supervised machine learning\nwhat is unsupervised machine learning\ntypes of supervised machine learning\ntypes of unsupervised machine learning")
print("                              --------------------------------------------                      ")
print("****************************** Have fun interacting with the MLExpert Bot **********************")
print("                              --------------------------------------------                      ")
print("Bot : Hi, I'm happy to see you here !!")
print("Please press Ctrl+C on the command line to quit interacting at any point of time\n")
while True:

	a = input('User: ')

	if a.lower() in greetings:
		reply = ["how are you","whats up","how you doing?"]
		print('MLExpert : '+random.choice(reply)+'\n')

	elif a.lower() in hyd:
		reply = ["Well that's great, Let's learn Machine Learning"]
		print('MLExpert : '+reply[0]+'\n')

	elif a.lower() in bye:
		reply = ["It was great catching up sith you, sad to see you go :(","Hope to see you again"]
		print('MLExpert : '+random.choice(reply)+'\n')

	elif a.lower() in Machine_Learning:
		reply = ["Machine Learning is the field of study that gives computers the capability to learn without being explicitly programmed. ML is one of the most exciting technologies that one would have ever come across. As it is evident from the name, it gives the computer that makes it more similar to humans: The ability to learn."]
		print('MLExpert : '+ reply[0]+'\n')

	elif a.lower() in name:
		reply = ["My name is MLExpert","You can call me TVC bot","TVC Bot in your service","My friends call me TVC Bot"]
		print('MLExpert : '+ random.choice(reply)+'\n')

	elif a.lower() in Types:
		reply = ["There are three types of Machine Learning: 1. Supervised 2. Unsupervised 3. Reinforecement Learning"]
		print('MLExpert : '+reply[0]+'\n')

	elif a.lower() in Supervised:
		reply = ["Supervised machine learning as the name indicates the presence of a supervisor as a teacher. Basically supervised learning is a learning in which we teach or train the machine using data which is well labeled that means some data is already tagged with the correct answer. After that, the machine is provided with a new set of examples(data) so that supervised learning algorithm analyses the training data(set of training examples) and produces a correct outcome from labeled data."]
		print('MLExpert : '+reply[0]+'\n')

	elif a.lower() in Unsupervised:
		reply = ["Unsupervised learning is the training of machine using information that is neither classified nor labeled and allowing the algorithm to act on that information without guidance. Here the task of machine is to group unsorted information according to similarities, patterns and differences without any prior training of data.  Unlike supervised learning, no teacher is provided that means no training will be given to the machine. Therefore machine is restricted to find the hidden structure in unlabeled data by our-self."]
		print('MLExpert : '+reply[0]+'\n')

	elif a.lower() in types_unsuper:
		reply = ["Different types of supervised machine learning algorithms are- Hierarchical clustering,K-means clustering,K-NN (k nearest neighbors),Principal Component Analysis,Singular Value Decomposition,Independent Component Analysis"]
		print('MLExpert : '+reply[0]+'\n')

	elif a.lower() in types_super:
		reply = ["Different types of supervised machine learning algorithms are- Linear Regression, Logistic Regression, Classification,Naïve Bayes Classifiers,Decision Trees,Support Vector Machine"]
		print('MLExpert : '+reply[0]+'\n')
	else:
		print("MLExpert : Sorry, I didn't get you ? I'm still in learning phase.\n")