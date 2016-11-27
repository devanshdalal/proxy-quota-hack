# Fast n Unlimited network downloads behind quota restricted proxy servers (script for IITD's servers). 

final script after a lots of iterative refinements

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need a remote virtual machine in cloud running, hosted by sites like koding.com, nitrous.io, c9.io, etc

## Installing

Just change the username and password in the script to be ready to use.

And run
```
chmod +x get.sh
```


## Running


```
./get.sh <link> <target_name>
```

this will download the remote file from ```<link>``` and save it in your local owncloud account(with name as ```<target_name>```) without afecting your week's quota. Then you just have to download the file from local owncloud server. Speed is the most important thing delivered by this method. You can download 100s of GB of files in just minutes if done properly.   



## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to me.

## Authors

* **Devansh Dalal - [devanshdalal](https://github.com/devanshdalal)**


## Acknowledgments

* stackoverflow
* Actually the script is not thorougly tested after I passed the college, so you might find some bugs. 
* Inspiration: given by my friend Rayala Bharadwaj
