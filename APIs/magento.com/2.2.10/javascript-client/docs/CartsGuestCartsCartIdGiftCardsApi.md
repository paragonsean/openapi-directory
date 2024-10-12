# MagentoB2B.CartsGuestCartsCartIdGiftCardsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost**](CartsGuestCartsCartIdGiftCardsApi.md#giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost) | **POST** /V1/carts/guest-carts/{cartId}/giftCards | carts/guest-carts/{cartId}/giftCards



## giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost

> Boolean giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost(cartId, opts)

carts/guest-carts/{cartId}/giftCards



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsGuestCartsCartIdGiftCardsApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest': new MagentoB2B.GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest() // GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest | 
};
apiInstance.giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost(cartId, opts, (error, data, response) => {
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
 **giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest** | [**GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest**](GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

