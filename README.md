
# redis-directory-buster

This tool uses a wordlist to identify accessible and existing directories through redis that exist or the user can change to. It cannot identify files.


### Usage:

```
kali > python3 redis-directory-buster -h

usage: redis-directory-buster [-h] -i RHOST [-port RPORT] -w WORDLIST [-u USERNAME] [-pass PASSWORD]

Perform directory enumeration by using redis

optional arguments:
  -h, --help            show this help message and exit
  -i RHOST, --rhost RHOST
                        IP address or hostname of the target redis server
  -port RPORT, --rport RPORT
                        Port of the target redis server. Default:6379
  -w WORDLIST, --wordlist WORDLIST
                        File to use to find paths, containing, e.g. /var/ or /var/lib line per line.
  -u USERNAME, --username USERNAME
                        Username used to authenticate to redis
  -pass PASSWORD, --password PASSWORD
                        Password used to authenticate to redis
```


### Why? What's the use-case?

As a penetration tester you might come accross situations where you are able to upload files to a directory that you know the name of, but you don't know where the directory is located on the filesystem (e.g. through ftp access). In these situations you can use this tool to find out where a folder is located on the filesystem that contains your uploaded files.

