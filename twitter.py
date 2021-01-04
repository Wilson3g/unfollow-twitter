import time
import sys
import tweepy

class Twitter():

    def auth(self):
        auth = tweepy.OAuthHandler('wO1ZWebiMTucsm9UUsvGFEY4r', 'izJq8GMrjEz7n0vU6BkKUd3laoMtvNeyf7uZKmyxYW8zt8zwxw')
        auth.set_access_token('1306019023583412224-f51AXW1FvLhmsR8a33MPmqTCVrLKHG', 'qH0aiESCiFGDNGIjMwnjhUNYuvsEn1lvhl8A3GjgEWlpc')
        api=tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        return api

    def follower(self):
        api = self.auth()
        followers = []
        for follower in tweepy.Cursor(api.followers).items():
            followers.append(follower)

        return followers

    def following(self):
        api = self.auth()
        friends = []
        for friend in tweepy.Cursor(api.friends).items():
            friends.append(friend)

        return friends

    def followers_following_dict(self, followers, friends):
        follower_dict = {}
        for follower in followers:
            follower_dict[follower.id] = follower

        friend_dict = {}
        for friend in friends:
            friend_dict[friend.id] = friend

        return follower_dict, friend_dict

    def users_who_no_following(self, friends, follower_dict):
        non_friends = [friend for friend in friends if friend.id not in follower_dict]
        return non_friends

    def unfollow_users(self, non_friends):
        api = self.auth()
        print('processing...')
        for non_friend in non_friends:
            print(f'unfollow user {non_friend.screen_name}')
            api.destroy_friendship(non_friend.id)
        return True
