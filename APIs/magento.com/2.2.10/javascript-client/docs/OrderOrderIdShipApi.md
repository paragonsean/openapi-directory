# MagentoB2B.OrderOrderIdShipApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesShipOrderV1ExecutePost**](OrderOrderIdShipApi.md#salesShipOrderV1ExecutePost) | **POST** /V1/order/{orderId}/ship | order/{orderId}/ship



## salesShipOrderV1ExecutePost

> Number salesShipOrderV1ExecutePost(orderId, opts)

order/{orderId}/ship

Creates new Shipment for given Order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrderOrderIdShipApi();
let orderId = 56; // Number | 
let opts = {
  'salesShipOrderV1ExecutePostRequest': new MagentoB2B.SalesShipOrderV1ExecutePostRequest() // SalesShipOrderV1ExecutePostRequest | 
};
apiInstance.salesShipOrderV1ExecutePost(orderId, opts, (error, data, response) => {
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
 **orderId** | **Number**|  | 
 **salesShipOrderV1ExecutePostRequest** | [**SalesShipOrderV1ExecutePostRequest**](SalesShipOrderV1ExecutePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

