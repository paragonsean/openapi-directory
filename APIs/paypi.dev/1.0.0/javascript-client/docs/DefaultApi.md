# EmailVerify.DefaultApi

All URIs are relative to *https://ev.apis.paypi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkCodePost**](DefaultApi.md#checkCodePost) | **POST** /checkCode | Check verification code
[**sendCodePost**](DefaultApi.md#sendCodePost) | **POST** /sendCode | Send verification code



## checkCodePost

> CheckCodePost200Response checkCodePost(checkCodePostRequest)

Check verification code

Checks the user&#39;s emailed code is valid.  If this returns success&#x3D;true, you can safely assume the user you are interacting with is the owner of that email address. 

### Example

```javascript
import EmailVerify from 'email_verify';
let defaultClient = EmailVerify.ApiClient.instance;
// Configure Bearer (Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EmailVerify.DefaultApi();
let checkCodePostRequest = new EmailVerify.CheckCodePostRequest(); // CheckCodePostRequest | 
apiInstance.checkCodePost(checkCodePostRequest, (error, data, response) => {
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
 **checkCodePostRequest** | [**CheckCodePostRequest**](CheckCodePostRequest.md)|  | 

### Return type

[**CheckCodePost200Response**](CheckCodePost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendCodePost

> SendCodePost200Response sendCodePost(sendCodePostRequest)

Send verification code

This request send&#39;s a code to the given email address, which should be returned to check it is correct.

### Example

```javascript
import EmailVerify from 'email_verify';
let defaultClient = EmailVerify.ApiClient.instance;
// Configure Bearer (Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EmailVerify.DefaultApi();
let sendCodePostRequest = {"email":"test@test.com"}; // SendCodePostRequest | 
apiInstance.sendCodePost(sendCodePostRequest, (error, data, response) => {
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
 **sendCodePostRequest** | [**SendCodePostRequest**](SendCodePostRequest.md)|  | 

### Return type

[**SendCodePost200Response**](SendCodePost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

