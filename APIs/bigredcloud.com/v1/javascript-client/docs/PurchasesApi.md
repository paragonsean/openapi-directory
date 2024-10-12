# BigRedCloudApi.PurchasesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchasesDelete**](PurchasesApi.md#purchasesDelete) | **DELETE** /v1/purchases/{id} | Removes an existing Purchase.
[**purchasesGet**](PurchasesApi.md#purchasesGet) | **GET** /v1/purchases | Returns a list of company&#39;s Purchases. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
[**purchasesPost**](PurchasesApi.md#purchasesPost) | **POST** /v1/purchases | Creates a new Purchase.
[**purchasesProcessBatch**](PurchasesApi.md#purchasesProcessBatch) | **PUT** /v1/purchases/batch | Processes a batch of Purchases.
[**purchasesPut**](PurchasesApi.md#purchasesPut) | **PUT** /v1/purchases/{id} | Updates an existing Purchase.
[**v1PurchasesIdGet**](PurchasesApi.md#v1PurchasesIdGet) | **GET** /v1/purchases/{id} | Returns information about a single Purchases.



## purchasesDelete

> Object purchasesDelete(id, timestamp)

Removes an existing Purchase.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PurchasesApi();
let id = 789; // Number | Id of Purchase to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Purchase to remove. Should be encoded in Base64.
apiInstance.purchasesDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Purchase to remove. | 
 **timestamp** | **String**| Timestamp of Purchase to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## purchasesGet

> PageResultPurchaseQueryDto purchasesGet()

Returns a list of company&#39;s Purchases. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PurchasesApi();
apiInstance.purchasesGet((error, data, response) => {
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

[**PageResultPurchaseQueryDto**](PageResultPurchaseQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## purchasesPost

> Object purchasesPost(purchaseDto)

Creates a new Purchase.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PurchasesApi();
let purchaseDto = new BigRedCloudApi.PurchaseDto(); // PurchaseDto | Information of Purchase to create.
apiInstance.purchasesPost(purchaseDto, (error, data, response) => {
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
 **purchaseDto** | [**PurchaseDto**](PurchaseDto.md)| Information of Purchase to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## purchasesProcessBatch

> Object purchasesProcessBatch(batchItemPurchaseDto)

Processes a batch of Purchases.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PurchasesApi();
let batchItemPurchaseDto = [new BigRedCloudApi.BatchItemPurchaseDto()]; // [BatchItemPurchaseDto] | Batch of Purchases to process.
apiInstance.purchasesProcessBatch(batchItemPurchaseDto, (error, data, response) => {
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
 **batchItemPurchaseDto** | [**[BatchItemPurchaseDto]**](BatchItemPurchaseDto.md)| Batch of Purchases to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## purchasesPut

> Object purchasesPut(id, purchaseDto)

Updates an existing Purchase.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PurchasesApi();
let id = 789; // Number | Id of Purchase to update.
let purchaseDto = new BigRedCloudApi.PurchaseDto(); // PurchaseDto | Information of Purchase to update.
apiInstance.purchasesPut(id, purchaseDto, (error, data, response) => {
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
 **id** | **Number**| Id of Purchase to update. | 
 **purchaseDto** | [**PurchaseDto**](PurchaseDto.md)| Information of Purchase to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1PurchasesIdGet

> PurchaseDto v1PurchasesIdGet(id)

Returns information about a single Purchases.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PurchasesApi();
let id = 789; // Number | Id of Purchase to return.
apiInstance.v1PurchasesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Purchase to return. | 

### Return type

[**PurchaseDto**](PurchaseDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

