# AntyodayaSaralHaryanaHaryana.APIsApi

All URIs are relative to *https://apisetu.gov.in/saralharyana/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nbcer**](APIsApi.md#nbcer) | **POST** /nbcer/certificate | NAC/Birth/Death Certificate



## nbcer

> nbcer(opts)

NAC/Birth/Death Certificate

API to verify NAC/Birth/Death Certificate.

### Example

```javascript
import AntyodayaSaralHaryanaHaryana from 'antyodaya_saral_haryana_haryana';
let defaultClient = AntyodayaSaralHaryanaHaryana.ApiClient.instance;
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

let apiInstance = new AntyodayaSaralHaryanaHaryana.APIsApi();
let opts = {
  'nbcerRequest': new AntyodayaSaralHaryanaHaryana.NbcerRequest() // NbcerRequest | Request format
};
apiInstance.nbcer(opts, (error, data, response) => {
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
 **nbcerRequest** | [**NbcerRequest**](NbcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

