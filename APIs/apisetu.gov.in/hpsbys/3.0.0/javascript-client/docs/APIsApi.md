# HpSwasthyaBimaYojnaSocietyHimachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/hpsbys/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rsbyc**](APIsApi.md#rsbyc) | **POST** /rsbyc/certificate | Health Card/ Certificate



## rsbyc

> rsbyc(opts)

Health Card/ Certificate

API to verify Health Card/ Certificate.

### Example

```javascript
import HpSwasthyaBimaYojnaSocietyHimachalPradesh from 'hp_swasthya_bima_yojna_society_himachal_pradesh';
let defaultClient = HpSwasthyaBimaYojnaSocietyHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HpSwasthyaBimaYojnaSocietyHimachalPradesh.APIsApi();
let opts = {
  'rsbycRequest': new HpSwasthyaBimaYojnaSocietyHimachalPradesh.RsbycRequest() // RsbycRequest | Request format
};
apiInstance.rsbyc(opts, (error, data, response) => {
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
 **rsbycRequest** | [**RsbycRequest**](RsbycRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

