# MinistryOfSkillDevelopmentAndEntrepreneurship.APIsApi

All URIs are relative to *https://apisetu.gov.in/msde/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iticr**](APIsApi.md#iticr) | **POST** /iticr/certificate | ITI Certificate



## iticr

> iticr(opts)

ITI Certificate

API to verify ITI Certificate.

### Example

```javascript
import MinistryOfSkillDevelopmentAndEntrepreneurship from 'ministry_of_skill_development_and_entrepreneurship';
let defaultClient = MinistryOfSkillDevelopmentAndEntrepreneurship.ApiClient.instance;
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

let apiInstance = new MinistryOfSkillDevelopmentAndEntrepreneurship.APIsApi();
let opts = {
  'iticrRequest': new MinistryOfSkillDevelopmentAndEntrepreneurship.IticrRequest() // IticrRequest | Request format
};
apiInstance.iticr(opts, (error, data, response) => {
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
 **iticrRequest** | [**IticrRequest**](IticrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

