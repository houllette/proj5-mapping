# Project 5: Mapping

Author: Holden Oullette, hjo@uoregon.edu

## Description ##
Runs Flask server that implements a Leaflet map with three points of interest. By
default, map starts with view of Eugene. Whenever a user clicks, the Latitude and
Longitude coordinates of that location are Reverse Geocoded to the closest address

## Installation & Deployment ##

	```bash
	git clone https://github.com/houllette/proj5-mapping
	cd proj5-mapping
	bash ./configure
	make run
    ```

    The program will also run using gunicorn by running
    ```bash
    make service
    ```
    This only works if you have already run bash ./configure
