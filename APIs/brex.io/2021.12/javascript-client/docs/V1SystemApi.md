# KycApiDocumentation.V1SystemApi

All URIs are relative to *https://api.kompany.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthCheck**](V1SystemApi.md#healthCheck) | **GET** /api/v1/system/health | Returns the health information for the official business registers based on usage.
[**systemCountries**](V1SystemApi.md#systemCountries) | **GET** /api/v1/system/countries | Returns a list of countries
[**systemPricelist**](V1SystemApi.md#systemPricelist) | **GET** /api/v1/system/pricelist | Returns a list of products with prices



## healthCheck

> [HealthCheck200ResponseInner] healthCheck()

Returns the health information for the official business registers based on usage.

Returns the health information for the official business registers based on usage.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1SystemApi();
apiInstance.healthCheck((error, data, response) => {
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

[**[HealthCheck200ResponseInner]**](HealthCheck200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## systemCountries

> [SystemCountries200ResponseInner] systemCountries()

Returns a list of countries

Retrieve the list of all currently enabled countries

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1SystemApi();
apiInstance.systemCountries((error, data, response) => {
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

[**[SystemCountries200ResponseInner]**](SystemCountries200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## systemPricelist

> [SystemPricelist200ResponseInner] systemPricelist()

Returns a list of products with prices

Retrieve pricing rules for your subscription plan

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1SystemApi();
apiInstance.systemPricelist((error, data, response) => {
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

[**[SystemPricelist200ResponseInner]**](SystemPricelist200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

