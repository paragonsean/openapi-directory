# MagentoB2B.GuestCartsCartIdShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestShippingMethodManagementV1GetListGet**](GuestCartsCartIdShippingMethodsApi.md#quoteGuestShippingMethodManagementV1GetListGet) | **GET** /V1/guest-carts/{cartId}/shipping-methods | guest-carts/{cartId}/shipping-methods



## quoteGuestShippingMethodManagementV1GetListGet

> [QuoteDataShippingMethodInterface] quoteGuestShippingMethodManagementV1GetListGet(cartId)

guest-carts/{cartId}/shipping-methods

List applicable shipping methods for a specified quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdShippingMethodsApi();
let cartId = "cartId_example"; // String | The shopping cart ID.
apiInstance.quoteGuestShippingMethodManagementV1GetListGet(cartId, (error, data, response) => {
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
 **cartId** | **String**| The shopping cart ID. | 

### Return type

[**[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

