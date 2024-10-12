# BigRedCloudApi.SalesRepApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRepDelete**](SalesRepApi.md#salesRepDelete) | **DELETE** /v1/salesReps/{id} | Removes an existing Sale Rep.
[**salesRepGet**](SalesRepApi.md#salesRepGet) | **GET** /v1/salesReps | Returns a list of company&#39;s SaleRep.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;.
[**salesRepPost**](SalesRepApi.md#salesRepPost) | **POST** /v1/salesReps | Creates a new SaleRep.
[**salesRepProcessBatch**](SalesRepApi.md#salesRepProcessBatch) | **PUT** /v1/salesReps/batch | Processes a batch of Sale Rep.
[**salesRepPut**](SalesRepApi.md#salesRepPut) | **PUT** /v1/salesReps/{id} | Updates an existing Sale Rep.
[**v1SalesRepsIdGet**](SalesRepApi.md#v1SalesRepsIdGet) | **GET** /v1/salesReps/{id} | Returns information about a single SaleRep.



## salesRepDelete

> Object salesRepDelete(id, timestamp)

Removes an existing Sale Rep.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesRepApi();
let id = 789; // Number | Id of Sale Rep to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Sale Rep to remove. Should be encoded in Base64.
apiInstance.salesRepDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Sale Rep to remove. | 
 **timestamp** | **String**| Timestamp of Sale Rep to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesRepGet

> PageResultSaleRepsDto salesRepGet()

Returns a list of company&#39;s SaleRep.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesRepApi();
apiInstance.salesRepGet((error, data, response) => {
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

[**PageResultSaleRepsDto**](PageResultSaleRepsDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesRepPost

> Object salesRepPost(saleRepsDto)

Creates a new SaleRep.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesRepApi();
let saleRepsDto = new BigRedCloudApi.SaleRepsDto(); // SaleRepsDto | Information of Sale Rep to create.
apiInstance.salesRepPost(saleRepsDto, (error, data, response) => {
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
 **saleRepsDto** | [**SaleRepsDto**](SaleRepsDto.md)| Information of Sale Rep to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesRepProcessBatch

> Object salesRepProcessBatch(batchItemSaleRepsDto)

Processes a batch of Sale Rep.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesRepApi();
let batchItemSaleRepsDto = [new BigRedCloudApi.BatchItemSaleRepsDto()]; // [BatchItemSaleRepsDto] | Batch of Sale Rep to process.
apiInstance.salesRepProcessBatch(batchItemSaleRepsDto, (error, data, response) => {
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
 **batchItemSaleRepsDto** | [**[BatchItemSaleRepsDto]**](BatchItemSaleRepsDto.md)| Batch of Sale Rep to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesRepPut

> Object salesRepPut(id, saleRepsDto)

Updates an existing Sale Rep.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesRepApi();
let id = 789; // Number | Id of Sale Rep to update.
let saleRepsDto = new BigRedCloudApi.SaleRepsDto(); // SaleRepsDto | Information of Sale Rep to update.
apiInstance.salesRepPut(id, saleRepsDto, (error, data, response) => {
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
 **id** | **Number**| Id of Sale Rep to update. | 
 **saleRepsDto** | [**SaleRepsDto**](SaleRepsDto.md)| Information of Sale Rep to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1SalesRepsIdGet

> SaleRepsDto v1SalesRepsIdGet(id)

Returns information about a single SaleRep.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SalesRepApi();
let id = 789; // Number | Id of Sale Rep to return.
apiInstance.v1SalesRepsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Sale Rep to return. | 

### Return type

[**SaleRepsDto**](SaleRepsDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

