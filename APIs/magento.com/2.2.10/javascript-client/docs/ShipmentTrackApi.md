# MagentoB2B.ShipmentTrackApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesShipmentTrackRepositoryV1SavePost**](ShipmentTrackApi.md#salesShipmentTrackRepositoryV1SavePost) | **POST** /V1/shipment/track | shipment/track



## salesShipmentTrackRepositoryV1SavePost

> SalesDataShipmentTrackInterface salesShipmentTrackRepositoryV1SavePost(opts)

shipment/track

Performs persist operations for a specified shipment track.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ShipmentTrackApi();
let opts = {
  'salesShipmentTrackRepositoryV1SavePostRequest': new MagentoB2B.SalesShipmentTrackRepositoryV1SavePostRequest() // SalesShipmentTrackRepositoryV1SavePostRequest | 
};
apiInstance.salesShipmentTrackRepositoryV1SavePost(opts, (error, data, response) => {
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
 **salesShipmentTrackRepositoryV1SavePostRequest** | [**SalesShipmentTrackRepositoryV1SavePostRequest**](SalesShipmentTrackRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesDataShipmentTrackInterface**](SalesDataShipmentTrackInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

