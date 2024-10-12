# MadhyaPradeshMedicalScienceUniversityJabalpurMPMadhyaPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/mpmsu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**micer**](APIsApi.md#micer) | **POST** /micer/certificate | Migration Certificate
[**pvcer**](APIsApi.md#pvcer) | **POST** /pvcer/certificate | Provisional Certificate



## micer

> micer(opts)

Migration Certificate

API to verify Migration Certificate.

### Example

```javascript
import MadhyaPradeshMedicalScienceUniversityJabalpurMPMadhyaPradesh from 'madhya_pradesh_medical_science_university_jabalpur_m_p__madhya_pradesh';
let defaultClient = MadhyaPradeshMedicalScienceUniversityJabalpurMPMadhyaPradesh.ApiClient.instance;
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

let apiInstance = new MadhyaPradeshMedicalScienceUniversityJabalpurMPMadhyaPradesh.APIsApi();
let opts = {
  'micerRequest': new MadhyaPradeshMedicalScienceUniversityJabalpurMPMadhyaPradesh.MicerRequest() // MicerRequest | Request format
};
apiInstance.micer(opts, (error, data, response) => {
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
 **micerRequest** | [**MicerRequest**](MicerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## pvcer

> pvcer(opts)

Provisional Certificate

API to verify Provisional Certificate.

### Example

```javascript
import MadhyaPradeshMedicalScienceUniversityJabalpurMPMadhyaPradesh from 'madhya_pradesh_medical_science_university_jabalpur_m_p__madhya_pradesh';
let defaultClient = MadhyaPradeshMedicalScienceUniversityJabalpurMPMadhyaPradesh.ApiClient.instance;
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

let apiInstance = new MadhyaPradeshMedicalScienceUniversityJabalpurMPMadhyaPradesh.APIsApi();
let opts = {
  'micerRequest': new MadhyaPradeshMedicalScienceUniversityJabalpurMPMadhyaPradesh.MicerRequest() // MicerRequest | Request format
};
apiInstance.pvcer(opts, (error, data, response) => {
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
 **micerRequest** | [**MicerRequest**](MicerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

