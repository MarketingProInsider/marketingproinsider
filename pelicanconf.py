# Import required module
import os

# Author and site information
AUTHOR = 'Bilal Khalid'
SITENAME = 'MarketingProInsider'
SITEURL = 'marketingproinsider.com'
CATEGORY = ''
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
    'Phone Number': '',
    'Email Address': 'marketingproinsider@gmail.com',
    'Street Address': "Al A'amal Street - Business Bay - Dubai - United Arab Emirates",
    'Map Embed URL': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3610.6860030359576!2d55.264665667777344!3d25.18007811938221!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5f69cb98cd9041%3A0xe6be587070e7a89d!2sDAMAC%20Executive%20Bay!5e0!3m2!1sen!2s!4v1717221569842!5m2!1sen!2s"
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
ARTICLE_SAVE_AS = '{slug}'

# Page settings
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index'

# Index settings
INDEX_URL = ''
INDEX_SAVE_AS = 'index'

# Category settings
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index'
CATEGORY_PAGINATION_URL = 'category/{slug}/page/{number}/'
CATEGORY_PAGINATION_SAVE_AS = 'category/{slug}/page/{number}/index'

# Tag settings
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index'
TAG_PAGINATION_URL = 'tag/{slug}/page/{number}/'
TAG_PAGINATION_SAVE_AS = 'tag/{slug}/page/{number}/index'

# Author settings
AUTHOR_URL = 'author/{slug}/'
AUTHOR_URL_SAVE_AS = 'author/{slug}/index'

# Pages
TEMPLATE_PAGES = {
    'contact.html': 'contact',
    '404.html': '404',
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
    ('facebook-f', 'https://www.facebook.com/profile.php?id=61559969553167&mibextid=ZbWKwL'),
    ('linkedin', 'https://www.linkedin.com/company/103871776/'),
    ('pinterest', 'https://pin.it/dJggaRJ3K'),
    # Add more social media links here
)

# Pagination settings
DEFAULT_PAGINATION = False
'''PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index'),
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