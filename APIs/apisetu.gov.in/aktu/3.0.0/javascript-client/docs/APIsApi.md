# DrAPJAbdulKalamTechnicalUniversityLucknowUttarPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/aktu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dgcer**](APIsApi.md#dgcer) | **POST** /dgcer/certificate | Degree/ Diploma Certificate
[**dgmst**](APIsApi.md#dgmst) | **POST** /dgmst/certificate | Degree/ Diploma Marksheet



## dgcer

> dgcer(opts)

Degree/ Diploma Certificate

API to verify Degree/ Diploma Certificate.

### Example

```javascript
import DrAPJAbdulKalamTechnicalUniversityLucknowUttarPradesh from 'dr__a__p__j__abdul_kalam_technical_university_lucknow_uttar_pradesh';
let defaultClient = DrAPJAbdulKalamTechnicalUniversityLucknowUttarPradesh.ApiClient.instance;
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

let apiInstance = new DrAPJAbdulKalamTechnicalUniversityLucknowUttarPradesh.APIsApi();
let opts = {
  'dgcerRequest': new DrAPJAbdulKalamTechnicalUniversityLucknowUttarPradesh.DgcerRequest() // DgcerRequest | Request format
};
apiInstance.dgcer(opts, (error, data, response) => {
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
 **dgcerRequest** | [**DgcerRequest**](DgcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## dgmst

> dgmst(opts)

Degree/ Diploma Marksheet

API to verify Degree/ Diploma Marksheet.

### Example

```javascript
import DrAPJAbdulKalamTechnicalUniversityLucknowUttarPradesh from 'dr__a__p__j__abdul_kalam_technical_university_lucknow_uttar_pradesh';
let defaultClient = DrAPJAbdulKalamTechnicalUniversityLucknowUttarPradesh.ApiClient.instance;
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

let apiInstance = new DrAPJAbdulKalamTechnicalUniversityLucknowUttarPradesh.APIsApi();
let opts = {
  'dgmstRequest': new DrAPJAbdulKalamTechnicalUniversityLucknowUttarPradesh.DgmstRequest() // DgmstRequest | Request format
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

