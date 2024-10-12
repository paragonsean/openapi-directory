# Apacta.PaymentTermTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentTermTypesGet**](PaymentTermTypesApi.md#paymentTermTypesGet) | **GET** /payment_term_types | Get a list of payment term types
[**paymentTermTypesPaymentTermTypeIdGet**](PaymentTermTypesApi.md#paymentTermTypesPaymentTermTypeIdGet) | **GET** /payment_term_types/{payment_term_type_id} | Details of 1 payment term type



## paymentTermTypesGet

> PaymentTermTypesGet200Response paymentTermTypesGet()

Get a list of payment term types

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.PaymentTermTypesApi();
apiInstance.paymentTermTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PaymentTermTypesGet200Response**](PaymentTermTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentTermTypesPaymentTermTypeIdGet

> PaymentTermTypesPaymentTermTypeIdGet200Response paymentTermTypesPaymentTermTypeIdGet(paymentTermTypeId)

Details of 1 payment term type

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.PaymentTermTypesApi();
let paymentTermTypeId = "paymentTermTypeId_example"; // String | 
apiInstance.paymentTermTypesPaymentTermTypeIdGet(paymentTermTypeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentTermTypeId** | **String**|  | 

### Return type

[**PaymentTermTypesPaymentTermTypeIdGet200Response**](PaymentTermTypesPaymentTermTypeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

