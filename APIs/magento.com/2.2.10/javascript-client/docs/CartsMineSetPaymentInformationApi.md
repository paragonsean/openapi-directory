# MagentoB2B.CartsMineSetPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutPaymentInformationManagementV1SavePaymentInformationPost**](CartsMineSetPaymentInformationApi.md#checkoutPaymentInformationManagementV1SavePaymentInformationPost) | **POST** /V1/carts/mine/set-payment-information | carts/mine/set-payment-information



## checkoutPaymentInformationManagementV1SavePaymentInformationPost

> Number checkoutPaymentInformationManagementV1SavePaymentInformationPost(opts)

carts/mine/set-payment-information

Set payment information for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineSetPaymentInformationApi();
let opts = {
  'checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest': new MagentoB2B.CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest() // CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
};
apiInstance.checkoutPaymentInformationManagementV1SavePaymentInformationPost(opts, (error, data, response) => {
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
 **checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest** | [**CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest**](CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

