#Imgur Uploader

A command-line helper to upload images to imgur, written in Python.

## Installation:
We use the soft link to install the Python script. The executable Python script is ```upload.py```

1. Clone the entire repo.
2. Make ```upload.py``` executable:
```chmod +x upload.py```
3. Check out one of the PATH addresses in your machine.
4. In the root dir of the repo:

		ln -s $PWD/src/upload.py ONE_PATH/upload

	In my case:

		ln -s $PWD/src/upload.py $HOME/bin/upload

	Note that you can specify the word "upload" at the end into some other words you like.


##First time logging in
At the first time, you need to login to authenticate this upload program.

1. At first, the cli-interface will ask you to log in your imgur account: 

![](http://i.imgur.com/yreYoC3.png)

At the same time, your browser will pop up and an imgur OAuth url is opened.

![](http://i.imgur.com/QTMKRfS.png)

Copy and paste the PIN in the page to the command line program and you will successfully logged in. At this time you are good to go.


##Usage

1. Just simply navigate your directory to the files you want to upload and type ```$upload your_image.jpg```, you can specify the ```upload``` command to some other preferences (check out Installation#4).

2. Arguments
	3. ```upload -c your_image.jpg image_2.png```: Upload your image(s) to your imgur account and copy the corresponding imgur url(s) into your clipboard.
	4. ```upload -o your_image.jpg```: Upload your image(s) to your imgur account and open the corresponding url(s) on your browser.
	
##Problem
1. Upload speed seems kind of slow. It need to be fixed soon.

