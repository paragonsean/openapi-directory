# MagentoB2B.CartsMineCheckoutFieldsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost**](CartsMineCheckoutFieldsApi.md#temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost) | **POST** /V1/carts/mine/checkout-fields | carts/mine/checkout-fields



## temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost

> ErrorResponse temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost(opts)

carts/mine/checkout-fields



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineCheckoutFieldsApi();
let opts = {
  'temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest': new MagentoB2B.TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest() // TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest | 
};
apiInstance.temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost(opts, (error, data, response) => {
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
 **temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest** | [**TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest**](TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest.md)|  | [optional] 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

