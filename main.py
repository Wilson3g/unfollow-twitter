import time
import sys
import tweepy
from twitter import Twitter

if __name__ == "__main__":
    t = Twitter()
    print('Loading followers..')
        
    t.followers = self.follower()
    t.friends = self.following()
    
    print(f'Found {len(followers)} followers and found {len(friends)} following')

    t.follower_dict, friend_dict = self.followers_following_dict()
    t.non_friends = self.users_who_no_following(follower_dict)

    print(f"{len(non_friends)} users who don't follow you")

    print('done')
