# FilesFiles.FoldersApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFilesV3FoldersFolderIdArchive**](FoldersApi.md#deleteFilesV3FoldersFolderIdArchive) | **DELETE** /files/v3/folders/{folderId} | Delete folder.
[**deleteFilesV3FoldersFolderPathArchiveByPath**](FoldersApi.md#deleteFilesV3FoldersFolderPathArchiveByPath) | **DELETE** /files/v3/folders/{folderPath} | Delete folder.
[**getFilesV3FoldersFolderIdGetById**](FoldersApi.md#getFilesV3FoldersFolderIdGetById) | **GET** /files/v3/folders/{folderId} | Get folder
[**getFilesV3FoldersFolderPathGetByPath**](FoldersApi.md#getFilesV3FoldersFolderPathGetByPath) | **GET** /files/v3/folders/{folderPath} | Get folder.
[**getFilesV3FoldersSearchDoSearch**](FoldersApi.md#getFilesV3FoldersSearchDoSearch) | **GET** /files/v3/folders/search | Search folders
[**getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus**](FoldersApi.md#getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus) | **GET** /files/v3/folders/update/async/tasks/{taskId}/status | Check folder update status.
[**postFilesV3FoldersCreate**](FoldersApi.md#postFilesV3FoldersCreate) | **POST** /files/v3/folders | Create folder.
[**postFilesV3FoldersUpdateAsyncUpdateProperties**](FoldersApi.md#postFilesV3FoldersUpdateAsyncUpdateProperties) | **POST** /files/v3/folders/update/async | Update folder properties



## deleteFilesV3FoldersFolderIdArchive

> deleteFilesV3FoldersFolderIdArchive(folderId)

Delete folder.

Delete folder by ID.

### Example

```javascript
import FilesFiles from 'files_files';
let defaultClient = FilesFiles.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new FilesFiles.FoldersApi();
let folderId = "folderId_example"; // String | ID of folder to delete.
apiInstance.deleteFilesV3FoldersFolderIdArchive(folderId, (error, data, response) => {
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
 **folderId** | **String**| ID of folder to delete. | 

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteFilesV3FoldersFolderPathArchiveByPath

> deleteFilesV3FoldersFolderPathArchiveByPath(folderPath)

Delete folder.

Delete folder by path.

### Example

```javascript
import FilesFiles from 'files_files';
let defaultClient = FilesFiles.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new FilesFiles.FoldersApi();
let folderPath = "folderPath_example"; // String | Path of folder to delete
apiInstance.deleteFilesV3FoldersFolderPathArchiveByPath(folderPath, (error, data, response) => {
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
 **folderPath** | **String**| Path of folder to delete | 

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getFilesV3FoldersFolderIdGetById

> Folder getFilesV3FoldersFolderIdGetById(folderId, opts)

Get folder

Get folder by ID

### Example

```javascript
import FilesFiles from 'files_files';
let defaultClient = FilesFiles.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new FilesFiles.FoldersApi();
let folderId = "folderId_example"; // String | ID of desired folder
let opts = {
  'properties': ["null"] // [String] | Properties to set on returned folder.
};
apiInstance.getFilesV3FoldersFolderIdGetById(folderId, opts, (error, data, response) => {
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
 **folderId** | **String**| ID of desired folder | 
 **properties** | [**[String]**](String.md)| Properties to set on returned folder. | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getFilesV3FoldersFolderPathGetByPath

> Folder getFilesV3FoldersFolderPathGetByPath(folderPath, opts)

Get folder.

Get folder by path.

### Example

```javascript
import FilesFiles from 'files_files';
let defaultClient = FilesFiles.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new FilesFiles.FoldersApi();
let folderPath = "folderPath_example"; // String | Path of desired folder.
let opts = {
  'properties': ["null"] // [String] | Properties to set on returned folder.
};
apiInstance.getFilesV3FoldersFolderPathGetByPath(folderPath, opts, (error, data, response) => {
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
 **folderPath** | **String**| Path of desired folder. | 
 **properties** | [**[String]**](String.md)| Properties to set on returned folder. | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getFilesV3FoldersSearchDoSearch

> CollectionResponseFolder getFilesV3FoldersSearchDoSearch(opts)

Search folders

Search for folders. Does not contain hidden or archived folders.

### Example

```javascript
import FilesFiles from 'files_files';
let defaultClient = FilesFiles.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new FilesFiles.FoldersApi();
let opts = {
  'properties': ["null"], // [String] | Properties that should be included in the returned folders.
  'after': "after_example", // String | The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit.
  'before': "before_example", // String | 
  'limit': 56, // Number | Limit of results to return. Max limit is 100.
  'sort': ["null"], // [String] | Sort results by given property. For example -name sorts by name field descending, name sorts by name field ascending.
  'id': "id_example", // String | Search folder by given ID.
  'createdAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Search for folders with the given creation timestamp.
  'createdAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'updatedAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Search for folder at given update timestamp.
  'updatedAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'updatedAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'name': "name_example", // String | Search for folders containing the specified name.
  'path': "path_example", // String | Search for folders by path.
  'parentFolderId': 789 // Number | Search for folders with the given parent folderId.
};
apiInstance.getFilesV3FoldersSearchDoSearch(opts, (error, data, response) => {
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
 **properties** | [**[String]**](String.md)| Properties that should be included in the returned folders. | [optional] 
 **after** | **String**| The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit. | [optional] 
 **before** | **String**|  | [optional] 
 **limit** | **Number**| Limit of results to return. Max limit is 100. | [optional] 
 **sort** | [**[String]**](String.md)| Sort results by given property. For example -name sorts by name field descending, name sorts by name field ascending. | [optional] 
 **id** | **String**| Search folder by given ID. | [optional] 
 **createdAt** | **Date**| Search for folders with the given creation timestamp. | [optional] 
 **createdAtLte** | **Date**|  | [optional] 
 **createdAtGte** | **Date**|  | [optional] 
 **updatedAt** | **Date**| Search for folder at given update timestamp. | [optional] 
 **updatedAtLte** | **Date**|  | [optional] 
 **updatedAtGte** | **Date**|  | [optional] 
 **name** | **String**| Search for folders containing the specified name. | [optional] 
 **path** | **String**| Search for folders by path. | [optional] 
 **parentFolderId** | **Number**| Search for folders with the given parent folderId. | [optional] 

### Return type

[**CollectionResponseFolder**](CollectionResponseFolder.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus

> FolderActionResponse getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus(taskId)

Check folder update status.

Check status of folder update. Folder updates happen asynchronously.

### Example

```javascript
import FilesFiles from 'files_files';
let defaultClient = FilesFiles.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new FilesFiles.FoldersApi();
let taskId = "taskId_example"; // String | TaskId of folder update
apiInstance.getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus(taskId, (error, data, response) => {
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
 **taskId** | **String**| TaskId of folder update | 

### Return type

[**FolderActionResponse**](FolderActionResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## postFilesV3FoldersCreate

> Folder postFilesV3FoldersCreate(folderInput)

Create folder.

Creates a folder.

### Example

```javascript
import FilesFiles from 'files_files';
let defaultClient = FilesFiles.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new FilesFiles.FoldersApi();
let folderInput = new FilesFiles.FolderInput(); // FolderInput | Folder creation options
apiInstance.postFilesV3FoldersCreate(folderInput, (error, data, response) => {
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
 **folderInput** | [**FolderInput**](FolderInput.md)| Folder creation options | 

### Return type

[**Folder**](Folder.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postFilesV3FoldersUpdateAsyncUpdateProperties

> FolderUpdateTaskLocator postFilesV3FoldersUpdateAsyncUpdateProperties(folderUpdateInput)

Update folder properties

Update properties of folder by given ID. This action happens asynchronously and will update all of the folder&#39;s children as well.

### Example

```javascript
import FilesFiles from 'files_files';
let defaultClient = FilesFiles.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new FilesFiles.FoldersApi();
let folderUpdateInput = new FilesFiles.FolderUpdateInput(); // FolderUpdateInput | Properties to change in the folder
apiInstance.postFilesV3FoldersUpdateAsyncUpdateProperties(folderUpdateInput, (error, data, response) => {
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
 **folderUpdateInput** | [**FolderUpdateInput**](FolderUpdateInput.md)| Properties to change in the folder | 

### Return type

[**FolderUpdateTaskLocator**](FolderUpdateTaskLocator.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*

