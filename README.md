wedrmedr ftw
============

Roadmap
-------

1. Implement the cli
2. Guess the location, Start making [API calls](https://github.com/toddmotto/public-apis)
3. Based on the location find whats the [wheather](https://www.metaweather.com/api/) there
4. Get the time based on location
5. Create tags based on the weather and time of day
6. Make an api call to find photos: [here](https://github.com/500px/legacy-api-documentation), [here](https://www.flickr.com/services/api/), [here](developers.gettyimages.com/en/), or find something on the this [list](https://github.com/toddmotto/public-apis#photography) based on the tags (select a random photo from results).
7. Make a call to the invironment (KDE, Gnome) and change the wallpaper with the selected photo

Dependencies
-------
Example for Debian:

First, install the dependencies:
apt-get install libcurl4-openssl-dev libx11-dev libxt-dev libimlib2-dev libxinerama-dev libjpeg-progs

Then, either get the latest tarball:
`wget http://feh.finalrewind.org/feh-2.25.1.tar.bz2`
`tar -xjf feh-2.25.1.tar.bz2`
`cd feh-2.25.1`

or check out the git version:
`git clone git://git.finalrewind.org/feh || git clone git://github.com/derf/feh.git`
`cd feh`

Now, compile and install feh:
`make`
`sudo make install`

## Build

`docker build -t wedrmedr:latest .`

## Run

`docker run -d wedrmedr:latest`