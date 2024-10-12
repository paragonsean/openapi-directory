# CpctMapitMadhyaPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/cpctmp/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skmst**](APIsApi.md#skmst) | **POST** /skmst/certificate | Skill Marksheet/ Score Card



## skmst

> skmst(opts)

Skill Marksheet/ Score Card

API to verify Skill Marksheet/ Score Card.

### Example

```javascript
import CpctMapitMadhyaPradesh from 'cpct_mapit_madhya_pradesh';
let defaultClient = CpctMapitMadhyaPradesh.ApiClient.instance;
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

let apiInstance = new CpctMapitMadhyaPradesh.APIsApi();
let opts = {
  'skmstRequest': new CpctMapitMadhyaPradesh.SkmstRequest() // SkmstRequest | Request format
};
apiInstance.skmst(opts, (error, data, response) => {
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
 **skmstRequest** | [**SkmstRequest**](SkmstRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

