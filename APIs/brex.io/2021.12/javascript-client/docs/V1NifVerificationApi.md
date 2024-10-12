# KycApiDocumentation.V1NifVerificationApi

All URIs are relative to *https://api.kompany.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nifBasic**](V1NifVerificationApi.md#nifBasic) | **POST** /api/v1/nif-verification/basic-check/{country} | Verifies a NIF number
[**nifComprehensive**](V1NifVerificationApi.md#nifComprehensive) | **POST** /api/v1/nif-verification/comprehensive-check/{country} | Verifies a NIF number and retrieves company data



## nifBasic

> NifBasic200Response nifBasic(country, nifNumber, opts)

Verifies a NIF number

Performs a basic verification check of a given NIF tax number against NIF.com. Optional parameters may be added to improve calculation of confidence score.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1NifVerificationApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let nifNumber = "nifNumber_example"; // String | NIF number to validate
let opts = {
  'companyAddress': "companyAddress_example", // String | company address lines
  'companyName': "companyName_example" // String | Company name
};
apiInstance.nifBasic(country, nifNumber, opts, (error, data, response) => {
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
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **nifNumber** | **String**| NIF number to validate | 
 **companyAddress** | **String**| company address lines | [optional] 
 **companyName** | **String**| Company name | [optional] 

### Return type

[**NifBasic200Response**](NifBasic200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## nifComprehensive

> NifComprehensive200Response nifComprehensive(country, nifNumber, opts)

Verifies a NIF number and retrieves company data

Comprehensive verification of given portuguese NIF number against NIF.com. Optional parameters may help to build a better confidence score. Additional company data will be provided.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1NifVerificationApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let nifNumber = "nifNumber_example"; // String | NIF number to validate
let opts = {
  'companyAddress': "companyAddress_example", // String | company address lines
  'companyName': "companyName_example" // String | Company name
};
apiInstance.nifComprehensive(country, nifNumber, opts, (error, data, response) => {
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
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **nifNumber** | **String**| NIF number to validate | 
 **companyAddress** | **String**| company address lines | [optional] 
 **companyName** | **String**| Company name | [optional] 

### Return type

[**NifComprehensive200Response**](NifComprehensive200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

