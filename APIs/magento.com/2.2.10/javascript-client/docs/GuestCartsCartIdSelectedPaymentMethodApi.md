# MagentoB2B.GuestCartsCartIdSelectedPaymentMethodApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestPaymentMethodManagementV1GetGet**](GuestCartsCartIdSelectedPaymentMethodApi.md#quoteGuestPaymentMethodManagementV1GetGet) | **GET** /V1/guest-carts/{cartId}/selected-payment-method | guest-carts/{cartId}/selected-payment-method
[**quoteGuestPaymentMethodManagementV1SetPut**](GuestCartsCartIdSelectedPaymentMethodApi.md#quoteGuestPaymentMethodManagementV1SetPut) | **PUT** /V1/guest-carts/{cartId}/selected-payment-method | guest-carts/{cartId}/selected-payment-method



## quoteGuestPaymentMethodManagementV1GetGet

> QuoteDataPaymentInterface quoteGuestPaymentMethodManagementV1GetGet(cartId)

guest-carts/{cartId}/selected-payment-method

Return the payment method for a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdSelectedPaymentMethodApi();
let cartId = "cartId_example"; // String | The cart ID.
apiInstance.quoteGuestPaymentMethodManagementV1GetGet(cartId, (error, data, response) => {
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
 **cartId** | **String**| The cart ID. | 

### Return type

[**QuoteDataPaymentInterface**](QuoteDataPaymentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteGuestPaymentMethodManagementV1SetPut

> Number quoteGuestPaymentMethodManagementV1SetPut(cartId, opts)

guest-carts/{cartId}/selected-payment-method

Add a specified payment method to a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdSelectedPaymentMethodApi();
let cartId = "cartId_example"; // String | The cart ID.
let opts = {
  'quotePaymentMethodManagementV1SetPutRequest': new MagentoB2B.QuotePaymentMethodManagementV1SetPutRequest() // QuotePaymentMethodManagementV1SetPutRequest | 
};
apiInstance.quoteGuestPaymentMethodManagementV1SetPut(cartId, opts, (error, data, response) => {
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
 **cartId** | **String**| The cart ID. | 
 **quotePaymentMethodManagementV1SetPutRequest** | [**QuotePaymentMethodManagementV1SetPutRequest**](QuotePaymentMethodManagementV1SetPutRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

