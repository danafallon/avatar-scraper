# Avatar scraper

Opens a link to stream any episode of Avatar: the Last Airbender, on a page free of ads and popups.

## Usage

Make sure you have python 3 and the `requests` library installed, then:
```
$ python3 avatar.py <season> <episode>
```

E.g., to watch season 1 episode 1:
```
$ python3 avatar.py 1 1
```

If using windows or a browser other than chrome, you'll need to change the `CHROME_PATH` constant to point to the location of your browser.
