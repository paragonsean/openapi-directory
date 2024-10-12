# WhatsAppBusinessApi.RegistrationApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registerAccount**](RegistrationApi.md#registerAccount) | **POST** /account/verify | Register-Account
[**requestCode**](RegistrationApi.md#requestCode) | **POST** /account | Request-Code



## registerAccount

> registerAccount(registerAccountRequestBody)

Register-Account

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.RegistrationApi();
let registerAccountRequestBody = {"code":"<Registration Code Received via SMS/Voice>"}; // RegisterAccountRequestBody | 
apiInstance.registerAccount(registerAccountRequestBody, (error, data, response) => {
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
 **registerAccountRequestBody** | [**RegisterAccountRequestBody**](RegisterAccountRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## requestCode

> requestCode(requestCodeRequestBody)

Request-Code

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.RegistrationApi();
let requestCodeRequestBody = {"cc":"<Country Code>","cert":"<Valid Cert from Business Manager>","method":"sms","phone_number":"<Phone Number>","pin":"<Two-Step Verification PIN"}; // RequestCodeRequestBody | 
apiInstance.requestCode(requestCodeRequestBody, (error, data, response) => {
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
 **requestCodeRequestBody** | [**RequestCodeRequestBody**](RequestCodeRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

