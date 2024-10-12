# EcosystemApi.ProductApi

All URIs are relative to *https://api.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productListingsAll**](ProductApi.md#productListingsAll) | **GET** /ecosystems/{ecosystem_id}/products/{id}/listings | List product listings
[**productsAll**](ProductApi.md#productsAll) | **GET** /ecosystems/{ecosystem_id}/products | List products
[**productsOne**](ProductApi.md#productsOne) | **GET** /ecosystems/{ecosystem_id}/products/{id} | Get product



## productListingsAll

> GetListingsResponse productListingsAll(ecosystemId, id, opts)

List product listings

List product listings

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.ProductApi();
let ecosystemId = "ecosystemId_example"; // String | 
let id = "id_example"; // String | ID of the record you are acting upon.
let opts = {
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 50 // Number | Number of records to return
};
apiInstance.productListingsAll(ecosystemId, id, opts, (error, data, response) => {
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
 **ecosystemId** | **String**|  | 
 **id** | **String**| ID of the record you are acting upon. | 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of records to return | [optional] [default to 50]

### Return type

[**GetListingsResponse**](GetListingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsAll

> GetProductsResponse productsAll(ecosystemId)

List products

List products

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.ProductApi();
let ecosystemId = "ecosystemId_example"; // String | 
apiInstance.productsAll(ecosystemId, (error, data, response) => {
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
 **ecosystemId** | **String**|  | 

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsOne

> GetProductResponse productsOne(ecosystemId, id)

Get product

Get product

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.ProductApi();
let ecosystemId = "ecosystemId_example"; // String | 
let id = "id_example"; // String | ID of the record you are acting upon.
apiInstance.productsOne(ecosystemId, id, (error, data, response) => {
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
 **ecosystemId** | **String**|  | 
 **id** | **String**| ID of the record you are acting upon. | 

### Return type

[**GetProductResponse**](GetProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

