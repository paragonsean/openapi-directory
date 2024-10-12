# MagentoB2B.InvoiceInvoiceIdRefundApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRefundInvoiceV1ExecutePost**](InvoiceInvoiceIdRefundApi.md#salesRefundInvoiceV1ExecutePost) | **POST** /V1/invoice/{invoiceId}/refund | invoice/{invoiceId}/refund



## salesRefundInvoiceV1ExecutePost

> Number salesRefundInvoiceV1ExecutePost(invoiceId, opts)

invoice/{invoiceId}/refund

Create refund for invoice

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.InvoiceInvoiceIdRefundApi();
let invoiceId = 56; // Number | 
let opts = {
  'salesRefundInvoiceV1ExecutePostRequest': new MagentoB2B.SalesRefundInvoiceV1ExecutePostRequest() // SalesRefundInvoiceV1ExecutePostRequest | 
};
apiInstance.salesRefundInvoiceV1ExecutePost(invoiceId, opts, (error, data, response) => {
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
 **invoiceId** | **Number**|  | 
 **salesRefundInvoiceV1ExecutePostRequest** | [**SalesRefundInvoiceV1ExecutePostRequest**](SalesRefundInvoiceV1ExecutePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

