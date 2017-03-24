# Proxy Quota Hack

#### Fast and infinite downloads behind quota restricted proxy servers (scripts for IITD proxy servers). 

Are you tired of squishing your network quota in just 2 days? Are you tired of not being able to download those heavy youtube lectures and playlists. Are you jealous of IITK? Well, be no more!

These scripts were written just to overcome those petty limitations at IITD. It will allow you to not only download massive amount of content, but to do so while avoiding using your proxy in the process. So, you may download 100s of GBs :scream: of data in a day\*\* and your proxy usage will only display 200-300 MB used. (\*\**Trust us, it's been verified, we have used it!* :muscle:)
Yeah, it sounds like fiction, but it's not!
So, what are you waiting for? Let's get started.

NOTE: The scripts provided here are only for fair usage. Please do not download illegal contents using these scipts. The authors and contributors do not provide any warranty with this free sofware.

Please read the following policies of IITD, before continuing:

1. [IITD IT usage policy](http://www.cc.iitd.ernet.in/CSC/index.php?option=com_content&view=article&id=50&Itemid=153)
2. [Network access and monitoring policy](http://www.cc.iitd.ernet.in/CSC/index.php?option=com_content&view=article&id=122&Itemid=155)
3. [Privacy policy for IT usage](http://www.cc.iitd.ernet.in/CSC/index.php?option=com_content&view=article&id=51&Itemid=154)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Choose your method to deploy the project on a live system.

### Prerequisites

You need a remote virtual machine in cloud running, hosted by sites like koding.com, nitrous.io, c9.io, codeanywhere, codenvy, codepen etc. Please make an account on any free VPS provider and you are good to go. These free VPS providers generally have a limit on network bandwidth, so reset your vm whenever you vm-quota is finished.

## Method-1 (Preferred)

This method is the fastest and has the least requirements.

### Installing

1. Keep the file **get.sh** on the root of your remote virtual machine.
2. Set USERID & PASSWORD in the **get.sh** to your *username* and *password*.
3. Run the following snippet in terminal in the root directory of your remote virtual machine to give *execute* permission to your script
```
chmod +x get.sh
```

### Running

1. Get the URL of the file you want to download. "*file_name.ext*" could be any ASCII name. Here *.ext* is the extension of the file e.g. .mp4, .mkv, .zip, etc.
2. Run ```./get.sh <URL> <file_name.ext>```
3. An example: ```./get.sh "http://example.com/abc.mp4" "abc.mp4"```
4. The file will be downloaded to the root of your OwnCloud directory with name as ```abc.mp4```.
5. Download this file from OwnCloud to your computer.
6. [Disco-1!](https://www.youtube.com/watch?v=oAG7ECgXjcs) :sparkles: :clap: :boom:


## Method-2

In this method we download the file in parts of specified size (e.g. 500 MB). Then we merge these parts to get the original file. This is slower than Method-1.

### Installing

1. Keep the file *download_by_parts.py* on the root of your remote virtual machine.
2. Keep the file *merge_parts.py* on your local computer.

### Running & Downloading

1. Get the URL of the file you want to download. "*file_name*" could be any string of ASCII characters.
2. Remember the extension of your file. It will be required during merging of file.
3. Change the **URL** and **file_name** in last line in *download_by_parts.py*. 
4. Run this snippet in terminal in the root directory of your remote virtual machine ```python download_by_parts.py```
5. The file is downloaded into parts to the root of your OwnCloud directory with names as abc_1, abc_2, etc.
6. Download these parts from OwnCloud on your computer.
7. Delete files parts from your OwnCloud directory **only** after all file parts have finished downloading to your computer.

### Merging

1. Move the downloaded parts to the directory where you have kept *merge_parts.py*.
2. Change the **FILE_PARTS_NAME** & **ORIGINAL_FILE_NAME** in *merge_parts.py*. Use the extension of the original file.
3. Run this snippet in terminal of current directory ```python merge_parts.py```
4. The final merged file with correct extention is generated in the current directory.
5. Delete the file parts from your computer.
6. [Disco-2!](https://www.youtube.com/watch?v=dQw4w9WgXcQ) :guitar: :cocktail: :metal:




## Authors

* **Devansh Dalal - [Devansh Dalal](https://github.com/devanshdalal)**
* **Ashish Ranjan - [Ashish Ranjan](https://github.com/ashish28ranjan)**

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on code of conduct, and the process for submitting pull requests.


## Bugs reporting

* The script has not been tested since we left College, so you may encounter some bugs. Please feel free to report them with exact situations on how you found them. We will try our best to find a solution :)


## Acknowledgments

* Stack Overflow
* Inspiration for the project was provided by Rayala Bharadwaj.
* Thanks to all our friends from IITD who helped us whenever our proxy got squished :P

## LICENSE

[GNU GENERAL PUBLIC LICENSE Version 3](https://www.gnu.org/licenses/gpl-3.0.en.html)

