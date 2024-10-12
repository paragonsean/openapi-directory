# SquareConnectApi.MobileAuthorizationApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMobileAuthorizationCode**](MobileAuthorizationApi.md#createMobileAuthorizationCode) | **POST** /mobile/authorization-code | CreateMobileAuthorizationCode



## createMobileAuthorizationCode

> CreateMobileAuthorizationCodeResponse createMobileAuthorizationCode(createMobileAuthorizationCodeRequest)

CreateMobileAuthorizationCode

Generates code to authorize a mobile application to connect to a Square card reader  Authorization codes are one-time-use and expire __60 minutes__ after being issued.  __Important:__ The &#x60;Authorization&#x60; header you provide to this endpoint must have the following format:  &#x60;&#x60;&#x60; Authorization: Bearer ACCESS_TOKEN &#x60;&#x60;&#x60;  Replace &#x60;ACCESS_TOKEN&#x60; with a [valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.MobileAuthorizationApi();
let createMobileAuthorizationCodeRequest = new SquareConnectApi.CreateMobileAuthorizationCodeRequest(); // CreateMobileAuthorizationCodeRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createMobileAuthorizationCode(createMobileAuthorizationCodeRequest, (error, data, response) => {
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
 **createMobileAuthorizationCodeRequest** | [**CreateMobileAuthorizationCodeRequest**](CreateMobileAuthorizationCodeRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateMobileAuthorizationCodeResponse**](CreateMobileAuthorizationCodeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

