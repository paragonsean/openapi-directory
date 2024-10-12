# KrishnaKantaHandiqueStateOpenUniversityKkhsouAssam.APIsApi

All URIs are relative to *https://apisetu.gov.in/kkhsou/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pvcer**](APIsApi.md#pvcer) | **POST** /pvcer/certificate | Provisional Certificate



## pvcer

> pvcer(opts)

Provisional Certificate

API to verify Provisional Certificate.

### Example

```javascript
import KrishnaKantaHandiqueStateOpenUniversityKkhsouAssam from 'krishna_kanta_handique_state_open_university__kkhsou_assam';
let defaultClient = KrishnaKantaHandiqueStateOpenUniversityKkhsouAssam.ApiClient.instance;
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

let apiInstance = new KrishnaKantaHandiqueStateOpenUniversityKkhsouAssam.APIsApi();
let opts = {
  'pvcerRequest': new KrishnaKantaHandiqueStateOpenUniversityKkhsouAssam.PvcerRequest() // PvcerRequest | Request format
};
apiInstance.pvcer(opts, (error, data, response) => {
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
 **pvcerRequest** | [**PvcerRequest**](PvcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

