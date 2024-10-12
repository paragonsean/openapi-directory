# IpQualityScoreApi.PhoneValidationApi

All URIs are relative to *https://ipqualityscore.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**phoneValidation**](PhoneValidationApi.md#phoneValidation) | **GET** /json/phone/{YOUR_API_KEY_HERE}/{USER_PHONE_HERE} | Phone Validation



## phoneValidation

> PhoneValidation200Response phoneValidation(YOUR_API_KEY_HERE, USER_PHONE_HERE, opts)

Phone Validation

Phone Validation

### Example

```javascript
import IpQualityScoreApi from 'ip_quality_score_api';

let apiInstance = new IpQualityScoreApi.PhoneValidationApi();
let YOUR_API_KEY_HERE = "asd24#sdfs322#"; // String | (Required) YOUR_API_KEY_HERE
let USER_PHONE_HERE = "18007132618"; // String | (Required) USER_PHONE_HERE
let opts = {
  'country': "UK" // String | country
};
apiInstance.phoneValidation(YOUR_API_KEY_HERE, USER_PHONE_HERE, opts, (error, data, response) => {
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
 **USER_PHONE_HERE** | **String**| (Required) USER_PHONE_HERE | 
 **country** | **String**| country | [optional] 

### Return type

[**PhoneValidation200Response**](PhoneValidation200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

