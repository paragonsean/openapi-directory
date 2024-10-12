# MagentoB2B.CartsCartIdGiftMessageApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdGiftMessageGet**](CartsCartIdGiftMessageApi.md#v1CartsCartIdGiftMessageGet) | **GET** /V1/carts/{cartId}/gift-message | carts/{cartId}/gift-message
[**v1CartsCartIdGiftMessagePost**](CartsCartIdGiftMessageApi.md#v1CartsCartIdGiftMessagePost) | **POST** /V1/carts/{cartId}/gift-message | carts/{cartId}/gift-message



## v1CartsCartIdGiftMessageGet

> GiftMessageDataMessageInterface v1CartsCartIdGiftMessageGet(cartId)

carts/{cartId}/gift-message

Return the gift message for a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdGiftMessageApi();
let cartId = 56; // Number | The shopping cart ID.
apiInstance.v1CartsCartIdGiftMessageGet(cartId, (error, data, response) => {
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
 **cartId** | **Number**| The shopping cart ID. | 

### Return type

[**GiftMessageDataMessageInterface**](GiftMessageDataMessageInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CartsCartIdGiftMessagePost

> Boolean v1CartsCartIdGiftMessagePost(cartId, opts)

carts/{cartId}/gift-message

Set the gift message for an entire order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdGiftMessageApi();
let cartId = 56; // Number | The cart ID.
let opts = {
  'giftMessageCartRepositoryV1SavePostRequest': new MagentoB2B.GiftMessageCartRepositoryV1SavePostRequest() // GiftMessageCartRepositoryV1SavePostRequest | 
};
apiInstance.v1CartsCartIdGiftMessagePost(cartId, opts, (error, data, response) => {
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
 **cartId** | **Number**| The cart ID. | 
 **giftMessageCartRepositoryV1SavePostRequest** | [**GiftMessageCartRepositoryV1SavePostRequest**](GiftMessageCartRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

