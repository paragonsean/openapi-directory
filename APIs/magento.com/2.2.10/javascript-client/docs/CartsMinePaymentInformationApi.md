# MagentoB2B.CartsMinePaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutPaymentInformationManagementV1GetPaymentInformationGet**](CartsMinePaymentInformationApi.md#checkoutPaymentInformationManagementV1GetPaymentInformationGet) | **GET** /V1/carts/mine/payment-information | carts/mine/payment-information
[**checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost**](CartsMinePaymentInformationApi.md#checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost) | **POST** /V1/carts/mine/payment-information | carts/mine/payment-information



## checkoutPaymentInformationManagementV1GetPaymentInformationGet

> CheckoutDataPaymentDetailsInterface checkoutPaymentInformationManagementV1GetPaymentInformationGet()

carts/mine/payment-information

Get payment information

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMinePaymentInformationApi();
apiInstance.checkoutPaymentInformationManagementV1GetPaymentInformationGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost

> Number checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(opts)

carts/mine/payment-information

Set payment information and place order for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMinePaymentInformationApi();
let opts = {
  'checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest': new MagentoB2B.CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest() // CheckoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
};
apiInstance.checkoutPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(opts, (error, data, response) => {
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

