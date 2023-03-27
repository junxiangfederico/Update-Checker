# Update-Checker
A python based update checker for websites.

A python based website update checker for MAC OS. 
Enter the webiste you want to supervise, when a new version is released you will receive a sound ping and a notification and/or a message notification on telegram.

# How it works
The html code for the website is fetched every 5 seconds, the hash of the content is generated and stored, the new version of the website is compared to the stored hashvalue, and if different the website content has changed.

 
# Usage for updateChecker.py:
1. Run updateChecker.py
2. Enter the URL you want to check (try with https://www.bbc.com/)
3. When a new version is released you will receive a sound ping and a local notification.
    
    
# Usage for updateChecker.py:
1. Setup the necessary fields in the source file
1. Run updateCheckerMessenger.py
3. Enter the URL you want to check (try with https://www.bbc.com/)
4. When a new version is released you will receive a sound ping and a telegram bot notification.
