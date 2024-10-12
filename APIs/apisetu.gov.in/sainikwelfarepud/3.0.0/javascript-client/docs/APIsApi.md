# DepartmentOfSainikWelfarePuducherry.APIsApi

All URIs are relative to *https://apisetu.gov.in/sainikwelfarepud/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dpcer**](APIsApi.md#dpcer) | **POST** /dpcer/certificate | Dependency Certificate



## dpcer

> dpcer(opts)

Dependency Certificate

API to verify Dependency Certificate.

### Example

```javascript
import DepartmentOfSainikWelfarePuducherry from 'department_of_sainik_welfare_puducherry';
let defaultClient = DepartmentOfSainikWelfarePuducherry.ApiClient.instance;
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

let apiInstance = new DepartmentOfSainikWelfarePuducherry.APIsApi();
let opts = {
  'dpcerRequest': new DepartmentOfSainikWelfarePuducherry.DpcerRequest() // DpcerRequest | Request format
};
apiInstance.dpcer(opts, (error, data, response) => {
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
 **dpcerRequest** | [**DpcerRequest**](DpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

