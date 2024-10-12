# BoardOfVocationalHigherSecondaryExaminationsKerala.APIsApi

All URIs are relative to *https://apisetu.gov.in/vhseker/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vochse**](APIsApi.md#vochse) | **POST** /vochse/certificate | Vocational Higher Secondary



## vochse

> vochse(opts)

Vocational Higher Secondary

API to verify Vocational Higher Secondary.

### Example

```javascript
import BoardOfVocationalHigherSecondaryExaminationsKerala from 'board_of_vocational_higher_secondary_examinations_kerala';
let defaultClient = BoardOfVocationalHigherSecondaryExaminationsKerala.ApiClient.instance;
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

let apiInstance = new BoardOfVocationalHigherSecondaryExaminationsKerala.APIsApi();
let opts = {
  'vochseRequest': new BoardOfVocationalHigherSecondaryExaminationsKerala.VochseRequest() // VochseRequest | Request format
};
apiInstance.vochse(opts, (error, data, response) => {
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
 **vochseRequest** | [**VochseRequest**](VochseRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

