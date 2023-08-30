import praw
import logging
from test_discord import DiscordBot

logging.basicConfig(filename='reddit.log',level=logging.INFO,
                    format='%(asctime)s %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# open the config file as read-only
config_file = open('config.txt', 'r')
config_settings = config_file.readlines()
config_file.close()

# make sure all of the configuration fields have been filled
for config in config_settings:
	if config[-2:] == '=\n' and config[:10] != 'submission':
		raise Exception('Configuration field left blank!')

# begin parsing the information from the configuration file into usable variables
# note the '.rstrip()' method being called on each string - this removes any newlines
username = config_settings[0][9:].rstrip()
password = config_settings[1][9:].rstrip()
client_id = config_settings[2][10:].rstrip()
client_secret = config_settings[3][14:].rstrip()
subreddit = config_settings[4][10:].rstrip()

try:
	# login to reddit...
	reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, username=username,
	                     user_agent="User")

	# create an instance of the subreddit class and submit the post!
	target_subreddit = reddit.subreddit(subreddit)

	postPath = 'C:/Users/giovi/Desktop/reddit-easy-post-1.0/post'
	title_file = open(postPath+'/title.txt', 'r')
	title = title_file.read()
	title_file.close()
	pictureList = [{"image_path": postPath+'/imgs/1.jpg'},{"image_path":postPath+'/imgs/2.jpg'},{"image_path":postPath+'/imgs/3.jpg'},]

	submission = target_subreddit.submit_gallery(title, pictureList)
	post = submission
	comment_file = open(postPath+'/reply.txt', 'r')
	comment = comment_file.read()
	comment_file.close()

	submission.reply(comment)

	# output to the logfile
	logging.info('Successful post to /r/{}'.format(subreddit))

	client = DiscordBot('%', "@here upvote please-> https://www.reddit.com"+post.permalink)
	client.run('your bot token')

except Exception as err:
	# if something went wrong with reddit, put the exception in the log file
	logging.error(err)