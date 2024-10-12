# EmployeesProvidentFundOrganization.APIsApi

All URIs are relative to *https://apisetu.gov.in/epfindia/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**epfsc**](APIsApi.md#epfsc) | **POST** /epfsc/certificate | Scheme Certificate
[**pecer**](APIsApi.md#pecer) | **POST** /pecer/certificate | Pension Certificate
[**uncrd**](APIsApi.md#uncrd) | **POST** /uncrd/certificate | UAN Card



## epfsc

> epfsc(opts)

Scheme Certificate

API to verify Scheme Certificate.

### Example

```javascript
import EmployeesProvidentFundOrganization from 'employees_provident_fund_organization';
let defaultClient = EmployeesProvidentFundOrganization.ApiClient.instance;
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

let apiInstance = new EmployeesProvidentFundOrganization.APIsApi();
let opts = {
  'epfscRequest': new EmployeesProvidentFundOrganization.EpfscRequest() // EpfscRequest | Request format
};
apiInstance.epfsc(opts, (error, data, response) => {
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
 **epfscRequest** | [**EpfscRequest**](EpfscRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## pecer

> pecer(opts)

Pension Certificate

API to verify Pension Certificate.

### Example

```javascript
import EmployeesProvidentFundOrganization from 'employees_provident_fund_organization';
let defaultClient = EmployeesProvidentFundOrganization.ApiClient.instance;
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

let apiInstance = new EmployeesProvidentFundOrganization.APIsApi();
let opts = {
  'pecerRequest': new EmployeesProvidentFundOrganization.PecerRequest() // PecerRequest | Request format
};
apiInstance.pecer(opts, (error, data, response) => {
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
 **pecerRequest** | [**PecerRequest**](PecerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## uncrd

> uncrd(opts)

UAN Card

API to verify UAN Card.

### Example

```javascript
import EmployeesProvidentFundOrganization from 'employees_provident_fund_organization';
let defaultClient = EmployeesProvidentFundOrganization.ApiClient.instance;
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

let apiInstance = new EmployeesProvidentFundOrganization.APIsApi();
let opts = {
  'uncrdRequest': new EmployeesProvidentFundOrganization.UncrdRequest() // UncrdRequest | Request format
};
apiInstance.uncrd(opts, (error, data, response) => {
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
 **uncrdRequest** | [**UncrdRequest**](UncrdRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

