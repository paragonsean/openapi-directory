# GeneralAdministrationDepartmentBihar.APIsApi

All URIs are relative to *https://apisetu.gov.in/gadbih/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ctcer**](APIsApi.md#ctcer) | **POST** /ctcer/certificate | Caste Certificate
[**ewcer**](APIsApi.md#ewcer) | **POST** /ewcer/certificate | Economically Weaker Section Certificate
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate
[**rscer**](APIsApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate



## ctcer

> ctcer(opts)

Caste Certificate

API to verify Caste Certificate.

### Example

```javascript
import GeneralAdministrationDepartmentBihar from 'general_administration_department_bihar';
let defaultClient = GeneralAdministrationDepartmentBihar.ApiClient.instance;
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

let apiInstance = new GeneralAdministrationDepartmentBihar.APIsApi();
let opts = {
  'ctcerRequest': new GeneralAdministrationDepartmentBihar.CtcerRequest() // CtcerRequest | Request format
};
apiInstance.ctcer(opts, (error, data, response) => {
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
 **ctcerRequest** | [**CtcerRequest**](CtcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## ewcer

> ewcer(opts)

Economically Weaker Section Certificate

API to verify Economically Weaker Section Certificate.

### Example

```javascript
import GeneralAdministrationDepartmentBihar from 'general_administration_department_bihar';
let defaultClient = GeneralAdministrationDepartmentBihar.ApiClient.instance;
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

let apiInstance = new GeneralAdministrationDepartmentBihar.APIsApi();
let opts = {
  'ctcerRequest': new GeneralAdministrationDepartmentBihar.CtcerRequest() // CtcerRequest | Request format
};
apiInstance.ewcer(opts, (error, data, response) => {
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
 **ctcerRequest** | [**CtcerRequest**](CtcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## incer

> incer(opts)

Income Certificate

API to verify Income Certificate.

### Example

```javascript
import GeneralAdministrationDepartmentBihar from 'general_administration_department_bihar';
let defaultClient = GeneralAdministrationDepartmentBihar.ApiClient.instance;
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

let apiInstance = new GeneralAdministrationDepartmentBihar.APIsApi();
let opts = {
  'ctcerRequest': new GeneralAdministrationDepartmentBihar.CtcerRequest() // CtcerRequest | Request format
};
apiInstance.incer(opts, (error, data, response) => {
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
 **ctcerRequest** | [**CtcerRequest**](CtcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## rscer

> rscer(opts)

Residence Certificate

API to verify Residence Certificate.

### Example

```javascript
import GeneralAdministrationDepartmentBihar from 'general_administration_department_bihar';
let defaultClient = GeneralAdministrationDepartmentBihar.ApiClient.instance;
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

let apiInstance = new GeneralAdministrationDepartmentBihar.APIsApi();
let opts = {
  'ctcerRequest': new GeneralAdministrationDepartmentBihar.CtcerRequest() // CtcerRequest | Request format
};
apiInstance.rscer(opts, (error, data, response) => {
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
 **ctcerRequest** | [**CtcerRequest**](CtcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

