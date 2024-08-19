# KycApiDocumentation.V1TinVerificationApi

All URIs are relative to *https://api.kompany.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tinVerificationBasicCheck**](V1TinVerificationApi.md#tinVerificationBasicCheck) | **GET** /api/v1/tin-verification/basic-check | Verifies a TIN number
[**tinVerificationComprehensiveCheck**](V1TinVerificationApi.md#tinVerificationComprehensiveCheck) | **GET** /api/v1/tin-verification/comprehensive-check | EIN Name Lookup with TIN number and retrieves company data
[**tinVerificationNameLookup**](V1TinVerificationApi.md#tinVerificationNameLookup) | **GET** /api/v1/tin-verification/name-lookup | EIN Name Lookup with TIN number



## tinVerificationBasicCheck

> TinVerificationBasicCheck200Response tinVerificationBasicCheck(tin, name)

Verifies a TIN number

Performs a basic verification check of a given TIN number and name.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1TinVerificationApi();
let tin = "tin_example"; // String | Nine letter TIN number with or without hyphens
let name = "name_example"; // String | Company Name
apiInstance.tinVerificationBasicCheck(tin, name, (error, data, response) => {
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
 **tin** | **String**| Nine letter TIN number with or without hyphens | 
 **name** | **String**| Company Name | 

### Return type

[**TinVerificationBasicCheck200Response**](TinVerificationBasicCheck200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tinVerificationComprehensiveCheck

> TinVerificationComprehensiveCheck200Response tinVerificationComprehensiveCheck(tin, name, opts)

EIN Name Lookup with TIN number and retrieves company data

Performs an EIN name match using provided TIN Number. Additionally to the name lookup it will lookup company details

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1TinVerificationApi();
let tin = "tin_example"; // String | Nine letter TIN number with or without hyphens
let name = "name_example"; // String | Company Name
let opts = {
  'threshold': 789 // Number | The percentage of minimum similarity threshold for company matching (optional, default: 70%)
};
apiInstance.tinVerificationComprehensiveCheck(tin, name, opts, (error, data, response) => {
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
 **tin** | **String**| Nine letter TIN number with or without hyphens | 
 **name** | **String**| Company Name | 
 **threshold** | **Number**| The percentage of minimum similarity threshold for company matching (optional, default: 70%) | [optional] 

### Return type

[**TinVerificationComprehensiveCheck200Response**](TinVerificationComprehensiveCheck200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tinVerificationNameLookup

> TinVerificationNameLookup200Response tinVerificationNameLookup(tin)

EIN Name Lookup with TIN number

Performs an EIN name match using provided TIN Number

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1TinVerificationApi();
let tin = "tin_example"; // String | Nine letter TIN number with or without hyphens
apiInstance.tinVerificationNameLookup(tin, (error, data, response) => {
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
 **tin** | **String**| Nine letter TIN number with or without hyphens | 

### Return type

[**TinVerificationNameLookup200Response**](TinVerificationNameLookup200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

