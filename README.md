**Stand Bog** is a **Pelican** **responsive**, **clean-coded**, and **optimized mobile devices** Pelican blog theme developed by [**PyPiThemes**](https://pypithemes.com). It works with **GitHub Pages**, **Cloudflare Pages**, and **Netlify Pages** so that you can host it for **free**.


![Stand Blog Home](Home-Stand-Blog-Home.png)

UX that needs to be followed: https://www.behance.net/gallery/194989379/Tech-Thrifty-Blog-Website?tracking_source=search_projects|tech+blog&l=39

Template replicated: https://templatemo.com/tm-551-stand-blog

## Future Additions (Source: https://www.github-zh.com/projects/6547965-pelican-plugins):
https://github.com/nogaems/pelican-ert
./post_stats
https://github.com/pelican-plugins/read-more
https://github.com/pelican-plugins/related-posts
https://github.com/pelican-plugins/photos
https://github.com/kura/pelican_youtube
https://github.com/jhshi/pelican.plugins.ga_page_view
https://github.com/kura/pelican-githubprojects
https://github.com/ingwinlu/pelican-toc
https://github.com/Shaked/pelican-version
https://github.com/tylerdave/pelican-meetup-info
https://github.com/mortada/pelican_javascript
https://github.com/bmcorser/pelicanfly
https://pypi.org/project/pelican_admin/#toc-entry-1


Demo:
-----

Experience the theme in action by visiting our live demo: [Demo](https://stand-blog.pages.dev/)

Features:
---------

*   **Section featured posts:** Showcase your best posts in a dedicated section.
*   **Section Blog:** Display your latest blog posts in a stylish and easy-to-read way.
*   **Section videos:** Share your videos with your readers in a dedicated section.
*   **Section author:** Give your authors their own page to showcase their work.
*   **Section tag:** Organize your posts by tags for easy navigation.
*   **Loading page:** Display a loading animation while your page loads.
*   **Super fast performance:** Stand Bog is optimized for speed and performance so your readers can enjoy your blog without lag.
*   **Social sharing buttons:** Let your readers easily share your posts on social media.
*   **Scroll to the top button:** Easily navigate back to the top of your page with a single click.
*   **Modern search form:** Find the posts you want with a modern and intuitive search form.
*   **Compatible with modern browsers:** Stand Bog is compatible with all modern browsers, so your readers can enjoy your blog regardless of their device.
*   **Support Meta tags and OpenGraph:** Stand Bog supports Meta tags and OpenGraph and is easy to customize.
*   **Image lazy loading:** Only load images when visible on the screen, improving performance.
*   **Image Gallery:** Create beautiful image galleries with ease.
*   **Author page:** Each author has their own page to showcase their work.
*   **Custom Icon support:** Upload your own icon to give your blog a unique look.
*   **Supports video posts:** Easily add videos to your posts.
*   **Supports multiple authors:** Easily manage multiple authors with Stand Bog.
*   **Supports contact form (Formspree):** Let your readers easily contact you using a Formspree contact form.
*   **Supports Disqus comments:** Enable Disqus comments on your blog so your readers can discuss your posts.
*   **Supports Google Analytics:** Track your website traffic with Google Analytics.
*   **Ionicons icons:** Use beautiful Ionicons icons throughout your blog.
*   **Free Google Fonts:** Style your blog with over 1,000 free Google Fonts.
*   **Free updates & support:** Stand Bog is constantly updated with new features and bug fixes. You also get free support from the PyPiThemes team.

## Clone git repo
sudo git clone https://github.com/MarketingProInsider/marketingproinsider.git

## Create a virtual environment in the directory you want
sudo python3 -m venv pythonenv

## Activate the virtual environment
source pythonenv/bin/activate

## Install the dependencies
pip install -r requirements.txt

## Install pelican on linux
sudo apt install pelican

## Install pelican plugin for share-post
python -m pip install pelican-share-post

## Install pelican plugin for minify
pip install pelican-minify

## To Build
pelican content -o output

## To listen
pelican --listen

## To debug:
pelican content --debug > pelicandebug.txt

## To deploy on global production
make html
make serve-global [SERVER=0.0.0.0]

## Install Apache2 and Necessary Modules
sudo apt update
sudo apt install apache2
sudo a2enmod proxy proxy_http ssl

## To install SSL on Apache2
sudo apt install certbot python3-certbot-apache
sudo certbot --apache -d yourdomain.com -d www.yourdomain.com

## Create an Apache Virtual Host File
sudo nano /etc/apache2/sites-available/pelican_site.conf

## Add the Configuration for Apache2 as a Reverse Proxy for Pelican
<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

<VirtualHost *:443>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com

    SSLEngine On
    SSLCertificateFile /etc/letsencrypt/live/yourdomain.com/fullchain.pem  # For Let's Encrypt
    SSLCertificateKeyFile /etc/letsencrypt/live/yourdomain.com/privkey.pem  # For Let's Encrypt

    # For a self-signed certificate, use:
    # SSLCertificateFile /etc/ssl/certs/pelican-selfsigned.crt
    # SSLCertificateKeyFile /etc/ssl/private/pelican-selfsigned.key

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

## Enable the New Site Configuration
sudo a2ensite pelican_site.conf

## Restart Apache to apply the new configuration
sudo systemctl restart apache2

## Configure DNS Records
To make your website accessible via a domain name instead of an IP address, you’ll need to set up DNS records.

- Access Your DNS Provider's Control Panel: Log into the DNS provider for your domain (such as GoDaddy, Namecheap, Cloudflare, etc.).
- Add an ‘A’ Record:
    - Type: A
    - Name: @ (represents the root domain, e.g., yourdomain.com)
    - Value: Your server’s IP address (e.g., 123.45.67.89)
    - TTL: Set to Auto or 1 hour

- (Optional) Add a ‘www’ CNAME Record:
    - Type: CNAME
    - Name: www
    - Value: yourdomain.com
    - TTL: Auto or 1 hour

- Save all the DNS records.

## Kill process at port 8000
sudo lsof -i :8000
sudo kill -9 [PID]

## Restart server with output log

### Create an output log file
sudo touch /home/marketingproinsider/output.log

### Check Directory Permissions and assign to user
ls -ld /home/marketingproinsider/
sudo chmod u+w /home/marketingproinsider/

### Change Ownership (if needed)
sudo chown $(whoami) /home/marketingproinsider/output.log

### Run with Elevated Privileges
sudo nohup make serve-global SERVER=127.0.0.1 > /home/marketingproinsider/output.log 2>&1 &





Technologies:
-------------

*   Pelican==4.9.1
*   Pelican-share-post==1.0.0
*   Bootstrap==v4.1.3
*   Font Awesome==4.3.0
