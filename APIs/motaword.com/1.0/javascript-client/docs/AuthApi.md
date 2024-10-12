# MotaWordApi.AuthApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccessToken**](AuthApi.md#getAccessToken) | **POST** /token | Retrieve an access token



## getAccessToken

> Token getAccessToken(opts)

Retrieve an access token

MotaWord API is using OAuth2 procedures when authenticating or authorizing your API call. 

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MotaWordApi.AuthApi();
let opts = {
  'tokenRequest': new MotaWordApi.TokenRequest() // TokenRequest | 
};
apiInstance.getAccessToken(opts, (error, data, response) => {
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
 **tokenRequest** | [**TokenRequest**](TokenRequest.md)|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

