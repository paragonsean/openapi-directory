# MagentoB2B.CartsMineGiftMessageApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftMessageCartRepositoryV1GetGet**](CartsMineGiftMessageApi.md#giftMessageCartRepositoryV1GetGet) | **GET** /V1/carts/mine/gift-message | carts/mine/gift-message
[**giftMessageCartRepositoryV1SavePost**](CartsMineGiftMessageApi.md#giftMessageCartRepositoryV1SavePost) | **POST** /V1/carts/mine/gift-message | carts/mine/gift-message



## giftMessageCartRepositoryV1GetGet

> GiftMessageDataMessageInterface giftMessageCartRepositoryV1GetGet()

carts/mine/gift-message

Return the gift message for a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineGiftMessageApi();
apiInstance.giftMessageCartRepositoryV1GetGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GiftMessageDataMessageInterface**](GiftMessageDataMessageInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## giftMessageCartRepositoryV1SavePost

> Boolean giftMessageCartRepositoryV1SavePost(opts)

carts/mine/gift-message

Set the gift message for an entire order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineGiftMessageApi();
let opts = {
  'giftMessageCartRepositoryV1SavePostRequest': new MagentoB2B.GiftMessageCartRepositoryV1SavePostRequest() // GiftMessageCartRepositoryV1SavePostRequest | 
};
apiInstance.giftMessageCartRepositoryV1SavePost(opts, (error, data, response) => {
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
 **giftMessageCartRepositoryV1SavePostRequest** | [**GiftMessageCartRepositoryV1SavePostRequest**](GiftMessageCartRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

