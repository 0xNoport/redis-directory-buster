
# redis-directory-buster

This tool uses a wordlist to identify accessible and existing directories through redis that exist or the user can change to. It cannot identify files.


### Usage:

```
kali > python3 redis-directory-buster -h

usage: redis-directory-buster [-h] --rhost RHOST [--rport RPORT] --wordlist WORDLIST
Rebus: error: the following arguments are required: --rhost, --wordlist
```


### Why? What's the use-case?

```
As a penetration tester you might come accross situations where you are able to upload files to a directory that you know the name of, but you don't know where the directory is located on the filesystem (e.g. through ftp access). In these situations you can use this tool to find out where a folder is located on the filesystem that contains your uploaded files.
```

