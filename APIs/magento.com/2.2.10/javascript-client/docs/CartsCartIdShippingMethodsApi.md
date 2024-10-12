# MagentoB2B.CartsCartIdShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdShippingMethodsGet**](CartsCartIdShippingMethodsApi.md#v1CartsCartIdShippingMethodsGet) | **GET** /V1/carts/{cartId}/shipping-methods | carts/{cartId}/shipping-methods



## v1CartsCartIdShippingMethodsGet

> [QuoteDataShippingMethodInterface] v1CartsCartIdShippingMethodsGet(cartId)

carts/{cartId}/shipping-methods

Lists applicable shipping methods for a specified quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdShippingMethodsApi();
let cartId = 56; // Number | The shopping cart ID.
apiInstance.v1CartsCartIdShippingMethodsGet(cartId, (error, data, response) => {
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
 **cartId** | **Number**| The shopping cart ID. | 

### Return type

[**[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

