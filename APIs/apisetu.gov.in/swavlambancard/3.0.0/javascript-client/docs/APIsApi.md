# DepartmentOfEmpowermentOfPersonsWithDisabilities.APIsApi

All URIs are relative to *https://apisetu.gov.in/swavlambancard/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dpicr**](APIsApi.md#dpicr) | **POST** /dpicr/certificate | Disabled Person Identity Card/ Certificate
[**govid**](APIsApi.md#govid) | **POST** /govid/certificate | ID Card



## dpicr

> dpicr(opts)

Disabled Person Identity Card/ Certificate

API to verify Disabled Person Identity Card/ Certificate.

### Example

```javascript
import DepartmentOfEmpowermentOfPersonsWithDisabilities from 'department_of_empowerment_of_persons_with_disabilities';
let defaultClient = DepartmentOfEmpowermentOfPersonsWithDisabilities.ApiClient.instance;
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

let apiInstance = new DepartmentOfEmpowermentOfPersonsWithDisabilities.APIsApi();
let opts = {
  'dpicrRequest': new DepartmentOfEmpowermentOfPersonsWithDisabilities.DpicrRequest() // DpicrRequest | Request format
};
apiInstance.dpicr(opts, (error, data, response) => {
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
 **dpicrRequest** | [**DpicrRequest**](DpicrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## govid

> govid(opts)

ID Card

API to verify ID Card.

### Example

```javascript
import DepartmentOfEmpowermentOfPersonsWithDisabilities from 'department_of_empowerment_of_persons_with_disabilities';
let defaultClient = DepartmentOfEmpowermentOfPersonsWithDisabilities.ApiClient.instance;
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

let apiInstance = new DepartmentOfEmpowermentOfPersonsWithDisabilities.APIsApi();
let opts = {
  'govidRequest': new DepartmentOfEmpowermentOfPersonsWithDisabilities.GovidRequest() // GovidRequest | Request format
};
apiInstance.govid(opts, (error, data, response) => {
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
 **govidRequest** | [**GovidRequest**](GovidRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json

