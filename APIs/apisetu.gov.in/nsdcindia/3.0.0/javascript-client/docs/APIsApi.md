# NationalSkillDevelopmentCorporationNsdc.APIsApi

All URIs are relative to *https://apisetu.gov.in/nsdcindia/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**escer**](APIsApi.md#escer) | **POST** /escer/certificate | Executive Skill Enhancement Certificate
[**skcer**](APIsApi.md#skcer) | **POST** /skcer/certificate | Skill Certificate



## escer

> escer(opts)

Executive Skill Enhancement Certificate

API to verify Executive Skill Enhancement Certificate.

### Example

```javascript
import NationalSkillDevelopmentCorporationNsdc from 'national_skill_development_corporation__nsdc';
let defaultClient = NationalSkillDevelopmentCorporationNsdc.ApiClient.instance;
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

let apiInstance = new NationalSkillDevelopmentCorporationNsdc.APIsApi();
let opts = {
  'escerRequest': new NationalSkillDevelopmentCorporationNsdc.EscerRequest() // EscerRequest | Request format
};
apiInstance.escer(opts, (error, data, response) => {
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
 **escerRequest** | [**EscerRequest**](EscerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## skcer

> skcer(opts)

Skill Certificate

API to verify Skill Certificate.

### Example

```javascript
import NationalSkillDevelopmentCorporationNsdc from 'national_skill_development_corporation__nsdc';
let defaultClient = NationalSkillDevelopmentCorporationNsdc.ApiClient.instance;
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

let apiInstance = new NationalSkillDevelopmentCorporationNsdc.APIsApi();
let opts = {
  'skcerRequest': new NationalSkillDevelopmentCorporationNsdc.SkcerRequest() // SkcerRequest | Request format
};
apiInstance.skcer(opts, (error, data, response) => {
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
 **skcerRequest** | [**SkcerRequest**](SkcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

