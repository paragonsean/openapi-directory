# BeezUpMerchantApi.PublicSecuritySecurityApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](PublicSecuritySecurityApi.md#login) | **POST** /v2/public/security/login | Login
[**lostPassword**](PublicSecuritySecurityApi.md#lostPassword) | **POST** /v2/public/security/lostpassword | Lost password
[**register**](PublicSecuritySecurityApi.md#register) | **POST** /v2/public/security/register | User Registration



## login

> ApiCredentials login(loginRequest)

Login

User Login - The login will give your tokens

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.PublicSecuritySecurityApi();
let loginRequest = new BeezUpMerchantApi.LoginRequest(); // LoginRequest | 
apiInstance.login(loginRequest, (error, data, response) => {
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
 **loginRequest** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**ApiCredentials**](ApiCredentials.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## lostPassword

> lostPassword(body)

Lost password

Lost password - Your password will be regenerated and sent to your email

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.PublicSecuritySecurityApi();
let body = "body_example"; // String | Your email
apiInstance.lostPassword(body, (error, data, response) => {
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
 **body** | **String**| Your email | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## register

> register(registerRequest)

User Registration

User Registration - Create a new user on BeezUP

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.PublicSecuritySecurityApi();
let registerRequest = new BeezUpMerchantApi.RegisterRequest(); // RegisterRequest | 
apiInstance.register(registerRequest, (error, data, response) => {
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
 **registerRequest** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

