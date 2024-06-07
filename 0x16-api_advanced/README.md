# API Usage Guide

This guide covers essential topics for effectively using APIs in your projects. Below are the sections included:

1. [How to Read API Documentation to Find the Endpoints You’re Looking For](#how-to-read-api-documentation)
2. [How to Use an API with Pagination](#how-to-use-an-api-with-pagination)
3. [How to Parse JSON Results from an API](#how-to-parse-json-results-from-an-api)
4. [How to Make a Recursive API Call](#how-to-make-a-recursive-api-call)
5. [How to Sort a Dictionary by Value](#how-to-sort-a-dictionary-by-value)

## How to Read API Documentation

API documentation is a comprehensive guide provided by API developers. It explains how to interact with the API, detailing endpoints, parameters, authentication methods, and request/response formats.

### Key Components of API Documentation:
- **Overview**: Introduction to the API’s purpose and functionality.
- **Endpoints**: Lists available endpoints with details such as URL, HTTP methods, and descriptions.
- **Parameters**: Required and optional parameters for each endpoint.
- **Request and Response Formats**: Formats for requests and responses, typically JSON or XML.
- **Authentication**: Methods for authenticating with the API.
- **Examples**: Example requests and responses.
- **Error Handling**: Possible error codes and messages.
- **Rate Limits**: Information on request limits.

### Where to Find API Documentation:
- Official API websites (e.g., [GitHub API](https://docs.github.com/en/rest)).
- Developer portals (e.g., [Google Developers](https://developers.google.com/)).
- API documentation platforms (e.g., [Swagger](https://swagger.io/tools/swagger-ui/)).
- GitHub repositories.

## How to Use an API with Pagination

Many APIs return results in pages. Handling pagination involves making multiple API calls to retrieve all results.

### Example:
```python
import requests

url = "https://api.example.com/data"
params = {
    'page': 1,
    'per_page': 100
}
all_data = []

while True:
    response = requests.get(url, params=params)
    data = response.json()
    if not data:
        break
    all_data.extend(data)
    params['page'] += 1

print(all_data)

