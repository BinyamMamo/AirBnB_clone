#!/usr/bin/env bash
# prepares the web server for deployment

apt update
apt install nginx -y

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
chown ubuntu:ubuntu -R /data

echo "hello world" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "
server {
	listen 80;
	server_name www.binyammamo.tech;
	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
" > /etc/nginx/sites-available/hbnb_static.conf

ln -sf /etc/nginx/sites-available/hbnb_static.conf /etc/nginx/sites-enabled/hbnb_static.conf

service nginx restart
