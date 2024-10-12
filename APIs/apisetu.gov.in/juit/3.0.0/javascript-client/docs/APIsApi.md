# JaypeeUniversityOfInformationTechnologyWaknaghatHP.APIsApi

All URIs are relative to *https://apisetu.gov.in/juit/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dgcer**](APIsApi.md#dgcer) | **POST** /dgcer/certificate | Degree/ Diploma Certificate



## dgcer

> dgcer(opts)

Degree/ Diploma Certificate

API to verify Degree/ Diploma Certificate.

### Example

```javascript
import JaypeeUniversityOfInformationTechnologyWaknaghatHP from 'jaypee_university_of_information_technology_waknaghat__h__p_';
let defaultClient = JaypeeUniversityOfInformationTechnologyWaknaghatHP.ApiClient.instance;
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

let apiInstance = new JaypeeUniversityOfInformationTechnologyWaknaghatHP.APIsApi();
let opts = {
  'dgcerRequest': new JaypeeUniversityOfInformationTechnologyWaknaghatHP.DgcerRequest() // DgcerRequest | Request format
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

