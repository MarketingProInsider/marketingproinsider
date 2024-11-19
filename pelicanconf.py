# Import required module
import os

GOOGLE_ANALYTICS = "G-J8RL7PZHWE"
GTM_CODE = 'GTM-P7X4J7P4'

# Author and site information
AUTHOR = 'Professor John'
SITENAME = 'MarketingProInsider'
SITEURL = 'marketingproinsider.com'
CATEGORY = ''
SITEDESCRIPTION = "Stay ahead with experts in social media solutions. Our experts on social media and social media specialists bring you the latest tips to grow your brand."
DEFAULT_LOCALE = 'en_US'

# Minify permissions
CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True

# To read markdown file in 
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html',
}

# Key takeaways for blogs
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {
            'title': 'Table of contents:',
            'toc_depth': '2',  # Ensures only H1 and H2 are included
        },
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
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
FAVEICON = '{}/theme/assets/images/icon.jpg'.format(SITEURL)
DELETE_OUTPUT_DIRECTORY = True
THEME = 'theme/'

# Feed generation settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Limitting related posts
RELATED_POSTS_MAX = 10

# Article settings
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}.html'

# Page settings
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Index settings
INDEX_URL = ''
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
PLUGINS = ["sitemap", "articlejson", "share_post", "minify"]

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
    'exclude': ['404', 'archives', 'tags', 'categories', 'authors'],  # ex: ['categories', 'tags']
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