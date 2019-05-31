# customhead.py

This simple script improve your SEO and the UX.
It add lang attribute to the html element and search and replace '$head$' string with personalized head elements.

### Usage

#### Fast view of the argument list

customhead.py -h
```
required arguments:
  -file PATH TO FILE   Path to file where want to add the custom head
                       elements.

optional arguments:
  --exclude-comment    Exclude 'Autogenerated SEO elements' comment.
  --exclude-html       Exclude html lang attribute.
  --exclude-special    Exclude special head elements.
  --exclude-basic      Exclude basic SEO elements.
  --exclude-opengraph  Exclude opengraph.
  --exclude-facebook   Exclude facebook.
  --exclude-twitter    Exclude twitter.
  --exclude-author     Exclude author.
```

#### 1 - Find the main file

This is the file that want to edit. It need to have a <html> element for add the lang attribute, and a '$head$' string that be replaced for the custom elements. Example:

_(my_index.html)_
```
<html> 
  <head>
    $head$
    ...
  </head>
</html>
```


If there isnt the html element, cant add the lang attribute. Sameway, if there isnt the '$head$' string, cant add the custom head elements.

#### 2 - Define personalized values

Create a file with this inside:

_(customhead.txt)_
```
values = {

    # Required, path to main file
    'path':             './my_index.html',

    # Basic SEO
    'title':            'Microsoft',
    'icon':             '/favicon.png',
    'preview':          '/preview.png', # Big image preview
    'description':      'Technology Solutions',
    'subject':          'Home Page',
    'keywords':         'Microsoft, Windows',

    # Opengraph
    'og:type':          'website', # http://ogp.me/#types

    # Facebook
    'fb:pages':         {'12345', '67890'}, # (Str) Facebook Pages ID separated by commas
    'fb:app_id':        '12345', # (Str) Facebook App ID

    # Twitter
    'tw:card':          'summary', # https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/summary.html
    'tw:domain':        'www.microsoft.com',
    'tw:page':          '@Microsoft', # Commerce Twitter account
    'tw:creator':       '@BillGates', # This page editor
    'tw:googleplay':    '12345', # Google Play app id
    'tw:ipad':          '12345', # iPad app id
    'tw:iphone':        '12345', # iPhone app id

    # Other
    'content-type':     'text/html; charset=utf-8',
    'viewport':         {'width': 'device-width', 'initial-scale': '1'},
    'locale':           'en_US',

    # Website author
    'author':           'Lucas Vazquez'
    
}
```

Look, there are a dictionary called values, they are used for pass values to script.
Please, dont change the dictionary 'values' name. Feel free to add comments like python inside the dict.
In values there are a key called 'path', this reffered to the path where are the file that you want to edit the html and head.
If some keys are omited, the elements reffered to them are ommited too.

#### 3 - Execute the script

makeseo.py -file customhead.txt --exclude-twitter

#### 4 - Results

_(my_index.html)_
```
<html lang="en_US">
    <head>
        <!-- Autogenerated SEO elements -->
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta http-equiv="Content-Language" content="en_US" />
        <title>Microsoft</title>
        <link rel="shortcut icon" href="/favicon.png" />
        <meta name="description" content="Technology Solutions" />
        <meta name="subject" content="Home Page" />
        <meta name="keywords" content="Microsoft, Windows" />
        <meta property="og:locale" content="en_US" />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="Microsoft" />
        <meta property="og:title" content="Microsoft" />
        <meta property="og:image" content="/preview.png" />
        <meta property="og:image:secure_url" content="/preview.png" />
        <meta property="og:description" content="Technology Solutions" />
        <meta property="fb:pages" content="67890, 12345" />
        <meta porperty="fb:app_id" content="12345" />
        <meta name="author" content="Lucas Vazquez" />
    </head>
</html>
```
