# MagentoB2B.GuestCartsCartIdDeliveryOptionApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost**](GuestCartsCartIdDeliveryOptionApi.md#temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost) | **POST** /V1/guest-carts/{cartId}/delivery-option | guest-carts/{cartId}/delivery-option



## temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost

> ErrorResponse temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost(cartId, opts)

guest-carts/{cartId}/delivery-option

Handle selected delivery option.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdDeliveryOptionApi();
let cartId = "cartId_example"; // String | The shopping cart ID.
let opts = {
  'temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest': new MagentoB2B.TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest() // TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest | 
};
apiInstance.temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost(cartId, opts, (error, data, response) => {
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
 **temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest** | [**TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest**](TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest.md)|  | [optional] 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

