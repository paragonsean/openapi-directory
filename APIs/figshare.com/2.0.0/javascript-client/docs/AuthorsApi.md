# FigshareApi.AuthorsApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateAuthorDetails**](AuthorsApi.md#privateAuthorDetails) | **GET** /account/authors/{author_id} | Author details
[**privateAuthorsSearch**](AuthorsApi.md#privateAuthorsSearch) | **POST** /account/authors/search | Search Authors



## privateAuthorDetails

> AuthorComplete privateAuthorDetails(authorId)

Author details

View author details

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.AuthorsApi();
let authorId = 789; // Number | Author unique identifier
apiInstance.privateAuthorDetails(authorId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorId** | **Number**| Author unique identifier | 

### Return type

[**AuthorComplete**](AuthorComplete.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateAuthorsSearch

> [Author] privateAuthorsSearch(opts)

Search Authors

Search for authors

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.AuthorsApi();
let opts = {
  'privateAuthorsSearch': new FigshareApi.PrivateAuthorsSearch() // PrivateAuthorsSearch | Search Parameters
};
apiInstance.privateAuthorsSearch(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privateAuthorsSearch** | [**PrivateAuthorsSearch**](PrivateAuthorsSearch.md)| Search Parameters | [optional] 

### Return type

[**[Author]**](Author.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

