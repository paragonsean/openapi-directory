# MagentoB2B.CartsMineShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteShippingMethodManagementV1GetListGet**](CartsMineShippingMethodsApi.md#quoteShippingMethodManagementV1GetListGet) | **GET** /V1/carts/mine/shipping-methods | carts/mine/shipping-methods



## quoteShippingMethodManagementV1GetListGet

> [QuoteDataShippingMethodInterface] quoteShippingMethodManagementV1GetListGet()

carts/mine/shipping-methods

Lists applicable shipping methods for a specified quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineShippingMethodsApi();
apiInstance.quoteShippingMethodManagementV1GetListGet((error, data, response) => {
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

[**[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

