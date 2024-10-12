# JointEntranceExaminationCouncilUttarPradeshUttarPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/jeecup/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adcrd**](APIsApi.md#adcrd) | **POST** /adcrd/certificate | Admit Card



## adcrd

> adcrd(opts)

Admit Card

API to verify Admit Card.

### Example

```javascript
import JointEntranceExaminationCouncilUttarPradeshUttarPradesh from 'joint_entrance_examination_council_uttar_pradesh_uttar_pradesh';
let defaultClient = JointEntranceExaminationCouncilUttarPradeshUttarPradesh.ApiClient.instance;
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

let apiInstance = new JointEntranceExaminationCouncilUttarPradeshUttarPradesh.APIsApi();
let opts = {
  'adcrdRequest': new JointEntranceExaminationCouncilUttarPradeshUttarPradesh.AdcrdRequest() // AdcrdRequest | Request format
};
apiInstance.adcrd(opts, (error, data, response) => {
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
 **adcrdRequest** | [**AdcrdRequest**](AdcrdRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

