# PunjabSchoolEducationBoardPunjab.APIsApi

All URIs are relative to *https://apisetu.gov.in/pseb/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cemst**](APIsApi.md#cemst) | **POST** /cemst/certificate | Class VIII Marksheet
[**cfmst**](APIsApi.md#cfmst) | **POST** /cfmst/certificate | Class V Marksheet
[**hscer**](APIsApi.md#hscer) | **POST** /hscer/certificate | Class XII Marksheet
[**micer**](APIsApi.md#micer) | **POST** /micer/certificate | Migration Certificate
[**sscer**](APIsApi.md#sscer) | **POST** /sscer/certificate | Class X Marksheet



## cemst

> cemst(opts)

Class VIII Marksheet

API to verify Class VIII Marksheet.

### Example

```javascript
import PunjabSchoolEducationBoardPunjab from 'punjab_school_education_board_punjab';
let defaultClient = PunjabSchoolEducationBoardPunjab.ApiClient.instance;
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

let apiInstance = new PunjabSchoolEducationBoardPunjab.APIsApi();
let opts = {
  'cemstRequest': new PunjabSchoolEducationBoardPunjab.CemstRequest() // CemstRequest | Request format
};
apiInstance.cemst(opts, (error, data, response) => {
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
 **cemstRequest** | [**CemstRequest**](CemstRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## cfmst

> cfmst(opts)

Class V Marksheet

API to verify Class V Marksheet.

### Example

```javascript
import PunjabSchoolEducationBoardPunjab from 'punjab_school_education_board_punjab';
let defaultClient = PunjabSchoolEducationBoardPunjab.ApiClient.instance;
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

let apiInstance = new PunjabSchoolEducationBoardPunjab.APIsApi();
let opts = {
  'cemstRequest': new PunjabSchoolEducationBoardPunjab.CemstRequest() // CemstRequest | Request format
};
apiInstance.cfmst(opts, (error, data, response) => {
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
 **cemstRequest** | [**CemstRequest**](CemstRequest.md)| Request format | [optional] 

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
import PunjabSchoolEducationBoardPunjab from 'punjab_school_education_board_punjab';
let defaultClient = PunjabSchoolEducationBoardPunjab.ApiClient.instance;
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

let apiInstance = new PunjabSchoolEducationBoardPunjab.APIsApi();
let opts = {
  'cemstRequest': new PunjabSchoolEducationBoardPunjab.CemstRequest() // CemstRequest | Request format
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
 **cemstRequest** | [**CemstRequest**](CemstRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## micer

> micer(opts)

Migration Certificate

API to verify Migration Certificate.

### Example

```javascript
import PunjabSchoolEducationBoardPunjab from 'punjab_school_education_board_punjab';
let defaultClient = PunjabSchoolEducationBoardPunjab.ApiClient.instance;
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

let apiInstance = new PunjabSchoolEducationBoardPunjab.APIsApi();
let opts = {
  'cemstRequest': new PunjabSchoolEducationBoardPunjab.CemstRequest() // CemstRequest | Request format
};
apiInstance.micer(opts, (error, data, response) => {
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
 **cemstRequest** | [**CemstRequest**](CemstRequest.md)| Request format | [optional] 

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
import PunjabSchoolEducationBoardPunjab from 'punjab_school_education_board_punjab';
let defaultClient = PunjabSchoolEducationBoardPunjab.ApiClient.instance;
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

let apiInstance = new PunjabSchoolEducationBoardPunjab.APIsApi();
let opts = {
  'cemstRequest': new PunjabSchoolEducationBoardPunjab.CemstRequest() // CemstRequest | Request format
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
 **cemstRequest** | [**CemstRequest**](CemstRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

