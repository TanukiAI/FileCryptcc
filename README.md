# FileCryptcc
OUTDATED FILES ON REPOSITORY
Wrapper for Filecrypt.cc


# Requirements
Python 3.x<br>
Requests

# Installation
`pip install filecrypt`

# How to use it?
Please look at [The Wiki](https://github.com/TA40/FileCryptcc/wiki). It always returns an dictionary to the given variable.
```
import FileCrypt
apiInfo = FileCrypt.userApiKey(xxxxxxxxxxxxxxxx)
print(apiInfo)

{'API_KEY_CREATE': True,
 'API_KEY_EARNINGS': False,
 'API_KEY_EDIT': True,
 'API_KEY_LIST': True,
 'API_KEY_REMOVE': True,
 'API_KEY_STATUS': True,
 'API_KEY_STATUS_MASTER': False,
 'key': 'xxxxxxxxxxxxxxxx',
 'state': 1
 }
```
