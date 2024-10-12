# BigRedCloudApi.SalesCreditNotesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesCreditNotesDelete**](SalesCreditNotesApi.md#salesCreditNotesDelete) | **DELETE** /v1/salesCreditNotes/{id} | Removes an existing Sales Credit Note.
[**salesCreditNotesGet**](SalesCreditNotesApi.md#salesCreditNotesGet) | **GET** /v1/salesCreditNotes | Returns a list of company&#39;s Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
[**salesCreditNotesPost**](SalesCreditNotesApi.md#salesCreditNotesPost) | **POST** /v1/salesCreditNotes | Creates a new Sales Credit Note.
[**salesCreditNotesProcessBatch**](SalesCreditNotesApi.md#salesCreditNotesProcessBatch) | **PUT** /v1/salesCreditNotes/batch | Processes a batch of Sales Credit Notes.
[**salesCreditNotesPut**](SalesCreditNotesApi.md#salesCreditNotesPut) | **PUT** /v1/salesCreditNotes/{id} | Updates an existing Sales Credit Note.
[**v1SalesCreditNotesIdGet**](SalesCreditNotesApi.md#v1SalesCreditNotesIdGet) | **GET** /v1/salesCreditNotes/{id} | Returns information about a single Sales Credit Note.



## salesCreditNotesDelete

> Object salesCreditNotesDelete(id, timestamp)

Removes an existing Sales Credit Note.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesCreditNotesApi();
let id = 789; // Number | Id of Sales Credit Note to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Sales Credit Note to remove. Should be encoded in Base64.
apiInstance.salesCreditNotesDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Sales Credit Note to remove. | 
 **timestamp** | **String**| Timestamp of Sales Credit Note to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesCreditNotesGet

> PageResultSalesCreditNoteQueryDto salesCreditNotesGet()

Returns a list of company&#39;s Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesCreditNotesApi();
apiInstance.salesCreditNotesGet((error, data, response) => {
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

[**PageResultSalesCreditNoteQueryDto**](PageResultSalesCreditNoteQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesCreditNotesPost

> Object salesCreditNotesPost(salesInvoiceCreditNoteDto)

Creates a new Sales Credit Note.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesCreditNotesApi();
let salesInvoiceCreditNoteDto = new BigRedCloudApi.SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sales Credit Note to create.
apiInstance.salesCreditNotesPost(salesInvoiceCreditNoteDto, (error, data, response) => {
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
 **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sales Credit Note to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesCreditNotesProcessBatch

> Object salesCreditNotesProcessBatch(batchItemSalesInvoiceCreditNoteDto)

Processes a batch of Sales Credit Notes.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesCreditNotesApi();
let batchItemSalesInvoiceCreditNoteDto = [new BigRedCloudApi.BatchItemSalesInvoiceCreditNoteDto()]; // [BatchItemSalesInvoiceCreditNoteDto] | Batch of Sales Credit Notes to process.
apiInstance.salesCreditNotesProcessBatch(batchItemSalesInvoiceCreditNoteDto, (error, data, response) => {
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
 **batchItemSalesInvoiceCreditNoteDto** | [**[BatchItemSalesInvoiceCreditNoteDto]**](BatchItemSalesInvoiceCreditNoteDto.md)| Batch of Sales Credit Notes to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesCreditNotesPut

> Object salesCreditNotesPut(id, salesInvoiceCreditNoteDto)

Updates an existing Sales Credit Note.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesCreditNotesApi();
let id = 789; // Number | Id of Sales Credit Note to update.
let salesInvoiceCreditNoteDto = new BigRedCloudApi.SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sales Credit Note to update.
apiInstance.salesCreditNotesPut(id, salesInvoiceCreditNoteDto, (error, data, response) => {
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
 **id** | **Number**| Id of Sales Credit Note to update. | 
 **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sales Credit Note to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1SalesCreditNotesIdGet

> SalesInvoiceCreditNoteDto v1SalesCreditNotesIdGet(id)

Returns information about a single Sales Credit Note.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesCreditNotesApi();
let id = 789; // Number | Id of Sales Credit Note to return.
apiInstance.v1SalesCreditNotesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Sales Credit Note to return. | 

### Return type

[**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

