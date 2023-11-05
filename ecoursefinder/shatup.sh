#!/bin/sh
APPFOLDERPATH=`pwd`
APPNAME='ecoursefinder'
DOMAINNAME='13.234.122.44'
if [ "$APPNAME" = "" ] || [ "$DOMAINNAME" = "" ]; then
    echo "Usage:"
    echo "  $ set_up.sh <project> <domain> "
    exit 1
fi
apt-update

. ../denv/bin/activate
pip install django gunicorn 

deactivate

cat > /etc/systemd/system/${APPNAME}.socket << EOF
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/${APPNAME}.sock

[Install]
WantedBy=sockets.target
EOF

cat > /etc/systemd/system/${APPNAME}.service << EOF
[Unit]
Description=gunicorn daemon
Requires=${APPNAME}.socket
After=network.target

[Service]           
User=root
Group=root
WorkingDirectory=${APPFOLDERPATH}
ExecStart=${APPFOLDERPATH}/denv/bin/gunicorn \\
          --access-logfile - \\
          --workers 3 \\
          --bind unix:/run/${APPNAME}.sock \\
          ${APPNAME}.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

cat > /etc/nginx/sites-available/${APPNAME} << EOF

server {
    listen 80;
    server_name ${DOMAINNAME};

location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root ${APPFOLDERPATH};
    }

location / {
        include proxy_params;
        proxy_pass http://unix:/run/${APPNAME}.sock;
    }

}
EOF
sudo systemctl enable ${APPNAME}.socket
sudo systemctl enable ${APPNAME}.service
sudo systemctl start ${APPNAME}.socket

sudo systemctl daemon-reload
sudo systemctl restart ${APPNAME}
sudo ln -s /etc/nginx/sites-available/${APPNAME} /etc/nginx/sites-enabled
sudo systemctl restart nginx
sudo systemctl status ${APPNAME}




