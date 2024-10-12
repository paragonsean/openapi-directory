# MagentoB2B.GuestCartsCartIdOrderApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestCartManagementV1PlaceOrderPut**](GuestCartsCartIdOrderApi.md#quoteGuestCartManagementV1PlaceOrderPut) | **PUT** /V1/guest-carts/{cartId}/order | guest-carts/{cartId}/order



## quoteGuestCartManagementV1PlaceOrderPut

> Number quoteGuestCartManagementV1PlaceOrderPut(cartId, opts)

guest-carts/{cartId}/order

Place an order for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdOrderApi();
let cartId = "cartId_example"; // String | The cart ID.
let opts = {
  'quoteCartManagementV1PlaceOrderPutRequest': new MagentoB2B.QuoteCartManagementV1PlaceOrderPutRequest() // QuoteCartManagementV1PlaceOrderPutRequest | 
};
apiInstance.quoteGuestCartManagementV1PlaceOrderPut(cartId, opts, (error, data, response) => {
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
 **quoteCartManagementV1PlaceOrderPutRequest** | [**QuoteCartManagementV1PlaceOrderPutRequest**](QuoteCartManagementV1PlaceOrderPutRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

