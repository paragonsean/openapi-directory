# Vimeo.VideosLanguagesApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLanguages**](VideosLanguagesApi.md#getLanguages) | **GET** /languages | Get all languages



## getLanguages

> [Language] getLanguages(opts)

Get all languages

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.VideosLanguagesApi();
let opts = {
  'filter': "filter_example" // String | The attribute by which to filter the results.  Option descriptions:  * `texttracks` - Only return text track supported languages 
};
apiInstance.getLanguages(opts, (error, data, response) => {
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
 **filter** | **String**| The attribute by which to filter the results.  Option descriptions:  * &#x60;texttracks&#x60; - Only return text track supported languages  | [optional] 

### Return type

[**[Language]**](Language.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.language+json

