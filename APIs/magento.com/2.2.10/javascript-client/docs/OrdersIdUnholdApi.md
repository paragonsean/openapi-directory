# MagentoB2B.OrdersIdUnholdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderManagementV1UnHoldPost**](OrdersIdUnholdApi.md#salesOrderManagementV1UnHoldPost) | **POST** /V1/orders/{id}/unhold | orders/{id}/unhold



## salesOrderManagementV1UnHoldPost

> Boolean salesOrderManagementV1UnHoldPost(id)

orders/{id}/unhold

Releases a specified order from hold status.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersIdUnholdApi();
let id = 56; // Number | The order ID.
apiInstance.salesOrderManagementV1UnHoldPost(id, (error, data, response) => {
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

