# EDistrictUttarPradeshUttarPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/edistrictup/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**btcer**](APIsApi.md#btcer) | **POST** /btcer/certificate | Birth Certificate
[**ctcer**](APIsApi.md#ctcer) | **POST** /ctcer/certificate | Caste Certificate
[**dmcer**](APIsApi.md#dmcer) | **POST** /dmcer/certificate | Domicile Certificate
[**dpicr**](APIsApi.md#dpicr) | **POST** /dpicr/certificate | Disabled Person Identity Card/ Certificate
[**dtcer**](APIsApi.md#dtcer) | **POST** /dtcer/certificate | Death Certificate
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate



## btcer

> btcer(opts)

Birth Certificate

API to verify Birth Certificate.

### Example

```javascript
import EDistrictUttarPradeshUttarPradesh from 'e_district_uttar_pradesh_uttar_pradesh';
let defaultClient = EDistrictUttarPradeshUttarPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictUttarPradeshUttarPradesh.APIsApi();
let opts = {
  'btcerRequest': new EDistrictUttarPradeshUttarPradesh.BtcerRequest() // BtcerRequest | Request format
};
apiInstance.btcer(opts, (error, data, response) => {
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
 **btcerRequest** | [**BtcerRequest**](BtcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json


## ctcer

> ctcer(opts)

Caste Certificate

API to verify Caste Certificate.

### Example

```javascript
import EDistrictUttarPradeshUttarPradesh from 'e_district_uttar_pradesh_uttar_pradesh';
let defaultClient = EDistrictUttarPradeshUttarPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictUttarPradeshUttarPradesh.APIsApi();
let opts = {
  'ctcerRequest': new EDistrictUttarPradeshUttarPradesh.CtcerRequest() // CtcerRequest | Request format
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


## dmcer

> dmcer(opts)

Domicile Certificate

API to verify Domicile Certificate.

### Example

```javascript
import EDistrictUttarPradeshUttarPradesh from 'e_district_uttar_pradesh_uttar_pradesh';
let defaultClient = EDistrictUttarPradeshUttarPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictUttarPradeshUttarPradesh.APIsApi();
let opts = {
  'dmcerRequest': new EDistrictUttarPradeshUttarPradesh.DmcerRequest() // DmcerRequest | Request format
};
apiInstance.dmcer(opts, (error, data, response) => {
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
 **dmcerRequest** | [**DmcerRequest**](DmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## dpicr

> dpicr(opts)

Disabled Person Identity Card/ Certificate

API to verify Disabled Person Identity Card/ Certificate.

### Example

```javascript
import EDistrictUttarPradeshUttarPradesh from 'e_district_uttar_pradesh_uttar_pradesh';
let defaultClient = EDistrictUttarPradeshUttarPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictUttarPradeshUttarPradesh.APIsApi();
let opts = {
  'dpicrRequest': new EDistrictUttarPradeshUttarPradesh.DpicrRequest() // DpicrRequest | Request format
};
apiInstance.dpicr(opts, (error, data, response) => {
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
 **dpicrRequest** | [**DpicrRequest**](DpicrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## dtcer

> dtcer(opts)

Death Certificate

API to verify Death Certificate.

### Example

```javascript
import EDistrictUttarPradeshUttarPradesh from 'e_district_uttar_pradesh_uttar_pradesh';
let defaultClient = EDistrictUttarPradeshUttarPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictUttarPradeshUttarPradesh.APIsApi();
let opts = {
  'dtcerRequest': new EDistrictUttarPradeshUttarPradesh.DtcerRequest() // DtcerRequest | Request format
};
apiInstance.dtcer(opts, (error, data, response) => {
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
 **dtcerRequest** | [**DtcerRequest**](DtcerRequest.md)| Request format | [optional] 

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
import EDistrictUttarPradeshUttarPradesh from 'e_district_uttar_pradesh_uttar_pradesh';
let defaultClient = EDistrictUttarPradeshUttarPradesh.ApiClient.instance;
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

let apiInstance = new EDistrictUttarPradeshUttarPradesh.APIsApi();
let opts = {
  'incerRequest': new EDistrictUttarPradeshUttarPradesh.IncerRequest() // IncerRequest | Request format
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
 **incerRequest** | [**IncerRequest**](IncerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

