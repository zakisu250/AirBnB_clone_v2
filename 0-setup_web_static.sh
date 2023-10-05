#!/usr/bin/env bash
# Setup the nginx servers with directories to deploy web static
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo '<h1 style="text-align:center; padding-top:2rem">This is it</h1>' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/error_page 404 \/page404.html;/a \\\n\tlocation /hbtn_static { \
	\n\t\talias /data/web_static/current/; \
	\n\t\tautoindex off; \
	\n\t}" /etc/nginx/sites-available/default
service nginx restart
