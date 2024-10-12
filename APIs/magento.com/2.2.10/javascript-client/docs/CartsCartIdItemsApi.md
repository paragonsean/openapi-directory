# MagentoB2B.CartsCartIdItemsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdItemsGet**](CartsCartIdItemsApi.md#v1CartsCartIdItemsGet) | **GET** /V1/carts/{cartId}/items | carts/{cartId}/items



## v1CartsCartIdItemsGet

> [QuoteDataCartItemInterface] v1CartsCartIdItemsGet(cartId)

carts/{cartId}/items

Lists items that are assigned to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdItemsApi();
let cartId = 56; // Number | The cart ID.
apiInstance.v1CartsCartIdItemsGet(cartId, (error, data, response) => {
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

### Return type

[**[QuoteDataCartItemInterface]**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

