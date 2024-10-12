# BoardOfHigherSecondaryExaminationKeralaKerala.APIsApi

All URIs are relative to *https://apisetu.gov.in/dhsekerala/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hpcer**](APIsApi.md#hpcer) | **POST** /hpcer/certificate | Class XII Passing Certificate



## hpcer

> hpcer(opts)

Class XII Passing Certificate

API to verify Class XII Passing Certificate.

### Example

```javascript
import BoardOfHigherSecondaryExaminationKeralaKerala from 'board_of_higher_secondary_examination_kerala_kerala';
let defaultClient = BoardOfHigherSecondaryExaminationKeralaKerala.ApiClient.instance;
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

let apiInstance = new BoardOfHigherSecondaryExaminationKeralaKerala.APIsApi();
let opts = {
  'hpcerRequest': new BoardOfHigherSecondaryExaminationKeralaKerala.HpcerRequest() // HpcerRequest | Request format
};
apiInstance.hpcer(opts, (error, data, response) => {
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
 **hpcerRequest** | [**HpcerRequest**](HpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

