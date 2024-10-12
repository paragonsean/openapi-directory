# AckoGeneralInsuranceLimited.APIsApi

All URIs are relative to *https://apisetu.gov.in/acko/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cripc**](APIsApi.md#cripc) | **POST** /cripc/certificate | Insurance Policy - Car
[**hlipc**](APIsApi.md#hlipc) | **POST** /hlipc/certificate | Insurance Policy - Health
[**twipc**](APIsApi.md#twipc) | **POST** /twipc/certificate | Insurance Policy - Two Wheeler



## cripc

> cripc(opts)

Insurance Policy - Car

API to verify Insurance Policy - Car.

### Example

```javascript
import AckoGeneralInsuranceLimited from 'acko_general_insurance_limited';
let defaultClient = AckoGeneralInsuranceLimited.ApiClient.instance;
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

let apiInstance = new AckoGeneralInsuranceLimited.APIsApi();
let opts = {
  'cripcRequest': new AckoGeneralInsuranceLimited.CripcRequest() // CripcRequest | Request format
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


## hlipc

> hlipc(opts)

Insurance Policy - Health

API to verify Insurance Policy - Health.

### Example

```javascript
import AckoGeneralInsuranceLimited from 'acko_general_insurance_limited';
let defaultClient = AckoGeneralInsuranceLimited.ApiClient.instance;
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

let apiInstance = new AckoGeneralInsuranceLimited.APIsApi();
let opts = {
  'cripcRequest': new AckoGeneralInsuranceLimited.CripcRequest() // CripcRequest | Request format
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


## twipc

> twipc(opts)

Insurance Policy - Two Wheeler

API to verify Insurance Policy - Two Wheeler.

### Example

```javascript
import AckoGeneralInsuranceLimited from 'acko_general_insurance_limited';
let defaultClient = AckoGeneralInsuranceLimited.ApiClient.instance;
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

let apiInstance = new AckoGeneralInsuranceLimited.APIsApi();
let opts = {
  'cripcRequest': new AckoGeneralInsuranceLimited.CripcRequest() // CripcRequest | Request format
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

