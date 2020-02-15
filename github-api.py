###########################
#!/usr/bin/python3        #
#Author: Nikhil           #
#Date: 16-02-2020         #
#GITHUB API               #
###########################

import requests
import json

user = ""             #username of github account
repo = ""             #repository_name
auth = ""             #authentication token
url = "https://api.github.com"
header = {"Authorization": "token %s" %(auth), 'Accept': 'application/vnd.github.v3.raw'}
tag_name = ""         #tag_name of release
releaseId = ""        #releaseID

# Fetch latest release from github
def latestRelease():
    try:
        releases = requests.get('%s/repos/%s/%s/releases/latest' %(url,user,repo), headers=header).json()
        print(releases['tag_name'], releases['id'])
    except:
        print('Release Not Found')

# Create latest release on github
def postNewrelease():
    try:
        with open('release.json') as newRelease:
            _release = json.load(newRelease)
            release_new = requests.post('%s/repos/%s/%s/releases' %(url,user,repo), json=_release, headers=header).json()
            print(release_new)
    except:
        print("error while creating new release")

# Delete release from github by passing tag_name & releaseId
def deleterelease():
    try:
        releaseDeleteTag = requests.delete('%s/repos/%s/%s/git/refs/tags/%s' %(url,user,repo,tag_name), headers=header)
        releaseDeleteId = requests.delete('%s/repos/%s/%s/releases/%s' %(url,user,repo,releaseId), headers=header)
        print(releaseDeleteId,releaseDeleteTag)
    except:
        print("errror wile deleteing release")
