# DepartmentOfAgriculturalMarketingKarnataka.APIsApi

All URIs are relative to *https://apisetu.gov.in/apmcservices/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apmcl**](APIsApi.md#apmcl) | **POST** /apmcl/certificate | Agriculture Produce Market Committee License



## apmcl

> apmcl(opts)

Agriculture Produce Market Committee License

API to verify Agriculture Produce Market Committee License.

### Example

```javascript
import DepartmentOfAgriculturalMarketingKarnataka from 'department_of_agricultural_marketing_karnataka';
let defaultClient = DepartmentOfAgriculturalMarketingKarnataka.ApiClient.instance;
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

let apiInstance = new DepartmentOfAgriculturalMarketingKarnataka.APIsApi();
let opts = {
  'apmclRequest': new DepartmentOfAgriculturalMarketingKarnataka.ApmclRequest() // ApmclRequest | Request format
};
apiInstance.apmcl(opts, (error, data, response) => {
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
 **apmclRequest** | [**ApmclRequest**](ApmclRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

