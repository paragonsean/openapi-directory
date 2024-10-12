# MagentoB2B.InvoicesIdCaptureApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesInvoiceManagementV1SetCapturePost**](InvoicesIdCaptureApi.md#salesInvoiceManagementV1SetCapturePost) | **POST** /V1/invoices/{id}/capture | invoices/{id}/capture



## salesInvoiceManagementV1SetCapturePost

> String salesInvoiceManagementV1SetCapturePost(id)

invoices/{id}/capture

Sets invoice capture.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.InvoicesIdCaptureApi();
let id = 56; // Number | 
apiInstance.salesInvoiceManagementV1SetCapturePost(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

