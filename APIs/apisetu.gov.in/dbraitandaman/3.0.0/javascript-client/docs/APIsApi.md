# DrBRAmbedkarInstituteOfTechnologyandamanNicobarIslands.APIsApi

All URIs are relative to *https://apisetu.gov.in/dbraitandaman/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trcer**](APIsApi.md#trcer) | **POST** /trcer/certificate | Transfer Certificate



## trcer

> trcer(opts)

Transfer Certificate

API to verify Transfer Certificate.

### Example

```javascript
import DrBRAmbedkarInstituteOfTechnologyandamanNicobarIslands from 'dr__b_r__ambedkar_institute_of_technologyandaman__nicobar_islands';
let defaultClient = DrBRAmbedkarInstituteOfTechnologyandamanNicobarIslands.ApiClient.instance;
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

let apiInstance = new DrBRAmbedkarInstituteOfTechnologyandamanNicobarIslands.APIsApi();
let opts = {
  'trcerRequest': new DrBRAmbedkarInstituteOfTechnologyandamanNicobarIslands.TrcerRequest() // TrcerRequest | Request format
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

