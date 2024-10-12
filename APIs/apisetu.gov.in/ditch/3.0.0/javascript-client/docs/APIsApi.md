# EDistrictChandigarhChandigarh.APIsApi

All URIs are relative to *https://apisetu.gov.in/ditch/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**incer**](APIsApi.md#incer) | **POST** /incer/certificate | Income Certificate
[**rmcer**](APIsApi.md#rmcer) | **POST** /rmcer/certificate | Marriage Certificate
[**rscer**](APIsApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate
[**sicrd**](APIsApi.md#sicrd) | **POST** /sicrd/certificate | Senior Citizen Identity Card/ Certificate



## incer

> incer(opts)

Income Certificate

API to verify Income Certificate.

### Example

```javascript
import EDistrictChandigarhChandigarh from 'e_district_chandigarh_chandigarh';
let defaultClient = EDistrictChandigarhChandigarh.ApiClient.instance;
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

let apiInstance = new EDistrictChandigarhChandigarh.APIsApi();
let opts = {
  'incerRequest': new EDistrictChandigarhChandigarh.IncerRequest() // IncerRequest | Request format
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


## rmcer

> rmcer(opts)

Marriage Certificate

API to verify Marriage Certificate.

### Example

```javascript
import EDistrictChandigarhChandigarh from 'e_district_chandigarh_chandigarh';
let defaultClient = EDistrictChandigarhChandigarh.ApiClient.instance;
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

let apiInstance = new EDistrictChandigarhChandigarh.APIsApi();
let opts = {
  'incerRequest': new EDistrictChandigarhChandigarh.IncerRequest() // IncerRequest | Request format
};
apiInstance.rmcer(opts, (error, data, response) => {
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


## rscer

> rscer(opts)

Residence Certificate

API to verify Residence Certificate.

### Example

```javascript
import EDistrictChandigarhChandigarh from 'e_district_chandigarh_chandigarh';
let defaultClient = EDistrictChandigarhChandigarh.ApiClient.instance;
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

let apiInstance = new EDistrictChandigarhChandigarh.APIsApi();
let opts = {
  'incerRequest': new EDistrictChandigarhChandigarh.IncerRequest() // IncerRequest | Request format
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
 **incerRequest** | [**IncerRequest**](IncerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## sicrd

> sicrd(opts)

Senior Citizen Identity Card/ Certificate

API to verify Senior Citizen Identity Card/ Certificate.

### Example

```javascript
import EDistrictChandigarhChandigarh from 'e_district_chandigarh_chandigarh';
let defaultClient = EDistrictChandigarhChandigarh.ApiClient.instance;
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

let apiInstance = new EDistrictChandigarhChandigarh.APIsApi();
let opts = {
  'sicrdRequest': new EDistrictChandigarhChandigarh.SicrdRequest() // SicrdRequest | Request format
};
apiInstance.sicrd(opts, (error, data, response) => {
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
 **sicrdRequest** | [**SicrdRequest**](SicrdRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

