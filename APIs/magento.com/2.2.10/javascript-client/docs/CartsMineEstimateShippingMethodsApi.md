# MagentoB2B.CartsMineEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteShipmentEstimationV1EstimateByExtendedAddressPost**](CartsMineEstimateShippingMethodsApi.md#quoteShipmentEstimationV1EstimateByExtendedAddressPost) | **POST** /V1/carts/mine/estimate-shipping-methods | carts/mine/estimate-shipping-methods



## quoteShipmentEstimationV1EstimateByExtendedAddressPost

> [QuoteDataShippingMethodInterface] quoteShipmentEstimationV1EstimateByExtendedAddressPost(opts)

carts/mine/estimate-shipping-methods

Estimate shipping by address and return list of available shipping methods

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineEstimateShippingMethodsApi();
let opts = {
  'quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest': new MagentoB2B.QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest() // QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest | 
};
apiInstance.quoteShipmentEstimationV1EstimateByExtendedAddressPost(opts, (error, data, response) => {
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
 **quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest** | [**QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest**](QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest.md)|  | [optional] 

### Return type

[**[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

