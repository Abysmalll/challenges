# Challenge Name
Genie

# Description
Make a wish and you might get it!

# Difficulty
esay

# Guide
When you enter some string(e.g. abc), what changes did you notice?
1. The URL now includes `/?input=abc`
2. `abc` also reflected as an output below

Knowing these and that it is a SSTI challenge. This means that inputs might treated as codes, you can lookup for some SSTI payloads and test it.

Using `{{7*7}}` as the input, there will be a output of `49`.   
Next you can try some strings which the flag might be stored at to get the flag.

If you did `{{flag}}` you will be able to get the flag!

# Hints

# Resources
https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server_Side_Template_Injection

# Solution
The input to get the flag is `{{flag}}`.
