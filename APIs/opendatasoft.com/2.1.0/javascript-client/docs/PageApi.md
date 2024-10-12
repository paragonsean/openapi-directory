# Opendatasoft.PageApi

All URIs are relative to *https://public.opendatasoft.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPage**](PageApi.md#getPage) | **GET** /pages/{slug} | 
[**getPages**](PageApi.md#getPages) | **GET** /pages | 



## getPage

> GetPages200ResponsePagesInner getPage(slug)



A single page&#39;s metadata from this portal 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.PageApi();
let slug = "slug_example"; // String | Page slug. 
apiInstance.getPage(slug, (error, data, response) => {
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
 **slug** | **String**| Page slug.  | 

### Return type

[**GetPages200ResponsePagesInner**](GetPages200ResponsePagesInner.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPages

> GetPages200Response getPages()



List of all pages from this portal. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.PageApi();
apiInstance.getPages((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPages200Response**](GetPages200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

