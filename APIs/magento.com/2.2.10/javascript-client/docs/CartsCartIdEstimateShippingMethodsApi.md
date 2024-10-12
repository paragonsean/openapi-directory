# MagentoB2B.CartsCartIdEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdEstimateShippingMethodsPost**](CartsCartIdEstimateShippingMethodsApi.md#v1CartsCartIdEstimateShippingMethodsPost) | **POST** /V1/carts/{cartId}/estimate-shipping-methods | carts/{cartId}/estimate-shipping-methods



## v1CartsCartIdEstimateShippingMethodsPost

> [QuoteDataShippingMethodInterface] v1CartsCartIdEstimateShippingMethodsPost(cartId, opts)

carts/{cartId}/estimate-shipping-methods

Estimate shipping by address and return list of available shipping methods

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdEstimateShippingMethodsApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest': new MagentoB2B.QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest() // QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest | 
};
apiInstance.v1CartsCartIdEstimateShippingMethodsPost(cartId, opts, (error, data, response) => {
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
 **quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest** | [**QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest**](QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest.md)|  | [optional] 

### Return type

[**[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

