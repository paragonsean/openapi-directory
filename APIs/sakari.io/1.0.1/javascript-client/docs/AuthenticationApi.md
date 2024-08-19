# Sakari.AuthenticationApi

All URIs are relative to *https://api.sakari.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authToken**](AuthenticationApi.md#authToken) | **POST** /oauth2/token | Get token for accessing APIs



## authToken

> TokenResponse authToken(opts)

Get token for accessing APIs

### Example

```javascript
import Sakari from 'sakari';

let apiInstance = new Sakari.AuthenticationApi();
let opts = {
  'tokenRequest': new Sakari.TokenRequest() // TokenRequest | 
};
apiInstance.authToken(opts, (error, data, response) => {
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

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

