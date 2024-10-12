# MagentoB2B.CartsCartIdEstimateShippingMethodsByAddressIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdEstimateShippingMethodsByAddressIdPost**](CartsCartIdEstimateShippingMethodsByAddressIdApi.md#v1CartsCartIdEstimateShippingMethodsByAddressIdPost) | **POST** /V1/carts/{cartId}/estimate-shipping-methods-by-address-id | carts/{cartId}/estimate-shipping-methods-by-address-id



## v1CartsCartIdEstimateShippingMethodsByAddressIdPost

> [QuoteDataShippingMethodInterface] v1CartsCartIdEstimateShippingMethodsByAddressIdPost(cartId, opts)

carts/{cartId}/estimate-shipping-methods-by-address-id

Estimate shipping

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdEstimateShippingMethodsByAddressIdApi();
let cartId = 56; // Number | The shopping cart ID.
let opts = {
  'quoteShippingMethodManagementV1EstimateByAddressIdPostRequest': new MagentoB2B.QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest() // QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest | 
};
apiInstance.v1CartsCartIdEstimateShippingMethodsByAddressIdPost(cartId, opts, (error, data, response) => {
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
 **cartId** | **Number**| The shopping cart ID. | 
 **quoteShippingMethodManagementV1EstimateByAddressIdPostRequest** | [**QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest**](QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest.md)|  | [optional] 

### Return type

[**[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

