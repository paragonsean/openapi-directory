# MagentoB2B.CartsCartIdOrderApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdOrderPut**](CartsCartIdOrderApi.md#v1CartsCartIdOrderPut) | **PUT** /V1/carts/{cartId}/order | carts/{cartId}/order



## v1CartsCartIdOrderPut

> Number v1CartsCartIdOrderPut(cartId, opts)

carts/{cartId}/order

Places an order for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdOrderApi();
let cartId = 56; // Number | The cart ID.
let opts = {
  'quoteCartManagementV1PlaceOrderPutRequest': new MagentoB2B.QuoteCartManagementV1PlaceOrderPutRequest() // QuoteCartManagementV1PlaceOrderPutRequest | 
};
apiInstance.v1CartsCartIdOrderPut(cartId, opts, (error, data, response) => {
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
 **quoteCartManagementV1PlaceOrderPutRequest** | [**QuoteCartManagementV1PlaceOrderPutRequest**](QuoteCartManagementV1PlaceOrderPutRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

