# Mailscript.VerificationsApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVerification**](VerificationsApi.md#addVerification) | **POST** /verifications | Start verification process for external email address or sms number
[**getAllVerifications**](VerificationsApi.md#getAllVerifications) | **GET** /verifications | Get all verificats for the user
[**verify**](VerificationsApi.md#verify) | **POST** /verifications/{verification}/verify | Verify an email address or sms number with a code



## addVerification

> AddVerificationResponse addVerification(addVerificationRequest)

Start verification process for external email address or sms number

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.VerificationsApi();
let addVerificationRequest = new Mailscript.AddVerificationRequest(); // AddVerificationRequest | Key body
apiInstance.addVerification(addVerificationRequest, (error, data, response) => {
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
 **addVerificationRequest** | [**AddVerificationRequest**](AddVerificationRequest.md)| Key body | 

### Return type

[**AddVerificationResponse**](AddVerificationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAllVerifications

> GetAllVerificationsResponse getAllVerifications()

Get all verificats for the user

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.VerificationsApi();
apiInstance.getAllVerifications((error, data, response) => {
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

[**GetAllVerificationsResponse**](GetAllVerificationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## verify

> verify(verification, verifyRequest)

Verify an email address or sms number with a code

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.VerificationsApi();
let verification = "verification_example"; // String | ID of the verification entry
let verifyRequest = new Mailscript.VerifyRequest(); // VerifyRequest | Verify action body
apiInstance.verify(verification, verifyRequest, (error, data, response) => {
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
 **verification** | **String**| ID of the verification entry | 
 **verifyRequest** | [**VerifyRequest**](VerifyRequest.md)| Verify action body | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

