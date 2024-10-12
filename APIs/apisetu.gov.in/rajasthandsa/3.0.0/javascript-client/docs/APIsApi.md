# SocialJusticeAndEmpowermentDepartmentRajasthan.APIsApi

All URIs are relative to *https://apisetu.gov.in/rajasthandsa/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dpicr**](APIsApi.md#dpicr) | **POST** /dpicr/certificate | Disabled Person Identity Card/ Certificate



## dpicr

> dpicr(opts)

Disabled Person Identity Card/ Certificate

API to verify Disabled Person Identity Card/ Certificate.

### Example

```javascript
import SocialJusticeAndEmpowermentDepartmentRajasthan from 'social_justice_and_empowerment_department_rajasthan';
let defaultClient = SocialJusticeAndEmpowermentDepartmentRajasthan.ApiClient.instance;
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

let apiInstance = new SocialJusticeAndEmpowermentDepartmentRajasthan.APIsApi();
let opts = {
  'dpicrRequest': new SocialJusticeAndEmpowermentDepartmentRajasthan.DpicrRequest() // DpicrRequest | Request format
};
apiInstance.dpicr(opts, (error, data, response) => {
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
 **dpicrRequest** | [**DpicrRequest**](DpicrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

