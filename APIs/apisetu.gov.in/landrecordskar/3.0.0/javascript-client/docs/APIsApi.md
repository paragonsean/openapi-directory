# RevenueDepartmentLandRecordsKarnataka.APIsApi

All URIs are relative to *https://apisetu.gov.in/landrecordskar/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cncer**](APIsApi.md#cncer) | **POST** /cncer/certificate | Conversion Certificate
[**mutan**](APIsApi.md#mutan) | **POST** /mutan/certificate | Mutation Report/ePattadar Passbook



## cncer

> cncer(opts)

Conversion Certificate

API to verify Conversion Certificate.

### Example

```javascript
import RevenueDepartmentLandRecordsKarnataka from 'revenue_department_land_records_karnataka';
let defaultClient = RevenueDepartmentLandRecordsKarnataka.ApiClient.instance;
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

let apiInstance = new RevenueDepartmentLandRecordsKarnataka.APIsApi();
let opts = {
  'cncerRequest': new RevenueDepartmentLandRecordsKarnataka.CncerRequest() // CncerRequest | Request format
};
apiInstance.cncer(opts, (error, data, response) => {
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
 **cncerRequest** | [**CncerRequest**](CncerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json


## mutan

> mutan(opts)

Mutation Report/ePattadar Passbook

API to verify Mutation Report/ePattadar Passbook.

### Example

```javascript
import RevenueDepartmentLandRecordsKarnataka from 'revenue_department_land_records_karnataka';
let defaultClient = RevenueDepartmentLandRecordsKarnataka.ApiClient.instance;
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

let apiInstance = new RevenueDepartmentLandRecordsKarnataka.APIsApi();
let opts = {
  'mutanRequest': new RevenueDepartmentLandRecordsKarnataka.MutanRequest() // MutanRequest | Request format
};
apiInstance.mutan(opts, (error, data, response) => {
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
 **mutanRequest** | [**MutanRequest**](MutanRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/xml, application/json

