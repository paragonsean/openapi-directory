# MagentoB2B.InvoicesIdEmailsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesInvoiceManagementV1NotifyPost**](InvoicesIdEmailsApi.md#salesInvoiceManagementV1NotifyPost) | **POST** /V1/invoices/{id}/emails | invoices/{id}/emails



## salesInvoiceManagementV1NotifyPost

> Boolean salesInvoiceManagementV1NotifyPost(id)

invoices/{id}/emails

Emails a user a specified invoice.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.InvoicesIdEmailsApi();
let id = 56; // Number | The invoice ID.
apiInstance.salesInvoiceManagementV1NotifyPost(id, (error, data, response) => {
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

