# LabourEmploymentSkillDevelopmentAndEntrepreneurshipMizoram.APIsApi

All URIs are relative to *https://apisetu.gov.in/mizoramlesde/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**govid**](APIsApi.md#govid) | **POST** /govid/certificate | ID Card



## govid

> govid(opts)

ID Card

API to verify ID Card.

### Example

```javascript
import LabourEmploymentSkillDevelopmentAndEntrepreneurshipMizoram from 'labour_employment_skill_development_and_entrepreneurship_mizoram';
let defaultClient = LabourEmploymentSkillDevelopmentAndEntrepreneurshipMizoram.ApiClient.instance;
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

let apiInstance = new LabourEmploymentSkillDevelopmentAndEntrepreneurshipMizoram.APIsApi();
let opts = {
  'govidRequest': new LabourEmploymentSkillDevelopmentAndEntrepreneurshipMizoram.GovidRequest() // GovidRequest | Request format
};
apiInstance.govid(opts, (error, data, response) => {
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
 **govidRequest** | [**GovidRequest**](GovidRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

