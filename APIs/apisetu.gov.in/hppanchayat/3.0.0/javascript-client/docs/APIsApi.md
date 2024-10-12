# PanchayatiRajDepartmentHimachalPradeshHimachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/hppanchayat/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fmcer**](APIsApi.md#fmcer) | **POST** /fmcer/certificate | Family Membership Certificate



## fmcer

> fmcer(opts)

Family Membership Certificate

API to verify Family Membership Certificate.

### Example

```javascript
import PanchayatiRajDepartmentHimachalPradeshHimachalPradesh from 'panchayati_raj_department_himachal_pradesh_himachal_pradesh';
let defaultClient = PanchayatiRajDepartmentHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new PanchayatiRajDepartmentHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'fmcerRequest': new PanchayatiRajDepartmentHimachalPradeshHimachalPradesh.FmcerRequest() // FmcerRequest | Request format
};
apiInstance.fmcer(opts, (error, data, response) => {
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
 **fmcerRequest** | [**FmcerRequest**](FmcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

