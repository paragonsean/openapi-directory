# MagentoB2B.OrdersIdHoldApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderManagementV1HoldPost**](OrdersIdHoldApi.md#salesOrderManagementV1HoldPost) | **POST** /V1/orders/{id}/hold | orders/{id}/hold



## salesOrderManagementV1HoldPost

> Boolean salesOrderManagementV1HoldPost(id)

orders/{id}/hold

Holds a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersIdHoldApi();
let id = 56; // Number | The order ID.
apiInstance.salesOrderManagementV1HoldPost(id, (error, data, response) => {
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

