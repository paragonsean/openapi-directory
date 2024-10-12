# MagentoB2B.InvoicesIdVoidApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesInvoiceManagementV1SetVoidPost**](InvoicesIdVoidApi.md#salesInvoiceManagementV1SetVoidPost) | **POST** /V1/invoices/{id}/void | invoices/{id}/void



## salesInvoiceManagementV1SetVoidPost

> Boolean salesInvoiceManagementV1SetVoidPost(id)

invoices/{id}/void

Voids a specified invoice.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.InvoicesIdVoidApi();
let id = 56; // Number | The invoice ID.
apiInstance.salesInvoiceManagementV1SetVoidPost(id, (error, data, response) => {
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
 **id** | **Number**| The invoice ID. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

