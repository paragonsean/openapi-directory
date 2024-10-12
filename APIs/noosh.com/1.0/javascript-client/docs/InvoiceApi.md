# NooshApiApplication.InvoiceApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInvoice**](InvoiceApi.md#getInvoice) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/{invoice_id} | List a specific invoice of project Level
[**getInvoiceFiles**](InvoiceApi.md#getInvoiceFiles) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/{invoice_id}/files | List files of invoice Level
[**getInvoices**](InvoiceApi.md#getInvoices) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/orders/{order_id} | List invoices by a specific order



## getInvoice

> InvoiceExpandVO getInvoice(workgroupId, projectId, invoiceId)

List a specific invoice of project Level

List a specific invoice of project Level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.InvoiceApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let invoiceId = "invoiceId_example"; // String | 
apiInstance.getInvoice(workgroupId, projectId, invoiceId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **invoiceId** | **String**|  | 

### Return type

[**InvoiceExpandVO**](InvoiceExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getInvoiceFiles

> FileListResponseVO getInvoiceFiles(workgroupId, projectId, invoiceId)

List files of invoice Level

List files of invoice Level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.InvoiceApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let invoiceId = "invoiceId_example"; // String | 
apiInstance.getInvoiceFiles(workgroupId, projectId, invoiceId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **invoiceId** | **String**|  | 

### Return type

[**FileListResponseVO**](FileListResponseVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getInvoices

> InvoiceDetailListExpandVO getInvoices(workgroupId, projectId, orderId)

List invoices by a specific order

List invoices by a specific order

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.InvoiceApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let orderId = "orderId_example"; // String | 
apiInstance.getInvoices(workgroupId, projectId, orderId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **orderId** | **String**|  | 

### Return type

[**InvoiceDetailListExpandVO**](InvoiceDetailListExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

