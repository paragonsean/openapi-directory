# MagentoB2B.CartsCartIdTotalsInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdTotalsInformationPost**](CartsCartIdTotalsInformationApi.md#v1CartsCartIdTotalsInformationPost) | **POST** /V1/carts/{cartId}/totals-information | carts/{cartId}/totals-information



## v1CartsCartIdTotalsInformationPost

> QuoteDataTotalsInterface v1CartsCartIdTotalsInformationPost(cartId, opts)

carts/{cartId}/totals-information

Calculate quote totals based on address and shipping method.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdTotalsInformationApi();
let cartId = 56; // Number | 
let opts = {
  'checkoutTotalsInformationManagementV1CalculatePostRequest': new MagentoB2B.CheckoutTotalsInformationManagementV1CalculatePostRequest() // CheckoutTotalsInformationManagementV1CalculatePostRequest | 
};
apiInstance.v1CartsCartIdTotalsInformationPost(cartId, opts, (error, data, response) => {
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
 **checkoutTotalsInformationManagementV1CalculatePostRequest** | [**CheckoutTotalsInformationManagementV1CalculatePostRequest**](CheckoutTotalsInformationManagementV1CalculatePostRequest.md)|  | [optional] 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

