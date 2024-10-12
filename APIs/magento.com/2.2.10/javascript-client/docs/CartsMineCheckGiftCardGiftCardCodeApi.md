# MagentoB2B.CartsMineCheckGiftCardGiftCardCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet**](CartsMineCheckGiftCardGiftCardCodeApi.md#giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet) | **GET** /V1/carts/mine/checkGiftCard/{giftCardCode} | carts/mine/checkGiftCard/{giftCardCode}



## giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet

> Number giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet(giftCardCode)

carts/mine/checkGiftCard/{giftCardCode}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineCheckGiftCardGiftCardCodeApi();
let giftCardCode = "giftCardCode_example"; // String | 
apiInstance.giftCardAccountGiftCardAccountManagementV1CheckGiftCardGet(giftCardCode, (error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

