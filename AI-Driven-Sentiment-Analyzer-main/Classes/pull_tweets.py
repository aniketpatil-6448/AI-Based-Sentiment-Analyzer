import pandas as pd
import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="xmTCZs9iOE7H0SGe0-Gprg",         # your client id
                                client_secret="m_vKfhPR1cieXzTw-zWNQ_CeBoZLXA",      # your client secret
                                user_agent="MyApi/0.0.1"      # your user agent
                                )


def pull_tweets(query):
    subreddit = reddit_read_only.subreddit(query)

    posts = subreddit.hot(limit=50)
    # Scraping the top posts of the current month

    posts_dict = {"Title": [], "Post Text": [],
                  "ID": [], "Score": [],
                  "Total Comments": [], "Post URL": []
                  }

    for post in posts:
        # Title of each post
        posts_dict["Title"].append(post.title)

        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)

        # Unique ID of each post
        posts_dict["ID"].append(post.id)

        # The score of a post
        posts_dict["Score"].append(post.score)

        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)

        # URL of each post
        posts_dict["Post URL"].append(post.url)

    # Saving the data in a pandas dataframe
    top_posts = pd.DataFrame(posts_dict)

    posts = []

    posts = top_posts['Title'].tolist()
    print(query)
    return posts
