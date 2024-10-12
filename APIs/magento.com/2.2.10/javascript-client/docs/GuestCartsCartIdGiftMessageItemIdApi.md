# MagentoB2B.GuestCartsCartIdGiftMessageItemIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftMessageGuestItemRepositoryV1GetGet**](GuestCartsCartIdGiftMessageItemIdApi.md#giftMessageGuestItemRepositoryV1GetGet) | **GET** /V1/guest-carts/{cartId}/gift-message/{itemId} | guest-carts/{cartId}/gift-message/{itemId}
[**giftMessageGuestItemRepositoryV1SavePost**](GuestCartsCartIdGiftMessageItemIdApi.md#giftMessageGuestItemRepositoryV1SavePost) | **POST** /V1/guest-carts/{cartId}/gift-message/{itemId} | guest-carts/{cartId}/gift-message/{itemId}



## giftMessageGuestItemRepositoryV1GetGet

> GiftMessageDataMessageInterface giftMessageGuestItemRepositoryV1GetGet(cartId, itemId)

guest-carts/{cartId}/gift-message/{itemId}

Return the gift message for a specified item in a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdGiftMessageItemIdApi();
let cartId = "cartId_example"; // String | The shopping cart ID.
let itemId = 56; // Number | The item ID.
apiInstance.giftMessageGuestItemRepositoryV1GetGet(cartId, itemId, (error, data, response) => {
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
 **cartId** | **String**| The shopping cart ID. | 
 **itemId** | **Number**| The item ID. | 

### Return type

[**GiftMessageDataMessageInterface**](GiftMessageDataMessageInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## giftMessageGuestItemRepositoryV1SavePost

> Boolean giftMessageGuestItemRepositoryV1SavePost(cartId, itemId, opts)

guest-carts/{cartId}/gift-message/{itemId}

Set the gift message for a specified item in a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdGiftMessageItemIdApi();
let cartId = "cartId_example"; // String | The cart ID.
let itemId = 56; // Number | The item ID.
let opts = {
  'giftMessageCartRepositoryV1SavePostRequest': new MagentoB2B.GiftMessageCartRepositoryV1SavePostRequest() // GiftMessageCartRepositoryV1SavePostRequest | 
};
apiInstance.giftMessageGuestItemRepositoryV1SavePost(cartId, itemId, opts, (error, data, response) => {
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
 **cartId** | **String**| The cart ID. | 
 **itemId** | **Number**| The item ID. | 
 **giftMessageCartRepositoryV1SavePostRequest** | [**GiftMessageCartRepositoryV1SavePostRequest**](GiftMessageCartRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

