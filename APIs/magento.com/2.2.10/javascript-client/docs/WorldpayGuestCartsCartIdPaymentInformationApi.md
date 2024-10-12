# MagentoB2B.WorldpayGuestCartsCartIdPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**worldpayGuestPaymentInformationManagementProxyV1SavePaymentInformationAndPlaceOrderPost**](WorldpayGuestCartsCartIdPaymentInformationApi.md#worldpayGuestPaymentInformationManagementProxyV1SavePaymentInformationAndPlaceOrderPost) | **POST** /V1/worldpay-guest-carts/{cartId}/payment-information | worldpay-guest-carts/{cartId}/payment-information



## worldpayGuestPaymentInformationManagementProxyV1SavePaymentInformationAndPlaceOrderPost

> Number worldpayGuestPaymentInformationManagementProxyV1SavePaymentInformationAndPlaceOrderPost(cartId, opts)

worldpay-guest-carts/{cartId}/payment-information

Proxy handler for guest place order

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.WorldpayGuestCartsCartIdPaymentInformationApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest': new MagentoB2B.CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest() // CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
};
apiInstance.worldpayGuestPaymentInformationManagementProxyV1SavePaymentInformationAndPlaceOrderPost(cartId, opts, (error, data, response) => {
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

