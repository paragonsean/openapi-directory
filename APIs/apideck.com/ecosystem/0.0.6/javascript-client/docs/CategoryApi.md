# EcosystemApi.CategoryApi

All URIs are relative to *https://api.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesAll**](CategoryApi.md#categoriesAll) | **GET** /ecosystems/{ecosystem_id}/categories | List categories
[**categoriesOne**](CategoryApi.md#categoriesOne) | **GET** /ecosystems/{ecosystem_id}/categories/{id} | Get category
[**categoryListingsAll**](CategoryApi.md#categoryListingsAll) | **GET** /ecosystems/{ecosystem_id}/categories/{id}/listings | List category listings



## categoriesAll

> GetCategoriesResponse categoriesAll(ecosystemId, opts)

List categories

List categories

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.CategoryApi();
let ecosystemId = "ecosystemId_example"; // String | 
let opts = {
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 50 // Number | Number of records to return
};
apiInstance.categoriesAll(ecosystemId, opts, (error, data, response) => {
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
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of records to return | [optional] [default to 50]

### Return type

[**GetCategoriesResponse**](GetCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesOne

> GetCategoryResponse categoriesOne(ecosystemId, id)

Get category

Get category

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.CategoryApi();
let ecosystemId = "ecosystemId_example"; // String | 
let id = "id_example"; // String | ID of the record you are acting upon.
apiInstance.categoriesOne(ecosystemId, id, (error, data, response) => {
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

[**GetCategoryResponse**](GetCategoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryListingsAll

> GetListingsResponse categoryListingsAll(ecosystemId, id, opts)

List category listings

List category listings

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.CategoryApi();
let ecosystemId = "ecosystemId_example"; // String | 
let id = "id_example"; // String | ID of the record you are acting upon.
let opts = {
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 50 // Number | Number of records to return
};
apiInstance.categoryListingsAll(ecosystemId, id, opts, (error, data, response) => {
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

