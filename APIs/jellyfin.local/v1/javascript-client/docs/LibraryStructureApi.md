# JellyfinApi.LibraryStructureApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addMediaPath**](LibraryStructureApi.md#addMediaPath) | **POST** /Library/VirtualFolders/Paths | Add a media path to a library.
[**addVirtualFolder**](LibraryStructureApi.md#addVirtualFolder) | **POST** /Library/VirtualFolders | Adds a virtual folder.
[**getVirtualFolders**](LibraryStructureApi.md#getVirtualFolders) | **GET** /Library/VirtualFolders | Gets all virtual folders.
[**removeMediaPath**](LibraryStructureApi.md#removeMediaPath) | **DELETE** /Library/VirtualFolders/Paths | Remove a media path.
[**removeVirtualFolder**](LibraryStructureApi.md#removeVirtualFolder) | **DELETE** /Library/VirtualFolders | Removes a virtual folder.
[**renameVirtualFolder**](LibraryStructureApi.md#renameVirtualFolder) | **POST** /Library/VirtualFolders/Name | Renames a virtual folder.
[**updateLibraryOptions**](LibraryStructureApi.md#updateLibraryOptions) | **POST** /Library/VirtualFolders/LibraryOptions | Update library options.
[**updateMediaPath**](LibraryStructureApi.md#updateMediaPath) | **POST** /Library/VirtualFolders/Paths/Update | Updates a media path.



## addMediaPath

> addMediaPath(mediaPathDto, opts)

Add a media path to a library.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryStructureApi();
let mediaPathDto = new JellyfinApi.MediaPathDto(); // MediaPathDto | The media path dto.
let opts = {
  'refreshLibrary': false // Boolean | Whether to refresh the library.
};
apiInstance.addMediaPath(mediaPathDto, opts, (error, data, response) => {
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
 **mediaPathDto** | [**MediaPathDto**](MediaPathDto.md)| The media path dto. | 
 **refreshLibrary** | **Boolean**| Whether to refresh the library. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## addVirtualFolder

> addVirtualFolder(opts)

Adds a virtual folder.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryStructureApi();
let opts = {
  'name': "name_example", // String | The name of the virtual folder.
  'collectionType': "collectionType_example", // String | The type of the collection.
  'paths': ["null"], // [String] | The paths of the virtual folder.
  'refreshLibrary': false, // Boolean | Whether to refresh the library.
  'addVirtualFolderDto': new JellyfinApi.AddVirtualFolderDto() // AddVirtualFolderDto | The library options.
};
apiInstance.addVirtualFolder(opts, (error, data, response) => {
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
 **name** | **String**| The name of the virtual folder. | [optional] 
 **collectionType** | **String**| The type of the collection. | [optional] 
 **paths** | [**[String]**](String.md)| The paths of the virtual folder. | [optional] 
 **refreshLibrary** | **Boolean**| Whether to refresh the library. | [optional] [default to false]
 **addVirtualFolderDto** | [**AddVirtualFolderDto**](AddVirtualFolderDto.md)| The library options. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## getVirtualFolders

> [VirtualFolderInfo] getVirtualFolders()

Gets all virtual folders.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryStructureApi();
apiInstance.getVirtualFolders((error, data, response) => {
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

[**[VirtualFolderInfo]**](VirtualFolderInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## removeMediaPath

> removeMediaPath(opts)

Remove a media path.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryStructureApi();
let opts = {
  'name': "name_example", // String | The name of the library.
  'path': "path_example", // String | The path to remove.
  'refreshLibrary': false // Boolean | Whether to refresh the library.
};
apiInstance.removeMediaPath(opts, (error, data, response) => {
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
 **name** | **String**| The name of the library. | [optional] 
 **path** | **String**| The path to remove. | [optional] 
 **refreshLibrary** | **Boolean**| Whether to refresh the library. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeVirtualFolder

> removeVirtualFolder(opts)

Removes a virtual folder.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryStructureApi();
let opts = {
  'name': "name_example", // String | The name of the folder.
  'refreshLibrary': false // Boolean | Whether to refresh the library.
};
apiInstance.removeVirtualFolder(opts, (error, data, response) => {
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
 **name** | **String**| The name of the folder. | [optional] 
 **refreshLibrary** | **Boolean**| Whether to refresh the library. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## renameVirtualFolder

> renameVirtualFolder(opts)

Renames a virtual folder.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryStructureApi();
let opts = {
  'name': "name_example", // String | The name of the virtual folder.
  'newName': "newName_example", // String | The new name.
  'refreshLibrary': false // Boolean | Whether to refresh the library.
};
apiInstance.renameVirtualFolder(opts, (error, data, response) => {
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
 **name** | **String**| The name of the virtual folder. | [optional] 
 **newName** | **String**| The new name. | [optional] 
 **refreshLibrary** | **Boolean**| Whether to refresh the library. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## updateLibraryOptions

> updateLibraryOptions(opts)

Update library options.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryStructureApi();
let opts = {
  'updateLibraryOptionsDto': new JellyfinApi.UpdateLibraryOptionsDto() // UpdateLibraryOptionsDto | The library name and options.
};
apiInstance.updateLibraryOptions(opts, (error, data, response) => {
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
 **updateLibraryOptionsDto** | [**UpdateLibraryOptionsDto**](UpdateLibraryOptionsDto.md)| The library name and options. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## updateMediaPath

> updateMediaPath(opts)

Updates a media path.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryStructureApi();
let opts = {
  'name': "name_example", // String | The name of the library.
  'mediaPathInfo': new JellyfinApi.MediaPathInfo() // MediaPathInfo | The path info.
};
apiInstance.updateMediaPath(opts, (error, data, response) => {
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
 **name** | **String**| The name of the library. | [optional] 
 **mediaPathInfo** | [**MediaPathInfo**](MediaPathInfo.md)| The path info. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined

