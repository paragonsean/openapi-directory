# DepartmentOfRegistrationStampsMaharashtra.APIsApi

All URIs are relative to *https://apisetu.gov.in/igrmaharashtra/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**llcer**](APIsApi.md#llcer) | **POST** /llcer/certificate | Leave and License Certificate



## llcer

> llcer(opts)

Leave and License Certificate

API to verify Leave and License Certificate.

### Example

```javascript
import DepartmentOfRegistrationStampsMaharashtra from 'department_of_registration__stamps_maharashtra';
let defaultClient = DepartmentOfRegistrationStampsMaharashtra.ApiClient.instance;
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

let apiInstance = new DepartmentOfRegistrationStampsMaharashtra.APIsApi();
let opts = {
  'llcerRequest': new DepartmentOfRegistrationStampsMaharashtra.LlcerRequest() // LlcerRequest | Request format
};
apiInstance.llcer(opts, (error, data, response) => {
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
 **llcerRequest** | [**LlcerRequest**](LlcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

