# MagentoB2B.ShipmentTrackIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesShipmentTrackRepositoryV1DeleteByIdDelete**](ShipmentTrackIdApi.md#salesShipmentTrackRepositoryV1DeleteByIdDelete) | **DELETE** /V1/shipment/track/{id} | shipment/track/{id}



## salesShipmentTrackRepositoryV1DeleteByIdDelete

> Boolean salesShipmentTrackRepositoryV1DeleteByIdDelete(id)

shipment/track/{id}

Deletes a specified shipment track by ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ShipmentTrackIdApi();
let id = 56; // Number | The shipment track ID.
apiInstance.salesShipmentTrackRepositoryV1DeleteByIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| The shipment track ID. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

