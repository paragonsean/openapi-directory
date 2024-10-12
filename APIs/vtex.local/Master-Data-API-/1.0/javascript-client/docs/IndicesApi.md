# MasterDataApiV2.IndicesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteindexbyname**](IndicesApi.md#deleteindexbyname) | **DELETE** /api/dataentities/{dataEntityName}/indices/{index_name} | Delete index by name
[**getindexbyname**](IndicesApi.md#getindexbyname) | **GET** /api/dataentities/{dataEntityName}/indices/{index_name} | Get index by name
[**getindices**](IndicesApi.md#getindices) | **GET** /api/dataentities/{dataEntityName}/indices | Get indices
[**putindices**](IndicesApi.md#putindices) | **PUT** /api/dataentities/{dataEntityName}/indices | Put indices



## deleteindexbyname

> deleteindexbyname(dataEntityName, contentType, indexName)

Delete index by name

Delete an index.

### Example

```javascript
import MasterDataApiV2 from 'master_data_api_v2';
let defaultClient = MasterDataApiV2.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV2.IndicesApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let contentType = "application/json"; // String | Type of the content being sent.
let indexName = "{{index_name}}"; // String | Name of the index.
apiInstance.deleteindexbyname(dataEntityName, contentType, indexName, (error, data, response) => {
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
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **contentType** | **String**| Type of the content being sent. | 
 **indexName** | **String**| Name of the index. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getindexbyname

> getindexbyname(dataEntityName, contentType, indexName)

Get index by name

Returns an index.

### Example

```javascript
import MasterDataApiV2 from 'master_data_api_v2';
let defaultClient = MasterDataApiV2.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV2.IndicesApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let contentType = "application/json"; // String | Type of the content being sent.
let indexName = "{{index_name}}"; // String | Name of the index.
apiInstance.getindexbyname(dataEntityName, contentType, indexName, (error, data, response) => {
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
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **contentType** | **String**| Type of the content being sent. | 
 **indexName** | **String**| Name of the index. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getindices

> getindices(dataEntityName, contentType)

Get indices

Returns the list of indices by data entity.

### Example

```javascript
import MasterDataApiV2 from 'master_data_api_v2';
let defaultClient = MasterDataApiV2.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV2.IndicesApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let contentType = "application/json"; // String | Type of the content being sent.
apiInstance.getindices(dataEntityName, contentType, (error, data, response) => {
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
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **contentType** | **String**| Type of the content being sent. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## putindices

> putindices(dataEntityName, putindicesRequest)

Put indices

Create an index.

### Example

```javascript
import MasterDataApiV2 from 'master_data_api_v2';
let defaultClient = MasterDataApiV2.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV2.IndicesApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let putindicesRequest = {"fields":"fieldName","multiple":false,"name":"indexName"}; // PutindicesRequest | Request body for creating an index
apiInstance.putindices(dataEntityName, putindicesRequest, (error, data, response) => {
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
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **putindicesRequest** | [**PutindicesRequest**](PutindicesRequest.md)| Request body for creating an index | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

