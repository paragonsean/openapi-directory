# Reverb.PaymentMethodsApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentMethodsGet**](PaymentMethodsApi.md#paymentMethodsGet) | **GET** /payment_methods | Get list of payment methods



## paymentMethodsGet

> paymentMethodsGet()

Get list of payment methods

Get list of payment methods

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.PaymentMethodsApi();
apiInstance.paymentMethodsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

