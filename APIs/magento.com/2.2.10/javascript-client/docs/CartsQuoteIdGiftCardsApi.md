# MagentoB2B.CartsQuoteIdGiftCardsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet**](CartsQuoteIdGiftCardsApi.md#giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet) | **GET** /V1/carts/{quoteId}/giftCards | carts/{quoteId}/giftCards



## giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet

> GiftCardAccountDataGiftCardAccountInterface giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet(quoteId)

carts/{quoteId}/giftCards

Return GiftCard Account cards

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsQuoteIdGiftCardsApi();
let quoteId = 56; // Number | 
apiInstance.giftCardAccountGiftCardAccountManagementV1GetListByQuoteIdGet(quoteId, (error, data, response) => {
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
 **quoteId** | **Number**|  | 

### Return type

[**GiftCardAccountDataGiftCardAccountInterface**](GiftCardAccountDataGiftCardAccountInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

