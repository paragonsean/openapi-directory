# DepartmentOfItAndCommunicationArunachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/ditarunachal/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ilpmt**](APIsApi.md#ilpmt) | **POST** /ilpmt/certificate | Inner Line Permit



## ilpmt

> ilpmt(opts)

Inner Line Permit

API to verify Inner Line Permit.

### Example

```javascript
import DepartmentOfItAndCommunicationArunachalPradesh from 'department_of_it_and_communication_arunachal_pradesh';
let defaultClient = DepartmentOfItAndCommunicationArunachalPradesh.ApiClient.instance;
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

let apiInstance = new DepartmentOfItAndCommunicationArunachalPradesh.APIsApi();
let opts = {
  'ilpmtRequest': new DepartmentOfItAndCommunicationArunachalPradesh.IlpmtRequest() // IlpmtRequest | Request format
};
apiInstance.ilpmt(opts, (error, data, response) => {
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
 **ilpmtRequest** | [**IlpmtRequest**](IlpmtRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

