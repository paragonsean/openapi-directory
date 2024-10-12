# MagentoB2B.ShipmentApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesShipmentRepositoryV1SavePost**](ShipmentApi.md#salesShipmentRepositoryV1SavePost) | **POST** /V1/shipment/ | shipment/



## salesShipmentRepositoryV1SavePost

> SalesDataShipmentInterface salesShipmentRepositoryV1SavePost(opts)

shipment/

Performs persist operations for a specified shipment.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ShipmentApi();
let opts = {
  'salesShipmentRepositoryV1SavePostRequest': new MagentoB2B.SalesShipmentRepositoryV1SavePostRequest() // SalesShipmentRepositoryV1SavePostRequest | 
};
apiInstance.salesShipmentRepositoryV1SavePost(opts, (error, data, response) => {
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
 **salesShipmentRepositoryV1SavePostRequest** | [**SalesShipmentRepositoryV1SavePostRequest**](SalesShipmentRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesDataShipmentInterface**](SalesDataShipmentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

