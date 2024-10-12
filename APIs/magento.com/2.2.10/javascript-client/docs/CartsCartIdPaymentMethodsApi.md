# MagentoB2B.CartsCartIdPaymentMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdPaymentMethodsGet**](CartsCartIdPaymentMethodsApi.md#v1CartsCartIdPaymentMethodsGet) | **GET** /V1/carts/{cartId}/payment-methods | carts/{cartId}/payment-methods



## v1CartsCartIdPaymentMethodsGet

> [QuoteDataPaymentMethodInterface] v1CartsCartIdPaymentMethodsGet(cartId)

carts/{cartId}/payment-methods

Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdPaymentMethodsApi();
let cartId = 56; // Number | The cart ID.
apiInstance.v1CartsCartIdPaymentMethodsGet(cartId, (error, data, response) => {
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

[**[QuoteDataPaymentMethodInterface]**](QuoteDataPaymentMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

