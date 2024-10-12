# RevenueDisasterManagementDepartmentAssamAssam.APIsApi

All URIs are relative to *https://apisetu.gov.in/revenueassam/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nncer**](APIsApi.md#nncer) | **POST** /nncer/certificate | Non-Encumbrance Certificate



## nncer

> nncer(opts)

Non-Encumbrance Certificate

API to verify Non-Encumbrance Certificate.

### Example

```javascript
import RevenueDisasterManagementDepartmentAssamAssam from 'revenue__disaster_management_department_assam_assam';
let defaultClient = RevenueDisasterManagementDepartmentAssamAssam.ApiClient.instance;
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

let apiInstance = new RevenueDisasterManagementDepartmentAssamAssam.APIsApi();
let opts = {
  'nncerRequest': new RevenueDisasterManagementDepartmentAssamAssam.NncerRequest() // NncerRequest | Request format
};
apiInstance.nncer(opts, (error, data, response) => {
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
 **nncerRequest** | [**NncerRequest**](NncerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

