# GoaWaterResourcesDepartmentGoa.APIsApi

All URIs are relative to *https://apisetu.gov.in/goawrd/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ercer**](APIsApi.md#ercer) | **POST** /ercer/certificate | Registration Certificate of Establishment Employing Contract Labour
[**pfdaw**](APIsApi.md#pfdaw) | **POST** /pfdaw/certificate | Permission/ Certificate for Well
[**tpcer**](APIsApi.md#tpcer) | **POST** /tpcer/certificate | Permission/ Certificate for Transportation (Petroleum Products, Water etc.)



## ercer

> ercer(opts)

Registration Certificate of Establishment Employing Contract Labour

API to verify Registration Certificate of Establishment Employing Contract Labour.

### Example

```javascript
import GoaWaterResourcesDepartmentGoa from 'goa_water_resources_department_goa';
let defaultClient = GoaWaterResourcesDepartmentGoa.ApiClient.instance;
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

let apiInstance = new GoaWaterResourcesDepartmentGoa.APIsApi();
let opts = {
  'ercerRequest': new GoaWaterResourcesDepartmentGoa.ErcerRequest() // ErcerRequest | Request format
};
apiInstance.ercer(opts, (error, data, response) => {
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
 **ercerRequest** | [**ErcerRequest**](ErcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## pfdaw

> pfdaw(opts)

Permission/ Certificate for Well

API to verify Permission/ Certificate for Well.

### Example

```javascript
import GoaWaterResourcesDepartmentGoa from 'goa_water_resources_department_goa';
let defaultClient = GoaWaterResourcesDepartmentGoa.ApiClient.instance;
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

let apiInstance = new GoaWaterResourcesDepartmentGoa.APIsApi();
let opts = {
  'ercerRequest': new GoaWaterResourcesDepartmentGoa.ErcerRequest() // ErcerRequest | Request format
};
apiInstance.pfdaw(opts, (error, data, response) => {
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
 **ercerRequest** | [**ErcerRequest**](ErcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## tpcer

> tpcer(opts)

Permission/ Certificate for Transportation (Petroleum Products, Water etc.)

API to verify Permission/ Certificate for Transportation (Petroleum Products, Water etc.).

### Example

```javascript
import GoaWaterResourcesDepartmentGoa from 'goa_water_resources_department_goa';
let defaultClient = GoaWaterResourcesDepartmentGoa.ApiClient.instance;
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

let apiInstance = new GoaWaterResourcesDepartmentGoa.APIsApi();
let opts = {
  'ercerRequest': new GoaWaterResourcesDepartmentGoa.ErcerRequest() // ErcerRequest | Request format
};
apiInstance.tpcer(opts, (error, data, response) => {
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
 **ercerRequest** | [**ErcerRequest**](ErcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

