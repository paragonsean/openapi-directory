# IncomeTaxDepartment.APIsApi

All URIs are relative to *https://apisetu.gov.in/pan/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pancr**](APIsApi.md#pancr) | **POST** /pancr/certificate | PAN Verification Record



## pancr

> pancr(opts)

PAN Verification Record

API to verify PAN Verification Record.

### Example

```javascript
import IncomeTaxDepartment from 'income_tax_department';
let defaultClient = IncomeTaxDepartment.ApiClient.instance;
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

let apiInstance = new IncomeTaxDepartment.APIsApi();
let opts = {
  'pancrRequest': new IncomeTaxDepartment.PancrRequest() // PancrRequest | Request format
};
apiInstance.pancr(opts, (error, data, response) => {
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
 **pancrRequest** | [**PancrRequest**](PancrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json

