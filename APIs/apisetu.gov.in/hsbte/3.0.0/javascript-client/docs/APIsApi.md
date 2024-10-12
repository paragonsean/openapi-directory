# HaryanaStateBoardOfTechnicalEducationHaryana.APIsApi

All URIs are relative to *https://apisetu.gov.in/hsbte/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dgmst**](APIsApi.md#dgmst) | **POST** /dgmst/certificate | Degree/ Diploma Marksheet



## dgmst

> dgmst(opts)

Degree/ Diploma Marksheet

API to verify Degree/ Diploma Marksheet.

### Example

```javascript
import HaryanaStateBoardOfTechnicalEducationHaryana from 'haryana_state_board_of_technical_education_haryana';
let defaultClient = HaryanaStateBoardOfTechnicalEducationHaryana.ApiClient.instance;
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

let apiInstance = new HaryanaStateBoardOfTechnicalEducationHaryana.APIsApi();
let opts = {
  'dgmstRequest': new HaryanaStateBoardOfTechnicalEducationHaryana.DgmstRequest() // DgmstRequest | Request format
};
apiInstance.dgmst(opts, (error, data, response) => {
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
 **dgmstRequest** | [**DgmstRequest**](DgmstRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

