Snoolock
========

Extract interesting information about redditors from their submissions and comments. Outputs data in JSON format.

Dependencies
------------
* Python 3.10.9
* [pytz](https://pypi.python.org/pypi/pytz/) (2022.7)
* [TextBlob](http://textblob.readthedocs.org/en/dev/) (0.18.0.post0)

Setup
-----
* Run `pip install -r requirements.txt` to install dependencies.
* Run `python -m textblob.download_corpora` to download TextBlob corpora.

Usage
-----
    python snoolock.py <reddit-username>
    
Example
-------
Command:

    python snoolock.py example

Output:

    Processing user example
	{"username": "example"...}}
	Processing complete... 0:00:06.084066


License
-------
MIT License