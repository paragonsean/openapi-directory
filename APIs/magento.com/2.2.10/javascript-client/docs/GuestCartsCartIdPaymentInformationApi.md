# MagentoB2B.GuestCartsCartIdPaymentInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet**](GuestCartsCartIdPaymentInformationApi.md#checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet) | **GET** /V1/guest-carts/{cartId}/payment-information | guest-carts/{cartId}/payment-information
[**checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost**](GuestCartsCartIdPaymentInformationApi.md#checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost) | **POST** /V1/guest-carts/{cartId}/payment-information | guest-carts/{cartId}/payment-information



## checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet

> CheckoutDataPaymentDetailsInterface checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet(cartId)

guest-carts/{cartId}/payment-information

Get payment information

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdPaymentInformationApi();
let cartId = "cartId_example"; // String | 
apiInstance.checkoutGuestPaymentInformationManagementV1GetPaymentInformationGet(cartId, (error, data, response) => {
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

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost

> Number checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(cartId, opts)

guest-carts/{cartId}/payment-information

Set payment information and place order for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdPaymentInformationApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest': new MagentoB2B.CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest() // CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest | 
};
apiInstance.checkoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPost(cartId, opts, (error, data, response) => {
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

