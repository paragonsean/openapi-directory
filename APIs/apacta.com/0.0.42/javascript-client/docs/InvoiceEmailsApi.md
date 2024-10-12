# Apacta.InvoiceEmailsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOneInvoiceEmails**](InvoiceEmailsApi.md#getOneInvoiceEmails) | **GET** /invoices/{invoice_id}/emails/{email_id} | Get an invoice emails



## getOneInvoiceEmails

> GetOneInvoiceEmails200Response getOneInvoiceEmails(invoiceId, emailId)

Get an invoice emails

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.InvoiceEmailsApi();
let invoiceId = "invoiceId_example"; // String | 
let emailId = "emailId_example"; // String | 
apiInstance.getOneInvoiceEmails(invoiceId, emailId, (error, data, response) => {
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
 **invoiceId** | **String**|  | 
 **emailId** | **String**|  | 

### Return type

[**GetOneInvoiceEmails200Response**](GetOneInvoiceEmails200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

