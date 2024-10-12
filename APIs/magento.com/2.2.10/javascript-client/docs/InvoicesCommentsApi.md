# MagentoB2B.InvoicesCommentsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesInvoiceCommentRepositoryV1SavePost**](InvoicesCommentsApi.md#salesInvoiceCommentRepositoryV1SavePost) | **POST** /V1/invoices/comments | invoices/comments



## salesInvoiceCommentRepositoryV1SavePost

> SalesDataInvoiceCommentInterface salesInvoiceCommentRepositoryV1SavePost(opts)

invoices/comments

Performs persist operations for a specified invoice comment.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.InvoicesCommentsApi();
let opts = {
  'salesInvoiceCommentRepositoryV1SavePostRequest': new MagentoB2B.SalesInvoiceCommentRepositoryV1SavePostRequest() // SalesInvoiceCommentRepositoryV1SavePostRequest | 
};
apiInstance.salesInvoiceCommentRepositoryV1SavePost(opts, (error, data, response) => {
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
 **salesInvoiceCommentRepositoryV1SavePostRequest** | [**SalesInvoiceCommentRepositoryV1SavePostRequest**](SalesInvoiceCommentRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesDataInvoiceCommentInterface**](SalesDataInvoiceCommentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

