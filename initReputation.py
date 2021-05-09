
totalNumOfTweets = 0


def initInfluence(users):
    CV = 1.0
    TV = 1.0
    avgInf = 0.0
    for usr in users:
        users[usr]["inf0"] = users[usr]["followers"] / (users[usr]["following"] + 1) / CV
        avgInf += users[usr]["inf0"]

    avgInf /= len(users)

    for usr in users:
        if users[usr]["inf0"] > TV:
            users[usr]["inf0"] = TV + users[usr]["followers"] / avgInf

    for usr in users:
        users[usr]["inft"] = users[usr]["inf0"]



def updTweets(user):
        user["tweets"] += 1
        global totalNumOfTweets
        totalNumOfTweets += 1

i = 0
def updateInfAndRetweet(users, reciever, sender): # sender retweets from reciever
    # global i
    # i+=1
    users[reciever]["retweets"] += 1
    users[sender]["retweetsSent"] += 1
    users[reciever]["inft"] += users[sender]["inf0"]
    users[reciever]["RetweetedBy"].append(sender)

    # if(i%100 == 0):
    #     print(sender,  sender["inf0"])


def updateReputation(users, usr):

    inf_t = users[usr]["inft"]
    inf_0 = users[usr]["inf0"]
    userNumTweets = users[usr]["tweets"]

    retweets_received = users[usr]["retweets"]
    retweets_sent = users[usr]["retweetsSent"]
    users[usr]["rep"] = inf_t - inf_0 + userNumTweets / totalNumOfTweets + retweets_received / (retweets_sent + 1)
