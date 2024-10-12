# KeralaPublicServiceCommissionKerala.APIsApi

All URIs are relative to *https://apisetu.gov.in/keralapsc/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otcer**](APIsApi.md#otcer) | **POST** /otcer/certificate | OTV Certificate



## otcer

> otcer(opts)

OTV Certificate

API to verify OTV Certificate.

### Example

```javascript
import KeralaPublicServiceCommissionKerala from 'kerala_public_service_commission_kerala';
let defaultClient = KeralaPublicServiceCommissionKerala.ApiClient.instance;
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

let apiInstance = new KeralaPublicServiceCommissionKerala.APIsApi();
let opts = {
  'otcerRequest': new KeralaPublicServiceCommissionKerala.OtcerRequest() // OtcerRequest | Request format
};
apiInstance.otcer(opts, (error, data, response) => {
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
 **otcerRequest** | [**OtcerRequest**](OtcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

