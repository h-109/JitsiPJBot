# Jitsi Bot for Keybase | Python
## Prerequisites: 
* Git
* Python 3.8.x
* Keybase App
* Paper Key of account

## How it actually works:
We set up a separate account for bot. The python program runs on the server and always listens to messages that the bot_username gets and replies if conditions are met.
The program uses ‘paper key’ to login and verify.


By default in most of the servers, we have Python 3.6.x installed.
You can check this with this command: python3 -V 

## Step #1:

Install Python 3.8.x and activate it as the default interpreter.
(All commands require root access. Use sudo when you are logged in as a normal user.)

Follow below commands to achieve the requirement:
Below command adds repo into our machine to fetch packages from.

> sudo add-apt-repository ppa:deadsnakes/ppa

Scans for any system changes in repos. Updates them. It’s a sort of refresh for installer.

> sudo apt-get update

This is the actual command to install python. 

> sudo apt-get install python3.8 -y

Below commands tell the system that we have these alternatives for Python older version.

> sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
> sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
Finally the below command changes the default used version of python.

> sudo update-alternatives --config python3
Choose option 2 in the above step. That makes your default Python interpreter as 3.8.x version.

Now check the version:
> python3 -V
Congrats! You have done the most essential step of this tutorial. Brace yourself.

Then install pip3 for obtaining python packages

>$ sudo apt install python3-pip


## Step #2:

Install Keybase

Follow below commands to install it.

>curl --remote-name https://prerelease.keybase.io/keybase_amd64.deb
>sudo apt install ./keybase_amd64.deb

## Step #3:
Clone github repo for code.

>$ git clone “https://github.com/h-109/JitsiPJBot.git”

Navigate to the folder downloaded. cd folder_name

Install required modules:
>$ pip3 install -r requirements.txt

Note: If the above command gives an error, manually run:
>$ pip3 install pykeybasebot asyncio

Change the PAPER_KEY and USERNAME strings in the code.
Hint: Use >$ sudo nano script_name.py< to access the editor.

## Step #4:
Run the script

>$ python3 script_name.py

Test the bot by sending the keyphrase we set in the script to bot_username
Keyphrase: !jitsipj

If you can see automated reply, it’s awesome.

Now, make sure this script always runs on the server, in the background. For this, use below command:

>$ nohup python3 script_name.py &

## 🎉 Congratulations on successful deployment of keybase bot.

Feel free to tweak the code.

Source Links:
Python 3.8 Installation and activation Guide: https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-8-on-ubuntu-18-04-lts/


### Drop a Hi 👋 on Keybase @h109 for any queries.
