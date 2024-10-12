# Shinobiapi.MoviesMoviesDocumentariesMadeForTelevisionMoviesApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**movieIDGet**](MoviesMoviesDocumentariesMadeForTelevisionMoviesApi.md#movieIDGet) | **GET** /Movie/ByID/{accesstoken}/{imdbID} | 
[**movieSearchGetAsync**](MoviesMoviesDocumentariesMadeForTelevisionMoviesApi.md#movieSearchGetAsync) | **GET** /Movie/Search/{AccessToken}/{Query} | Searches for movies, result set limited to 5 records



## movieIDGet

> MovieInformation movieIDGet(accesstoken, imdbID)



### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MoviesMoviesDocumentariesMadeForTelevisionMoviesApi();
let accesstoken = "accesstoken_example"; // String | 
let imdbID = "imdbID_example"; // String | 
apiInstance.movieIDGet(accesstoken, imdbID, (error, data, response) => {
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
 **accesstoken** | **String**|  | 
 **imdbID** | **String**|  | 

### Return type

[**MovieInformation**](MovieInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## movieSearchGetAsync

> [MovieInformation] movieSearchGetAsync(accessToken, query)

Searches for movies, result set limited to 5 records

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MoviesMoviesDocumentariesMadeForTelevisionMoviesApi();
let accessToken = "accessToken_example"; // String | 
let query = "query_example"; // String | 
apiInstance.movieSearchGetAsync(accessToken, query, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **query** | **String**|  | 

### Return type

[**[MovieInformation]**](MovieInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

