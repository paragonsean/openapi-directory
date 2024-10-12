# MagentoB2B.CartsMineShippingInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutShippingInformationManagementV1SaveAddressInformationPost**](CartsMineShippingInformationApi.md#checkoutShippingInformationManagementV1SaveAddressInformationPost) | **POST** /V1/carts/mine/shipping-information | carts/mine/shipping-information



## checkoutShippingInformationManagementV1SaveAddressInformationPost

> CheckoutDataPaymentDetailsInterface checkoutShippingInformationManagementV1SaveAddressInformationPost(opts)

carts/mine/shipping-information



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineShippingInformationApi();
let opts = {
  'checkoutShippingInformationManagementV1SaveAddressInformationPostRequest': new MagentoB2B.CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest() // CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest | 
};
apiInstance.checkoutShippingInformationManagementV1SaveAddressInformationPost(opts, (error, data, response) => {
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
 **checkoutShippingInformationManagementV1SaveAddressInformationPostRequest** | [**CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest**](CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest.md)|  | [optional] 

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

