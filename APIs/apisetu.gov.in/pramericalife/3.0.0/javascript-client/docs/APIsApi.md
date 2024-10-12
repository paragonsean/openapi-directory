# PramericaLifeInsuranceLtd.APIsApi

All URIs are relative to *https://apisetu.gov.in/pramericalife/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licer**](APIsApi.md#licer) | **POST** /licer/certificate | Insurance Policy - Life



## licer

> licer(opts)

Insurance Policy - Life

API to verify Insurance Policy - Life.

### Example

```javascript
import PramericaLifeInsuranceLtd from 'pramerica_life_insurance_ltd_';
let defaultClient = PramericaLifeInsuranceLtd.ApiClient.instance;
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

let apiInstance = new PramericaLifeInsuranceLtd.APIsApi();
let opts = {
  'licerRequest': new PramericaLifeInsuranceLtd.LicerRequest() // LicerRequest | Request format
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

