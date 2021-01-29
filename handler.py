from twitter import Twitter
import json


def main(event, context):
    t = Twitter()

    followers = t.follower()
    friends = t.following()

    follower_dict, friend_dict = t.followers_following_dict(followers, friends)
    non_friends = t.users_who_no_following(friends, follower_dict)

    t.unfollow_users(non_friends)

    return {'message': 'okay!'}