# MagentoB2B.CartsCartIdGiftMessageItemIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdGiftMessageItemIdGet**](CartsCartIdGiftMessageItemIdApi.md#v1CartsCartIdGiftMessageItemIdGet) | **GET** /V1/carts/{cartId}/gift-message/{itemId} | carts/{cartId}/gift-message/{itemId}
[**v1CartsCartIdGiftMessageItemIdPost**](CartsCartIdGiftMessageItemIdApi.md#v1CartsCartIdGiftMessageItemIdPost) | **POST** /V1/carts/{cartId}/gift-message/{itemId} | carts/{cartId}/gift-message/{itemId}



## v1CartsCartIdGiftMessageItemIdGet

> GiftMessageDataMessageInterface v1CartsCartIdGiftMessageItemIdGet(cartId, itemId)

carts/{cartId}/gift-message/{itemId}

Return the gift message for a specified item in a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdGiftMessageItemIdApi();
let cartId = 56; // Number | The shopping cart ID.
let itemId = 56; // Number | The item ID.
apiInstance.v1CartsCartIdGiftMessageItemIdGet(cartId, itemId, (error, data, response) => {
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
 **itemId** | **Number**| The item ID. | 

### Return type

[**GiftMessageDataMessageInterface**](GiftMessageDataMessageInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CartsCartIdGiftMessageItemIdPost

> Boolean v1CartsCartIdGiftMessageItemIdPost(cartId, itemId, opts)

carts/{cartId}/gift-message/{itemId}

Set the gift message for a specified item in a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdGiftMessageItemIdApi();
let cartId = 56; // Number | The cart ID.
let itemId = 56; // Number | The item ID.
let opts = {
  'giftMessageCartRepositoryV1SavePostRequest': new MagentoB2B.GiftMessageCartRepositoryV1SavePostRequest() // GiftMessageCartRepositoryV1SavePostRequest | 
};
apiInstance.v1CartsCartIdGiftMessageItemIdPost(cartId, itemId, opts, (error, data, response) => {
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
 **itemId** | **Number**| The item ID. | 
 **giftMessageCartRepositoryV1SavePostRequest** | [**GiftMessageCartRepositoryV1SavePostRequest**](GiftMessageCartRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

