# MagentoB2B.OrderOrderIdRefundApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRefundOrderV1ExecutePost**](OrderOrderIdRefundApi.md#salesRefundOrderV1ExecutePost) | **POST** /V1/order/{orderId}/refund | order/{orderId}/refund



## salesRefundOrderV1ExecutePost

> Number salesRefundOrderV1ExecutePost(orderId, opts)

order/{orderId}/refund

Create offline refund for order

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrderOrderIdRefundApi();
let orderId = 56; // Number | 
let opts = {
  'salesRefundOrderV1ExecutePostRequest': new MagentoB2B.SalesRefundOrderV1ExecutePostRequest() // SalesRefundOrderV1ExecutePostRequest | 
};
apiInstance.salesRefundOrderV1ExecutePost(orderId, opts, (error, data, response) => {
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
 **salesRefundOrderV1ExecutePostRequest** | [**SalesRefundOrderV1ExecutePostRequest**](SalesRefundOrderV1ExecutePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

