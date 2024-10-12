# KarnatakaDepartmentOfTransportKarnataka.APIsApi

All URIs are relative to *https://apisetu.gov.in/transportka/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drvlc**](APIsApi.md#drvlc) | **POST** /drvlc/certificate | Driving License
[**rvcer**](APIsApi.md#rvcer) | **POST** /rvcer/certificate | Registration of Vehicles



## drvlc

> drvlc(opts)

Driving License

API to verify Driving License.

### Example

```javascript
import KarnatakaDepartmentOfTransportKarnataka from 'karnataka_department_of_transport_karnataka';
let defaultClient = KarnatakaDepartmentOfTransportKarnataka.ApiClient.instance;
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

let apiInstance = new KarnatakaDepartmentOfTransportKarnataka.APIsApi();
let opts = {
  'drvlcRequest': new KarnatakaDepartmentOfTransportKarnataka.DrvlcRequest() // DrvlcRequest | Request format
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


## rvcer

> rvcer(opts)

Registration of Vehicles

API to verify Registration of Vehicles.

### Example

```javascript
import KarnatakaDepartmentOfTransportKarnataka from 'karnataka_department_of_transport_karnataka';
let defaultClient = KarnatakaDepartmentOfTransportKarnataka.ApiClient.instance;
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

let apiInstance = new KarnatakaDepartmentOfTransportKarnataka.APIsApi();
let opts = {
  'rvcerRequest': new KarnatakaDepartmentOfTransportKarnataka.RvcerRequest() // RvcerRequest | Request format
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

