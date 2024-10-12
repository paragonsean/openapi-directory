# MagentoB2B.NegotiableCartsCartIdShippingInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost**](NegotiableCartsCartIdShippingInformationApi.md#negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost) | **POST** /V1/negotiable-carts/{cartId}/shipping-information | negotiable-carts/{cartId}/shipping-information



## negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost

> CheckoutDataPaymentDetailsInterface negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost(cartId, opts)

negotiable-carts/{cartId}/shipping-information



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdShippingInformationApi();
let cartId = 56; // Number | 
let opts = {
  'checkoutShippingInformationManagementV1SaveAddressInformationPostRequest': new MagentoB2B.CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest() // CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest | 
};
apiInstance.negotiableQuoteShippingInformationManagementV1SaveAddressInformationPost(cartId, opts, (error, data, response) => {
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

