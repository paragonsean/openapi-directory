# MagentoB2B.GuestCartsCartIdCheckoutFieldsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost**](GuestCartsCartIdCheckoutFieldsApi.md#temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost) | **POST** /V1/guest-carts/{cartId}/checkout-fields | guest-carts/{cartId}/checkout-fields



## temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost

> ErrorResponse temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost(cartId, opts)

guest-carts/{cartId}/checkout-fields



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdCheckoutFieldsApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest': new MagentoB2B.TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest() // TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest | 
};
apiInstance.temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost(cartId, opts, (error, data, response) => {
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
 **cartId** | **String**|  | 
 **temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest** | [**TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest**](TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest.md)|  | [optional] 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

