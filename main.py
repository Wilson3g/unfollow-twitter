from twitter import Twitter

if __name__ == "__main__":
    t = Twitter()
    print('Loading followers..')
        
    followers = t.follower()
    friends = t.following()
    
    print(f'Found {len(followers)} followers and found {len(friends)} following')

    follower_dict, friend_dict = t.followers_following_dict(followers, friends)
    non_friends = t.users_who_no_following(friends, follower_dict)

    print(f"{len(non_friends)} users who don't follow you")

    # t.unfollow_users(non_friends)

    print('done')
