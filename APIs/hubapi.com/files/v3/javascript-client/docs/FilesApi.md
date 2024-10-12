# FilesFiles.FilesApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFilesV3FilesFileIdArchive**](FilesApi.md#deleteFilesV3FilesFileIdArchive) | **DELETE** /files/v3/files/{fileId} | Delete file
[**deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR**](FilesApi.md#deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR) | **DELETE** /files/v3/files/{fileId}/gdpr-delete | GDPR delete
[**getFilesV3FilesFileIdGetById**](FilesApi.md#getFilesV3FilesFileIdGetById) | **GET** /files/v3/files/{fileId} | Get file.
[**getFilesV3FilesFileIdSignedUrlGetSignedUrl**](FilesApi.md#getFilesV3FilesFileIdSignedUrlGetSignedUrl) | **GET** /files/v3/files/{fileId}/signed-url | Get signed URL to access private file.
[**getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport**](FilesApi.md#getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport) | **GET** /files/v3/files/import-from-url/async/tasks/{taskId}/status | Check import status.
[**getFilesV3FilesSearchDoSearch**](FilesApi.md#getFilesV3FilesSearchDoSearch) | **GET** /files/v3/files/search | Search files
[**getFilesV3FilesStatPathGetMetadata**](FilesApi.md#getFilesV3FilesStatPathGetMetadata) | **GET** /files/v3/files/stat/{path} | 
[**patchFilesV3FilesFileIdUpdateProperties**](FilesApi.md#patchFilesV3FilesFileIdUpdateProperties) | **PATCH** /files/v3/files/{fileId} | update file properties
[**postFilesV3FilesImportFromUrlAsyncImportFromUrl**](FilesApi.md#postFilesV3FilesImportFromUrlAsyncImportFromUrl) | **POST** /files/v3/files/import-from-url/async | Import a file from a URL into the file manager.
[**postFilesV3FilesUpload**](FilesApi.md#postFilesV3FilesUpload) | **POST** /files/v3/files | Upload file
[**putFilesV3FilesFileIdReplace**](FilesApi.md#putFilesV3FilesFileIdReplace) | **PUT** /files/v3/files/{fileId} | Replace file.



## deleteFilesV3FilesFileIdArchive

> deleteFilesV3FilesFileIdArchive(fileId)

Delete file

Delete file by ID

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

let apiInstance = new FilesFiles.FilesApi();
let fileId = "fileId_example"; // String | FileId to delete
apiInstance.deleteFilesV3FilesFileIdArchive(fileId, (error, data, response) => {
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
 **fileId** | **String**| FileId to delete | 

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR

> deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR(fileId)

GDPR delete

GDRP delete file

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

let apiInstance = new FilesFiles.FilesApi();
let fileId = "fileId_example"; // String | ID of file to GDPR delete
apiInstance.deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR(fileId, (error, data, response) => {
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
 **fileId** | **String**| ID of file to GDPR delete | 

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getFilesV3FilesFileIdGetById

> File getFilesV3FilesFileIdGetById(fileId, opts)

Get file.

Get file by ID.

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

let apiInstance = new FilesFiles.FilesApi();
let fileId = "fileId_example"; // String | ID of the desired file.
let opts = {
  'properties': ["null"] // [String] | 
};
apiInstance.getFilesV3FilesFileIdGetById(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| ID of the desired file. | 
 **properties** | [**[String]**](String.md)|  | [optional] 

### Return type

**File**

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getFilesV3FilesFileIdSignedUrlGetSignedUrl

> SignedUrl getFilesV3FilesFileIdSignedUrlGetSignedUrl(fileId, opts)

Get signed URL to access private file.

Generates signed URL that allows temporary access to a private file.

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

let apiInstance = new FilesFiles.FilesApi();
let fileId = "fileId_example"; // String | ID of file.
let opts = {
  'size': "size_example", // String | For image files. This will resize the image to the desired size before sharing. Does not affect the original file, just the file served by this signed URL.
  'expirationSeconds': 789, // Number | How long in seconds the link will provide access to the file.
  'upscale': true // Boolean | If size is provided, this will upscale the image to fit the size dimensions.
};
apiInstance.getFilesV3FilesFileIdSignedUrlGetSignedUrl(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| ID of file. | 
 **size** | **String**| For image files. This will resize the image to the desired size before sharing. Does not affect the original file, just the file served by this signed URL. | [optional] 
 **expirationSeconds** | **Number**| How long in seconds the link will provide access to the file. | [optional] 
 **upscale** | **Boolean**| If size is provided, this will upscale the image to fit the size dimensions. | [optional] 

### Return type

[**SignedUrl**](SignedUrl.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport

> FileActionResponse getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport(taskId)

Check import status.

Check the status of requested import.

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

let apiInstance = new FilesFiles.FilesApi();
let taskId = "taskId_example"; // String | Import by URL task ID
apiInstance.getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport(taskId, (error, data, response) => {
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
 **taskId** | **String**| Import by URL task ID | 

### Return type

[**FileActionResponse**](FileActionResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getFilesV3FilesSearchDoSearch

> CollectionResponseFile getFilesV3FilesSearchDoSearch(opts)

Search files

Search through files in the file manager. Does not display hidden or archived files.

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

let apiInstance = new FilesFiles.FilesApi();
let opts = {
  'properties': ["null"], // [String] | Desired file properties in the return object.
  'after': "after_example", // String | The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit.
  'before': "before_example", // String | 
  'limit': 56, // Number | Number of items to return. Maximum limit is 100.
  'sort': ["null"], // [String] | Sort files by a given field.
  'id': "id_example", // String | Search files by given ID.
  'createdAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Search files by time of creation.
  'createdAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'updatedAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Search files by time of latest updated.
  'updatedAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'updatedAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'name': "name_example", // String | Search for files containing the given name.
  'path': "path_example", // String | Search files by path.
  'parentFolderId': 789, // Number | Search files within given folderId.
  'size': 789, // Number | Query by file size.
  'height': 56, // Number | Search files by height of image or video.
  'width': 56, // Number | Search files by width of image or video.
  'encoding': "encoding_example", // String | Search files with specified encoding.
  'type': "type_example", // String | Filter by provided file type.
  'extension': "extension_example", // String | Search files by given extension.
  'url': "url_example", // String | Search for given URL
  'isUsableInContent': true, // Boolean | If true shows files that have been marked to be used in new content. It false shows files that should not be used in new content.
  'allowsAnonymousAccess': true // Boolean | If 'true' will show private files; if 'false' will show public files
};
apiInstance.getFilesV3FilesSearchDoSearch(opts, (error, data, response) => {
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
 **properties** | [**[String]**](String.md)| Desired file properties in the return object. | [optional] 
 **after** | **String**| The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit. | [optional] 
 **before** | **String**|  | [optional] 
 **limit** | **Number**| Number of items to return. Maximum limit is 100. | [optional] 
 **sort** | [**[String]**](String.md)| Sort files by a given field. | [optional] 
 **id** | **String**| Search files by given ID. | [optional] 
 **createdAt** | **Date**| Search files by time of creation. | [optional] 
 **createdAtLte** | **Date**|  | [optional] 
 **createdAtGte** | **Date**|  | [optional] 
 **updatedAt** | **Date**| Search files by time of latest updated. | [optional] 
 **updatedAtLte** | **Date**|  | [optional] 
 **updatedAtGte** | **Date**|  | [optional] 
 **name** | **String**| Search for files containing the given name. | [optional] 
 **path** | **String**| Search files by path. | [optional] 
 **parentFolderId** | **Number**| Search files within given folderId. | [optional] 
 **size** | **Number**| Query by file size. | [optional] 
 **height** | **Number**| Search files by height of image or video. | [optional] 
 **width** | **Number**| Search files by width of image or video. | [optional] 
 **encoding** | **String**| Search files with specified encoding. | [optional] 
 **type** | **String**| Filter by provided file type. | [optional] 
 **extension** | **String**| Search files by given extension. | [optional] 
 **url** | **String**| Search for given URL | [optional] 
 **isUsableInContent** | **Boolean**| If true shows files that have been marked to be used in new content. It false shows files that should not be used in new content. | [optional] 
 **allowsAnonymousAccess** | **Boolean**| If &#39;true&#39; will show private files; if &#39;false&#39; will show public files | [optional] 

### Return type

[**CollectionResponseFile**](CollectionResponseFile.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getFilesV3FilesStatPathGetMetadata

> FileStat getFilesV3FilesStatPathGetMetadata(path, opts)



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

let apiInstance = new FilesFiles.FilesApi();
let path = "path_example"; // String | 
let opts = {
  'properties': ["null"] // [String] | 
};
apiInstance.getFilesV3FilesStatPathGetMetadata(path, opts, (error, data, response) => {
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
 **path** | **String**|  | 
 **properties** | [**[String]**](String.md)|  | [optional] 

### Return type

[**FileStat**](FileStat.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## patchFilesV3FilesFileIdUpdateProperties

> File patchFilesV3FilesFileIdUpdateProperties(fileId, fileUpdateInput)

update file properties

Update properties of file by ID.

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

let apiInstance = new FilesFiles.FilesApi();
let fileId = "fileId_example"; // String | ID of file to update
let fileUpdateInput = new FilesFiles.FileUpdateInput(); // FileUpdateInput | Options to update.
apiInstance.patchFilesV3FilesFileIdUpdateProperties(fileId, fileUpdateInput, (error, data, response) => {
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
 **fileId** | **String**| ID of file to update | 
 **fileUpdateInput** | [**FileUpdateInput**](FileUpdateInput.md)| Options to update. | 

### Return type

**File**

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postFilesV3FilesImportFromUrlAsyncImportFromUrl

> ImportFromUrlTaskLocator postFilesV3FilesImportFromUrlAsyncImportFromUrl(importFromUrlInput)

Import a file from a URL into the file manager.

Asynchronously imports the file at the given URL into the file manager.

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

let apiInstance = new FilesFiles.FilesApi();
let importFromUrlInput = new FilesFiles.ImportFromUrlInput(); // ImportFromUrlInput | 
apiInstance.postFilesV3FilesImportFromUrlAsyncImportFromUrl(importFromUrlInput, (error, data, response) => {
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
 **importFromUrlInput** | [**ImportFromUrlInput**](ImportFromUrlInput.md)|  | 

### Return type

[**ImportFromUrlTaskLocator**](ImportFromUrlTaskLocator.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postFilesV3FilesUpload

> File postFilesV3FilesUpload(opts)

Upload file

Upload a single file with content specified in request body.

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

let apiInstance = new FilesFiles.FilesApi();
let opts = {
  'charsetHunch': "charsetHunch_example", // String | Character set of the uploaded file.
  'file': "/path/to/file", // File | File to be uploaded.
  'fileName': "fileName_example", // String | Desired name for the uploaded file.
  'folderId': "folderId_example", // String | Either 'folderId' or 'folderPath' is required. folderId is the ID of the folder the file will be uploaded to.
  'folderPath': "folderPath_example", // String | Either 'folderPath' or 'folderId' is required. This field represents the destination folder path for the uploaded file. If a path doesn't exist, the system will try to create one.
  'options': "options_example" // String | JSON string representing FileUploadOptions.
};
apiInstance.postFilesV3FilesUpload(opts, (error, data, response) => {
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
 **charsetHunch** | **String**| Character set of the uploaded file. | [optional] 
 **file** | **File**| File to be uploaded. | [optional] 
 **fileName** | **String**| Desired name for the uploaded file. | [optional] 
 **folderId** | **String**| Either &#39;folderId&#39; or &#39;folderPath&#39; is required. folderId is the ID of the folder the file will be uploaded to. | [optional] 
 **folderPath** | **String**| Either &#39;folderPath&#39; or &#39;folderId&#39; is required. This field represents the destination folder path for the uploaded file. If a path doesn&#39;t exist, the system will try to create one. | [optional] 
 **options** | **String**| JSON string representing FileUploadOptions. | [optional] 

### Return type

**File**

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, */*


## putFilesV3FilesFileIdReplace

> File putFilesV3FilesFileIdReplace(fileId, opts)

Replace file.

Replace existing file data with new file data. Can be used to change image content without having to upload a new file and update all references.

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

let apiInstance = new FilesFiles.FilesApi();
let fileId = "fileId_example"; // String | ID of the desired file.
let opts = {
  'charsetHunch': "charsetHunch_example", // String | Character set of given file data.
  'file': "/path/to/file", // File | File data that will replace existing file in the file manager.
  'options': "options_example" // String | JSON String representing FileReplaceOptions
};
apiInstance.putFilesV3FilesFileIdReplace(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| ID of the desired file. | 
 **charsetHunch** | **String**| Character set of given file data. | [optional] 
 **file** | **File**| File data that will replace existing file in the file manager. | [optional] 
 **options** | **String**| JSON String representing FileReplaceOptions | [optional] 

### Return type

**File**

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, */*

