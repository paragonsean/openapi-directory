# MagentoB2B.NegotiableCartsCartIdGiftCardsGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete**](NegotiableCartsCartIdGiftCardsGiftCardCodeApi.md#negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete) | **DELETE** /V1/negotiable-carts/{cartId}/giftCards/{giftCardCode} | negotiable-carts/{cartId}/giftCards/{giftCardCode}



## negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete

> Boolean negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete(cartId, giftCardCode)

negotiable-carts/{cartId}/giftCards/{giftCardCode}

Remove GiftCard Account entity

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdGiftCardsGiftCardCodeApi();
let cartId = 56; // Number | 
let giftCardCode = "giftCardCode_example"; // String | 
apiInstance.negotiableQuoteGiftCardAccountManagementV1DeleteByQuoteIdDelete(cartId, giftCardCode, (error, data, response) => {
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
 **giftCardCode** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

