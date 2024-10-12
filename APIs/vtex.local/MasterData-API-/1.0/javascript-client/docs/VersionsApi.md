# MasterDataApiV1.VersionsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getversion**](VersionsApi.md#getversion) | **GET** /api/dataentities/{acronym}/documents/{id}/versions/{versionId} | Get version
[**listversions**](VersionsApi.md#listversions) | **GET** /api/dataentities/{acronym}/documents/{id}/versions | List versions
[**putversion**](VersionsApi.md#putversion) | **PUT** /api/dataentities/{acronym}/documents/{id}/versions/{versionId} | Put version



## getversion

> Getversion getversion(contentType, accept, acronym, id, versionId)

Get version

Returns the version of a document.

### Example

```javascript
import MasterDataApiV1 from 'master_data_api_v1';
let defaultClient = MasterDataApiV1.ApiClient.instance;
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

let apiInstance = new MasterDataApiV1.VersionsApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let versionId = "'{{versionId}}'"; // String | Id of the version to get
apiInstance.getversion(contentType, accept, acronym, id, versionId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/vnd.vtex.ds.v10+json&#39;]
 **acronym** | **String**| Two letter word that identifies the data structure | [default to &#39;{{acronym}}&#39;]
 **id** | **String**| Id of the document | [default to &#39;{{id}}&#39;]
 **versionId** | **String**| Id of the version to get | [default to &#39;{{versionId}}&#39;]

### Return type

[**Getversion**](Getversion.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listversions

> [Listversion] listversions(contentType, accept, acronym, id)

List versions

Allows to list the versions of a document.

### Example

```javascript
import MasterDataApiV1 from 'master_data_api_v1';
let defaultClient = MasterDataApiV1.ApiClient.instance;
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

let apiInstance = new MasterDataApiV1.VersionsApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
apiInstance.listversions(contentType, accept, acronym, id, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/vnd.vtex.ds.v10+json&#39;]
 **acronym** | **String**| Two letter word that identifies the data structure | [default to &#39;{{acronym}}&#39;]
 **id** | **String**| Id of the document | [default to &#39;{{id}}&#39;]

### Return type

[**[Listversion]**](Listversion.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putversion

> Putversion putversion(contentType, accept, acronym, id, versionId)

Put version

Updates document with version values.

### Example

```javascript
import MasterDataApiV1 from 'master_data_api_v1';
let defaultClient = MasterDataApiV1.ApiClient.instance;
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

let apiInstance = new MasterDataApiV1.VersionsApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let versionId = "'{{versionId}}'"; // String | Id of the version to update
apiInstance.putversion(contentType, accept, acronym, id, versionId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/vnd.vtex.ds.v10+json&#39;]
 **acronym** | **String**| Two letter word that identifies the data structure | [default to &#39;{{acronym}}&#39;]
 **id** | **String**| Id of the document | [default to &#39;{{id}}&#39;]
 **versionId** | **String**| Id of the version to update | [default to &#39;{{versionId}}&#39;]

### Return type

[**Putversion**](Putversion.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

