# MagentoB2B.CartsCartIdGiftCardsGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdGiftCardsGiftCardCodeDelete**](CartsCartIdGiftCardsGiftCardCodeApi.md#v1CartsCartIdGiftCardsGiftCardCodeDelete) | **DELETE** /V1/carts/{cartId}/giftCards/{giftCardCode} | carts/{cartId}/giftCards/{giftCardCode}



## v1CartsCartIdGiftCardsGiftCardCodeDelete

> Boolean v1CartsCartIdGiftCardsGiftCardCodeDelete(cartId, giftCardCode)

carts/{cartId}/giftCards/{giftCardCode}

Remove GiftCard Account entity

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdGiftCardsGiftCardCodeApi();
let cartId = 56; // Number | 
let giftCardCode = "giftCardCode_example"; // String | 
apiInstance.v1CartsCartIdGiftCardsGiftCardCodeDelete(cartId, giftCardCode, (error, data, response) => {
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

