# MagentoB2B.GuestCartsCartIdSetPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost**](GuestCartsCartIdSetPaymentInformationApi.md#checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost) | **POST** /V1/guest-carts/{cartId}/set-payment-information | guest-carts/{cartId}/set-payment-information



## checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost

> Number checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost(cartId, opts)

guest-carts/{cartId}/set-payment-information

Set payment information for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdSetPaymentInformationApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest': new MagentoB2B.CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest() // CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
};
apiInstance.checkoutGuestPaymentInformationManagementV1SavePaymentInformationPost(cartId, opts, (error, data, response) => {
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
 **checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest** | [**CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest**](CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

