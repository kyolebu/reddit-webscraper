import praw

reddit = praw.Reddit(
    client_id="mKZyCDDkbvWNq2T6J_kB2w",
    client_secret="xo7JGufGvtylfQv73l89QR3N8snGeg",
    user_agent="interviews"
)

subreddit = reddit.subreddit("cscareerquestions")

top_posts = subreddit.top(limit=10)
new_posts = subreddit.new(limit=10)

for post in top_posts:
    print("Title – ", post.title)
    print("ID – ", post.id)
    print("Author – ", post.author)
    print("URL – ", post.url)
    print("Score – ", post.score)
    print("Comment count – ", post.num_comments)
    print("Created – ", post.created_utc)
    print("\n")