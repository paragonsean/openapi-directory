# IllumiDesk.SearchApi

All URIs are relative to *https://api.illumidesk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /v1/{namespace}/search/ | Get a search results



## search

> [Object] search(namespace, q, opts)

Get a search results

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.SearchApi();
let namespace = "namespace_example"; // String | User or team name.
let q = "q_example"; // String | Search string.
let opts = {
  'type': "type_example", // String | Limit results to specific types.
  'limit': "limit_example", // String | Limit data when getting items.
  'offset': "offset_example" // String | Offset data when getting items.
};
apiInstance.search(namespace, q, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **q** | **String**| Search string. | 
 **type** | **String**| Limit results to specific types. | [optional] 
 **limit** | **String**| Limit data when getting items. | [optional] 
 **offset** | **String**| Offset data when getting items. | [optional] 

### Return type

**[Object]**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html

