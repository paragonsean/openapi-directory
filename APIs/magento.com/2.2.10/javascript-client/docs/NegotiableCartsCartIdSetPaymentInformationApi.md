# MagentoB2B.NegotiableCartsCartIdSetPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost**](NegotiableCartsCartIdSetPaymentInformationApi.md#negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost) | **POST** /V1/negotiable-carts/{cartId}/set-payment-information | negotiable-carts/{cartId}/set-payment-information



## negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost

> Number negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost(cartId, opts)

negotiable-carts/{cartId}/set-payment-information

Set payment information for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdSetPaymentInformationApi();
let cartId = 56; // Number | 
let opts = {
  'checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest': new MagentoB2B.CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest() // CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
};
apiInstance.negotiableQuotePaymentInformationManagementV1SavePaymentInformationPost(cartId, opts, (error, data, response) => {
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
 **checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest** | [**CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest**](CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

