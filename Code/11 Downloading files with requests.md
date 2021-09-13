# Downloading Files with Requests


```python
# The requests package can also be used to download files from the web.
import requests
```

## Naive downloading


```python
# One way to 'download' a file is to send a request to it.
# Then, export the content of the response to a local file
```


```python
# Let's use an image from wikipedia for this purpose
file_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Collage_of_Nine_Dogs.jpg/1024px-Collage_of_Nine_Dogs.jpg"
```


```python
response = requests.get(file_url)
response.status_code
```




    200




```python
# Printing out the begining of the content of the response
# It is in a binary-encoded format, thus it looks like gibberish
response.content[:500]
```




    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xfe\x00OFile source: https://commons.wikimedia.org/wiki/File:Collage_of_Nine_Dogs.jpg\xff\xe2\x02\x1cICC_PROFILE\x00\x01\x01\x00\x00\x02\x0clcms\x02\x10\x00\x00mntrRGB XYZ \x07\xdc\x00\x01\x00\x19\x00\x03\x00)\x009acspAPPL\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf6\xd6\x00\x01\x00\x00\x00\x00\xd3-lcms\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\ndesc\x00\x00\x00\xfc\x00\x00\x00^cprt\x00\x00\x01\\\x00\x00\x00\x0bwtpt\x00\x00\x01h\x00\x00\x00\x14bkpt\x00\x00\x01|\x00\x00\x00\x14rXYZ\x00\x00\x01\x90\x00\x00\x00\x14gXYZ\x00\x00\x01\xa4\x00\x00\x00\x14bXYZ\x00\x00\x01\xb8\x00\x00\x00\x14rTRC\x00\x00\x01\xcc\x00\x00\x00@gTRC\x00\x00\x01\xcc\x00\x00\x00@bTRC\x00\x00\x01\xcc\x00\x00\x00@desc\x00\x00\x00\x00\x00\x00\x00\x03c2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00text\x00\x00\x00\x00FB\x00\x00XYZ \x00\x00\x00\x00\x00\x00\xf6\xd6\x00\x01\x00\x00\x00\x00\xd3-X'




```python
# We need to export this to an image file (jpg, png, gif...)
```

### Writing to a file


```python
# We open/create a file with the function 'open()'
file = open("dog_image.jpg", "wb")

# Then, write to it
file.write(response.content)

# And close the file after finishing
file.close()
```


```python
# The two parameters in the function open() are:
# - the name of the file (along with a path to it if it is not in the same directory as our program)
# - the mode in wich we want to edit the file

# Some popular modes are:
# - 'r' : Opens the file in read-only mode;
# - 'rb' : Opens the file as read-only in binary format;
# - 'w' : Creates a file in write-only mode. If the file already exists, it will overwrite it;
# - 'wb': Write-only mode in binary format;
# - 'a' : Opens the file for appending new information to the end;
# - 'w+' : Opens the file for writing and reading;

# We have used 'wb' in this example, since we want to export the data to a file (thus, write to it)
# and response.content is in bytes

# Never forget to close the file!
```


```python
# To ensure the file will always be closed, use the 'with' statement
# This automatically calls file.close() at the end
```


```python
with open("dog_image_2.jpg", "wb") as file:
    file.write(response.content)
```


```python

```


```python
# Here, we first receive the whole file and store it in the RAM, then export it to the hard disk
# This method is really inefficient, especially for bigger files
# In effect we download the file to the RAM

# We can fix that with a couple of small changes to our code
```

## Streaming the download to a file


```python
# Instead of reading the whole response immidiatelly, 
# we can signal the program to only read part of the response when we tell it to.

# This is achieved with the 'stream' parameter
```


```python
# I will use test video files provided by file-examples.com
url = "https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_480_1_5MG.mp4"
```


```python
r = requests.get(url, stream = True)

with open("Sample_video_1,5_MB.mp4", "wb") as f:
    
    # Now we iterate over the response in chunks
    for chunk in r.iter_content(chunk_size = 16*1024):
        f.write(chunk)
```


```python
# You can change the chunk size to optimize the fastest download speed for your system
```


```python
# However, when using 'stream=True' requests will not close the connection to the server until all data has been read
# Thus, sometimes the connection needs to be closed manually

# Again, that is best done using the 'with' statement
```


```python
# So, the final code for file download is
url = "https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_1920_18MG.mp4"

with requests.get(url, stream = True) as r:
    with open("Sample_video_18_MB.mp4", "wb") as f:
        for chunk in r.iter_content(chunk_size = 16*1024):
            f.write(chunk)

```

