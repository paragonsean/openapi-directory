# SailuMunicipalCouncilMaharashtra.APIsApi

All URIs are relative to *https://apisetu.gov.in/npsailu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ndcer**](APIsApi.md#ndcer) | **POST** /ndcer/certificate | No Dues/ Objection Certificate



## ndcer

> ndcer(opts)

No Dues/ Objection Certificate

API to verify No Dues/ Objection Certificate.

### Example

```javascript
import SailuMunicipalCouncilMaharashtra from 'sailu_municipal_council_maharashtra';
let defaultClient = SailuMunicipalCouncilMaharashtra.ApiClient.instance;
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

let apiInstance = new SailuMunicipalCouncilMaharashtra.APIsApi();
let opts = {
  'ndcerRequest': new SailuMunicipalCouncilMaharashtra.NdcerRequest() // NdcerRequest | Request format
};
apiInstance.ndcer(opts, (error, data, response) => {
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
 **ndcerRequest** | [**NdcerRequest**](NdcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

