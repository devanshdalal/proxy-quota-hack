USERID="me1120245"
PASSWORD="example"

curl --progress-bar -L -C -v $1 | curl -u $USERID:$PASSWORD -T - "https://owncloud.iitd.ac.in/owncloud/remote.php/webdav/$2"