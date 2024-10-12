# KeralaStateBoardOfPublicExaminationsKerala.APIsApi

All URIs are relative to *https://apisetu.gov.in/pareekshabhavanker/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sslcr**](APIsApi.md#sslcr) | **POST** /sslcr/certificate | Class X School Leaving Certificate



## sslcr

> sslcr(opts)

Class X School Leaving Certificate

API to verify Class X School Leaving Certificate.

### Example

```javascript
import KeralaStateBoardOfPublicExaminationsKerala from 'kerala_state_board_of_public_examinations_kerala';
let defaultClient = KeralaStateBoardOfPublicExaminationsKerala.ApiClient.instance;
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

let apiInstance = new KeralaStateBoardOfPublicExaminationsKerala.APIsApi();
let opts = {
  'sslcrRequest': new KeralaStateBoardOfPublicExaminationsKerala.SslcrRequest() // SslcrRequest | Request format
};
apiInstance.sslcr(opts, (error, data, response) => {
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
 **sslcrRequest** | [**SslcrRequest**](SslcrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

