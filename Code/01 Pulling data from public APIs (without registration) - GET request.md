# Pulling data from public APIs (without registration) - GET request



```py
# !pip install requests-html
# loading the packages
# requests provides us with the capabilities of sending an HTTP request to a server
import requests
```

## Extracting data on currency exchange rates


```python
# We will use an API containing currency exchange rates as published by the European Central Bank
# Documentation at https://exchangeratesapi.io
```

### Sending a GET request


```python
# Define the base URL
# Base URL: the part of the URL common to all requests, not containing the parameters
base_url = "https://api.exchangeratesapi.io/latest"
```


```python
# We can make a GET request to this API endpoint with requests.get
response = requests.get(base_url)

# This method returns the response from the server
# We store this response in a variable for future processing
```

### Investigating the response


```python
# Checking if the request went through ok
response.ok
```




    True




```python
# Checking the status code of the response
response.status_code
```




    200




```python
# Inspecting the content body of the response (as a regular 'string')
response.text
```




    '{\n  "success": false,\n  "error": {\n    "code": 101,\n    "type": "missing_access_key",\n    "info": "You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"\n  }\n}\n'




```python
# Inspecting the content of the response (in 'bytes' format)
response.content
```




    b'{\n  "success": false,\n  "error": {\n    "code": 101,\n    "type": "missing_access_key",\n    "info": "You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"\n  }\n}\n'




```python
# The data is presented in JSON format
```

### Handling the JSON


```python
# Requests has in-build method to directly convert the response to JSON format
response.json()
```




    {'rates': {'CAD': 1.5613,
      'HKD': 8.9041,
      'ISK': 145.0,
      'PHP': 58.013,
      'DKK': 7.4695,
      'HUF': 336.25,
      'CZK': 25.504,
      'AUD': 1.733,
      'RON': 4.8175,
      'SEK': 10.7203,
      'IDR': 16488.05,
      'INR': 84.96,
      'BRL': 5.4418,
      'RUB': 85.1553,
      'HRK': 7.55,
      'JPY': 117.12,
      'THB': 36.081,
      'CHF': 1.0594,
      'SGD': 1.5841,
      'PLN': 4.3132,
      'BGN': 1.9558,
      'TRY': 7.0002,
      'CNY': 7.96,
      'NOK': 10.89,
      'NZD': 1.8021,
      'ZAR': 18.2898,
      'USD': 1.1456,
      'MXN': 24.3268,
      'ILS': 4.0275,
      'GBP': 0.87383,
      'KRW': 1374.71,
      'MYR': 4.8304},
     'base': 'EUR',
     'date': '2020-03-09'}




```python
# In Python, this JSON is stored as a dictionary
type(response.json())
```




    dict




```python
# A useful library for JSON manipulation and pretty print
import json

# It has two main methods:
# .loads(), which creates a Python dictionary from a JSON format string (just as response.json() does)
# .dumps(), which creates a JSON format string out of a Python dictionary 
```


```python
# .dumps() has options to make the string 'prettier', more readable
# We can choose the number of spaces to be used as indentation
json.dumps(response.json(), indent=4)
```




    '{\n    "rates": {\n        "CAD": 1.5613,\n        "HKD": 8.9041,\n        "ISK": 145.0,\n        "PHP": 58.013,\n        "DKK": 7.4695,\n        "HUF": 336.25,\n        "CZK": 25.504,\n        "AUD": 1.733,\n        "RON": 4.8175,\n        "SEK": 10.7203,\n        "IDR": 16488.05,\n        "INR": 84.96,\n        "BRL": 5.4418,\n        "RUB": 85.1553,\n        "HRK": 7.55,\n        "JPY": 117.12,\n        "THB": 36.081,\n        "CHF": 1.0594,\n        "SGD": 1.5841,\n        "PLN": 4.3132,\n        "BGN": 1.9558,\n        "TRY": 7.0002,\n        "CNY": 7.96,\n        "NOK": 10.89,\n        "NZD": 1.8021,\n        "ZAR": 18.2898,\n        "USD": 1.1456,\n        "MXN": 24.3268,\n        "ILS": 4.0275,\n        "GBP": 0.87383,\n        "KRW": 1374.71,\n        "MYR": 4.8304\n    },\n    "base": "EUR",\n    "date": "2020-03-09"\n}'




```python
# In order to visualize these changes, we need to print the string
print(json.dumps(response.json(), indent=4))
```

    {
        "rates": {
            "CAD": 1.5613,
            "HKD": 8.9041,
            "ISK": 145.0,
            "PHP": 58.013,
            "DKK": 7.4695,
            "HUF": 336.25,
            "CZK": 25.504,
            "AUD": 1.733,
            "RON": 4.8175,
            "SEK": 10.7203,
            "IDR": 16488.05,
            "INR": 84.96,
            "BRL": 5.4418,
            "RUB": 85.1553,
            "HRK": 7.55,
            "JPY": 117.12,
            "THB": 36.081,
            "CHF": 1.0594,
            "SGD": 1.5841,
            "PLN": 4.3132,
            "BGN": 1.9558,
            "TRY": 7.0002,
            "CNY": 7.96,
            "NOK": 10.89,
            "NZD": 1.8021,
            "ZAR": 18.2898,
            "USD": 1.1456,
            "MXN": 24.3268,
            "ILS": 4.0275,
            "GBP": 0.87383,
            "KRW": 1374.71,
            "MYR": 4.8304
        },
        "base": "EUR",
        "date": "2020-03-09"
    }
    


```python
# It contains 3 keys; the value for the 'rates' key is another dictionary
response.json().keys()
```




    dict_keys(['rates', 'base', 'date'])


