# BigRedCloudApi.CashPaymentsApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cashPaymentsDelete**](CashPaymentsApi.md#cashPaymentsDelete) | **DELETE** /v1/cashPayments/{id} | Removes an existing Cash Payment.
[**cashPaymentsGet**](CashPaymentsApi.md#cashPaymentsGet) | **GET** /v1/cashPayments | Returns a list of company&#39;s Cash Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
[**cashPaymentsPost**](CashPaymentsApi.md#cashPaymentsPost) | **POST** /v1/cashPayments | Creates a new Cash Payment.
[**cashPaymentsProcessBatch**](CashPaymentsApi.md#cashPaymentsProcessBatch) | **PUT** /v1/cashPayments/batch | Processes a batch of Cash Payments.
[**cashPaymentsPut**](CashPaymentsApi.md#cashPaymentsPut) | **PUT** /v1/cashPayments/{id} | Updates an existing Cash Payment.
[**v1CashPaymentsIdGet**](CashPaymentsApi.md#v1CashPaymentsIdGet) | **GET** /v1/cashPayments/{id} | Returns information about a single Cash Payment.



## cashPaymentsDelete

> Object cashPaymentsDelete(id, timestamp)

Removes an existing Cash Payment.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashPaymentsApi();
let id = 789; // Number | Id of Cash Receipt to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Cash Receipt to remove. Should be encoded in Base64.
apiInstance.cashPaymentsDelete(id, timestamp, (error, data, response) => {
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


## cashPaymentsGet

> PageResultCashPaymentQueryDto cashPaymentsGet()

Returns a list of company&#39;s Cash Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashPaymentsApi();
apiInstance.cashPaymentsGet((error, data, response) => {
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

[**PageResultCashPaymentQueryDto**](PageResultCashPaymentQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cashPaymentsPost

> Object cashPaymentsPost(cashPaymentDto)

Creates a new Cash Payment.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashPaymentsApi();
let cashPaymentDto = new BigRedCloudApi.CashPaymentDto(); // CashPaymentDto | Information of Cash Receipt to create.
apiInstance.cashPaymentsPost(cashPaymentDto, (error, data, response) => {
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
 **cashPaymentDto** | [**CashPaymentDto**](CashPaymentDto.md)| Information of Cash Receipt to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cashPaymentsProcessBatch

> Object cashPaymentsProcessBatch(batchItemCashPaymentDto)

Processes a batch of Cash Payments.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashPaymentsApi();
let batchItemCashPaymentDto = [new BigRedCloudApi.BatchItemCashPaymentDto()]; // [BatchItemCashPaymentDto] | Batch of Cash Receipts to process.
apiInstance.cashPaymentsProcessBatch(batchItemCashPaymentDto, (error, data, response) => {
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
 **batchItemCashPaymentDto** | [**[BatchItemCashPaymentDto]**](BatchItemCashPaymentDto.md)| Batch of Cash Receipts to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cashPaymentsPut

> Object cashPaymentsPut(id, cashPaymentDto)

Updates an existing Cash Payment.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashPaymentsApi();
let id = 789; // Number | Id of Cash Receipt to update.
let cashPaymentDto = new BigRedCloudApi.CashPaymentDto(); // CashPaymentDto | Information of Cash Receipt to update.
apiInstance.cashPaymentsPut(id, cashPaymentDto, (error, data, response) => {
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
 **cashPaymentDto** | [**CashPaymentDto**](CashPaymentDto.md)| Information of Cash Receipt to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1CashPaymentsIdGet

> CashPaymentDto v1CashPaymentsIdGet(id)

Returns information about a single Cash Payment.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CashPaymentsApi();
let id = 789; // Number | Id of Cash Receipt to return.
apiInstance.v1CashPaymentsIdGet(id, (error, data, response) => {
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

[**CashPaymentDto**](CashPaymentDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

