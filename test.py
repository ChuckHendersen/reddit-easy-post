import praw
postPath = './post'
comment_file = open(postPath+'/reply.txt', 'r')
comment = comment_file.read()
comment_file.close()
print(comment)


reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, username=username,
	                     user_agent="User")

subreddit = reddit.subreddit(subreddit_name)

# Sostituisci 'flair_text' con il testo del flair che vuoi cercare
flair_text = 'Recruiting'

# Cerca tra tutti i flair del subreddit
for flair in subreddit.flair.link_templates:
    if flair['text'] == flair_text:
        flair_id = flair['id']
        print(f"Flair ID for '{flair_text}': {flair_id}")
        break
