# TamilNaduStateBoardTamilNaduDirectorateOfGovernmentExaminationsTamilNadu.APIsApi

All URIs are relative to *https://apisetu.gov.in/dgecerttn/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hscer**](APIsApi.md#hscer) | **POST** /hscer/certificate | Class XII Marksheet
[**sscer**](APIsApi.md#sscer) | **POST** /sscer/certificate | Class X Marksheet



## hscer

> hscer(opts)

Class XII Marksheet

API to verify Class XII Marksheet.

### Example

```javascript
import TamilNaduStateBoardTamilNaduDirectorateOfGovernmentExaminationsTamilNadu from 'tamil_nadu_state_board__tamil_nadu_directorate_of_government_examinations_tamil_nadu';
let defaultClient = TamilNaduStateBoardTamilNaduDirectorateOfGovernmentExaminationsTamilNadu.ApiClient.instance;
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

let apiInstance = new TamilNaduStateBoardTamilNaduDirectorateOfGovernmentExaminationsTamilNadu.APIsApi();
let opts = {
  'hscerRequest': new TamilNaduStateBoardTamilNaduDirectorateOfGovernmentExaminationsTamilNadu.HscerRequest() // HscerRequest | Request format
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
 **hscerRequest** | [**HscerRequest**](HscerRequest.md)| Request format | [optional] 

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
import TamilNaduStateBoardTamilNaduDirectorateOfGovernmentExaminationsTamilNadu from 'tamil_nadu_state_board__tamil_nadu_directorate_of_government_examinations_tamil_nadu';
let defaultClient = TamilNaduStateBoardTamilNaduDirectorateOfGovernmentExaminationsTamilNadu.ApiClient.instance;
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

let apiInstance = new TamilNaduStateBoardTamilNaduDirectorateOfGovernmentExaminationsTamilNadu.APIsApi();
let opts = {
  'hscerRequest': new TamilNaduStateBoardTamilNaduDirectorateOfGovernmentExaminationsTamilNadu.HscerRequest() // HscerRequest | Request format
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
 **hscerRequest** | [**HscerRequest**](HscerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

