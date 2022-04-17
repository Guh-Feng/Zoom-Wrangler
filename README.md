# The Zoom Wrangler
A program for those who can't bother to dig around for the right Zoom link for their appointments.

## User dependencies:
```
pip install selenium beautifulsoup4 lxml plyer pyautogui
```

## If using Chrome: requires ChromeDriver.
### The chromedriver executable needs to be in PATH
#### First, download the correct version of chromedriver that corresponds to your version of Chrome:
```https://chromedriver.chromium.org/downloads```
#### Then, unpackage the ZIP file and add the resulting binary to your PATH
##### This will vary by machine. One could run ```echo $PATH``` in terminal to view the directories that are in the PATH environment variable. 
#### Put the binary in one of these directories or run this command in terminal:

```export PATH=[INSERT_DIRECTORY_HERE]:$PATH```

#### where ```[INSERT_DIRECTORY_HERE]``` is replaced with the complete path to ```chromedriver```

#### For example:
```export PATH=/Users/username/Documents/driverfolder:$PATH```

##### NOTE: It is crucial that ```:$PATH``` is appended to this command, otherwise your PATH environment variable may be irreversibly modified.
#### Then, restart your machine.
### Developer tests require ```pytest```

## Additional information for MacOS & Safari (please read instructions carefully and completely before proceeding):

### The 'Allow Remote Automation' option in Safari's Develop Menu must be enabled for Selenium compatability.
### Safari's Develop menu must be enabled for access in the Menu Bar.
#### This can be enabled through Preferences -> Advanced -> Show Develop menu in menu bar.
### Enable the 'Allow Remote Automation' option under the Develop menu.
#### Some devices may have to scroll within the Develop menu to see this option.

### Safari has to enable WebDriver support
#### For High Sierra (10.13) and later, run this command in terminal: ```safaridriver --enable```

#### NOTE: If upgraded from a previous MacOS release, the ```sudo``` command may need to be used.

### For Sierra (10.12) and earlier, you must authorize ```safaridriver``` to launch the XPC service that hosts the local web server.
#### Manually run ```/usr/bin/safaridriver``` in terminal and follow the authentication prompt.