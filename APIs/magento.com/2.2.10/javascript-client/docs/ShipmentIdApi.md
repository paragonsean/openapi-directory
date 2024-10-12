# MagentoB2B.ShipmentIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesShipmentRepositoryV1GetGet**](ShipmentIdApi.md#salesShipmentRepositoryV1GetGet) | **GET** /V1/shipment/{id} | shipment/{id}



## salesShipmentRepositoryV1GetGet

> SalesDataShipmentInterface salesShipmentRepositoryV1GetGet(id)

shipment/{id}

Loads a specified shipment.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ShipmentIdApi();
let id = 56; // Number | The shipment ID.
apiInstance.salesShipmentRepositoryV1GetGet(id, (error, data, response) => {
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

[**SalesDataShipmentInterface**](SalesDataShipmentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

