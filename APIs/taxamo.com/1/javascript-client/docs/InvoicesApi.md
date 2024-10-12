# Taxamo.InvoicesApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emailInvoice**](InvoicesApi.md#emailInvoice) | **POST** /api/v1/transactions/{key}/invoice/send_email | Email invoice
[**emailRefund**](InvoicesApi.md#emailRefund) | **POST** /api/v1/transactions/{key}/invoice/refunds/{refund_note_number}/send_email | Email credit note



## emailInvoice

> EmailInvoiceOut emailInvoice(key, input)

Email invoice

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.InvoicesApi();
let key = "key_example"; // String | Transaction key.
let input = new Taxamo.EmailInvoiceIn(); // EmailInvoiceIn | Input
apiInstance.emailInvoice(key, input, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 
 **input** | [**EmailInvoiceIn**](EmailInvoiceIn.md)| Input | 

### Return type

[**EmailInvoiceOut**](EmailInvoiceOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## emailRefund

> EmailRefundOut emailRefund(key, refundNoteNumber, input)

Email credit note

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.InvoicesApi();
let key = "key_example"; // String | Transaction key.
let refundNoteNumber = "refundNoteNumber_example"; // String | Refund note id.
let input = new Taxamo.EmailRefundIn(); // EmailRefundIn | Input
apiInstance.emailRefund(key, refundNoteNumber, input, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 
 **refundNoteNumber** | **String**| Refund note id. | 
 **input** | [**EmailRefundIn**](EmailRefundIn.md)| Input | 

### Return type

[**EmailRefundOut**](EmailRefundOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

