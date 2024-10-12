# MagentoB2B.GuestCartsCartIdItemsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestCartItemRepositoryV1GetListGet**](GuestCartsCartIdItemsApi.md#quoteGuestCartItemRepositoryV1GetListGet) | **GET** /V1/guest-carts/{cartId}/items | guest-carts/{cartId}/items
[**quoteGuestCartItemRepositoryV1SavePost**](GuestCartsCartIdItemsApi.md#quoteGuestCartItemRepositoryV1SavePost) | **POST** /V1/guest-carts/{cartId}/items | guest-carts/{cartId}/items



## quoteGuestCartItemRepositoryV1GetListGet

> [QuoteDataCartItemInterface] quoteGuestCartItemRepositoryV1GetListGet(cartId)

guest-carts/{cartId}/items

List items that are assigned to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdItemsApi();
let cartId = "cartId_example"; // String | The cart ID.
apiInstance.quoteGuestCartItemRepositoryV1GetListGet(cartId, (error, data, response) => {
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

### Return type

[**[QuoteDataCartItemInterface]**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteGuestCartItemRepositoryV1SavePost

> QuoteDataCartItemInterface quoteGuestCartItemRepositoryV1SavePost(cartId, opts)

guest-carts/{cartId}/items

Add/update the specified cart item.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdItemsApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'quoteCartItemRepositoryV1SavePostRequest': new MagentoB2B.QuoteCartItemRepositoryV1SavePostRequest() // QuoteCartItemRepositoryV1SavePostRequest | 
};
apiInstance.quoteGuestCartItemRepositoryV1SavePost(cartId, opts, (error, data, response) => {
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
 **quoteCartItemRepositoryV1SavePostRequest** | [**QuoteCartItemRepositoryV1SavePostRequest**](QuoteCartItemRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

