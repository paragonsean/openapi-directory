# MagentoB2B.CartsMineGiftMessageItemIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftMessageItemRepositoryV1GetGet**](CartsMineGiftMessageItemIdApi.md#giftMessageItemRepositoryV1GetGet) | **GET** /V1/carts/mine/gift-message/{itemId} | carts/mine/gift-message/{itemId}
[**giftMessageItemRepositoryV1SavePost**](CartsMineGiftMessageItemIdApi.md#giftMessageItemRepositoryV1SavePost) | **POST** /V1/carts/mine/gift-message/{itemId} | carts/mine/gift-message/{itemId}



## giftMessageItemRepositoryV1GetGet

> GiftMessageDataMessageInterface giftMessageItemRepositoryV1GetGet(itemId)

carts/mine/gift-message/{itemId}

Return the gift message for a specified item in a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineGiftMessageItemIdApi();
let itemId = 56; // Number | The item ID.
apiInstance.giftMessageItemRepositoryV1GetGet(itemId, (error, data, response) => {
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
 **itemId** | **Number**| The item ID. | 

### Return type

[**GiftMessageDataMessageInterface**](GiftMessageDataMessageInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## giftMessageItemRepositoryV1SavePost

> Boolean giftMessageItemRepositoryV1SavePost(itemId, opts)

carts/mine/gift-message/{itemId}

Set the gift message for a specified item in a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineGiftMessageItemIdApi();
let itemId = 56; // Number | The item ID.
let opts = {
  'giftMessageCartRepositoryV1SavePostRequest': new MagentoB2B.GiftMessageCartRepositoryV1SavePostRequest() // GiftMessageCartRepositoryV1SavePostRequest | 
};
apiInstance.giftMessageItemRepositoryV1SavePost(itemId, opts, (error, data, response) => {
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
 **itemId** | **Number**| The item ID. | 
 **giftMessageCartRepositoryV1SavePostRequest** | [**GiftMessageCartRepositoryV1SavePostRequest**](GiftMessageCartRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

