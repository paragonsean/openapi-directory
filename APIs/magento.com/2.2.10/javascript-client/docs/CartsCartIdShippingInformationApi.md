# MagentoB2B.CartsCartIdShippingInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdShippingInformationPost**](CartsCartIdShippingInformationApi.md#v1CartsCartIdShippingInformationPost) | **POST** /V1/carts/{cartId}/shipping-information | carts/{cartId}/shipping-information



## v1CartsCartIdShippingInformationPost

> CheckoutDataPaymentDetailsInterface v1CartsCartIdShippingInformationPost(cartId, opts)

carts/{cartId}/shipping-information



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdShippingInformationApi();
let cartId = 56; // Number | 
let opts = {
  'checkoutShippingInformationManagementV1SaveAddressInformationPostRequest': new MagentoB2B.CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest() // CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest | 
};
apiInstance.v1CartsCartIdShippingInformationPost(cartId, opts, (error, data, response) => {
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
 **cartId** | **Number**|  | 
 **checkoutShippingInformationManagementV1SaveAddressInformationPostRequest** | [**CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest**](CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest.md)|  | [optional] 

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

