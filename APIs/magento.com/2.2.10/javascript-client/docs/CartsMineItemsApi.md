# MagentoB2B.CartsMineItemsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteCartItemRepositoryV1GetListGet**](CartsMineItemsApi.md#quoteCartItemRepositoryV1GetListGet) | **GET** /V1/carts/mine/items | carts/mine/items
[**quoteCartItemRepositoryV1SavePost**](CartsMineItemsApi.md#quoteCartItemRepositoryV1SavePost) | **POST** /V1/carts/mine/items | carts/mine/items



## quoteCartItemRepositoryV1GetListGet

> [QuoteDataCartItemInterface] quoteCartItemRepositoryV1GetListGet()

carts/mine/items

Lists items that are assigned to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineItemsApi();
apiInstance.quoteCartItemRepositoryV1GetListGet((error, data, response) => {
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

[**[QuoteDataCartItemInterface]**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteCartItemRepositoryV1SavePost

> QuoteDataCartItemInterface quoteCartItemRepositoryV1SavePost(opts)

carts/mine/items

Add/update the specified cart item.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineItemsApi();
let opts = {
  'quoteCartItemRepositoryV1SavePostRequest': new MagentoB2B.QuoteCartItemRepositoryV1SavePostRequest() // QuoteCartItemRepositoryV1SavePostRequest | 
};
apiInstance.quoteCartItemRepositoryV1SavePost(opts, (error, data, response) => {
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
 **quoteCartItemRepositoryV1SavePostRequest** | [**QuoteCartItemRepositoryV1SavePostRequest**](QuoteCartItemRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

