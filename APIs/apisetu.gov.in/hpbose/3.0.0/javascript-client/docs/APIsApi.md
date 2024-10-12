# HimachalPradeshBoardOfSchoolEducationHimachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/hpbose/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hvcer**](APIsApi.md#hvcer) | **POST** /hvcer/certificate | Class XII Provisional Certificate
[**svcer**](APIsApi.md#svcer) | **POST** /svcer/certificate | Class X Provisional Certificate



## hvcer

> hvcer(opts)

Class XII Provisional Certificate

API to verify Class XII Provisional Certificate.

### Example

```javascript
import HimachalPradeshBoardOfSchoolEducationHimachalPradesh from 'himachal_pradesh_board_of_school_education_himachal_pradesh';
let defaultClient = HimachalPradeshBoardOfSchoolEducationHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshBoardOfSchoolEducationHimachalPradesh.APIsApi();
let opts = {
  'hvcerRequest': new HimachalPradeshBoardOfSchoolEducationHimachalPradesh.HvcerRequest() // HvcerRequest | Request format
};
apiInstance.hvcer(opts, (error, data, response) => {
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
 **hvcerRequest** | [**HvcerRequest**](HvcerRequest.md)| Request format | [optional] 

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
import HimachalPradeshBoardOfSchoolEducationHimachalPradesh from 'himachal_pradesh_board_of_school_education_himachal_pradesh';
let defaultClient = HimachalPradeshBoardOfSchoolEducationHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshBoardOfSchoolEducationHimachalPradesh.APIsApi();
let opts = {
  'hvcerRequest': new HimachalPradeshBoardOfSchoolEducationHimachalPradesh.HvcerRequest() // HvcerRequest | Request format
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
 **hvcerRequest** | [**HvcerRequest**](HvcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

