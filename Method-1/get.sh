# Author: Devansh Dalal
# License: GNU GENERAL PUBLIC LICENSE Version 3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
# Version: 1.0

USERID="ee1120430"
PASSWORD="example"

curl --progress-bar -L $1 | curl -u $USERID:$PASSWORD -T - "https://owncloud.iitd.ac.in/owncloud/remote.php/webdav/$2"
