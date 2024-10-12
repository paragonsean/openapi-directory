# MagentoB2B.GuestCartsCartIdItemsItemIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestCartItemRepositoryV1DeleteByIdDelete**](GuestCartsCartIdItemsItemIdApi.md#quoteGuestCartItemRepositoryV1DeleteByIdDelete) | **DELETE** /V1/guest-carts/{cartId}/items/{itemId} | guest-carts/{cartId}/items/{itemId}
[**quoteGuestCartItemRepositoryV1SavePut**](GuestCartsCartIdItemsItemIdApi.md#quoteGuestCartItemRepositoryV1SavePut) | **PUT** /V1/guest-carts/{cartId}/items/{itemId} | guest-carts/{cartId}/items/{itemId}



## quoteGuestCartItemRepositoryV1DeleteByIdDelete

> Boolean quoteGuestCartItemRepositoryV1DeleteByIdDelete(cartId, itemId)

guest-carts/{cartId}/items/{itemId}

Remove the specified item from the specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdItemsItemIdApi();
let cartId = "cartId_example"; // String | The cart ID.
let itemId = 56; // Number | The item ID of the item to be removed.
apiInstance.quoteGuestCartItemRepositoryV1DeleteByIdDelete(cartId, itemId, (error, data, response) => {
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
 **itemId** | **Number**| The item ID of the item to be removed. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteGuestCartItemRepositoryV1SavePut

> QuoteDataCartItemInterface quoteGuestCartItemRepositoryV1SavePut(cartId, itemId, opts)

guest-carts/{cartId}/items/{itemId}

Add/update the specified cart item.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdItemsItemIdApi();
let cartId = "cartId_example"; // String | 
let itemId = "itemId_example"; // String | 
let opts = {
  'quoteCartItemRepositoryV1SavePostRequest': new MagentoB2B.QuoteCartItemRepositoryV1SavePostRequest() // QuoteCartItemRepositoryV1SavePostRequest | 
};
apiInstance.quoteGuestCartItemRepositoryV1SavePut(cartId, itemId, opts, (error, data, response) => {
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
 **itemId** | **String**|  | 
 **quoteCartItemRepositoryV1SavePostRequest** | [**QuoteCartItemRepositoryV1SavePostRequest**](QuoteCartItemRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

