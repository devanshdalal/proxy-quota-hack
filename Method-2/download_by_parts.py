# Author: Devansh Dalal, Ashish Ranjan
# License: GNU GENERAL PUBLIC LICENSE Version 3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

import thread
import cookielib,sys
import requests,os,subprocess

PresentInCloud = {}
# Set your username & password here
USERNAME = "ee1120430"
PASSWORD = "yourpassword"
# Set limit of each part below. e.g. 450MB = 450*1024*1024
Limit=450*1024*1024;

def upload(file_name):
    global PresentInCloud
    print file_name
    if file_name not in PresentInCloud:
        PresentInCloud[file_name]=True
        print subprocess.check_output('curl -u '+USERNAME+':'+PASSWORD+' -T '+file_name+' "https://owncloud.iitd.ac.in/owncloud/remote.php/webdav/'+ file_name +'"',shell=True)
        print subprocess.check_output('rm '+file_name , shell=True)

def get(url,title):
    global PresentInCloud
    PresentInCloud={}
    local_filename = title
    part=1;
    r = requests.get(url,stream=True)
    print r.status_code
    Part=Limit/20
    file_size=0;
    for chunk in r.iter_content(chunk_size=Part):
        if chunk: # filter out keep-alive new chunks
            with open(local_filename+'_'+str(part), 'ab') as f:
                f.write(chunk)
                file_size+=len(chunk)
                f.flush()
                os.fsync(f.fileno())
                if file_size>=Limit:
                    f.close();
                    file_size=0;
                    thread.start_new_thread(upload, (local_filename+'_'+str(part), ) )
                    part+=1
                    f=open(local_filename+'_'+str(part),'wb')
    upload(local_filename+'_'+str(part) )
    return

# To download a file, you need a URL for that file.
# When you have the URL, just do the following
get("http://example.com/abc.mp4", 'abc')
