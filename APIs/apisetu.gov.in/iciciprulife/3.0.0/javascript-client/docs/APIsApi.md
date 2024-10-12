# IciciPrudentialLifeInsuranceCompanyLtd.APIsApi

All URIs are relative to *https://apisetu.gov.in/iciciprulife/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licer**](APIsApi.md#licer) | **POST** /licer/certificate | Insurance Policy - Life



## licer

> licer(opts)

Insurance Policy - Life

API to verify Insurance Policy - Life.

### Example

```javascript
import IciciPrudentialLifeInsuranceCompanyLtd from 'icici_prudential_life_insurance_company_ltd';
let defaultClient = IciciPrudentialLifeInsuranceCompanyLtd.ApiClient.instance;
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

let apiInstance = new IciciPrudentialLifeInsuranceCompanyLtd.APIsApi();
let opts = {
  'licerRequest': new IciciPrudentialLifeInsuranceCompanyLtd.LicerRequest() // LicerRequest | Request format
};
apiInstance.licer(opts, (error, data, response) => {
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
 **licerRequest** | [**LicerRequest**](LicerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

