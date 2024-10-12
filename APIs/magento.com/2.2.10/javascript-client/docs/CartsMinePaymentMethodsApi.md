# MagentoB2B.CartsMinePaymentMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotePaymentMethodManagementV1GetListGet**](CartsMinePaymentMethodsApi.md#quotePaymentMethodManagementV1GetListGet) | **GET** /V1/carts/mine/payment-methods | carts/mine/payment-methods



## quotePaymentMethodManagementV1GetListGet

> [QuoteDataPaymentMethodInterface] quotePaymentMethodManagementV1GetListGet()

carts/mine/payment-methods

Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMinePaymentMethodsApi();
apiInstance.quotePaymentMethodManagementV1GetListGet((error, data, response) => {
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

[**[QuoteDataPaymentMethodInterface]**](QuoteDataPaymentMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

