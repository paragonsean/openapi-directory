# AccountantsGeneralTripura.APIsApi

All URIs are relative to *https://apisetu.gov.in/agtripura/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pecer**](APIsApi.md#pecer) | **POST** /pecer/certificate | Pension Certificate
[**prfnd**](APIsApi.md#prfnd) | **POST** /prfnd/certificate | Provident Fund



## pecer

> pecer(opts)

Pension Certificate

API to verify Pension Certificate.

### Example

```javascript
import AccountantsGeneralTripura from 'accountants_general_tripura';
let defaultClient = AccountantsGeneralTripura.ApiClient.instance;
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

let apiInstance = new AccountantsGeneralTripura.APIsApi();
let opts = {
  'pecerRequest': new AccountantsGeneralTripura.PecerRequest() // PecerRequest | Request format
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


## prfnd

> prfnd(opts)

Provident Fund

API to verify Provident Fund.

### Example

```javascript
import AccountantsGeneralTripura from 'accountants_general_tripura';
let defaultClient = AccountantsGeneralTripura.ApiClient.instance;
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

let apiInstance = new AccountantsGeneralTripura.APIsApi();
let opts = {
  'pecerRequest': new AccountantsGeneralTripura.PecerRequest() // PecerRequest | Request format
};
apiInstance.prfnd(opts, (error, data, response) => {
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

