# MagentoB2B.CartsCartIdSelectedPaymentMethodApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdSelectedPaymentMethodGet**](CartsCartIdSelectedPaymentMethodApi.md#v1CartsCartIdSelectedPaymentMethodGet) | **GET** /V1/carts/{cartId}/selected-payment-method | carts/{cartId}/selected-payment-method
[**v1CartsCartIdSelectedPaymentMethodPut**](CartsCartIdSelectedPaymentMethodApi.md#v1CartsCartIdSelectedPaymentMethodPut) | **PUT** /V1/carts/{cartId}/selected-payment-method | carts/{cartId}/selected-payment-method



## v1CartsCartIdSelectedPaymentMethodGet

> QuoteDataPaymentInterface v1CartsCartIdSelectedPaymentMethodGet(cartId)

carts/{cartId}/selected-payment-method

Returns the payment method for a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdSelectedPaymentMethodApi();
let cartId = 56; // Number | The cart ID.
apiInstance.v1CartsCartIdSelectedPaymentMethodGet(cartId, (error, data, response) => {
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
 **cartId** | **Number**| The cart ID. | 

### Return type

[**QuoteDataPaymentInterface**](QuoteDataPaymentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CartsCartIdSelectedPaymentMethodPut

> String v1CartsCartIdSelectedPaymentMethodPut(cartId, opts)

carts/{cartId}/selected-payment-method

Adds a specified payment method to a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdSelectedPaymentMethodApi();
let cartId = 56; // Number | The cart ID.
let opts = {
  'quotePaymentMethodManagementV1SetPutRequest': new MagentoB2B.QuotePaymentMethodManagementV1SetPutRequest() // QuotePaymentMethodManagementV1SetPutRequest | 
};
apiInstance.v1CartsCartIdSelectedPaymentMethodPut(cartId, opts, (error, data, response) => {
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
 **cartId** | **Number**| The cart ID. | 
 **quotePaymentMethodManagementV1SetPutRequest** | [**QuotePaymentMethodManagementV1SetPutRequest**](QuotePaymentMethodManagementV1SetPutRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

