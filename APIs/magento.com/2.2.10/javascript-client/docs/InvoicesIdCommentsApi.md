# MagentoB2B.InvoicesIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesInvoiceManagementV1GetCommentsListGet**](InvoicesIdCommentsApi.md#salesInvoiceManagementV1GetCommentsListGet) | **GET** /V1/invoices/{id}/comments | invoices/{id}/comments



## salesInvoiceManagementV1GetCommentsListGet

> SalesDataInvoiceCommentSearchResultInterface salesInvoiceManagementV1GetCommentsListGet(id)

invoices/{id}/comments

Lists comments for a specified invoice.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.InvoicesIdCommentsApi();
let id = 56; // Number | The invoice ID.
apiInstance.salesInvoiceManagementV1GetCommentsListGet(id, (error, data, response) => {
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

[**SalesDataInvoiceCommentSearchResultInterface**](SalesDataInvoiceCommentSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

