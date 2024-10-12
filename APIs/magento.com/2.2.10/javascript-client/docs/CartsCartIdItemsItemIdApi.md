# MagentoB2B.CartsCartIdItemsItemIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdItemsItemIdDelete**](CartsCartIdItemsItemIdApi.md#v1CartsCartIdItemsItemIdDelete) | **DELETE** /V1/carts/{cartId}/items/{itemId} | carts/{cartId}/items/{itemId}
[**v1CartsCartIdItemsItemIdPut**](CartsCartIdItemsItemIdApi.md#v1CartsCartIdItemsItemIdPut) | **PUT** /V1/carts/{cartId}/items/{itemId} | carts/{cartId}/items/{itemId}



## v1CartsCartIdItemsItemIdDelete

> Boolean v1CartsCartIdItemsItemIdDelete(cartId, itemId)

carts/{cartId}/items/{itemId}

Removes the specified item from the specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdItemsItemIdApi();
let cartId = 56; // Number | The cart ID.
let itemId = 56; // Number | The item ID of the item to be removed.
apiInstance.v1CartsCartIdItemsItemIdDelete(cartId, itemId, (error, data, response) => {
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
 **itemId** | **Number**| The item ID of the item to be removed. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CartsCartIdItemsItemIdPut

> QuoteDataCartItemInterface v1CartsCartIdItemsItemIdPut(cartId, itemId, opts)

carts/{cartId}/items/{itemId}

Add/update the specified cart item.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdItemsItemIdApi();
let cartId = "cartId_example"; // String | 
let itemId = "itemId_example"; // String | 
let opts = {
  'quoteCartItemRepositoryV1SavePostRequest': new MagentoB2B.QuoteCartItemRepositoryV1SavePostRequest() // QuoteCartItemRepositoryV1SavePostRequest | 
};
apiInstance.v1CartsCartIdItemsItemIdPut(cartId, itemId, opts, (error, data, response) => {
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

