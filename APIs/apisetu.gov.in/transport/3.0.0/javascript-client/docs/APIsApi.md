# MinistryOfRoadTransportAndHighways.APIsApi

All URIs are relative to *https://apisetu.gov.in/transport/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drvlc**](APIsApi.md#drvlc) | **POST** /drvlc/certificate | Driving License
[**fitcer**](APIsApi.md#fitcer) | **POST** /fitcer/certificate | Fitness Certificate
[**rvcer**](APIsApi.md#rvcer) | **POST** /rvcer/certificate | Registration of Vehicles
[**vhinsc**](APIsApi.md#vhinsc) | **POST** /vhinsc/certificate | Vehicle Insurance Certificate
[**vhtax**](APIsApi.md#vhtax) | **POST** /vhtax/certificate | Vehicle Tax Receipt



## drvlc

> drvlc(opts)

Driving License

API to verify Driving License.

### Example

```javascript
import MinistryOfRoadTransportAndHighways from 'ministry_of_road_transport_and_highways';
let defaultClient = MinistryOfRoadTransportAndHighways.ApiClient.instance;
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

let apiInstance = new MinistryOfRoadTransportAndHighways.APIsApi();
let opts = {
  'drvlcRequest': new MinistryOfRoadTransportAndHighways.DrvlcRequest() // DrvlcRequest | Request format
};
apiInstance.drvlc(opts, (error, data, response) => {
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
 **drvlcRequest** | [**DrvlcRequest**](DrvlcRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json


## fitcer

> fitcer(opts)

Fitness Certificate

API to verify Fitness Certificate.

### Example

```javascript
import MinistryOfRoadTransportAndHighways from 'ministry_of_road_transport_and_highways';
let defaultClient = MinistryOfRoadTransportAndHighways.ApiClient.instance;
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

let apiInstance = new MinistryOfRoadTransportAndHighways.APIsApi();
let opts = {
  'fitcerRequest': new MinistryOfRoadTransportAndHighways.FitcerRequest() // FitcerRequest | Request format
};
apiInstance.fitcer(opts, (error, data, response) => {
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
 **fitcerRequest** | [**FitcerRequest**](FitcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json


## rvcer

> rvcer(opts)

Registration of Vehicles

API to verify Registration of Vehicles.

### Example

```javascript
import MinistryOfRoadTransportAndHighways from 'ministry_of_road_transport_and_highways';
let defaultClient = MinistryOfRoadTransportAndHighways.ApiClient.instance;
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

let apiInstance = new MinistryOfRoadTransportAndHighways.APIsApi();
let opts = {
  'rvcerRequest': new MinistryOfRoadTransportAndHighways.RvcerRequest() // RvcerRequest | Request format
};
apiInstance.rvcer(opts, (error, data, response) => {
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
 **rvcerRequest** | [**RvcerRequest**](RvcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json


## vhinsc

> vhinsc(opts)

Vehicle Insurance Certificate

API to verify Vehicle Insurance Certificate.

### Example

```javascript
import MinistryOfRoadTransportAndHighways from 'ministry_of_road_transport_and_highways';
let defaultClient = MinistryOfRoadTransportAndHighways.ApiClient.instance;
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

let apiInstance = new MinistryOfRoadTransportAndHighways.APIsApi();
let opts = {
  'vhinscRequest': new MinistryOfRoadTransportAndHighways.VhinscRequest() // VhinscRequest | Request format
};
apiInstance.vhinsc(opts, (error, data, response) => {
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
 **vhinscRequest** | [**VhinscRequest**](VhinscRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## vhtax

> vhtax(opts)

Vehicle Tax Receipt

API to verify Vehicle Tax Receipt.

### Example

```javascript
import MinistryOfRoadTransportAndHighways from 'ministry_of_road_transport_and_highways';
let defaultClient = MinistryOfRoadTransportAndHighways.ApiClient.instance;
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

let apiInstance = new MinistryOfRoadTransportAndHighways.APIsApi();
let opts = {
  'vhtaxRequest': new MinistryOfRoadTransportAndHighways.VhtaxRequest() // VhtaxRequest | Request format
};
apiInstance.vhtax(opts, (error, data, response) => {
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
 **vhtaxRequest** | [**VhtaxRequest**](VhtaxRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

