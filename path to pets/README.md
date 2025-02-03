# Challenge Name
path to pets

# Description
Find my pets location and you will be rewarded.

# Difficulty
Easy

# Guide
On the frontpage of the site, there are three pets which are shown Ash, Mello, and Bob.

Upon clicking on Bob, it brings us to another page with the url ending with `?img=Bob.jpg`. This means that it is querying for pet3.jpg, which is the image of Bob if you inspect the elements.

What does the query mean and why it matters?   
A query parameter is often used to select files or resoruces relating to the query, this case it will be selecting Bob.jpg since I clicked on Bob.

Since we know that it is trying to select a file, we can try to change the url query to `?img=flag.txt`. Because the page was meant to display an image, if there was a `flag.txt` file we will still need to change the HTML tag `<img>` to another tag which would display text content such as `<iframe>`. Once we changed the HTMl tag, it showed an error message file not found. This confirms that it is getting the file from the directory.

Know that we can now path traversal through the system and look for the flag.txt. When we try `../flag.txt`, which should fetch the flag.txt from the parent directory. Instead the image source from inspecting the elements is still `?img=flag.txt`.

This means that there is a filter which is filtering out `../`, so how do we bypass it?   
- URL Encoding
- Different commands to change directory
- Mangled Path

To find out [click here](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Directory%20Traversal/README.md)

Now we can just use `?img=....//flag.txt`, this will remove `../` while still leaving behind one more set of `../` which leads us to the flag. Lastly change the HTML tag from `<img>` to `<iframe>` to get the flag. 

# Hints
Different ways to change directory

# Resources
https://ctf101.org/web-exploitation/directory-traversal/what-is-directory-traversal/   
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Directory%20Traversal/README.md

# Solution
Using Brup Suite as a proxy, click on one of the images and change the query to `img=....//flag.txt` and the flag can be found in the response.