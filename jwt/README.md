# Challenge Name
jwt

# Description
Login with the credentials user:password

# Difficulty
easy

# Guide
You can start by logging in with the credentials user:password

At the community page there are some announcements by the admin.   
One of the announcement says `Inspection is going on!`, which is hinted for you to inspect the page. After you looked through the HTML, there is a `N0t_th3_5eCReT_K3y` which we will use later.

Since we logged in to gain access to the page, there should be a cookie. When you find the cookie and its value you can refer back to the challenge title which is JWT.

With a quick search on JWT and [this](https://jwt.io/) you should be able to solve the challenge!

# Hints
Something hidden from plain sight

# Resources
https://jwt.io/

# Solution
Login with the credentials user:password

Upon inspecting the elements, we can get a key `N0t_th3_5eCReT_K3y`, we also managed get the JWT token from the cookie.

We can then modify the token `role:user` to `role:admin` with the secret key `N0t_th3_5eCReT_K3y` to get our new token. Next just replace the token and refresh you will be able to get the flag.