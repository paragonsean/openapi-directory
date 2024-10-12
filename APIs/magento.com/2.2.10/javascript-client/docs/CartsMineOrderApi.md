# MagentoB2B.CartsMineOrderApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteCartManagementV1PlaceOrderPut**](CartsMineOrderApi.md#quoteCartManagementV1PlaceOrderPut) | **PUT** /V1/carts/mine/order | carts/mine/order



## quoteCartManagementV1PlaceOrderPut

> Number quoteCartManagementV1PlaceOrderPut(opts)

carts/mine/order

Places an order for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineOrderApi();
let opts = {
  'quoteCartManagementV1PlaceOrderPutRequest': new MagentoB2B.QuoteCartManagementV1PlaceOrderPutRequest() // QuoteCartManagementV1PlaceOrderPutRequest | 
};
apiInstance.quoteCartManagementV1PlaceOrderPut(opts, (error, data, response) => {
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
 **quoteCartManagementV1PlaceOrderPutRequest** | [**QuoteCartManagementV1PlaceOrderPutRequest**](QuoteCartManagementV1PlaceOrderPutRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

