# BiharStateBoardOfSchoolExaminationBihar.APIsApi

All URIs are relative to *https://apisetu.gov.in/biharboard/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sscer**](APIsApi.md#sscer) | **POST** /sscer/certificate | Class X Marksheet
[**svcer**](APIsApi.md#svcer) | **POST** /svcer/certificate | Class X Provisional Certificate



## sscer

> sscer(opts)

Class X Marksheet

API to verify Class X Marksheet.

### Example

```javascript
import BiharStateBoardOfSchoolExaminationBihar from 'bihar_state_board_of_school_examination_bihar';
let defaultClient = BiharStateBoardOfSchoolExaminationBihar.ApiClient.instance;
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

let apiInstance = new BiharStateBoardOfSchoolExaminationBihar.APIsApi();
let opts = {
  'sscerRequest': new BiharStateBoardOfSchoolExaminationBihar.SscerRequest() // SscerRequest | Request format
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
 **sscerRequest** | [**SscerRequest**](SscerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## svcer

> svcer(opts)

Class X Provisional Certificate

API to verify Class X Provisional Certificate.

### Example

```javascript
import BiharStateBoardOfSchoolExaminationBihar from 'bihar_state_board_of_school_examination_bihar';
let defaultClient = BiharStateBoardOfSchoolExaminationBihar.ApiClient.instance;
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

let apiInstance = new BiharStateBoardOfSchoolExaminationBihar.APIsApi();
let opts = {
  'sscerRequest': new BiharStateBoardOfSchoolExaminationBihar.SscerRequest() // SscerRequest | Request format
};
apiInstance.svcer(opts, (error, data, response) => {
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
 **sscerRequest** | [**SscerRequest**](SscerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

