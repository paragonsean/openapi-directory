# UcoBank.APIsApi

All URIs are relative to *https://apisetu.gov.in/ucobank/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tdcer**](APIsApi.md#tdcer) | **POST** /tdcer/certificate | TDS Certificate



## tdcer

> tdcer(opts)

TDS Certificate

API to verify TDS Certificate.

### Example

```javascript
import UcoBank from 'uco_bank';
let defaultClient = UcoBank.ApiClient.instance;
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

let apiInstance = new UcoBank.APIsApi();
let opts = {
  'tdcerRequest': new UcoBank.TdcerRequest() // TdcerRequest | Request format
};
apiInstance.tdcer(opts, (error, data, response) => {
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
 **tdcerRequest** | [**TdcerRequest**](TdcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

