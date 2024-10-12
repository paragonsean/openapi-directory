# DrBabasahebAmbedkarResearchTrainingInstituteMaharashtra.APIsApi

All URIs are relative to *https://apisetu.gov.in/barti/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cvcer**](APIsApi.md#cvcer) | **POST** /cvcer/certificate | Caste Validity Certificate



## cvcer

> cvcer(opts)

Caste Validity Certificate

API to verify Caste Validity Certificate.

### Example

```javascript
import DrBabasahebAmbedkarResearchTrainingInstituteMaharashtra from 'dr__babasaheb_ambedkar_research__training_institute_maharashtra';
let defaultClient = DrBabasahebAmbedkarResearchTrainingInstituteMaharashtra.ApiClient.instance;
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

let apiInstance = new DrBabasahebAmbedkarResearchTrainingInstituteMaharashtra.APIsApi();
let opts = {
  'cvcerRequest': new DrBabasahebAmbedkarResearchTrainingInstituteMaharashtra.CvcerRequest() // CvcerRequest | Request format
};
apiInstance.cvcer(opts, (error, data, response) => {
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
 **cvcerRequest** | [**CvcerRequest**](CvcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

