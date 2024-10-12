# MagentoB2B.OrdersIdStatusesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderManagementV1GetStatusGet**](OrdersIdStatusesApi.md#salesOrderManagementV1GetStatusGet) | **GET** /V1/orders/{id}/statuses | orders/{id}/statuses



## salesOrderManagementV1GetStatusGet

> String salesOrderManagementV1GetStatusGet(id)

orders/{id}/statuses

Gets the status for a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersIdStatusesApi();
let id = 56; // Number | The order ID.
apiInstance.salesOrderManagementV1GetStatusGet(id, (error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

