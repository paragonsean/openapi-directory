# Taxamo.PaymentsApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capturePayment**](PaymentsApi.md#capturePayment) | **POST** /api/v1/transactions/{key}/payments/capture | Capture payment
[**createPayment**](PaymentsApi.md#createPayment) | **POST** /api/v1/transactions/{key}/payments | Register a payment
[**listPayments**](PaymentsApi.md#listPayments) | **GET** /api/v1/transactions/{key}/payments | List payments



## capturePayment

> CapturePaymentOut capturePayment(key)

Capture payment

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.PaymentsApi();
let key = "key_example"; // String | Transaction key.
apiInstance.capturePayment(key, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 

### Return type

[**CapturePaymentOut**](CapturePaymentOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createPayment

> CreatePaymentOut createPayment(key, input)

Register a payment

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.PaymentsApi();
let key = "key_example"; // String | Transaction key.
let input = new Taxamo.CreatePaymentIn(); // CreatePaymentIn | Input
apiInstance.createPayment(key, input, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 
 **input** | [**CreatePaymentIn**](CreatePaymentIn.md)| Input | 

### Return type

[**CreatePaymentOut**](CreatePaymentOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPayments

> ListPaymentsOut listPayments(key, opts)

List payments

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.PaymentsApi();
let key = "key_example"; // String | Transaction key.
let opts = {
  'limit': "limit_example", // String | Max record count (no more than 100, defaults to 10).
  'offset': "offset_example" // String | How many records need to be skipped, defaults to 0.
};
apiInstance.listPayments(key, opts, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 
 **limit** | **String**| Max record count (no more than 100, defaults to 10). | [optional] 
 **offset** | **String**| How many records need to be skipped, defaults to 0. | [optional] 

### Return type

[**ListPaymentsOut**](ListPaymentsOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

