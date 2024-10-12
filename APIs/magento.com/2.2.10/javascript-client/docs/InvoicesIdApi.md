# MagentoB2B.InvoicesIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesInvoiceRepositoryV1GetGet**](InvoicesIdApi.md#salesInvoiceRepositoryV1GetGet) | **GET** /V1/invoices/{id} | invoices/{id}



## salesInvoiceRepositoryV1GetGet

> SalesDataInvoiceInterface salesInvoiceRepositoryV1GetGet(id)

invoices/{id}

Loads a specified invoice.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.InvoicesIdApi();
let id = 56; // Number | The invoice ID.
apiInstance.salesInvoiceRepositoryV1GetGet(id, (error, data, response) => {
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

[**SalesDataInvoiceInterface**](SalesDataInvoiceInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

