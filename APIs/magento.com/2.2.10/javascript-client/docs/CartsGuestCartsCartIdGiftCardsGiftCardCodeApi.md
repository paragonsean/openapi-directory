# MagentoB2B.CartsGuestCartsCartIdGiftCardsGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete**](CartsGuestCartsCartIdGiftCardsGiftCardCodeApi.md#giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete) | **DELETE** /V1/carts/guest-carts/{cartId}/giftCards/{giftCardCode} | carts/guest-carts/{cartId}/giftCards/{giftCardCode}



## giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete

> Boolean giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete(cartId, giftCardCode)

carts/guest-carts/{cartId}/giftCards/{giftCardCode}

Remove GiftCard Account entity

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsGuestCartsCartIdGiftCardsGiftCardCodeApi();
let cartId = "cartId_example"; // String | 
let giftCardCode = "giftCardCode_example"; // String | 
apiInstance.giftCardAccountGuestGiftCardAccountManagementV1DeleteByQuoteIdDelete(cartId, giftCardCode, (error, data, response) => {
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
 **giftCardCode** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

