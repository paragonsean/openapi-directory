# MagentoB2B.GiftregistryMineEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost**](GiftregistryMineEstimateShippingMethodsApi.md#giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost) | **POST** /V1/giftregistry/mine/estimate-shipping-methods | giftregistry/mine/estimate-shipping-methods



## giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost

> [QuoteDataShippingMethodInterface] giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost(opts)

giftregistry/mine/estimate-shipping-methods

Estimate shipping

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GiftregistryMineEstimateShippingMethodsApi();
let opts = {
  'giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest': new MagentoB2B.GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest() // GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest | 
};
apiInstance.giftRegistryShippingMethodManagementV1EstimateByRegistryIdPost(opts, (error, data, response) => {
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
 **giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest** | [**GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest**](GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest.md)|  | [optional] 

### Return type

[**[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

