# MagentoB2B.CartsMineGiftCardsGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete**](CartsMineGiftCardsGiftCardCodeApi.md#giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete) | **DELETE** /V1/carts/mine/giftCards/{giftCardCode} | carts/mine/giftCards/{giftCardCode}



## giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete

> Boolean giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete(giftCardCode)

carts/mine/giftCards/{giftCardCode}

Remove GiftCard Account entity

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineGiftCardsGiftCardCodeApi();
let giftCardCode = "giftCardCode_example"; // String | 
apiInstance.giftCardAccountGiftCardAccountManagementV1DeleteByQuoteIdDelete(giftCardCode, (error, data, response) => {
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
 **giftCardCode** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

