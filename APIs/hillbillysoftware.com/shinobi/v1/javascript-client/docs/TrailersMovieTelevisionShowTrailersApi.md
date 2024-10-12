# Shinobiapi.TrailersMovieTelevisionShowTrailersApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trailerCountByIDGet**](TrailersMovieTelevisionShowTrailersApi.md#trailerCountByIDGet) | **GET** /Trailers/CountByID/{AccessToken}/{imdbID} | Get trailer count for passed ID
[**trailerCountByNameGet**](TrailersMovieTelevisionShowTrailersApi.md#trailerCountByNameGet) | **GET** /Trailers/CountByName/{AccessToken}/{Name} | Get trailer count for passed name (Movie title or TVShow name)
[**trailerSearchGet**](TrailersMovieTelevisionShowTrailersApi.md#trailerSearchGet) | **GET** /Trailers/Search/{AccessToken}/{Phrase} | Gets trailers by search phrase (limited to 10 records)
[**trailersbyIDGet**](TrailersMovieTelevisionShowTrailersApi.md#trailersbyIDGet) | **GET** /Trailers/ByID/{AccessToken}/{imdbID} | Get Trailers for passed imdbID



## trailerCountByIDGet

> TrailerCount trailerCountByIDGet(accessToken, imdbID)

Get trailer count for passed ID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TrailersMovieTelevisionShowTrailersApi();
let accessToken = "accessToken_example"; // String | 
let imdbID = "imdbID_example"; // String | 
apiInstance.trailerCountByIDGet(accessToken, imdbID, (error, data, response) => {
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
 **imdbID** | **String**|  | 

### Return type

[**TrailerCount**](TrailerCount.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## trailerCountByNameGet

> TrailerCount trailerCountByNameGet(accessToken, name)

Get trailer count for passed name (Movie title or TVShow name)

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TrailersMovieTelevisionShowTrailersApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | 
apiInstance.trailerCountByNameGet(accessToken, name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**TrailerCount**](TrailerCount.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## trailerSearchGet

> [Trailer] trailerSearchGet(accessToken, phrase)

Gets trailers by search phrase (limited to 10 records)

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TrailersMovieTelevisionShowTrailersApi();
let accessToken = "accessToken_example"; // String | 
let phrase = "phrase_example"; // String | Trailer you like to search for
apiInstance.trailerSearchGet(accessToken, phrase, (error, data, response) => {
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
 **phrase** | **String**| Trailer you like to search for | 

### Return type

[**[Trailer]**](Trailer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## trailersbyIDGet

> [Trailer] trailersbyIDGet(accessToken, imdbID)

Get Trailers for passed imdbID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TrailersMovieTelevisionShowTrailersApi();
let accessToken = "accessToken_example"; // String | 
let imdbID = "imdbID_example"; // String | 
apiInstance.trailersbyIDGet(accessToken, imdbID, (error, data, response) => {
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
 **imdbID** | **String**|  | 

### Return type

[**[Trailer]**](Trailer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

