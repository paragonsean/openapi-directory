# IpQualityScoreApi.EmailValidationApi

All URIs are relative to *https://ipqualityscore.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emailValidation**](EmailValidationApi.md#emailValidation) | **GET** /json/email/{YOUR_API_KEY_HERE}/{USER_EMAIL_HERE} | Email Validation



## emailValidation

> EmailValidation200Response emailValidation(YOUR_API_KEY_HERE, USER_EMAIL_HERE)

Email Validation

Email Validation

### Example

```javascript
import IpQualityScoreApi from 'ip_quality_score_api';

let apiInstance = new IpQualityScoreApi.EmailValidationApi();
let YOUR_API_KEY_HERE = "asd24#sdfs322#"; // String | (Required) YOUR_API_KEY_HERE
let USER_EMAIL_HERE = "example@example.com"; // String | (Required) USER_EMAIL_HERE
apiInstance.emailValidation(YOUR_API_KEY_HERE, USER_EMAIL_HERE, (error, data, response) => {
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
 **YOUR_API_KEY_HERE** | **String**| (Required) YOUR_API_KEY_HERE | 
 **USER_EMAIL_HERE** | **String**| (Required) USER_EMAIL_HERE | 

### Return type

[**EmailValidation200Response**](EmailValidation200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

