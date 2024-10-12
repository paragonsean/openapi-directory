# MagentoB2B.CartsMineSelectedPaymentMethodApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotePaymentMethodManagementV1GetGet**](CartsMineSelectedPaymentMethodApi.md#quotePaymentMethodManagementV1GetGet) | **GET** /V1/carts/mine/selected-payment-method | carts/mine/selected-payment-method
[**quotePaymentMethodManagementV1SetPut**](CartsMineSelectedPaymentMethodApi.md#quotePaymentMethodManagementV1SetPut) | **PUT** /V1/carts/mine/selected-payment-method | carts/mine/selected-payment-method



## quotePaymentMethodManagementV1GetGet

> QuoteDataPaymentInterface quotePaymentMethodManagementV1GetGet()

carts/mine/selected-payment-method

Returns the payment method for a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineSelectedPaymentMethodApi();
apiInstance.quotePaymentMethodManagementV1GetGet((error, data, response) => {
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

[**QuoteDataPaymentInterface**](QuoteDataPaymentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quotePaymentMethodManagementV1SetPut

> String quotePaymentMethodManagementV1SetPut(opts)

carts/mine/selected-payment-method

Adds a specified payment method to a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineSelectedPaymentMethodApi();
let opts = {
  'quotePaymentMethodManagementV1SetPutRequest': new MagentoB2B.QuotePaymentMethodManagementV1SetPutRequest() // QuotePaymentMethodManagementV1SetPutRequest | 
};
apiInstance.quotePaymentMethodManagementV1SetPut(opts, (error, data, response) => {
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
 **quotePaymentMethodManagementV1SetPutRequest** | [**QuotePaymentMethodManagementV1SetPutRequest**](QuotePaymentMethodManagementV1SetPutRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

