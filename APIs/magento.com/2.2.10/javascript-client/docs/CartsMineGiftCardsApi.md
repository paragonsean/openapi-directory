# MagentoB2B.CartsMineGiftCardsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost**](CartsMineGiftCardsApi.md#giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost) | **POST** /V1/carts/mine/giftCards | carts/mine/giftCards



## giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost

> Boolean giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost(opts)

carts/mine/giftCards



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineGiftCardsApi();
let opts = {
  'giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest': new MagentoB2B.GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest() // GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest | 
};
apiInstance.giftCardAccountGiftCardAccountManagementV1SaveByQuoteIdPost(opts, (error, data, response) => {
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
 **giftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest** | [**GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest**](GiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

