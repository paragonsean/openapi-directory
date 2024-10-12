# EDistrictOdishaOdisha.APIsApi

All URIs are relative to *https://apisetu.gov.in/edistrictodisha/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ctcer**](APIsApi.md#ctcer) | **POST** /ctcer/certificate | Caste Certificate
[**ewcer**](APIsApi.md#ewcer) | **POST** /ewcer/certificate | Economically Weaker Section Certificate
[**lhcer**](APIsApi.md#lhcer) | **POST** /lhcer/certificate | Legal Heir Certificate
[**obcer**](APIsApi.md#obcer) | **POST** /obcer/certificate | OBC Certificate
[**ror1b**](APIsApi.md#ror1b) | **POST** /ror1b/certificate | Records of Rights
[**slcer**](APIsApi.md#slcer) | **POST** /slcer/certificate | Solvency Certificate



## ctcer

> ctcer(opts)

Caste Certificate

API to verify Caste Certificate.

### Example

```javascript
import EDistrictOdishaOdisha from 'e_district_odisha_odisha';
let defaultClient = EDistrictOdishaOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaOdisha.APIsApi();
let opts = {
  'ctcerRequest': new EDistrictOdishaOdisha.CtcerRequest() // CtcerRequest | Request format
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
import EDistrictOdishaOdisha from 'e_district_odisha_odisha';
let defaultClient = EDistrictOdishaOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaOdisha.APIsApi();
let opts = {
  'ctcerRequest': new EDistrictOdishaOdisha.CtcerRequest() // CtcerRequest | Request format
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


## lhcer

> lhcer(opts)

Legal Heir Certificate

API to verify Legal Heir Certificate.

### Example

```javascript
import EDistrictOdishaOdisha from 'e_district_odisha_odisha';
let defaultClient = EDistrictOdishaOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaOdisha.APIsApi();
let opts = {
  'ctcerRequest': new EDistrictOdishaOdisha.CtcerRequest() // CtcerRequest | Request format
};
apiInstance.lhcer(opts, (error, data, response) => {
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


## obcer

> obcer(opts)

OBC Certificate

API to verify OBC Certificate.

### Example

```javascript
import EDistrictOdishaOdisha from 'e_district_odisha_odisha';
let defaultClient = EDistrictOdishaOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaOdisha.APIsApi();
let opts = {
  'ctcerRequest': new EDistrictOdishaOdisha.CtcerRequest() // CtcerRequest | Request format
};
apiInstance.obcer(opts, (error, data, response) => {
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


## ror1b

> ror1b(opts)

Records of Rights

API to verify Records of Rights.

### Example

```javascript
import EDistrictOdishaOdisha from 'e_district_odisha_odisha';
let defaultClient = EDistrictOdishaOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaOdisha.APIsApi();
let opts = {
  'ctcerRequest': new EDistrictOdishaOdisha.CtcerRequest() // CtcerRequest | Request format
};
apiInstance.ror1b(opts, (error, data, response) => {
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


## slcer

> slcer(opts)

Solvency Certificate

API to verify Solvency Certificate.

### Example

```javascript
import EDistrictOdishaOdisha from 'e_district_odisha_odisha';
let defaultClient = EDistrictOdishaOdisha.ApiClient.instance;
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

let apiInstance = new EDistrictOdishaOdisha.APIsApi();
let opts = {
  'ctcerRequest': new EDistrictOdishaOdisha.CtcerRequest() // CtcerRequest | Request format
};
apiInstance.slcer(opts, (error, data, response) => {
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

