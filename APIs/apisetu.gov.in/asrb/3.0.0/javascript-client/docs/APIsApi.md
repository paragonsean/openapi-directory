# AgriculturalScientistsRecruitmentBoard.APIsApi

All URIs are relative to *https://apisetu.gov.in/asrb/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mrcer**](APIsApi.md#mrcer) | **POST** /mrcer/certificate | Merit Certificate



## mrcer

> mrcer(opts)

Merit Certificate

API to verify Merit Certificate.

### Example

```javascript
import AgriculturalScientistsRecruitmentBoard from 'agricultural_scientists_recruitment_board';
let defaultClient = AgriculturalScientistsRecruitmentBoard.ApiClient.instance;
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

let apiInstance = new AgriculturalScientistsRecruitmentBoard.APIsApi();
let opts = {
  'mrcerRequest': new AgriculturalScientistsRecruitmentBoard.MrcerRequest() // MrcerRequest | Request format
};
apiInstance.mrcer(opts, (error, data, response) => {
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
 **mrcerRequest** | [**MrcerRequest**](MrcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

