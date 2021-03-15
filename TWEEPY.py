import tweepy

auth = tweepy.OAuthHandler("kPSSNQ7xCEtrKMwdNzEmqD5F6", "WxFlvSuJ8bmOgN1JoLPswctlCDp1UaYJiQHT7Yz3fapVevgP7z")
auth.set_access_token("1371542454818705413-eCV3wCTu5MRtelRuOVYIyFmkbDm0T0", "Br718A0jJDUQaFwq1Cbys2xZdKkfFaeXpS2XHkg2dxjwl")
api = tweepy.API(auth)
user2 = api.me()
print(user2.name)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


user = api.get_user('hajime_hippo')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.followers():
#    print(friend.screen_name)

def abonnements():
    user = api.get_user('hajime_hippo')
    users = tweepy.Cursor(api.friends, screen_name=user.screen_name, count=200).items()
    # users crée un curseur qui selectionne les 200 abonnements.
    while True:
        try:
            user = next(users)
    # sélectionne le suivant
        except tweepy.TweepError:
            time.sleep(60*15)
            user = next(users)
    # évite un bug de l'api récurrent (bug de répétition)
        except StopIteration:
            break
    # permet de s'arreter au nombre d'abonnements présent meme si le conteur en demande plus
        print("@" + user.screen_name)



def follow (nom):
    try:
        user = api.get_user(nom)
        user.follow()
        print("@",user.screen_name," a été follow")
    except:
        print('marche pas')

def unfollow (nom):
    try:
        user = api.get_user(nom)
        user.unfollow()
        print("@",user.screen_name," a été unfollow")
    except:
        print('marche pas')


def bot_concour():
    search = "#CONCOURS -filter:retweets"
    numberoftweets = 2
    for tweet in tweepy.Cursor(api.search, search).items(numberoftweets):
        try:
            tweet.favorite()
            tweet.retweet()
            api.create_friendship(tweet.user.id)
            print("Le tweet a été retweeté et la personne a été follow")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
