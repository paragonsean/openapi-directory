# MagentoB2B.ShipmentIdEmailsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesShipmentManagementV1NotifyPost**](ShipmentIdEmailsApi.md#salesShipmentManagementV1NotifyPost) | **POST** /V1/shipment/{id}/emails | shipment/{id}/emails



## salesShipmentManagementV1NotifyPost

> Boolean salesShipmentManagementV1NotifyPost(id)

shipment/{id}/emails

Emails user a specified shipment.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ShipmentIdEmailsApi();
let id = 56; // Number | The shipment ID.
apiInstance.salesShipmentManagementV1NotifyPost(id, (error, data, response) => {
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
 **id** | **Number**| The shipment ID. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

