#gittweet
  [NeoRetro Group](https://neoretro.net)

##Summary
gittweet is a simple python script that will query Github for specific repositories and their current commit version.  If a new commit is detected, a Tweet is sent out according to settings within the script.


##Requirements

[ttytter](http://www.floodgap.com/software/ttytter/)

  * Download the latest version available [here](http://www.floodgap.com/software/ttytter/dist2/)
    * `sudo wget http://www.floodgap.com/software/ttytter/dist2/2.1.00.txt -O /usr/local/bin/ttytter`
    * `sudo chmod +x /usr/local/bin/ttytter`
  * Generate OAuth keyfile
    * `ttytter -oauthwizard -keyf=KEYNAME`
    * This will generate **./.ttytterkeyKEYNAME**

##Configuration

  * Adjust the location of ttytter binary if it is not found in */usr/local/bin*
  * Tell the script where you would like to keep your state database file
  * Change/Add repositories you wish to monitor and the ttytter keyfiles associated with the Twitter accounts you wish to use to send tweets

  * Add gittweet.py to your crontab via `crontab -e`.  Remember, cron doesn't have access to shell variables, so don't use relative directories in the crontab task itself.

`*/5 * * * * /home/earthmeLon/src/gittweet/gittweet.py`

