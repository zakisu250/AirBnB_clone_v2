#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install nginx -y
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://zakisu.vercel.app;
    }

    error_page 404 /404.html;
        location /404 {
            root /var/www/html;
            internal;
        }
    }" > /etc/nginx/sites-available/default
service nginx restart
