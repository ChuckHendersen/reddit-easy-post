Put your information in the config.txt file
Username and password are the ones from your account. Client id and secret are from a "Reddit App" that needs to be created.
To create a reddit app head to "https://www.reddit.com/prefs/apps" and select "create new app". 
Give it a name, select the option "script" and put as redirection uri whatever you wish (http://localhost:8080 will do the job).
After that the app is created. The app secret can be found next to "secret" and the app id is the alphanumerical text right under the bot's name.

This is a full detailed tutorial that explains in greater detail what I just said
https://docs.google.com/document/d/1wHvqQwCYdJrQg4BKlGIVDLksPN0KpOnJWniT6PbZSrI/edit#heading=h.l5jmxmj14k2j

Open the terminal in folder and type "python3 post-cron.py", press Enter.

Check "reddit.log" file for exit status.