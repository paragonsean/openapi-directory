# MagentoB2B.OrdersIdCancelApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderManagementV1CancelPost**](OrdersIdCancelApi.md#salesOrderManagementV1CancelPost) | **POST** /V1/orders/{id}/cancel | orders/{id}/cancel



## salesOrderManagementV1CancelPost

> Boolean salesOrderManagementV1CancelPost(id)

orders/{id}/cancel

Cancels a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersIdCancelApi();
let id = 56; // Number | The order ID.
apiInstance.salesOrderManagementV1CancelPost(id, (error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

