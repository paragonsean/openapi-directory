# BigRedCloudApi.ProductsApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsDelete**](ProductsApi.md#productsDelete) | **DELETE** /v1/products/{id} | Removes an existing Product.
[**productsGet**](ProductsApi.md#productsGet) | **GET** /v1/products | Returns a list of company&#39;s Products. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;stockCode\&quot; fields.
[**productsPost**](ProductsApi.md#productsPost) | **POST** /v1/products | Creates a new Product.
[**productsProcessBatch**](ProductsApi.md#productsProcessBatch) | **PUT** /v1/products/batch | Processes a batch of Products.
[**productsPut**](ProductsApi.md#productsPut) | **PUT** /v1/products/{id} | Updates an existing Product.
[**v1ProductsIdGet**](ProductsApi.md#v1ProductsIdGet) | **GET** /v1/products/{id} | Returns information about a single Product.



## productsDelete

> Object productsDelete(id, timestamp)

Removes an existing Product.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.ProductsApi();
let id = 789; // Number | Id of Product to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Product to remove. Should be encoded in Base64.
apiInstance.productsDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Product to remove. | 
 **timestamp** | **String**| Timestamp of Product to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsGet

> PageResultProductDto productsGet()

Returns a list of company&#39;s Products. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;stockCode\&quot; fields.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.ProductsApi();
apiInstance.productsGet((error, data, response) => {
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

[**PageResultProductDto**](PageResultProductDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsPost

> Object productsPost(productDto)

Creates a new Product.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.ProductsApi();
let productDto = new BigRedCloudApi.ProductDto(); // ProductDto | Information of Product to create.
apiInstance.productsPost(productDto, (error, data, response) => {
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
 **productDto** | [**ProductDto**](ProductDto.md)| Information of Product to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsProcessBatch

> Object productsProcessBatch(batchItemProductDto)

Processes a batch of Products.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.ProductsApi();
let batchItemProductDto = [new BigRedCloudApi.BatchItemProductDto()]; // [BatchItemProductDto] | Batch of Products to process.
apiInstance.productsProcessBatch(batchItemProductDto, (error, data, response) => {
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
 **batchItemProductDto** | [**[BatchItemProductDto]**](BatchItemProductDto.md)| Batch of Products to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsPut

> Object productsPut(id, productDto)

Updates an existing Product.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.ProductsApi();
let id = 789; // Number | Id of Product to update.
let productDto = new BigRedCloudApi.ProductDto(); // ProductDto | Information of Product to update.
apiInstance.productsPut(id, productDto, (error, data, response) => {
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
 **id** | **Number**| Id of Product to update. | 
 **productDto** | [**ProductDto**](ProductDto.md)| Information of Product to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1ProductsIdGet

> ProductDto v1ProductsIdGet(id)

Returns information about a single Product.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.ProductsApi();
let id = 789; // Number | Id of Product to return.
apiInstance.v1ProductsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Product to return. | 

### Return type

[**ProductDto**](ProductDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

