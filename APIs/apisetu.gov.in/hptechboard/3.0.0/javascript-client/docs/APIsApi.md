# HimachalPradeshTaknikiShikshaBoardDharamshalaHimachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/hptechboard/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dipcr**](APIsApi.md#dipcr) | **POST** /dipcr/certificate | Diploma Certificate



## dipcr

> dipcr(opts)

Diploma Certificate

API to verify Diploma Certificate.

### Example

```javascript
import HimachalPradeshTaknikiShikshaBoardDharamshalaHimachalPradesh from 'himachal_pradesh_takniki_shiksha_board_dharamshala_himachal_pradesh';
let defaultClient = HimachalPradeshTaknikiShikshaBoardDharamshalaHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HimachalPradeshTaknikiShikshaBoardDharamshalaHimachalPradesh.APIsApi();
let opts = {
  'dipcrRequest': new HimachalPradeshTaknikiShikshaBoardDharamshalaHimachalPradesh.DipcrRequest() // DipcrRequest | Request format
};
apiInstance.dipcr(opts, (error, data, response) => {
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
 **dipcrRequest** | [**DipcrRequest**](DipcrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

