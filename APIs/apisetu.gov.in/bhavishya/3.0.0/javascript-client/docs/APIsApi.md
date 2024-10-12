# DepartmentOfPensionAndPensionersWelfare.APIsApi

All URIs are relative to *https://apisetu.gov.in/bhavishya/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pecer**](APIsApi.md#pecer) | **POST** /pecer/certificate | Pension Certificate



## pecer

> pecer(opts)

Pension Certificate

API to verify Pension Certificate.

### Example

```javascript
import DepartmentOfPensionAndPensionersWelfare from 'department_of_pension_and_pensioners_welfare';
let defaultClient = DepartmentOfPensionAndPensionersWelfare.ApiClient.instance;
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

let apiInstance = new DepartmentOfPensionAndPensionersWelfare.APIsApi();
let opts = {
  'pecerRequest': new DepartmentOfPensionAndPensionersWelfare.PecerRequest() // PecerRequest | Request format
};
apiInstance.pecer(opts, (error, data, response) => {
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
 **pecerRequest** | [**PecerRequest**](PecerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

