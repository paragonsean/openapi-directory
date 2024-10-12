# RedirectionIo.ForgotPasswordRequestApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postForgotPasswordRequestCollection**](ForgotPasswordRequestApi.md#postForgotPasswordRequestCollection) | **POST** /users/forgot-password-request | Creates a ForgotPasswordRequest resource.



## postForgotPasswordRequestCollection

> ForgotPasswordRequest postForgotPasswordRequestCollection(opts)

Creates a ForgotPasswordRequest resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ForgotPasswordRequestApi();
let opts = {
  'forgotPasswordRequest': new RedirectionIo.ForgotPasswordRequest() // ForgotPasswordRequest | The new ForgotPasswordRequest resource
};
apiInstance.postForgotPasswordRequestCollection(opts, (error, data, response) => {
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
 **forgotPasswordRequest** | [**ForgotPasswordRequest**](ForgotPasswordRequest.md)| The new ForgotPasswordRequest resource | [optional] 

### Return type

[**ForgotPasswordRequest**](ForgotPasswordRequest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

