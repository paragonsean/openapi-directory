# MagentoB2B.GuestCartsCartIdPaymentMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestPaymentMethodManagementV1GetListGet**](GuestCartsCartIdPaymentMethodsApi.md#quoteGuestPaymentMethodManagementV1GetListGet) | **GET** /V1/guest-carts/{cartId}/payment-methods | guest-carts/{cartId}/payment-methods



## quoteGuestPaymentMethodManagementV1GetListGet

> [QuoteDataPaymentMethodInterface] quoteGuestPaymentMethodManagementV1GetListGet(cartId)

guest-carts/{cartId}/payment-methods

List available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#GuestPaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdPaymentMethodsApi();
let cartId = "cartId_example"; // String | The cart ID.
apiInstance.quoteGuestPaymentMethodManagementV1GetListGet(cartId, (error, data, response) => {
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

[**[QuoteDataPaymentMethodInterface]**](QuoteDataPaymentMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

