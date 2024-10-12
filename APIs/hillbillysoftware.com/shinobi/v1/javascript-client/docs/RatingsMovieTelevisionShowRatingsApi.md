# Shinobiapi.RatingsMovieTelevisionShowRatingsApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ratingByNameGet**](RatingsMovieTelevisionShowRatingsApi.md#ratingByNameGet) | **GET** /Rating/ByName/{AccessToken}/{Name} | 
[**ratingGet**](RatingsMovieTelevisionShowRatingsApi.md#ratingGet) | **GET** /Rating/ByID/{AccessToken}/{imdbID} | Returns ratings from various resources(IMDB,Rotten Tomatoes, metaCritics, TVMaze etc) of passed IMDBid



## ratingByNameGet

> [RatingItem] ratingByNameGet(accessToken, name)



### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.RatingsMovieTelevisionShowRatingsApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | 
apiInstance.ratingByNameGet(accessToken, name, (error, data, response) => {
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

[**[RatingItem]**](RatingItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## ratingGet

> RatingItem ratingGet(accessToken, imdbID)

Returns ratings from various resources(IMDB,Rotten Tomatoes, metaCritics, TVMaze etc) of passed IMDBid

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.RatingsMovieTelevisionShowRatingsApi();
let accessToken = "accessToken_example"; // String | 
let imdbID = "imdbID_example"; // String | 
apiInstance.ratingGet(accessToken, imdbID, (error, data, response) => {
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

[**RatingItem**](RatingItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

