# KotakMahindraGeneralInsuranceCompanyLtd.APIsApi

All URIs are relative to *https://apisetu.gov.in/kotakgeneralinsurance/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cripc**](APIsApi.md#cripc) | **POST** /cripc/certificate | Insurance Policy - Car
[**cvipc**](APIsApi.md#cvipc) | **POST** /cvipc/certificate | Insurance Policy - Commercial Vehicle
[**gicer**](APIsApi.md#gicer) | **POST** /gicer/certificate | Insurance Policy - Group
[**hlipc**](APIsApi.md#hlipc) | **POST** /hlipc/certificate | Insurance Policy - Health
[**hmipc**](APIsApi.md#hmipc) | **POST** /hmipc/certificate | Insurance Policy - Home
[**twipc**](APIsApi.md#twipc) | **POST** /twipc/certificate | Insurance Policy - Two Wheeler



## cripc

> cripc(opts)

Insurance Policy - Car

API to verify Insurance Policy - Car.

### Example

```javascript
import KotakMahindraGeneralInsuranceCompanyLtd from 'kotak_mahindra_general_insurance_company_ltd_';
let defaultClient = KotakMahindraGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new KotakMahindraGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new KotakMahindraGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
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
import KotakMahindraGeneralInsuranceCompanyLtd from 'kotak_mahindra_general_insurance_company_ltd_';
let defaultClient = KotakMahindraGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new KotakMahindraGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new KotakMahindraGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
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


## gicer

> gicer(opts)

Insurance Policy - Group

API to verify Insurance Policy - Group.

### Example

```javascript
import KotakMahindraGeneralInsuranceCompanyLtd from 'kotak_mahindra_general_insurance_company_ltd_';
let defaultClient = KotakMahindraGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new KotakMahindraGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new KotakMahindraGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
};
apiInstance.gicer(opts, (error, data, response) => {
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
import KotakMahindraGeneralInsuranceCompanyLtd from 'kotak_mahindra_general_insurance_company_ltd_';
let defaultClient = KotakMahindraGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new KotakMahindraGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new KotakMahindraGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
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


## hmipc

> hmipc(opts)

Insurance Policy - Home

API to verify Insurance Policy - Home.

### Example

```javascript
import KotakMahindraGeneralInsuranceCompanyLtd from 'kotak_mahindra_general_insurance_company_ltd_';
let defaultClient = KotakMahindraGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new KotakMahindraGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new KotakMahindraGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
};
apiInstance.hmipc(opts, (error, data, response) => {
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
import KotakMahindraGeneralInsuranceCompanyLtd from 'kotak_mahindra_general_insurance_company_ltd_';
let defaultClient = KotakMahindraGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new KotakMahindraGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'cripcRequest': new KotakMahindraGeneralInsuranceCompanyLtd.CripcRequest() // CripcRequest | Request format
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

