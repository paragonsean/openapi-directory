# Search.AdditionalDataApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchVersionNumberAdditionalDataExtGet**](AdditionalDataApi.md#searchVersionNumberAdditionalDataExtGet) | **GET** /search/{versionNumber}/additionalData.{ext} | Additional Data



## searchVersionNumberAdditionalDataExtGet

> searchVersionNumberAdditionalDataExtGet(versionNumber, ext, geometries, opts)

Additional Data

### Example

```javascript
import Search from 'search';
let defaultClient = Search.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Search.AdditionalDataApi();
let versionNumber = 56; // Number | Service version number. The current value is 2.
let ext = "ext_example"; // String | Expected response format.
let geometries = "00004631-3400-3c00-0000-0000673c4d2e,00004631-3400-3c00-0000-0000673c42fe"; // String | Comma separated list of geometry UUIDs, previously retrieved from an Search API request.
let opts = {
  'geometriesZoom': 56 // Number | Defines the precision of the geometries.
};
apiInstance.searchVersionNumberAdditionalDataExtGet(versionNumber, ext, geometries, opts, (error, data, response) => {
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
 **versionNumber** | **Number**| Service version number. The current value is 2. | 
 **ext** | **String**| Expected response format. | 
 **geometries** | **String**| Comma separated list of geometry UUIDs, previously retrieved from an Search API request. | 
 **geometriesZoom** | **Number**| Defines the precision of the geometries. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

