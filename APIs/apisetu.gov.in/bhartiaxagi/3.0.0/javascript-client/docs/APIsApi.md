# BhartiAxaGeneralInsuranceCompanyLtd.APIsApi

All URIs are relative to *https://apisetu.gov.in/bhartiaxagi/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cripc**](APIsApi.md#cripc) | **POST** /cripc/certificate | Insurance Policy - Car
[**cvipc**](APIsApi.md#cvipc) | **POST** /cvipc/certificate | Insurance Policy - Commercial Vehicle
[**hlipc**](APIsApi.md#hlipc) | **POST** /hlipc/certificate | Insurance Policy - Health
[**tripc**](APIsApi.md#tripc) | **POST** /tripc/certificate | Insurance Policy - Travel
[**twipc**](APIsApi.md#twipc) | **POST** /twipc/certificate | Insurance Policy - Two Wheeler



## cripc

> cripc(opts)

Insurance Policy - Car

API to verify Insurance Policy - Car.

### Example

```javascript
import BhartiAxaGeneralInsuranceCompanyLtd from 'bharti_axa_general_insurance_company_ltd_';
let defaultClient = BhartiAxaGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new BhartiAxaGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new BhartiAxaGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
};
apiInstance.cripc(opts, (error, data, response) => {
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
 **cripcRequest** | [**CripcRequest**](CripcRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## cvipc

> cvipc(opts)

Insurance Policy - Commercial Vehicle

API to verify Insurance Policy - Commercial Vehicle.

### Example

```javascript
import BhartiAxaGeneralInsuranceCompanyLtd from 'bharti_axa_general_insurance_company_ltd_';
let defaultClient = BhartiAxaGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new BhartiAxaGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new BhartiAxaGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
};
apiInstance.cvipc(opts, (error, data, response) => {
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
 **cripcRequest** | [**CripcRequest**](CripcRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## hlipc

> hlipc(opts)

Insurance Policy - Health

API to verify Insurance Policy - Health.

### Example

```javascript
import BhartiAxaGeneralInsuranceCompanyLtd from 'bharti_axa_general_insurance_company_ltd_';
let defaultClient = BhartiAxaGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new BhartiAxaGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new BhartiAxaGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
};
apiInstance.hlipc(opts, (error, data, response) => {
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
 **cripcRequest** | [**CripcRequest**](CripcRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## tripc

> tripc(opts)

Insurance Policy - Travel

API to verify Insurance Policy - Travel.

### Example

```javascript
import BhartiAxaGeneralInsuranceCompanyLtd from 'bharti_axa_general_insurance_company_ltd_';
let defaultClient = BhartiAxaGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new BhartiAxaGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new BhartiAxaGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
};
apiInstance.tripc(opts, (error, data, response) => {
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
 **cripcRequest** | [**CripcRequest**](CripcRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## twipc

> twipc(opts)

Insurance Policy - Two Wheeler

API to verify Insurance Policy - Two Wheeler.

### Example

```javascript
import BhartiAxaGeneralInsuranceCompanyLtd from 'bharti_axa_general_insurance_company_ltd_';
let defaultClient = BhartiAxaGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new BhartiAxaGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new BhartiAxaGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
};
apiInstance.twipc(opts, (error, data, response) => {
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
 **cripcRequest** | [**CripcRequest**](CripcRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

