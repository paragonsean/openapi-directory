# MagentoB2B.GuestCartsCartIdGiftMessageApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftMessageGuestCartRepositoryV1GetGet**](GuestCartsCartIdGiftMessageApi.md#giftMessageGuestCartRepositoryV1GetGet) | **GET** /V1/guest-carts/{cartId}/gift-message | guest-carts/{cartId}/gift-message
[**giftMessageGuestCartRepositoryV1SavePost**](GuestCartsCartIdGiftMessageApi.md#giftMessageGuestCartRepositoryV1SavePost) | **POST** /V1/guest-carts/{cartId}/gift-message | guest-carts/{cartId}/gift-message



## giftMessageGuestCartRepositoryV1GetGet

> GiftMessageDataMessageInterface giftMessageGuestCartRepositoryV1GetGet(cartId)

guest-carts/{cartId}/gift-message

Return the gift message for a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdGiftMessageApi();
let cartId = "cartId_example"; // String | The shopping cart ID.
apiInstance.giftMessageGuestCartRepositoryV1GetGet(cartId, (error, data, response) => {
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

### Return type

[**GiftMessageDataMessageInterface**](GiftMessageDataMessageInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## giftMessageGuestCartRepositoryV1SavePost

> Boolean giftMessageGuestCartRepositoryV1SavePost(cartId, opts)

guest-carts/{cartId}/gift-message

Set the gift message for an entire order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdGiftMessageApi();
let cartId = "cartId_example"; // String | The cart ID.
let opts = {
  'giftMessageCartRepositoryV1SavePostRequest': new MagentoB2B.GiftMessageCartRepositoryV1SavePostRequest() // GiftMessageCartRepositoryV1SavePostRequest | 
};
apiInstance.giftMessageGuestCartRepositoryV1SavePost(cartId, opts, (error, data, response) => {
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
 **giftMessageCartRepositoryV1SavePostRequest** | [**GiftMessageCartRepositoryV1SavePostRequest**](GiftMessageCartRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

