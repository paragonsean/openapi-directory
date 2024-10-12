# MizoramStateBoardOfSchoolEducation.APIsApi

All URIs are relative to *https://apisetu.gov.in/mbse/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hpcer**](APIsApi.md#hpcer) | **POST** /hpcer/certificate | Class XII Passing Certificate
[**hscer**](APIsApi.md#hscer) | **POST** /hscer/certificate | Class XII Marksheet
[**spcer**](APIsApi.md#spcer) | **POST** /spcer/certificate | Class X Passing Certificate
[**sscer**](APIsApi.md#sscer) | **POST** /sscer/certificate | Class X Marksheet



## hpcer

> hpcer(opts)

Class XII Passing Certificate

API to verify Class XII Passing Certificate.

### Example

```javascript
import MizoramStateBoardOfSchoolEducation from 'mizoram_state_board_of_school_education';
let defaultClient = MizoramStateBoardOfSchoolEducation.ApiClient.instance;
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

let apiInstance = new MizoramStateBoardOfSchoolEducation.APIsApi();
let opts = {
  'hpcerRequest': new MizoramStateBoardOfSchoolEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.hpcer(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## hscer

> hscer(opts)

Class XII Marksheet

API to verify Class XII Marksheet.

### Example

```javascript
import MizoramStateBoardOfSchoolEducation from 'mizoram_state_board_of_school_education';
let defaultClient = MizoramStateBoardOfSchoolEducation.ApiClient.instance;
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

let apiInstance = new MizoramStateBoardOfSchoolEducation.APIsApi();
let opts = {
  'hpcerRequest': new MizoramStateBoardOfSchoolEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.hscer(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## spcer

> spcer(opts)

Class X Passing Certificate

API to verify Class X Passing Certificate.

### Example

```javascript
import MizoramStateBoardOfSchoolEducation from 'mizoram_state_board_of_school_education';
let defaultClient = MizoramStateBoardOfSchoolEducation.ApiClient.instance;
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

let apiInstance = new MizoramStateBoardOfSchoolEducation.APIsApi();
let opts = {
  'hpcerRequest': new MizoramStateBoardOfSchoolEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.spcer(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## sscer

> sscer(opts)

Class X Marksheet

API to verify Class X Marksheet.

### Example

```javascript
import MizoramStateBoardOfSchoolEducation from 'mizoram_state_board_of_school_education';
let defaultClient = MizoramStateBoardOfSchoolEducation.ApiClient.instance;
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

let apiInstance = new MizoramStateBoardOfSchoolEducation.APIsApi();
let opts = {
  'hpcerRequest': new MizoramStateBoardOfSchoolEducation.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.sscer(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

