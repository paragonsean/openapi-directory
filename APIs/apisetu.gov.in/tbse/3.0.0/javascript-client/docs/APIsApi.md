# TripuraStateBoardOfSecondaryEducationTripura.APIsApi

All URIs are relative to *https://apisetu.gov.in/tbse/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hscer**](APIsApi.md#hscer) | **POST** /hscer/certificate | Class XII Marksheet



## hscer

> hscer(opts)

Class XII Marksheet

API to verify Class XII Marksheet.

### Example

```javascript
import TripuraStateBoardOfSecondaryEducationTripura from 'tripura_state_board_of_secondary_education_tripura';
let defaultClient = TripuraStateBoardOfSecondaryEducationTripura.ApiClient.instance;
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

let apiInstance = new TripuraStateBoardOfSecondaryEducationTripura.APIsApi();
let opts = {
  'hscerRequest': new TripuraStateBoardOfSecondaryEducationTripura.HscerRequest() // HscerRequest | Request format
};
apiInstance.hscer(opts, (error, data, response) => {
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
 **hscerRequest** | [**HscerRequest**](HscerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

