# MagentoB2B.OrdersItemsIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderItemRepositoryV1GetGet**](OrdersItemsIdApi.md#salesOrderItemRepositoryV1GetGet) | **GET** /V1/orders/items/{id} | orders/items/{id}



## salesOrderItemRepositoryV1GetGet

> SalesDataOrderItemInterface salesOrderItemRepositoryV1GetGet(id)

orders/items/{id}

Loads a specified order item.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersItemsIdApi();
let id = 56; // Number | The order item ID.
apiInstance.salesOrderItemRepositoryV1GetGet(id, (error, data, response) => {
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
 **id** | **Number**| The order item ID. | 

### Return type

[**SalesDataOrderItemInterface**](SalesDataOrderItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

