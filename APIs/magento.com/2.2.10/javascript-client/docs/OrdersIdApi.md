# MagentoB2B.OrdersIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderRepositoryV1GetGet**](OrdersIdApi.md#salesOrderRepositoryV1GetGet) | **GET** /V1/orders/{id} | orders/{id}



## salesOrderRepositoryV1GetGet

> SalesDataOrderInterface salesOrderRepositoryV1GetGet(id)

orders/{id}

Loads a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersIdApi();
let id = 56; // Number | The order ID.
apiInstance.salesOrderRepositoryV1GetGet(id, (error, data, response) => {
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
 **id** | **Number**| The order ID. | 

### Return type

[**SalesDataOrderInterface**](SalesDataOrderInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

