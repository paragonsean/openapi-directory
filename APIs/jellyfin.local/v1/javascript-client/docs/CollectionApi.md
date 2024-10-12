# JellyfinApi.CollectionApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addToCollection**](CollectionApi.md#addToCollection) | **POST** /Collections/{collectionId}/Items | Adds items to a collection.
[**createCollection**](CollectionApi.md#createCollection) | **POST** /Collections | Creates a new collection.
[**removeFromCollection**](CollectionApi.md#removeFromCollection) | **DELETE** /Collections/{collectionId}/Items | Removes items from a collection.



## addToCollection

> addToCollection(collectionId, ids)

Adds items to a collection.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.CollectionApi();
let collectionId = "collectionId_example"; // String | The collection id.
let ids = ["null"]; // [String] | Item ids, comma delimited.
apiInstance.addToCollection(collectionId, ids, (error, data, response) => {
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
 **collectionId** | **String**| The collection id. | 
 **ids** | [**[String]**](String.md)| Item ids, comma delimited. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createCollection

> CollectionCreationResult createCollection(opts)

Creates a new collection.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.CollectionApi();
let opts = {
  'name': "name_example", // String | The name of the collection.
  'ids': ["null"], // [String] | Item Ids to add to the collection.
  'parentId': "parentId_example", // String | Optional. Create the collection within a specific folder.
  'isLocked': false // Boolean | Whether or not to lock the new collection.
};
apiInstance.createCollection(opts, (error, data, response) => {
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
 **name** | **String**| The name of the collection. | [optional] 
 **ids** | [**[String]**](String.md)| Item Ids to add to the collection. | [optional] 
 **parentId** | **String**| Optional. Create the collection within a specific folder. | [optional] 
 **isLocked** | **Boolean**| Whether or not to lock the new collection. | [optional] [default to false]

### Return type

[**CollectionCreationResult**](CollectionCreationResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## removeFromCollection

> removeFromCollection(collectionId, ids)

Removes items from a collection.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.CollectionApi();
let collectionId = "collectionId_example"; // String | The collection id.
let ids = ["null"]; // [String] | Item ids, comma delimited.
apiInstance.removeFromCollection(collectionId, ids, (error, data, response) => {
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
 **collectionId** | **String**| The collection id. | 
 **ids** | [**[String]**](String.md)| Item ids, comma delimited. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

