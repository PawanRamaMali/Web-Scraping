# API requiring registration - POST request

### Registering to the API


```python
# We will use a nutritional analysis API
# It requires registration (we need an API key to validate ourselves)
# Many APIs require this kind of registration
```


```python
# You can sign-up for the Developer (Free) edition here: 
#        https://developer.edamam.com/edamam-nutrition-api

# API documentation: 
#        https://developer.edamam.com/edamam-docs-nutrition-api
```

### Initial Setup


```python
# loading the packages
import requests
import json
```


```python
# Store the ID and Key in variables

#APP_ID = "your_API_ID_here"
#APP_KEY = "your_API_key_here"

# Note: Those are not real ID and Key,
# Replace the string with your own ones that you recieved upon registration
```


```python
# Setting up the request URL
api_endpoint = "https://api.edamam.com/api/nutrition-details"

url = api_endpoint + "?app_id=" + APP_ID + "&app_key=" + APP_KEY
```

