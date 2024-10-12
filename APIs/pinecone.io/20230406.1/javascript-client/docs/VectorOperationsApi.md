# PineconeApi.VectorOperationsApi

All URIs are relative to *https://controller.us-east1-gcp.pinecone.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callDelete**](VectorOperationsApi.md#callDelete) | **POST** /vectors/delete | Delete
[**describeIndexStats**](VectorOperationsApi.md#describeIndexStats) | **POST** /describe_index_stats | Describe Index Stats
[**fetch**](VectorOperationsApi.md#fetch) | **POST** /vectors/fetch | Fetch
[**query**](VectorOperationsApi.md#query) | **POST** /query | Query
[**update**](VectorOperationsApi.md#update) | **POST** /vectors/update | Fetch
[**upsert**](VectorOperationsApi.md#upsert) | **POST** /vectors/upsert | Upsert



## callDelete

> Object callDelete(deleteRequest)

Delete

The &#x60;Delete&#x60; operation deletes vectors, by id, from a single namespace. You can delete items by their id, from a single namespace.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.VectorOperationsApi();
let deleteRequest = new PineconeApi.DeleteRequest(); // DeleteRequest | 
apiInstance.callDelete(deleteRequest, (error, data, response) => {
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
 **deleteRequest** | [**DeleteRequest**](DeleteRequest.md)|  | 

### Return type

**Object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeIndexStats

> DescribeIndexStatsResponse describeIndexStats(describeIndexStatsRequest)

Describe Index Stats

The &#x60;DescribeIndexStats&#x60; operation returns statistics about the index&#39;s contents, including the vector count per namespace and the number of dimensions.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.VectorOperationsApi();
let describeIndexStatsRequest = new PineconeApi.DescribeIndexStatsRequest(); // DescribeIndexStatsRequest | 
apiInstance.describeIndexStats(describeIndexStatsRequest, (error, data, response) => {
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
 **describeIndexStatsRequest** | [**DescribeIndexStatsRequest**](DescribeIndexStatsRequest.md)|  | 

### Return type

[**DescribeIndexStatsResponse**](DescribeIndexStatsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fetch

> FetchResponse fetch(fetchRequest)

Fetch

The &#x60;Fetch&#x60; operation looks up and returns vectors, by ID, from a single namespace. The returned vectors include the vector data and/or metadata.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.VectorOperationsApi();
let fetchRequest = new PineconeApi.FetchRequest(); // FetchRequest | 
apiInstance.fetch(fetchRequest, (error, data, response) => {
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
 **fetchRequest** | [**FetchRequest**](FetchRequest.md)|  | 

### Return type

[**FetchResponse**](FetchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## query

> QueryResponse query(queryRequest)

Query

The &#x60;Query&#x60; operation searches a namespace, using a query vector. It retrieves the ids of the most similar items in a namespace, along with their similarity scores.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.VectorOperationsApi();
let queryRequest = new PineconeApi.QueryRequest(); // QueryRequest | 
apiInstance.query(queryRequest, (error, data, response) => {
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
 **queryRequest** | [**QueryRequest**](QueryRequest.md)|  | 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## update

> Object update(updateRequest)

Fetch

The &#x60;Update&#x60; operation updates vector in a namespace. If a value is included, it will overwrite the previous value. If a set_metadata is included, the values of the fields specified in it will be added or overwrite the previous value.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.VectorOperationsApi();
let updateRequest = new PineconeApi.UpdateRequest(); // UpdateRequest | 
apiInstance.update(updateRequest, (error, data, response) => {
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
 **updateRequest** | [**UpdateRequest**](UpdateRequest.md)|  | 

### Return type

**Object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upsert

> UpsertResponse upsert(upsertRequest)

Upsert

The Upsert operation writes vectors into a namespace. If a new value is upserted for an existing vector id, it will overwrite the previous value.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.VectorOperationsApi();
let upsertRequest = new PineconeApi.UpsertRequest(); // UpsertRequest | 
apiInstance.upsert(upsertRequest, (error, data, response) => {
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
 **upsertRequest** | [**UpsertRequest**](UpsertRequest.md)|  | 

### Return type

[**UpsertResponse**](UpsertResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

