# MagentoB2B.CartsGuestCartsCartIdCheckGiftCardGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet**](CartsGuestCartsCartIdCheckGiftCardGiftCardCodeApi.md#giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet) | **GET** /V1/carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode} | carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode}



## giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet

> Number giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet(cartId, giftCardCode)

carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsGuestCartsCartIdCheckGiftCardGiftCardCodeApi();
let cartId = "cartId_example"; // String | 
let giftCardCode = "giftCardCode_example"; // String | 
apiInstance.giftCardAccountGuestGiftCardAccountManagementV1CheckGiftCardGet(cartId, giftCardCode, (error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

