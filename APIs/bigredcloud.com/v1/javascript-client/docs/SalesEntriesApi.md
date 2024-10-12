# BigRedCloudApi.SalesEntriesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesEntriesDelete**](SalesEntriesApi.md#salesEntriesDelete) | **DELETE** /v1/salesEntries/{id} | Removes an existing Sales Entry.
[**salesEntriesGet**](SalesEntriesApi.md#salesEntriesGet) | **GET** /v1/salesEntries | Returns a list of company&#39;s Sales Entries. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
[**salesEntriesPost**](SalesEntriesApi.md#salesEntriesPost) | **POST** /v1/salesEntries | Creates a new Sales Entry.
[**salesEntriesProcessBatch**](SalesEntriesApi.md#salesEntriesProcessBatch) | **PUT** /v1/salesEntries/batch | Processes a batch of Sales Entries.
[**salesEntriesPut**](SalesEntriesApi.md#salesEntriesPut) | **PUT** /v1/salesEntries/{id} | Updates an existing Sales Entry.
[**v1SalesEntriesIdGet**](SalesEntriesApi.md#v1SalesEntriesIdGet) | **GET** /v1/salesEntries/{id} | Returns information about a single Sales Entry.



## salesEntriesDelete

> Object salesEntriesDelete(id, timestamp)

Removes an existing Sales Entry.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesEntriesApi();
let id = 789; // Number | Id of Sales Entry to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Sales Entry to remove. Should be encoded in Base64.
apiInstance.salesEntriesDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Sales Entry to remove. | 
 **timestamp** | **String**| Timestamp of Sales Entry to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesEntriesGet

> PageResultSalesEntryQueryDto salesEntriesGet()

Returns a list of company&#39;s Sales Entries. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesEntriesApi();
apiInstance.salesEntriesGet((error, data, response) => {
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

[**PageResultSalesEntryQueryDto**](PageResultSalesEntryQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesEntriesPost

> Object salesEntriesPost(salesEntryDto)

Creates a new Sales Entry.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesEntriesApi();
let salesEntryDto = new BigRedCloudApi.SalesEntryDto(); // SalesEntryDto | Information of Sales Entry to create.
apiInstance.salesEntriesPost(salesEntryDto, (error, data, response) => {
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
 **salesEntryDto** | [**SalesEntryDto**](SalesEntryDto.md)| Information of Sales Entry to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesEntriesProcessBatch

> Object salesEntriesProcessBatch(batchItemSalesEntryDto)

Processes a batch of Sales Entries.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesEntriesApi();
let batchItemSalesEntryDto = [new BigRedCloudApi.BatchItemSalesEntryDto()]; // [BatchItemSalesEntryDto] | Batch of Sales Entries to process.
apiInstance.salesEntriesProcessBatch(batchItemSalesEntryDto, (error, data, response) => {
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
 **batchItemSalesEntryDto** | [**[BatchItemSalesEntryDto]**](BatchItemSalesEntryDto.md)| Batch of Sales Entries to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesEntriesPut

> Object salesEntriesPut(id, salesEntryDto)

Updates an existing Sales Entry.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesEntriesApi();
let id = 789; // Number | Id of Sales Entry to update.
let salesEntryDto = new BigRedCloudApi.SalesEntryDto(); // SalesEntryDto | Information of Sales Entry to update.
apiInstance.salesEntriesPut(id, salesEntryDto, (error, data, response) => {
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
 **id** | **Number**| Id of Sales Entry to update. | 
 **salesEntryDto** | [**SalesEntryDto**](SalesEntryDto.md)| Information of Sales Entry to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1SalesEntriesIdGet

> SalesEntryDto v1SalesEntriesIdGet(id)

Returns information about a single Sales Entry.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesEntriesApi();
let id = 789; // Number | Id of Sales Entry to return.
apiInstance.v1SalesEntriesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Sales Entry to return. | 

### Return type

[**SalesEntryDto**](SalesEntryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

