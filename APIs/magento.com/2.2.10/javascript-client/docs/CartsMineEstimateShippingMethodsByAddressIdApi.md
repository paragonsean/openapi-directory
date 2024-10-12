# MagentoB2B.CartsMineEstimateShippingMethodsByAddressIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteShippingMethodManagementV1EstimateByAddressIdPost**](CartsMineEstimateShippingMethodsByAddressIdApi.md#quoteShippingMethodManagementV1EstimateByAddressIdPost) | **POST** /V1/carts/mine/estimate-shipping-methods-by-address-id | carts/mine/estimate-shipping-methods-by-address-id



## quoteShippingMethodManagementV1EstimateByAddressIdPost

> [QuoteDataShippingMethodInterface] quoteShippingMethodManagementV1EstimateByAddressIdPost(opts)

carts/mine/estimate-shipping-methods-by-address-id

Estimate shipping

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineEstimateShippingMethodsByAddressIdApi();
let opts = {
  'quoteShippingMethodManagementV1EstimateByAddressIdPostRequest': new MagentoB2B.QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest() // QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest | 
};
apiInstance.quoteShippingMethodManagementV1EstimateByAddressIdPost(opts, (error, data, response) => {
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
 **quoteShippingMethodManagementV1EstimateByAddressIdPostRequest** | [**QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest**](QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest.md)|  | [optional] 

### Return type

[**[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

