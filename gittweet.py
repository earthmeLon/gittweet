#!/usr/bin/env python
# -*- coding: utf8 -*-
""" Interface with GitHub
https://api.github.com/repos/USER/REPO/commits

NeoRetro Group
"""

import requests
import json
import sqlite3
import subprocess

ttytter = '/usr/bin/ttytter'
statefile = '/home/earthmeLon/.gittweet.db'


class github(object):

    repos = []

    def add(self, user, repo, keyfile):
        #Check if the repo exists
        rurl = 'https://api.github.com/repos/' + user + '/' + repo + '/commits'
        if requests.get(rurl):
            self.repos.append((repo, (rurl, keyfile)))
            print "Added " + rurl
        else:
            print "Unable to add " + rurl

    def poll(self):
        try:
            for repo in self.repos:
                rurl = repo[1][0]
                keyfile = repo[1][1]
                r = requests.get(rurl)
                if r.content:
                    jsonx = json.loads(r.content)
                    commit = jsonx[0]['commit']['tree']['sha']
                    message = jsonx[0]['commit']['message']
                    author = jsonx[0]['committer']['login']
                    preText = '#Update from ' + author + ': '
                    if len(message) > 140 - len(preText):
                        message = message[:140 - len(preText)]
                print commit + ': ' + message
                state.execute("SELECT * FROM state WHERE commitx=? LIMIT 1", (commit,))
                if state.fetchall():
                    print "Already seen commit: " + commit
                else:
                    state.execute("INSERT into state (commitx) VALUES (?)", (commit,))
                    db.commit()
                    subprocess.call([ttytter, '-keyf=' + keyfile, '-status=' + preText + message])
            #return (commit, message)
        except Exception, e:
            print repo
            print e

''' Configuration '''
github = github()
github.add('cjdelisle', 'cjdns', '/home/earthmeLon/.ttytterkeycjdns')
#github.add('cjdelisle', 'cjdns', '/home/earthmeLon/.ttytterkeycjdns')
#github.add('cjdelisle', 'cjdns', '/home/earthmeLon/.ttytterkeycjdns')

''' Runtime '''
try:
    db = sqlite3.connect(statefile, check_same_thread=False)
    state = db.cursor()
    sql = 'create table if not exists "state" (id INTEGER PRIMARY KEY ASC AUTOINCREMENT, commitx BLOB)'
    state.execute(sql)
except Exception, e:
    print "Unable to open state database: "
    print e

github.poll()
