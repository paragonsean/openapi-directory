# MinistryOfPetroleumAndNaturalGasIocl.APIsApi

All URIs are relative to *https://apisetu.gov.in/iocl/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lpgsv**](APIsApi.md#lpgsv) | **POST** /lpgsv/certificate | LPG Subscription Voucher
[**lpgtv**](APIsApi.md#lpgtv) | **POST** /lpgtv/certificate | Termination Voucher



## lpgsv

> lpgsv(opts)

LPG Subscription Voucher

API to verify LPG Subscription Voucher.

### Example

```javascript
import MinistryOfPetroleumAndNaturalGasIocl from 'ministry_of_petroleum_and_natural_gas__iocl';
let defaultClient = MinistryOfPetroleumAndNaturalGasIocl.ApiClient.instance;
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

let apiInstance = new MinistryOfPetroleumAndNaturalGasIocl.APIsApi();
let opts = {
  'lpgsvRequest': new MinistryOfPetroleumAndNaturalGasIocl.LpgsvRequest() // LpgsvRequest | Request format
};
apiInstance.lpgsv(opts, (error, data, response) => {
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
 **lpgsvRequest** | [**LpgsvRequest**](LpgsvRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## lpgtv

> lpgtv(opts)

Termination Voucher

API to verify Termination Voucher.

### Example

```javascript
import MinistryOfPetroleumAndNaturalGasIocl from 'ministry_of_petroleum_and_natural_gas__iocl';
let defaultClient = MinistryOfPetroleumAndNaturalGasIocl.ApiClient.instance;
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

let apiInstance = new MinistryOfPetroleumAndNaturalGasIocl.APIsApi();
let opts = {
  'lpgsvRequest': new MinistryOfPetroleumAndNaturalGasIocl.LpgsvRequest() // LpgsvRequest | Request format
};
apiInstance.lpgtv(opts, (error, data, response) => {
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
 **lpgsvRequest** | [**LpgsvRequest**](LpgsvRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

