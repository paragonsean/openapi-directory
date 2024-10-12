# MagentoB2B.CartsMineDeliveryOptionApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingQuoteCartDeliveryOptionManagementV1SavePost**](CartsMineDeliveryOptionApi.md#temandoShippingQuoteCartDeliveryOptionManagementV1SavePost) | **POST** /V1/carts/mine/delivery-option | carts/mine/delivery-option



## temandoShippingQuoteCartDeliveryOptionManagementV1SavePost

> ErrorResponse temandoShippingQuoteCartDeliveryOptionManagementV1SavePost(opts)

carts/mine/delivery-option

Handle selected delivery option.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineDeliveryOptionApi();
let opts = {
  'temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest': new MagentoB2B.TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest() // TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest | 
};
apiInstance.temandoShippingQuoteCartDeliveryOptionManagementV1SavePost(opts, (error, data, response) => {
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
 **temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest** | [**TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest**](TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest.md)|  | [optional] 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

