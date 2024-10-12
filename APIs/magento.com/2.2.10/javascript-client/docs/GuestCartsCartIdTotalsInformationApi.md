# MagentoB2B.GuestCartsCartIdTotalsInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutGuestTotalsInformationManagementV1CalculatePost**](GuestCartsCartIdTotalsInformationApi.md#checkoutGuestTotalsInformationManagementV1CalculatePost) | **POST** /V1/guest-carts/{cartId}/totals-information | guest-carts/{cartId}/totals-information



## checkoutGuestTotalsInformationManagementV1CalculatePost

> QuoteDataTotalsInterface checkoutGuestTotalsInformationManagementV1CalculatePost(cartId, opts)

guest-carts/{cartId}/totals-information

Calculate quote totals based on address and shipping method.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdTotalsInformationApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'checkoutTotalsInformationManagementV1CalculatePostRequest': new MagentoB2B.CheckoutTotalsInformationManagementV1CalculatePostRequest() // CheckoutTotalsInformationManagementV1CalculatePostRequest | 
};
apiInstance.checkoutGuestTotalsInformationManagementV1CalculatePost(cartId, opts, (error, data, response) => {
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
 **checkoutTotalsInformationManagementV1CalculatePostRequest** | [**CheckoutTotalsInformationManagementV1CalculatePostRequest**](CheckoutTotalsInformationManagementV1CalculatePostRequest.md)|  | [optional] 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

