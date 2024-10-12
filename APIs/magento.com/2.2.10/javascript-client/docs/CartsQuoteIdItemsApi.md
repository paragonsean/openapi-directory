# MagentoB2B.CartsQuoteIdItemsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsQuoteIdItemsPost**](CartsQuoteIdItemsApi.md#v1CartsQuoteIdItemsPost) | **POST** /V1/carts/{quoteId}/items | carts/{quoteId}/items



## v1CartsQuoteIdItemsPost

> QuoteDataCartItemInterface v1CartsQuoteIdItemsPost(quoteId, opts)

carts/{quoteId}/items

Add/update the specified cart item.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsQuoteIdItemsApi();
let quoteId = "quoteId_example"; // String | 
let opts = {
  'quoteCartItemRepositoryV1SavePostRequest': new MagentoB2B.QuoteCartItemRepositoryV1SavePostRequest() // QuoteCartItemRepositoryV1SavePostRequest | 
};
apiInstance.v1CartsQuoteIdItemsPost(quoteId, opts, (error, data, response) => {
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
 **quoteId** | **String**|  | 
 **quoteCartItemRepositoryV1SavePostRequest** | [**QuoteCartItemRepositoryV1SavePostRequest**](QuoteCartItemRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

