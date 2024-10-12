# MagentoB2B.GuestGiftregistryCartIdEstimateShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost**](GuestGiftregistryCartIdEstimateShippingMethodsApi.md#giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost) | **POST** /V1/guest-giftregistry/{cartId}/estimate-shipping-methods | guest-giftregistry/{cartId}/estimate-shipping-methods



## giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost

> [QuoteDataShippingMethodInterface] giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost(cartId, opts)

guest-giftregistry/{cartId}/estimate-shipping-methods

Estimate shipping

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestGiftregistryCartIdEstimateShippingMethodsApi();
let cartId = "cartId_example"; // String | The shopping cart ID.
let opts = {
  'giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest': new MagentoB2B.GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest() // GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest | 
};
apiInstance.giftRegistryGuestCartShippingMethodManagementV1EstimateByRegistryIdPost(cartId, opts, (error, data, response) => {
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
 **cartId** | **String**| The shopping cart ID. | 
 **giftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest** | [**GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest**](GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest.md)|  | [optional] 

### Return type

[**[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

