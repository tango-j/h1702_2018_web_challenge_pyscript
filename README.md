# h1702_2018_web_challenge
Python script used to automate the retrival of id of the flag

h1702-web challenge was quite interesting although I was not able to retrive the flag.

Take-aways from the challenge:
- Inspect Source code.
- Bruteforce directories.
- Read the documention of the discovered service (if any).
- Analyze the application behaviour.
- Inspect and focus on the web headers.

Brief Summary of the challenge:
-Browsing the IP address(http://159.203.178.9) of the challenge greeted us with a welcome page giving us a hint to bruteforce directory/pages.

-One page was identified http://159.203.178.9/README.html which contained documentation of the secure note service running. It provided valid JWT token of the user. Also readme page contained a hint of the 2nd version of the api in use which use to sort notes created on basis of their ID unlike its 1st version which used to sort on the basis of note's creation date.

-The JWT's library in the server suffered with a attack of using algorithm to sign JWT as "NONE". Thereby we could easily manipulate the id from 2 to 1 in JWT.

-User with id as 1 had a note with epoch 1528911533 was the flag for whoes ID was supposed to be retrived so that we could read the flag.

Automating the retrival of ID with a python script executing a linear search instead of a binary search(much easier).
