# MagentoB2B.OrderOrderIdInvoiceApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesInvoiceOrderV1ExecutePost**](OrderOrderIdInvoiceApi.md#salesInvoiceOrderV1ExecutePost) | **POST** /V1/order/{orderId}/invoice | order/{orderId}/invoice



## salesInvoiceOrderV1ExecutePost

> Number salesInvoiceOrderV1ExecutePost(orderId, opts)

order/{orderId}/invoice



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrderOrderIdInvoiceApi();
let orderId = 56; // Number | 
let opts = {
  'salesInvoiceOrderV1ExecutePostRequest': new MagentoB2B.SalesInvoiceOrderV1ExecutePostRequest() // SalesInvoiceOrderV1ExecutePostRequest | 
};
apiInstance.salesInvoiceOrderV1ExecutePost(orderId, opts, (error, data, response) => {
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
 **salesInvoiceOrderV1ExecutePostRequest** | [**SalesInvoiceOrderV1ExecutePostRequest**](SalesInvoiceOrderV1ExecutePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

