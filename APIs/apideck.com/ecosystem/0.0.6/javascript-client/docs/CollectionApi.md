# EcosystemApi.CollectionApi

All URIs are relative to *https://api.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collectionListingsAll**](CollectionApi.md#collectionListingsAll) | **GET** /ecosystems/{ecosystem_id}/collections/{id}/listings | List collection listings
[**collectionsAll**](CollectionApi.md#collectionsAll) | **GET** /ecosystems/{ecosystem_id}/collections | List collections
[**collectionsOne**](CollectionApi.md#collectionsOne) | **GET** /ecosystems/{ecosystem_id}/collections/{id} | Get collection



## collectionListingsAll

> GetListingsResponse collectionListingsAll(ecosystemId, id, opts)

List collection listings

List collection listings

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.CollectionApi();
let ecosystemId = "ecosystemId_example"; // String | 
let id = "id_example"; // String | ID of the record you are acting upon.
let opts = {
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 50 // Number | Number of records to return
};
apiInstance.collectionListingsAll(ecosystemId, id, opts, (error, data, response) => {
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


## collectionsAll

> GetCollectionsResponse collectionsAll(ecosystemId, opts)

List collections

List collections

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.CollectionApi();
let ecosystemId = "ecosystemId_example"; // String | 
let opts = {
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 50 // Number | Number of records to return
};
apiInstance.collectionsAll(ecosystemId, opts, (error, data, response) => {
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

[**GetCollectionsResponse**](GetCollectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionsOne

> GetCollectionResponse collectionsOne(ecosystemId, id)

Get collection

Get collection

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.CollectionApi();
let ecosystemId = "ecosystemId_example"; // String | 
let id = "id_example"; // String | ID of the record you are acting upon.
apiInstance.collectionsOne(ecosystemId, id, (error, data, response) => {
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

[**GetCollectionResponse**](GetCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

