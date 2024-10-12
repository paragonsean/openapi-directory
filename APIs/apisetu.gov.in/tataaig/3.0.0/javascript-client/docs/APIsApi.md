# TataAigGeneralInsuranceCompanyLtd.APIsApi

All URIs are relative to *https://apisetu.gov.in/tataaig/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**podoc**](APIsApi.md#podoc) | **POST** /podoc/certificate | Policy Document



## podoc

> podoc(opts)

Policy Document

API to verify Policy Document.

### Example

```javascript
import TataAigGeneralInsuranceCompanyLtd from 'tata_aig_general_insurance_company_ltd_';
let defaultClient = TataAigGeneralInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new TataAigGeneralInsuranceCompanyLtd.APIsApi();
let opts = {
  'podocRequest': new TataAigGeneralInsuranceCompanyLtd.PodocRequest() // PodocRequest | Request format
};
apiInstance.podoc(opts, (error, data, response) => {
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
 **podocRequest** | [**PodocRequest**](PodocRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

