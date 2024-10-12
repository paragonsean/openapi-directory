# MeilisearchV11.KeyManagementApi

All URIs are relative to *http://localhost:7700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAKey**](KeyManagementApi.md#createAKey) | **POST** /keys | Create a key
[**deleteAKey**](KeyManagementApi.md#deleteAKey) | **DELETE** /keys/kN2aK9EO8a7b627e425717d9196c8081552ca004e513545ed178f8a56981dbd3080d4a5b | Delete a key
[**getKeys**](KeyManagementApi.md#getKeys) | **GET** /keys | Get keys
[**getOneKey**](KeyManagementApi.md#getOneKey) | **GET** /keys/L8l05tFb188aab693735bbaf1f898b9902fb39f865160d39dddba2b47b940115a0430705 | Get one key
[**updateAKey**](KeyManagementApi.md#updateAKey) | **PATCH** /keys/wYZjGJyBcdb0621b97999c233246a8ec0a35d0fcd9a6417ef8ccee0c8978b64b123af2dd | Update a key



## createAKey

> createAKey(opts)

Create a key

Create a key

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.KeyManagementApi();
let opts = {
  'createAKeyRequest': {"actions":["documents.add","documents.delete"],"description":"Key to add and delete documents, in `books` index.","expiresAt":null,"indexes":["books"],"name":"docs-key"} // CreateAKeyRequest | 
};
apiInstance.createAKey(opts, (error, data, response) => {
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
 **createAKeyRequest** | [**CreateAKeyRequest**](CreateAKeyRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteAKey

> deleteAKey()

Delete a key

Delete a key

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.KeyManagementApi();
apiInstance.deleteAKey((error, data, response) => {
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


## getKeys

> getKeys(opts)

Get keys

Get keys

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.KeyManagementApi();
let opts = {
  'offset': "0", // String | 
  'limit': "10" // String | 
};
apiInstance.getKeys(opts, (error, data, response) => {
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


## getOneKey

> getOneKey()

Get one key

Get one key

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.KeyManagementApi();
apiInstance.getOneKey((error, data, response) => {
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


## updateAKey

> updateAKey(opts)

Update a key

Update a key

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.KeyManagementApi();
let opts = {
  'updateAKeyRequest': {"description":"Key to add and delete documents, but also to create indexes, in `book` index."} // UpdateAKeyRequest | 
};
apiInstance.updateAKey(opts, (error, data, response) => {
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
 **updateAKeyRequest** | [**UpdateAKeyRequest**](UpdateAKeyRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

