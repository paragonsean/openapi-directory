# MagentoB2B.GuestCartsCartIdShippingInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutGuestShippingInformationManagementV1SaveAddressInformationPost**](GuestCartsCartIdShippingInformationApi.md#checkoutGuestShippingInformationManagementV1SaveAddressInformationPost) | **POST** /V1/guest-carts/{cartId}/shipping-information | guest-carts/{cartId}/shipping-information



## checkoutGuestShippingInformationManagementV1SaveAddressInformationPost

> CheckoutDataPaymentDetailsInterface checkoutGuestShippingInformationManagementV1SaveAddressInformationPost(cartId, opts)

guest-carts/{cartId}/shipping-information



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdShippingInformationApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'checkoutShippingInformationManagementV1SaveAddressInformationPostRequest': new MagentoB2B.CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest() // CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest | 
};
apiInstance.checkoutGuestShippingInformationManagementV1SaveAddressInformationPost(cartId, opts, (error, data, response) => {
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
 **checkoutShippingInformationManagementV1SaveAddressInformationPostRequest** | [**CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest**](CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest.md)|  | [optional] 

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

