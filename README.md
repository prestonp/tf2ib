tf2ib
=====

An IRC Pick-Up-Game bot for TF2

This project has been developed on Linux. The installation instructions have been tested on Linux. 

If you need a local IRC server I recommend you ngIRCD, I made a post about it there: 
http://stackoverflow.com/questions/144049/recommended-irc-server-ircd-for-a-small-site/990201#990201


Configure the database 
----------------------
I use PostgreSQL and I recommend it for this project.


This command needs to be run as root:

```bash
su postgres
```

Configure database:

    psql -c "CREATE USER tf2ib WITH PASSWORD 'jw8s0F4'"
    psql -c "CREATE DATABASE tf2ib"
    psql tf2ib < database.sql
    psql tf2ib < sample.sql // Run this command only if you want to populate your database with testing data.


Install dependencies and run the scripts
---------------------------------------- 
Before running these two scripts you need to change the value of some variables in the file "config.py"

Note: You can use `apt-get` or `yum`, as long as you install properly the pyscopg2 library you are good to go.
```bash
aptitude install python-psycopg2
```

```bash
./pug.py
```

The second argument is the nickname of your messenger.
```bash
./send.py PUG-MESSENGER
```

Files:
* BeautifulSoup.py - Library used to parse HTML, it's only used on the ESEA bot.
* config.py - Configuration file used by some scripts, you will probably set the variable values to what you need.
* data.sh - Script that is intended to run as a cron job on a TF2 server. It does copy the stats and STV files to the web server.
* database.sql - File used to create the tables for the bot database.
* esea.py - Very basic bot (300 lines of code) used for the ESEA channel.
* irclib.py - Library used by the different bots to connect and communicate through the IRC protocol.
* pug.py - Main bot, it is strongly recommended to analyze the code before doing any modifications.
* run.sh - Wrapper script that automatically re-launches the bot when it crashes (this will happen). You usually use the script as follows (arguments are optionnals): ./run.sh script.py argument1 argument2
* sample.sql - Data for the database, this is mostly for if you need to fill the tables with some testing data.
* send.py - Messenger bot, you need at least one running.
* SRCDS.py - Library used to send rcon commands and control the TF2 servers.
