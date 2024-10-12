# MagentoB2B.NegotiableCartsCartIdEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPost**](NegotiableCartsCartIdEstimateShippingMethodsApi.md#negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPost) | **POST** /V1/negotiable-carts/{cartId}/estimate-shipping-methods | negotiable-carts/{cartId}/estimate-shipping-methods



## negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPost

> [QuoteDataShippingMethodInterface] negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPost(cartId, opts)

negotiable-carts/{cartId}/estimate-shipping-methods

Estimate shipping by address and return list of available shipping methods

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdEstimateShippingMethodsApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest': new MagentoB2B.QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest() // QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest | 
};
apiInstance.negotiableQuoteShipmentEstimationV1EstimateByExtendedAddressPost(cartId, opts, (error, data, response) => {
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

