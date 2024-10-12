# NationalInstituteOfElectronicsAndInformationTechnology.APIsApi

All URIs are relative to *https://apisetu.gov.in/neilit/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skcer**](APIsApi.md#skcer) | **POST** /skcer/certificate | Skill Certificate



## skcer

> skcer(opts)

Skill Certificate

API to verify Skill Certificate.

### Example

```javascript
import NationalInstituteOfElectronicsAndInformationTechnology from 'national_institute_of_electronics_and_information_technology';
let defaultClient = NationalInstituteOfElectronicsAndInformationTechnology.ApiClient.instance;
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

let apiInstance = new NationalInstituteOfElectronicsAndInformationTechnology.APIsApi();
let opts = {
  'skcerRequest': new NationalInstituteOfElectronicsAndInformationTechnology.SkcerRequest() // SkcerRequest | Request format
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

