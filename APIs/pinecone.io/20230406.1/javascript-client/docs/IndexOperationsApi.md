# PineconeApi.IndexOperationsApi

All URIs are relative to *https://controller.us-east1-gcp.pinecone.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureIndex**](IndexOperationsApi.md#configureIndex) | **PATCH** /databases/{indexName} | Configure index
[**createCollection**](IndexOperationsApi.md#createCollection) | **POST** /collections | Create collection
[**createIndex**](IndexOperationsApi.md#createIndex) | **POST** /databases | Create index
[**deleteCollection**](IndexOperationsApi.md#deleteCollection) | **DELETE** /collections/{collectionName} | Delete Collection
[**deleteIndex**](IndexOperationsApi.md#deleteIndex) | **DELETE** /databases/{indexName} | Delete Index
[**describeCollection**](IndexOperationsApi.md#describeCollection) | **GET** /collections/{collectionName} | Describe collection
[**describeIndex**](IndexOperationsApi.md#describeIndex) | **GET** /databases/{indexName} | Describe index
[**listCollections**](IndexOperationsApi.md#listCollections) | **GET** /collections | List collections
[**listIndexes**](IndexOperationsApi.md#listIndexes) | **GET** /databases | List indexes



## configureIndex

> configureIndex(indexName, indexConfiguration)

Configure index

This operation specifies the pod type and number of replicas for an index.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.IndexOperationsApi();
let indexName = "indexName_example"; // String | 
let indexConfiguration = new PineconeApi.IndexConfiguration(); // IndexConfiguration | 
apiInstance.configureIndex(indexName, indexConfiguration, (error, data, response) => {
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
 **indexName** | **String**|  | 
 **indexConfiguration** | [**IndexConfiguration**](IndexConfiguration.md)|  | 

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## createCollection

> createCollection(collectionDefinition)

Create collection

This operation creates a Pinecone collection.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.IndexOperationsApi();
let collectionDefinition = new PineconeApi.CollectionDefinition(); // CollectionDefinition | 
apiInstance.createCollection(collectionDefinition, (error, data, response) => {
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
 **collectionDefinition** | [**CollectionDefinition**](CollectionDefinition.md)|  | 

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## createIndex

> createIndex(indexDefinition)

Create index

This operation creates a Pinecone index. You can use it to specify the measure of similarity, the dimension of vectors to be stored in the index, the numbers of replicas to use, and more.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.IndexOperationsApi();
let indexDefinition = new PineconeApi.IndexDefinition(); // IndexDefinition | 
apiInstance.createIndex(indexDefinition, (error, data, response) => {
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
 **indexDefinition** | [**IndexDefinition**](IndexDefinition.md)|  | 

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## deleteCollection

> deleteCollection(collectionName)

Delete Collection

This operation deletes an existing collection.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.IndexOperationsApi();
let collectionName = "collectionName_example"; // String | 
apiInstance.deleteCollection(collectionName, (error, data, response) => {
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
 **collectionName** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## deleteIndex

> deleteIndex(indexName)

Delete Index

This operation deletes an existing index.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.IndexOperationsApi();
let indexName = "indexName_example"; // String | 
apiInstance.deleteIndex(indexName, (error, data, response) => {
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
 **indexName** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## describeCollection

> Collection describeCollection(collectionName)

Describe collection

Get a description of a collection.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.IndexOperationsApi();
let collectionName = "collectionName_example"; // String | 
apiInstance.describeCollection(collectionName, (error, data, response) => {
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
 **collectionName** | **String**|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## describeIndex

> Index describeIndex(indexName)

Describe index

Get a description of an index.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.IndexOperationsApi();
let indexName = "indexName_example"; // String | 
apiInstance.describeIndex(indexName, (error, data, response) => {
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
 **indexName** | **String**|  | 

### Return type

[**Index**](Index.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## listCollections

> [String] listCollections()

List collections

This operation returns a list of your Pinecone collections.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.IndexOperationsApi();
apiInstance.listCollections((error, data, response) => {
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

**[String]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIndexes

> [String] listIndexes()

List indexes

This operation returns a list of your Pinecone indexes.

### Example

```javascript
import PineconeApi from 'pinecone_api';
let defaultClient = PineconeApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PineconeApi.IndexOperationsApi();
apiInstance.listIndexes((error, data, response) => {
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

**[String]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

