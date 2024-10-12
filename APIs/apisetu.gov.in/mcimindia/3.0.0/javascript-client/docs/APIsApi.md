# MaharashtraCouncilOfIndianMedicine.APIsApi

All URIs are relative to *https://apisetu.gov.in/mcimindia/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**govid**](APIsApi.md#govid) | **POST** /govid/certificate | ID Card
[**phcer**](APIsApi.md#phcer) | **POST** /phcer/certificate | Pharmacist Registration Certificate



## govid

> govid(opts)

ID Card

API to verify ID Card.

### Example

```javascript
import MaharashtraCouncilOfIndianMedicine from 'maharashtra_council_of_indian_medicine';
let defaultClient = MaharashtraCouncilOfIndianMedicine.ApiClient.instance;
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

let apiInstance = new MaharashtraCouncilOfIndianMedicine.APIsApi();
let opts = {
  'govidRequest': new MaharashtraCouncilOfIndianMedicine.GovidRequest() // GovidRequest | Request format
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


## phcer

> phcer(opts)

Pharmacist Registration Certificate

API to verify Pharmacist Registration Certificate.

### Example

```javascript
import MaharashtraCouncilOfIndianMedicine from 'maharashtra_council_of_indian_medicine';
let defaultClient = MaharashtraCouncilOfIndianMedicine.ApiClient.instance;
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

let apiInstance = new MaharashtraCouncilOfIndianMedicine.APIsApi();
let opts = {
  'govidRequest': new MaharashtraCouncilOfIndianMedicine.GovidRequest() // GovidRequest | Request format
};
apiInstance.phcer(opts, (error, data, response) => {
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

