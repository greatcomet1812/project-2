# UOCIS322 - Project 2 #

Author: Sewon Sohn
Contact: ssohn@uoregon.edu
This program builds and runs Docker. It uses Flask to search for and open the file requested and throws an error if the file is not found or contains invalid characters. 

## Grading Rubric

* If everything works as expected, 100 will be assigned.
* If existing pages and files are NOT handled correctly, 20 points will be docked.
* For each of the errors not handled correctly (403, and 404), 20 points will be docked.
* For each the two HTML files (`404.html` and `403.html`) not in the appropriate location, 5 points will be docked.
* If `README.md` is not updated with your name and info, 5 points will be docked.
* If `Dockerfile` doesn't contain your name and email, 5 points will be docked.
* If docker builds and runs, but does not have the expected functionalities implemented, or the server is unreachable, 20 will be assigned.
	* ⚠️ NOTE: If `app.py` does not read port number and debug mode from `credentials.ini` (or `default.ini` if not found), autograder will mark this as unreachable, as it cannot look for the correct port number.
* If docker builds, but fails to run, 15 will be assigned.
* If docker fails to build, 5 will be assigned.
* If `credentials.ini` is incorrect or not submitted, 0 will be assigned.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
