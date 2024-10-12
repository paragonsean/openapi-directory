# BigRedCloudApi.SalesInvoicesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesInvoicesDelete**](SalesInvoicesApi.md#salesInvoicesDelete) | **DELETE** /v1/salesInvoices/{id} | Removes an existing Sales Invoice.
[**salesInvoicesGet**](SalesInvoicesApi.md#salesInvoicesGet) | **GET** /v1/salesInvoices | Returns a list of company&#39;s Sales Invoices. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
[**salesInvoicesPost**](SalesInvoicesApi.md#salesInvoicesPost) | **POST** /v1/salesInvoices | Creates a new Sales Invoice.
[**salesInvoicesPostCreateSaleInvoiceWithGeneratingReference**](SalesInvoicesApi.md#salesInvoicesPostCreateSaleInvoiceWithGeneratingReference) | **POST** /v1/salesInvoices/createSaleInvoiceWithGeneratingReference | Creates a new Sale Invoice with auto generating reference.
[**salesInvoicesProcessBatch**](SalesInvoicesApi.md#salesInvoicesProcessBatch) | **PUT** /v1/salesInvoices/batch | Processes a batch of Sales Invoices.
[**salesInvoicesPut**](SalesInvoicesApi.md#salesInvoicesPut) | **PUT** /v1/salesInvoices/{id} | Updates an existing Sales Invoice.
[**v1SalesInvoicesIdGet**](SalesInvoicesApi.md#v1SalesInvoicesIdGet) | **GET** /v1/salesInvoices/{id} | Returns information about a single Sales Invoice.



## salesInvoicesDelete

> Object salesInvoicesDelete(id, timestamp)

Removes an existing Sales Invoice.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesInvoicesApi();
let id = 789; // Number | Id of Sales Invoice to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Sales Invoice to remove. Should be encoded in Base64.
apiInstance.salesInvoicesDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Sales Invoice to remove. | 
 **timestamp** | **String**| Timestamp of Sales Invoice to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesInvoicesGet

> PageResultSalesInvoiceQueryDto salesInvoicesGet()

Returns a list of company&#39;s Sales Invoices. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesInvoicesApi();
apiInstance.salesInvoicesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PageResultSalesInvoiceQueryDto**](PageResultSalesInvoiceQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesInvoicesPost

> Object salesInvoicesPost(salesInvoiceCreditNoteDto)

Creates a new Sales Invoice.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesInvoicesApi();
let salesInvoiceCreditNoteDto = new BigRedCloudApi.SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sales Invoice to create.
apiInstance.salesInvoicesPost(salesInvoiceCreditNoteDto, (error, data, response) => {
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
 **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sales Invoice to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesInvoicesPostCreateSaleInvoiceWithGeneratingReference

> Object salesInvoicesPostCreateSaleInvoiceWithGeneratingReference(salesInvoiceCreditNoteDto)

Creates a new Sale Invoice with auto generating reference.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesInvoicesApi();
let salesInvoiceCreditNoteDto = new BigRedCloudApi.SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sale Invoice to create.
apiInstance.salesInvoicesPostCreateSaleInvoiceWithGeneratingReference(salesInvoiceCreditNoteDto, (error, data, response) => {
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
 **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sale Invoice to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesInvoicesProcessBatch

> Object salesInvoicesProcessBatch(batchItemSalesInvoiceCreditNoteDto)

Processes a batch of Sales Invoices.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesInvoicesApi();
let batchItemSalesInvoiceCreditNoteDto = [new BigRedCloudApi.BatchItemSalesInvoiceCreditNoteDto()]; // [BatchItemSalesInvoiceCreditNoteDto] | Batch of Sales Invoices to process.
apiInstance.salesInvoicesProcessBatch(batchItemSalesInvoiceCreditNoteDto, (error, data, response) => {
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
 **batchItemSalesInvoiceCreditNoteDto** | [**[BatchItemSalesInvoiceCreditNoteDto]**](BatchItemSalesInvoiceCreditNoteDto.md)| Batch of Sales Invoices to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesInvoicesPut

> Object salesInvoicesPut(id, salesInvoiceCreditNoteDto)

Updates an existing Sales Invoice.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesInvoicesApi();
let id = 789; // Number | Id of Sales Invoice to update.
let salesInvoiceCreditNoteDto = new BigRedCloudApi.SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sales Invoice to update.
apiInstance.salesInvoicesPut(id, salesInvoiceCreditNoteDto, (error, data, response) => {
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
 **id** | **Number**| Id of Sales Invoice to update. | 
 **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sales Invoice to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1SalesInvoicesIdGet

> SalesInvoiceCreditNoteDto v1SalesInvoicesIdGet(id)

Returns information about a single Sales Invoice.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesInvoicesApi();
let id = 789; // Number | Id of Sales Invoice to return.
apiInstance.v1SalesInvoicesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Sales Invoice to return. | 

### Return type

[**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

