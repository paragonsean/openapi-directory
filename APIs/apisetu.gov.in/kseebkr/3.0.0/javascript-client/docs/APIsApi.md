# KarnatakaSecondaryEducationExaminationBoardKarnataka.APIsApi

All URIs are relative to *https://apisetu.gov.in/kseebkr/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sscer**](APIsApi.md#sscer) | **POST** /sscer/certificate | Class X Marksheet



## sscer

> sscer(opts)

Class X Marksheet

API to verify Class X Marksheet.

### Example

```javascript
import KarnatakaSecondaryEducationExaminationBoardKarnataka from 'karnataka_secondary_education_examination_board_karnataka';
let defaultClient = KarnatakaSecondaryEducationExaminationBoardKarnataka.ApiClient.instance;
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

let apiInstance = new KarnatakaSecondaryEducationExaminationBoardKarnataka.APIsApi();
let opts = {
  'sscerRequest': new KarnatakaSecondaryEducationExaminationBoardKarnataka.SscerRequest() // SscerRequest | Request format
};
apiInstance.sscer(opts, (error, data, response) => {
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
 **sscerRequest** | [**SscerRequest**](SscerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

