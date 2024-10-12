# Omdb.DefaultApi

All URIs are relative to *http://www.omdbapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOMDbSearch**](DefaultApi.md#getOMDbSearch) | **GET** / | OMDb Search



## getOMDbSearch

> CombinedResult getOMDbSearch(r, opts)

OMDb Search

Find a movie, series or episode from the OMDb by title, IMDb-id or by free-text search

### Example

```javascript
import Omdb from 'omdb';

let apiInstance = new Omdb.DefaultApi();
let r = "'json'"; // String | The data type to return.
let opts = {
  't': "t_example", // String | Movie title to search for. One of t, i or s is required.
  'i': "i_example", // String | A valid IMDb ID (e.g. tt1285016). One of t, i or s is required.
  's': "s_example", // String | Movie title to search for. One of t, i or s is required.
  'y': 56, // Number | Year of release.
  'type': "type_example", // String | Type of result to return.
  'plot': "'short'", // String | Return short or full plot.
  'tomatoes': false, // Boolean | Include Rotten Tomatoes ratings.
  'v': 1, // Number | API version (reserved for future use).
  'page': 1, // Number | Page number to return.
  'callback': "callback_example" // String | JSONP callback name.
};
apiInstance.getOMDbSearch(r, opts, (error, data, response) => {
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
 **r** | **String**| The data type to return. | [default to &#39;json&#39;]
 **t** | **String**| Movie title to search for. One of t, i or s is required. | [optional] 
 **i** | **String**| A valid IMDb ID (e.g. tt1285016). One of t, i or s is required. | [optional] 
 **s** | **String**| Movie title to search for. One of t, i or s is required. | [optional] 
 **y** | **Number**| Year of release. | [optional] 
 **type** | **String**| Type of result to return. | [optional] 
 **plot** | **String**| Return short or full plot. | [optional] [default to &#39;short&#39;]
 **tomatoes** | **Boolean**| Include Rotten Tomatoes ratings. | [optional] [default to false]
 **v** | **Number**| API version (reserved for future use). | [optional] [default to 1]
 **page** | **Number**| Page number to return. | [optional] [default to 1]
 **callback** | **String**| JSONP callback name. | [optional] 

### Return type

[**CombinedResult**](CombinedResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

