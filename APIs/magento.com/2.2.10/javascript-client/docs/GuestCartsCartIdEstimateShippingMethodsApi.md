# MagentoB2B.GuestCartsCartIdEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestShipmentEstimationV1EstimateByExtendedAddressPost**](GuestCartsCartIdEstimateShippingMethodsApi.md#quoteGuestShipmentEstimationV1EstimateByExtendedAddressPost) | **POST** /V1/guest-carts/{cartId}/estimate-shipping-methods | guest-carts/{cartId}/estimate-shipping-methods



## quoteGuestShipmentEstimationV1EstimateByExtendedAddressPost

> [QuoteDataShippingMethodInterface] quoteGuestShipmentEstimationV1EstimateByExtendedAddressPost(cartId, opts)

guest-carts/{cartId}/estimate-shipping-methods

Estimate shipping by address and return list of available shipping methods

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdEstimateShippingMethodsApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'quoteShipmentEstimationV1EstimateByExtendedAddressPostRequest': new MagentoB2B.QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest() // QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest | 
};
apiInstance.quoteGuestShipmentEstimationV1EstimateByExtendedAddressPost(cartId, opts, (error, data, response) => {
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

