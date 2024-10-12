# MagentoB2B.CartsCartIdGiftCardsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut**](CartsCartIdGiftCardsApi.md#giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut) | **PUT** /V1/carts/{cartId}/giftCards | carts/{cartId}/giftCards



## giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut

> Boolean giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut(cartId, opts)

carts/{cartId}/giftCards



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdGiftCardsApi();
let cartId = 56; // Number | 
let opts = {
  'giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest': new MagentoB2B.GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest() // GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest | 
};
apiInstance.giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPut(cartId, opts, (error, data, response) => {
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
 **giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest** | [**GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest**](GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

