import urllib2
import simplejson
import urllib
import errno
import os

# Fixed
globalSearchURL = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&start=%s"
fetch = urllib2.build_opener()

# Image goes into the same folder
def get_image_google(searchTerm, amount):
    for position in range(0, amount):
        searchUrl = globalSearchURL % (searchTerm, str(position))
        f = fetch.open(searchUrl)
        a = simplejson.load(f)
        imageUrl = a['responseData']['results'][0]['unescapedUrl']
        print "Downloading", str(position)
        urllib.urlretrieve(imageUrl, "image_" + str(position))

# Operation to check if the directory currently already exists
def require_dir(path):
    try:
        os.makedirs(path)
    except OSError, exc:
        if exc.errno != errno.EEXIST:
            raise

# Image goes into a seperate folder
def get_image_google_to_directory(searchTerm, amount, directoryName):

    # Check if the current directory exists
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), directoryName)
    require_dir(directory)

    # Goes through the positions
    for position in range(0, amount):
        # Get Image, and tell user to start downloading it
        searchUrl = globalSearchURL % (searchTerm, str(position))
        f = fetch.open(searchUrl)
        a = simplejson.load(f)
        imageUrl = a['responseData']['results'][0]['unescapedUrl']
        print "Downloading", str(position)

        # Check if directory exists, and make the file
        filename = os.path.join(directory, "image_" + str(position))

        # Save it into the current file
        urllib.urlretrieve(imageUrl, filename)

if __name__ == '__main__':
    # get_image_google('parrot', 10)
    get_image_google_to_directory('parrot', 10, 'images')
