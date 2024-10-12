# MagentoB2B.CartsMineItemsItemIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteCartItemRepositoryV1DeleteByIdDelete**](CartsMineItemsItemIdApi.md#quoteCartItemRepositoryV1DeleteByIdDelete) | **DELETE** /V1/carts/mine/items/{itemId} | carts/mine/items/{itemId}
[**quoteCartItemRepositoryV1SavePut**](CartsMineItemsItemIdApi.md#quoteCartItemRepositoryV1SavePut) | **PUT** /V1/carts/mine/items/{itemId} | carts/mine/items/{itemId}



## quoteCartItemRepositoryV1DeleteByIdDelete

> Boolean quoteCartItemRepositoryV1DeleteByIdDelete(itemId)

carts/mine/items/{itemId}

Removes the specified item from the specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineItemsItemIdApi();
let itemId = 56; // Number | The item ID of the item to be removed.
apiInstance.quoteCartItemRepositoryV1DeleteByIdDelete(itemId, (error, data, response) => {
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
 **itemId** | **Number**| The item ID of the item to be removed. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteCartItemRepositoryV1SavePut

> QuoteDataCartItemInterface quoteCartItemRepositoryV1SavePut(itemId, opts)

carts/mine/items/{itemId}

Add/update the specified cart item.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineItemsItemIdApi();
let itemId = "itemId_example"; // String | 
let opts = {
  'quoteCartItemRepositoryV1SavePostRequest': new MagentoB2B.QuoteCartItemRepositoryV1SavePostRequest() // QuoteCartItemRepositoryV1SavePostRequest | 
};
apiInstance.quoteCartItemRepositoryV1SavePut(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**|  | 
 **quoteCartItemRepositoryV1SavePostRequest** | [**QuoteCartItemRepositoryV1SavePostRequest**](QuoteCartItemRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

