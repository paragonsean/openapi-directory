# JawaharlalNehruRajkeeyaMahavidyalaya.APIsApi

All URIs are relative to *https://apisetu.gov.in/jnrmand/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trcer**](APIsApi.md#trcer) | **POST** /trcer/certificate | Transfer Certificate



## trcer

> trcer(opts)

Transfer Certificate

API to verify Transfer Certificate.

### Example

```javascript
import JawaharlalNehruRajkeeyaMahavidyalaya from 'jawaharlal_nehru_rajkeeya_mahavidyalaya';
let defaultClient = JawaharlalNehruRajkeeyaMahavidyalaya.ApiClient.instance;
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

let apiInstance = new JawaharlalNehruRajkeeyaMahavidyalaya.APIsApi();
let opts = {
  'trcerRequest': new JawaharlalNehruRajkeeyaMahavidyalaya.TrcerRequest() // TrcerRequest | Request format
};
apiInstance.trcer(opts, (error, data, response) => {
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
 **trcerRequest** | [**TrcerRequest**](TrcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

