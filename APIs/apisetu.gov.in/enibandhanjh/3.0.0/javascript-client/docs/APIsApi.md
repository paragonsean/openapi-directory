# RevenueRegistrationLandReformsDepartmentJharkhand.APIsApi

All URIs are relative to *https://apisetu.gov.in/enibandhanjh/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rdcer**](APIsApi.md#rdcer) | **POST** /rdcer/certificate | Copy of Registered Deed
[**regrii**](APIsApi.md#regrii) | **POST** /regrii/certificate | ROR Register 2
[**rmcer**](APIsApi.md#rmcer) | **POST** /rmcer/certificate | Marriage Certificate



## rdcer

> rdcer(opts)

Copy of Registered Deed

API to verify Copy of Registered Deed.

### Example

```javascript
import RevenueRegistrationLandReformsDepartmentJharkhand from 'revenue_registration__land_reforms_department_jharkhand';
let defaultClient = RevenueRegistrationLandReformsDepartmentJharkhand.ApiClient.instance;
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

let apiInstance = new RevenueRegistrationLandReformsDepartmentJharkhand.APIsApi();
let opts = {
  'rdcerRequest': new RevenueRegistrationLandReformsDepartmentJharkhand.RdcerRequest() // RdcerRequest | Request format
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


## regrii

> regrii(opts)

ROR Register 2

API to verify ROR Register 2.

### Example

```javascript
import RevenueRegistrationLandReformsDepartmentJharkhand from 'revenue_registration__land_reforms_department_jharkhand';
let defaultClient = RevenueRegistrationLandReformsDepartmentJharkhand.ApiClient.instance;
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

let apiInstance = new RevenueRegistrationLandReformsDepartmentJharkhand.APIsApi();
let opts = {
  'regriiRequest': new RevenueRegistrationLandReformsDepartmentJharkhand.RegriiRequest() // RegriiRequest | Request format
};
apiInstance.regrii(opts, (error, data, response) => {
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
 **regriiRequest** | [**RegriiRequest**](RegriiRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## rmcer

> rmcer(opts)

Marriage Certificate

API to verify Marriage Certificate.

### Example

```javascript
import RevenueRegistrationLandReformsDepartmentJharkhand from 'revenue_registration__land_reforms_department_jharkhand';
let defaultClient = RevenueRegistrationLandReformsDepartmentJharkhand.ApiClient.instance;
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

let apiInstance = new RevenueRegistrationLandReformsDepartmentJharkhand.APIsApi();
let opts = {
  'regriiRequest': new RevenueRegistrationLandReformsDepartmentJharkhand.RegriiRequest() // RegriiRequest | Request format
};
apiInstance.rmcer(opts, (error, data, response) => {
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
 **regriiRequest** | [**RegriiRequest**](RegriiRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

