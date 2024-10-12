# DepartmentOfLegalMetrologyUttarPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/legalmetrologyup/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delcs**](APIsApi.md#delcs) | **POST** /delcs/certificate | Dealer License
[**malcs**](APIsApi.md#malcs) | **POST** /malcs/certificate | Manufacturer License
[**palcs**](APIsApi.md#palcs) | **POST** /palcs/certificate | Packers License
[**relcs**](APIsApi.md#relcs) | **POST** /relcs/certificate | Repairer License



## delcs

> delcs(opts)

Dealer License

API to verify Dealer License.

### Example

```javascript
import DepartmentOfLegalMetrologyUttarPradesh from 'department_of_legal_metrology_uttar_pradesh';
let defaultClient = DepartmentOfLegalMetrologyUttarPradesh.ApiClient.instance;
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

let apiInstance = new DepartmentOfLegalMetrologyUttarPradesh.APIsApi();
let opts = {
  'delcsRequest': new DepartmentOfLegalMetrologyUttarPradesh.DelcsRequest() // DelcsRequest | Request format
};
apiInstance.delcs(opts, (error, data, response) => {
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
 **delcsRequest** | [**DelcsRequest**](DelcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## malcs

> malcs(opts)

Manufacturer License

API to verify Manufacturer License.

### Example

```javascript
import DepartmentOfLegalMetrologyUttarPradesh from 'department_of_legal_metrology_uttar_pradesh';
let defaultClient = DepartmentOfLegalMetrologyUttarPradesh.ApiClient.instance;
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

let apiInstance = new DepartmentOfLegalMetrologyUttarPradesh.APIsApi();
let opts = {
  'delcsRequest': new DepartmentOfLegalMetrologyUttarPradesh.DelcsRequest() // DelcsRequest | Request format
};
apiInstance.malcs(opts, (error, data, response) => {
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
 **delcsRequest** | [**DelcsRequest**](DelcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## palcs

> palcs(opts)

Packers License

API to verify Packers License.

### Example

```javascript
import DepartmentOfLegalMetrologyUttarPradesh from 'department_of_legal_metrology_uttar_pradesh';
let defaultClient = DepartmentOfLegalMetrologyUttarPradesh.ApiClient.instance;
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

let apiInstance = new DepartmentOfLegalMetrologyUttarPradesh.APIsApi();
let opts = {
  'delcsRequest': new DepartmentOfLegalMetrologyUttarPradesh.DelcsRequest() // DelcsRequest | Request format
};
apiInstance.palcs(opts, (error, data, response) => {
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
 **delcsRequest** | [**DelcsRequest**](DelcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## relcs

> relcs(opts)

Repairer License

API to verify Repairer License.

### Example

```javascript
import DepartmentOfLegalMetrologyUttarPradesh from 'department_of_legal_metrology_uttar_pradesh';
let defaultClient = DepartmentOfLegalMetrologyUttarPradesh.ApiClient.instance;
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

let apiInstance = new DepartmentOfLegalMetrologyUttarPradesh.APIsApi();
let opts = {
  'delcsRequest': new DepartmentOfLegalMetrologyUttarPradesh.DelcsRequest() // DelcsRequest | Request format
};
apiInstance.relcs(opts, (error, data, response) => {
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
 **delcsRequest** | [**DelcsRequest**](DelcsRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

