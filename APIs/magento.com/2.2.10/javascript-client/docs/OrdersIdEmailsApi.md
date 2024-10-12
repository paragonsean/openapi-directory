# MagentoB2B.OrdersIdEmailsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderManagementV1NotifyPost**](OrdersIdEmailsApi.md#salesOrderManagementV1NotifyPost) | **POST** /V1/orders/{id}/emails | orders/{id}/emails



## salesOrderManagementV1NotifyPost

> Boolean salesOrderManagementV1NotifyPost(id)

orders/{id}/emails

Emails a user a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersIdEmailsApi();
let id = 56; // Number | The order ID.
apiInstance.salesOrderManagementV1NotifyPost(id, (error, data, response) => {
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

