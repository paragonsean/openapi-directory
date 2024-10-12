# MagentoB2B.NegotiableCartsCartIdPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet**](NegotiableCartsCartIdPaymentInformationApi.md#negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet) | **GET** /V1/negotiable-carts/{cartId}/payment-information | negotiable-carts/{cartId}/payment-information
[**negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost**](NegotiableCartsCartIdPaymentInformationApi.md#negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost) | **POST** /V1/negotiable-carts/{cartId}/payment-information | negotiable-carts/{cartId}/payment-information



## negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet

> CheckoutDataPaymentDetailsInterface negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet(cartId)

negotiable-carts/{cartId}/payment-information

Get payment information

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdPaymentInformationApi();
let cartId = 56; // Number | 
apiInstance.negotiableQuotePaymentInformationManagementV1GetPaymentInformationGet(cartId, (error, data, response) => {
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

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost

> Number negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(cartId, opts)

negotiable-carts/{cartId}/payment-information

Set payment information and place order for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdPaymentInformationApi();
let cartId = 56; // Number | 
let opts = {
  'checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest': new MagentoB2B.CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest() // CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
};
apiInstance.negotiableQuotePaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(cartId, opts, (error, data, response) => {
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

