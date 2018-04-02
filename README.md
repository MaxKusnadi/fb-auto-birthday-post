# Facebook Auto Post Birthday Message

This hack can probably save 2 to 3 hours of your life.

## Setting Up

1. Download [Python 3.xx](https://www.python.org/downloads/) (*3.6 is recommended*)
2. Clone this repo by typing `git clone https://github.com/MaxKusnadi/fb-auto-birthday-post.git` on your command line
3. Enter `cd fb-auto-birthday-post`
4. Enter `pip install -r requirements.txt`
5. Download `chromedriver` from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Unzip and put inside the `fb-auto-birthday-post` folder. **This is an important step, otherwise the program will not work**
6. Enter `python app.py` if *Setup Successful* appears on your command line, it means everything is fine

## Entering your credential

There are 2 ways of entering your credential:

1. Open `config.py` using your favourite text editor and fill in your credentials there. This is recommended for automatic login.
2. Key in your credentials when your screen ask you to.

## Customizing your birthday wishes

1. Open `wishes.py`
2. Add your custom messages to the list

## Running this script on startup

Linux user, check [this](http://askubuntu.com/questions/814/how-to-run-scripts-on-start-up) out.

Windows user, you can go [here](https://www.howtogeek.com/138159/how-to-enable-programs-and-custom-scripts-to-run-at-boot/).

## GitBash Problem


People who use windows git bash may get a problem in which password prompt does not appear after the email prompt. The solution can be found [here](http://stackoverflow.com/questions/32597209/python-not-working-in-the-command-line-of-git-bash) or else, just update `config.py` file

---

Created by [me](https://maxkusnadi.github.io)
