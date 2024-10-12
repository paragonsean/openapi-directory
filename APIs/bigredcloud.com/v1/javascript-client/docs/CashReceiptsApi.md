# BigRedCloudApi.CashReceiptsApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cashReceiptsDelete**](CashReceiptsApi.md#cashReceiptsDelete) | **DELETE** /v1/cashReceipts/{id} | Removes an existing Cash Receipt.
[**cashReceiptsGet**](CashReceiptsApi.md#cashReceiptsGet) | **GET** /v1/cashReceipts | Returns a list of company&#39;s Cash Receipts. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
[**cashReceiptsPost**](CashReceiptsApi.md#cashReceiptsPost) | **POST** /v1/cashReceipts | Creates a new Cash Receipt.
[**cashReceiptsProcessBatch**](CashReceiptsApi.md#cashReceiptsProcessBatch) | **PUT** /v1/cashReceipts/batch | Processes a batch of Cash Receipts.
[**cashReceiptsPut**](CashReceiptsApi.md#cashReceiptsPut) | **PUT** /v1/cashReceipts/{id} | Updates an existing Cash Receipt.
[**v1CashReceiptsIdGet**](CashReceiptsApi.md#v1CashReceiptsIdGet) | **GET** /v1/cashReceipts/{id} | Returns information about a single Cash Receipt.



## cashReceiptsDelete

> Object cashReceiptsDelete(id, timestamp)

Removes an existing Cash Receipt.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashReceiptsApi();
let id = 789; // Number | Id of Cash Receipt to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Cash Receipt to remove. Should be encoded in Base64.
apiInstance.cashReceiptsDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Cash Receipt to remove. | 
 **timestamp** | **String**| Timestamp of Cash Receipt to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cashReceiptsGet

> PageResultCashReceiptQueryDto cashReceiptsGet()

Returns a list of company&#39;s Cash Receipts. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashReceiptsApi();
apiInstance.cashReceiptsGet((error, data, response) => {
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

[**PageResultCashReceiptQueryDto**](PageResultCashReceiptQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cashReceiptsPost

> Object cashReceiptsPost(cashReceiptDto)

Creates a new Cash Receipt.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashReceiptsApi();
let cashReceiptDto = new BigRedCloudApi.CashReceiptDto(); // CashReceiptDto | Information of Cash Receipt to create.
apiInstance.cashReceiptsPost(cashReceiptDto, (error, data, response) => {
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
 **cashReceiptDto** | [**CashReceiptDto**](CashReceiptDto.md)| Information of Cash Receipt to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cashReceiptsProcessBatch

> Object cashReceiptsProcessBatch(batchItemCashReceiptDto)

Processes a batch of Cash Receipts.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashReceiptsApi();
let batchItemCashReceiptDto = [new BigRedCloudApi.BatchItemCashReceiptDto()]; // [BatchItemCashReceiptDto] | Batch of Cash Receipts to process.
apiInstance.cashReceiptsProcessBatch(batchItemCashReceiptDto, (error, data, response) => {
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
 **batchItemCashReceiptDto** | [**[BatchItemCashReceiptDto]**](BatchItemCashReceiptDto.md)| Batch of Cash Receipts to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cashReceiptsPut

> Object cashReceiptsPut(id, cashReceiptDto)

Updates an existing Cash Receipt.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashReceiptsApi();
let id = 789; // Number | Id of Cash Receipt to update.
let cashReceiptDto = new BigRedCloudApi.CashReceiptDto(); // CashReceiptDto | Information of Cash Receipt to update.
apiInstance.cashReceiptsPut(id, cashReceiptDto, (error, data, response) => {
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
 **id** | **Number**| Id of Cash Receipt to update. | 
 **cashReceiptDto** | [**CashReceiptDto**](CashReceiptDto.md)| Information of Cash Receipt to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1CashReceiptsIdGet

> CashReceiptDto v1CashReceiptsIdGet(id)

Returns information about a single Cash Receipt.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashReceiptsApi();
let id = 789; // Number | Id of Cash Receipt to return.
apiInstance.v1CashReceiptsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Cash Receipt to return. | 

### Return type

[**CashReceiptDto**](CashReceiptDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

