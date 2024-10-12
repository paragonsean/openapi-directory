# MeilisearchV11.IndexesApi

All URIs are relative to *http://localhost:7700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIndexWithPrimaryKey**](IndexesApi.md#createIndexWithPrimaryKey) | **POST** /indexes | Create index with primary key
[**deleteAnIndex**](IndexesApi.md#deleteAnIndex) | **DELETE** /indexes/books | Delete an index
[**getIndexes**](IndexesApi.md#getIndexes) | **GET** /indexes | Get indexes
[**showIndex**](IndexesApi.md#showIndex) | **GET** /indexes/books | Show index
[**swapIndexes**](IndexesApi.md#swapIndexes) | **POST** /indexes/swap-indexes | Swap indexes
[**updateIndex**](IndexesApi.md#updateIndex) | **PATCH** /indexes/books | Update index



## createIndexWithPrimaryKey

> createIndexWithPrimaryKey(opts)

Create index with primary key

Create index with primary key

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.IndexesApi();
let opts = {
  'createIndexWithPrimaryKeyRequest': {"primaryKey":"number","uid":"books"} // CreateIndexWithPrimaryKeyRequest | 
};
apiInstance.createIndexWithPrimaryKey(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createIndexWithPrimaryKeyRequest** | [**CreateIndexWithPrimaryKeyRequest**](CreateIndexWithPrimaryKeyRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteAnIndex

> deleteAnIndex()

Delete an index

Delete an index

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.IndexesApi();
apiInstance.deleteAnIndex((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIndexes

> getIndexes(opts)

Get indexes

Get indexes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.IndexesApi();
let opts = {
  'offset': "0", // String | 
  'limit': "2" // String | 
};
apiInstance.getIndexes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## showIndex

> showIndex()

Show index

Show index

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.IndexesApi();
apiInstance.showIndex((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## swapIndexes

> swapIndexes(opts)

Swap indexes

Swap indexes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.IndexesApi();
let opts = {
  'swapIndexesRequestInner': [{"indexes":["books","books_temp"]}] // [SwapIndexesRequestInner] | 
};
apiInstance.swapIndexes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swapIndexesRequestInner** | [**[SwapIndexesRequestInner]**](SwapIndexesRequestInner.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateIndex

> updateIndex(opts)

Update index

Can only change the document identifier if it has not already been added before.

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.IndexesApi();
let opts = {
  'updateIndexRequest': {"primaryKey":"title"} // UpdateIndexRequest | 
};
apiInstance.updateIndex(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateIndexRequest** | [**UpdateIndexRequest**](UpdateIndexRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

