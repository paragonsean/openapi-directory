# DepartmentOfLabourGovtOfPunjabPunjab.APIsApi

All URIs are relative to *https://apisetu.gov.in/pblabour/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alsfc**](APIsApi.md#alsfc) | **POST** /alsfc/certificate | Application/ License for Factory
[**clcer**](APIsApi.md#clcer) | **POST** /clcer/certificate | Registration Certificate for Contract Labour License
[**srcer**](APIsApi.md#srcer) | **POST** /srcer/certificate | Registration Certificate of Shops And Commercial Establishment



## alsfc

> alsfc(opts)

Application/ License for Factory

API to verify Application/ License for Factory.

### Example

```javascript
import DepartmentOfLabourGovtOfPunjabPunjab from 'department_of_labour_govt_of_punjab_punjab';
let defaultClient = DepartmentOfLabourGovtOfPunjabPunjab.ApiClient.instance;
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

let apiInstance = new DepartmentOfLabourGovtOfPunjabPunjab.APIsApi();
let opts = {
  'alsfcRequest': new DepartmentOfLabourGovtOfPunjabPunjab.AlsfcRequest() // AlsfcRequest | Request format
};
apiInstance.alsfc(opts, (error, data, response) => {
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
 **alsfcRequest** | [**AlsfcRequest**](AlsfcRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## clcer

> clcer(opts)

Registration Certificate for Contract Labour License

API to verify Registration Certificate for Contract Labour License.

### Example

```javascript
import DepartmentOfLabourGovtOfPunjabPunjab from 'department_of_labour_govt_of_punjab_punjab';
let defaultClient = DepartmentOfLabourGovtOfPunjabPunjab.ApiClient.instance;
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

let apiInstance = new DepartmentOfLabourGovtOfPunjabPunjab.APIsApi();
let opts = {
  'alsfcRequest': new DepartmentOfLabourGovtOfPunjabPunjab.AlsfcRequest() // AlsfcRequest | Request format
};
apiInstance.clcer(opts, (error, data, response) => {
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
 **alsfcRequest** | [**AlsfcRequest**](AlsfcRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## srcer

> srcer(opts)

Registration Certificate of Shops And Commercial Establishment

API to verify Registration Certificate of Shops And Commercial Establishment.

### Example

```javascript
import DepartmentOfLabourGovtOfPunjabPunjab from 'department_of_labour_govt_of_punjab_punjab';
let defaultClient = DepartmentOfLabourGovtOfPunjabPunjab.ApiClient.instance;
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

let apiInstance = new DepartmentOfLabourGovtOfPunjabPunjab.APIsApi();
let opts = {
  'alsfcRequest': new DepartmentOfLabourGovtOfPunjabPunjab.AlsfcRequest() // AlsfcRequest | Request format
};
apiInstance.srcer(opts, (error, data, response) => {
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
 **alsfcRequest** | [**AlsfcRequest**](AlsfcRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

