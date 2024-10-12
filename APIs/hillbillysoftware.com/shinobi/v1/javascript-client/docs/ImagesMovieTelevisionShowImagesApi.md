# Shinobiapi.ImagesMovieTelevisionShowImagesApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imageSearchGet**](ImagesMovieTelevisionShowImagesApi.md#imageSearchGet) | **GET** /Images/Search/{Accesstoken}/{Query} | Get images available for movie/tv show with passed query
[**imagesGet**](ImagesMovieTelevisionShowImagesApi.md#imagesGet) | **GET** /Images/ByID/{AccessToken}/{imdbID} | Get images available for movie/tv show with passed imdbID



## imageSearchGet

> [ImdbImages] imageSearchGet(accesstoken, query, opts)

Get images available for movie/tv show with passed query

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.ImagesMovieTelevisionShowImagesApi();
let accesstoken = "accesstoken_example"; // String | 
let query = "query_example"; // String | Name or part of name from Movie or Show
let opts = {
  'strictmatch': true // Boolean | 
};
apiInstance.imageSearchGet(accesstoken, query, opts, (error, data, response) => {
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
 **query** | **String**| Name or part of name from Movie or Show | 
 **strictmatch** | **Boolean**|  | [optional] 

### Return type

[**[ImdbImages]**](ImdbImages.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## imagesGet

> [ImdbImages] imagesGet(accessToken, imdbID)

Get images available for movie/tv show with passed imdbID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.ImagesMovieTelevisionShowImagesApi();
let accessToken = "accessToken_example"; // String | 
let imdbID = "imdbID_example"; // String | 
apiInstance.imagesGet(accessToken, imdbID, (error, data, response) => {
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

[**[ImdbImages]**](ImdbImages.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

