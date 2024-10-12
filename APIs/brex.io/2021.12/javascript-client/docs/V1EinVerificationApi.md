# KycApiDocumentation.V1EinVerificationApi

All URIs are relative to *https://api.kompany.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**einVerificationBasic**](V1EinVerificationApi.md#einVerificationBasic) | **GET** /api/v1/ein-verification/basic-check | Verifies an EIN number
[**einVerificationComprehensive**](V1EinVerificationApi.md#einVerificationComprehensive) | **GET** /api/v1/ein-verification/comprehensive-check | Verifies EIN number and retrieves company data
[**einVerificationLookup**](V1EinVerificationApi.md#einVerificationLookup) | **GET** /api/v1/ein-verification/lookup | Retrieves a list of EIN numbers



## einVerificationBasic

> EinVerificationBasic200Response einVerificationBasic(ein)

Verifies an EIN number

Performs a basic verification check of a given EIN tax number.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1EinVerificationApi();
let ein = "ein_example"; // String | Nine letter EIN number with or without hyphens
apiInstance.einVerificationBasic(ein, (error, data, response) => {
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
 **ein** | **String**| Nine letter EIN number with or without hyphens | 

### Return type

[**EinVerificationBasic200Response**](EinVerificationBasic200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## einVerificationComprehensive

> EinVerificationComprehensive200Response einVerificationComprehensive(ein)

Verifies EIN number and retrieves company data

Comprehensive verification of a given EIN number. Additionally to the basic verification it will lookup company details

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1EinVerificationApi();
let ein = "ein_example"; // String | Nine letter EIN number with or without hyphens
apiInstance.einVerificationComprehensive(ein, (error, data, response) => {
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
 **ein** | **String**| Nine letter EIN number with or without hyphens | 

### Return type

[**EinVerificationComprehensive200Response**](EinVerificationComprehensive200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## einVerificationLookup

> EinVerificationLookup200Response einVerificationLookup(name, opts)

Retrieves a list of EIN numbers

Lookup EIN number for a company by its company name

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1EinVerificationApi();
let name = "name_example"; // String | Business name of the company
let opts = {
  'state': "state_example", // String | Optional state parameter to improve results. (Two letter code for example CA or US-CA for California)
  'zip': "zip_example", // String | Optional zip code parameter to improve results. (Zip is preferred over state)
  'tight': true // Boolean | Optional parameter to do tight matching. (Only the best match will be returned rather then the top 5)
};
apiInstance.einVerificationLookup(name, opts, (error, data, response) => {
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
 **name** | **String**| Business name of the company | 
 **state** | **String**| Optional state parameter to improve results. (Two letter code for example CA or US-CA for California) | [optional] 
 **zip** | **String**| Optional zip code parameter to improve results. (Zip is preferred over state) | [optional] 
 **tight** | **Boolean**| Optional parameter to do tight matching. (Only the best match will be returned rather then the top 5) | [optional] 

### Return type

[**EinVerificationLookup200Response**](EinVerificationLookup200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

