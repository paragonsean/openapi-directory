# DepartmentOfItAndBtKarnataka.APIsApi

All URIs are relative to *https://apisetu.gov.in/ktech/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cocer**](APIsApi.md#cocer) | **POST** /cocer/certificate | Company Related Certificate
[**rfcer**](APIsApi.md#rfcer) | **POST** /rfcer/certificate | Registration Certificate of Firm/ Company



## cocer

> cocer(opts)

Company Related Certificate

API to verify Company Related Certificate.

### Example

```javascript
import DepartmentOfItAndBtKarnataka from 'department_of_it_and_bt_karnataka';
let defaultClient = DepartmentOfItAndBtKarnataka.ApiClient.instance;
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

let apiInstance = new DepartmentOfItAndBtKarnataka.APIsApi();
let opts = {
  'cocerRequest': new DepartmentOfItAndBtKarnataka.CocerRequest() // CocerRequest | Request format
};
apiInstance.cocer(opts, (error, data, response) => {
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
 **cocerRequest** | [**CocerRequest**](CocerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## rfcer

> rfcer(opts)

Registration Certificate of Firm/ Company

API to verify Registration Certificate of Firm/ Company.

### Example

```javascript
import DepartmentOfItAndBtKarnataka from 'department_of_it_and_bt_karnataka';
let defaultClient = DepartmentOfItAndBtKarnataka.ApiClient.instance;
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

let apiInstance = new DepartmentOfItAndBtKarnataka.APIsApi();
let opts = {
  'cocerRequest': new DepartmentOfItAndBtKarnataka.CocerRequest() // CocerRequest | Request format
};
apiInstance.rfcer(opts, (error, data, response) => {
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
 **cocerRequest** | [**CocerRequest**](CocerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

