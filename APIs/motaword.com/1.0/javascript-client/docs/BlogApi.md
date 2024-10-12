# MotaWordApi.BlogApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBlogPosts**](BlogApi.md#getBlogPosts) | **GET** /blogs | Get blog posts - ordered by created desc by default



## getBlogPosts

> BlogArticleList getBlogPosts(opts)

Get blog posts - ordered by created desc by default

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.BlogApi();
let opts = {
  'locale': "locale_example", // String | Article language, default `en`. When no blog article is available and `fallback=true` is specified, it falls back to `en`.
  'fallback': true, // Boolean | When `true`, and no article is found in the locale, it falls back to `locale=en`.
  'page': 1, // Number | 
  'perPage': 1 // Number | 
};
apiInstance.getBlogPosts(opts, (error, data, response) => {
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
 **locale** | **String**| Article language, default &#x60;en&#x60;. When no blog article is available and &#x60;fallback&#x3D;true&#x60; is specified, it falls back to &#x60;en&#x60;. | [optional] 
 **fallback** | **Boolean**| When &#x60;true&#x60;, and no article is found in the locale, it falls back to &#x60;locale&#x3D;en&#x60;. | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 1]

### Return type

[**BlogArticleList**](BlogArticleList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

