# Import required module
import os

# Author and site information
AUTHOR = 'Bilal Khalid'
SITENAME = 'MarketingProInsider'
SITEURL = ''
CATEGORY = ''
SITEMETATITLE = 'Achieve Your Goals with New Free Social Media Solutions Now'
SITEDESCRIPTION = "Stay ahead of the competition by implementing the latest free social media solutions today. Don't miss out on this opportunity to revolutionize your online presence"
DEFAULT_LOCALE = 'en_US'

# To read markdown file in 
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html',
}

# Explicitly define the Markdown reader
from pelican.readers import MarkdownReader
READERS = {'md': MarkdownReader}

# Contact information
CONTACT_INFORMATION = {
    'Phone Number': '+92 342-270-0268',
    'Email Address': 'captivesmeta@gmail.com',
    'Street Address': 'Shahrah e Sher Shah Suri, North Nazimabad Town, Karachi, Pakistan',
    'Map Embed URL': 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d28941.979462981402!2d67.0418153!3d24.9406726!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3eb33f8014fe5943%3A0x11df7a65effb1ef6!2sNorth%20Nazimabad%20Town%2C%20Karachi%2C%20Karachi%20City%2C%20Sindh!5e0!3m2!1sen!2s!4v1713872000240!5m2!1sen!2s'
}

# Content settings
PATH = 'content/'

# Time and language settings
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'

# Appearance settings
SITELOGO = ""
FAVEICON = '{}/theme/assets/images/icon.png'.format(SITEURL)
DELETE_OUTPUT_DIRECTORY = True
THEME = 'theme/'

# Feed generation settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Article settings
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'

# Page settings
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Index settings
INDEX_URL = '/'
INDEX_SAVE_AS = 'index.html'

# Category settings
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_PAGINATION_URL = 'category/{slug}/page/{number}/'
CATEGORY_PAGINATION_SAVE_AS = 'category/{slug}/page/{number}/index.html'

# Tag settings
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_PAGINATION_URL = 'tag/{slug}/page/{number}/'
TAG_PAGINATION_SAVE_AS = 'tag/{slug}/page/{number}/index.html'

# Author settings
AUTHOR_URL = 'author/{slug}/'
AUTHOR_URL_SAVE_AS = 'author/{slug}/index.html'

# Pages
TEMPLATE_PAGES = {
    'contact.html': 'contact.html',
    '404.html': '404.html',
}

# Static files
STATIC_PATHS = ['extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Blogroll links
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    ('You can modify those links in your config file', '#'),
)

# Social media links
SOCIAL_MEDIA_LINKS = (
    ('linkedin', 'https://www.linkedin.com/company/103871776/'),
    ('pinterest', 'https://pin.it/dJggaRJ3K'),
    ('reddit', 'https://www.reddit.com/user/MarketingProInsider/'),
    ('quora', 'https://marketingproinsider.quora.com/'),
    ('facebook-f', 'https://www.facebook.com/profile.php?id=61559969553167&mibextid=ZbWKwL'),
    # Add more social media links here
)

# Pagination settings
DEFAULT_PAGINATION = False
'''PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)'''

# Plugins
PLUGINS_PATH = os.path.join(os.getcwd(), "pelican-plugins")
PLUGIN_PATHS = [PLUGINS_PATH]
PLUGINS = ["sitemap", "articlejson", "share_post"]

# Sitemap settings
SITEMAP = {
    'siteurl': SITEURL,
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'pages': 'weekly',
        'indexes': 'monthly',
    },
    'exclude': [],  # ex: ['categories', 'tags']
}

# SEO settings
OPEN_GRAPH = True
TWITTER_TAGS = True
YOUR_TWITTER_HANDLE = "pytheme"
REL_CANONICAL = True
USE_GOOGLE_FONTS = True

# KwesForms settings
KWESFORMS_ACTION = "https://kwesforms.com/api/foreign/forms/S9CLmleGJB99fnH4f3kw"

# Disqus settings
DISQUS = True

# HIGHLIGHTER = True