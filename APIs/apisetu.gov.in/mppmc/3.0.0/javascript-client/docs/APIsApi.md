# ParamedicalCouncilMadhyaPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/mppmc/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**socer**](APIsApi.md#socer) | **POST** /socer/certificate | Educational/ Exam Registration Certificate



## socer

> socer(opts)

Educational/ Exam Registration Certificate

API to verify Educational/ Exam Registration Certificate.

### Example

```javascript
import ParamedicalCouncilMadhyaPradesh from 'paramedical_council_madhya_pradesh';
let defaultClient = ParamedicalCouncilMadhyaPradesh.ApiClient.instance;
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

let apiInstance = new ParamedicalCouncilMadhyaPradesh.APIsApi();
let opts = {
  'socerRequest': new ParamedicalCouncilMadhyaPradesh.SocerRequest() // SocerRequest | Request format
};
apiInstance.socer(opts, (error, data, response) => {
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
 **socerRequest** | [**SocerRequest**](SocerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

