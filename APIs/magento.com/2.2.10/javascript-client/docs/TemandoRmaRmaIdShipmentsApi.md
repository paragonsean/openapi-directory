# MagentoB2B.TemandoRmaRmaIdShipmentsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut**](TemandoRmaRmaIdShipmentsApi.md#temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut) | **PUT** /V1/temando/rma/{rmaId}/shipments | temando/rma/{rmaId}/shipments



## temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut

> Number temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut(rmaId, opts)

temando/rma/{rmaId}/shipments

Assign platform shipment IDs to a core RMA entity.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TemandoRmaRmaIdShipmentsApi();
let rmaId = 56; // Number | 
let opts = {
  'temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest': new MagentoB2B.TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest() // TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest | 
};
apiInstance.temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut(rmaId, opts, (error, data, response) => {
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
 **rmaId** | **Number**|  | 
 **temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest** | [**TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest**](TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

