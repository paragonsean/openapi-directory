# TraktApi.LanguagesApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLanguages**](LanguagesApi.md#getLanguages) | **GET** /languages/{type} | Get languages



## getLanguages

> getLanguages(type, opts)

Get languages

Get a list of all langauges, including names and codes.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.LanguagesApi();
let type = "movies"; // String | 
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getLanguages(type, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**|  | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

