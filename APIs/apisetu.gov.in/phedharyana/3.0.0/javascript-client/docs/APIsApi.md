# PublicHealthEngineeringDepartmentHaryanaHaryana.APIsApi

All URIs are relative to *https://apisetu.gov.in/phedharyana/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**etcer**](APIsApi.md#etcer) | **POST** /etcer/certificate | Enlistment Certificate
[**govid**](APIsApi.md#govid) | **POST** /govid/certificate | ID Card
[**sicer**](APIsApi.md#sicer) | **POST** /sicer/certificate | Sanction Letter/ Certificate



## etcer

> etcer(opts)

Enlistment Certificate

API to verify Enlistment Certificate.

### Example

```javascript
import PublicHealthEngineeringDepartmentHaryanaHaryana from 'public_health_engineering_department_haryana_haryana';
let defaultClient = PublicHealthEngineeringDepartmentHaryanaHaryana.ApiClient.instance;
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

let apiInstance = new PublicHealthEngineeringDepartmentHaryanaHaryana.APIsApi();
let opts = {
  'etcerRequest': new PublicHealthEngineeringDepartmentHaryanaHaryana.EtcerRequest() // EtcerRequest | Request format
};
apiInstance.etcer(opts, (error, data, response) => {
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
 **etcerRequest** | [**EtcerRequest**](EtcerRequest.md)| Request format | [optional] 

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
import PublicHealthEngineeringDepartmentHaryanaHaryana from 'public_health_engineering_department_haryana_haryana';
let defaultClient = PublicHealthEngineeringDepartmentHaryanaHaryana.ApiClient.instance;
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

let apiInstance = new PublicHealthEngineeringDepartmentHaryanaHaryana.APIsApi();
let opts = {
  'govidRequest': new PublicHealthEngineeringDepartmentHaryanaHaryana.GovidRequest() // GovidRequest | Request format
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
- **Accept**: application/pdf, application/json


## sicer

> sicer(opts)

Sanction Letter/ Certificate

API to verify Sanction Letter/ Certificate.

### Example

```javascript
import PublicHealthEngineeringDepartmentHaryanaHaryana from 'public_health_engineering_department_haryana_haryana';
let defaultClient = PublicHealthEngineeringDepartmentHaryanaHaryana.ApiClient.instance;
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

let apiInstance = new PublicHealthEngineeringDepartmentHaryanaHaryana.APIsApi();
let opts = {
  'sicerRequest': new PublicHealthEngineeringDepartmentHaryanaHaryana.SicerRequest() // SicerRequest | Request format
};
apiInstance.sicer(opts, (error, data, response) => {
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
 **sicerRequest** | [**SicerRequest**](SicerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

