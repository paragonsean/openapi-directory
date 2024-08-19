# KycApiDocumentation.V1IbanVerificationApi

All URIs are relative to *https://api.kompany.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ibanBasic**](V1IbanVerificationApi.md#ibanBasic) | **POST** /api/v1/iban-verification/check-iban | Checks validity of an IBAN number
[**ibanComprehensive**](V1IbanVerificationApi.md#ibanComprehensive) | **POST** /api/v1/iban-verification/comprehensive-check-iban | Checks validity of an IBAN number



## ibanBasic

> IbanBasic200Response ibanBasic(ibanNumber)

Checks validity of an IBAN number

Basic verification of an IBAN number validating its structure

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1IbanVerificationApi();
let ibanNumber = "ibanNumber_example"; // String | IBAN number to validate
apiInstance.ibanBasic(ibanNumber, (error, data, response) => {
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
 **ibanNumber** | **String**| IBAN number to validate | 

### Return type

[**IbanBasic200Response**](IbanBasic200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## ibanComprehensive

> Object ibanComprehensive(ibanNumber)

Checks validity of an IBAN number

Comprehensive verification of IBAN number using a service provider for verification

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1IbanVerificationApi();
let ibanNumber = "ibanNumber_example"; // String | IBAN number to validate
apiInstance.ibanComprehensive(ibanNumber, (error, data, response) => {
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
 **ibanNumber** | **String**| IBAN number to validate | 

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

