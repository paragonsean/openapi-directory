# RevenueDepartmentOdisha.APIsApi

All URIs are relative to *https://apisetu.gov.in/revenueodisha/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rdcer**](APIsApi.md#rdcer) | **POST** /rdcer/certificate | Copy of Registered Deed
[**ror1b**](APIsApi.md#ror1b) | **POST** /ror1b/certificate | Records of Rights



## rdcer

> rdcer(opts)

Copy of Registered Deed

API to verify Copy of Registered Deed.

### Example

```javascript
import RevenueDepartmentOdisha from 'revenue_department_odisha';
let defaultClient = RevenueDepartmentOdisha.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RevenueDepartmentOdisha.APIsApi();
let opts = {
  'rdcerRequest': new RevenueDepartmentOdisha.RdcerRequest() // RdcerRequest | Request format
};
apiInstance.rdcer(opts, (error, data, response) => {
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
 **rdcerRequest** | [**RdcerRequest**](RdcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ror1b

> ror1b(opts)

Records of Rights

API to verify Records of Rights.

### Example

```javascript
import RevenueDepartmentOdisha from 'revenue_department_odisha';
let defaultClient = RevenueDepartmentOdisha.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RevenueDepartmentOdisha.APIsApi();
let opts = {
  'ror1bRequest': new RevenueDepartmentOdisha.Ror1bRequest() // Ror1bRequest | Request format
};
apiInstance.ror1b(opts, (error, data, response) => {
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
 **ror1bRequest** | [**Ror1bRequest**](Ror1bRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

