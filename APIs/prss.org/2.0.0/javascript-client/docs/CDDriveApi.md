# ContentDepot.CDDriveApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2CddriveFilesContentPost**](CDDriveApi.md#apiV2CddriveFilesContentPost) | **POST** /api/v2/cddrive/files/content | Upload a file.
[**apiV2CddriveFilesFileIdContentGet**](CDDriveApi.md#apiV2CddriveFilesFileIdContentGet) | **GET** /api/v2/cddrive/files/{file-id}/content | UNDER DEVELOPMENT - Download a file.
[**apiV2CddriveFilesFileIdDelete**](CDDriveApi.md#apiV2CddriveFilesFileIdDelete) | **DELETE** /api/v2/cddrive/files/{file-id} | Delete a file.
[**apiV2CddriveFilesFileIdGet**](CDDriveApi.md#apiV2CddriveFilesFileIdGet) | **GET** /api/v2/cddrive/files/{file-id} | Get file information.
[**apiV2CddriveFoldersFolderIdDelete**](CDDriveApi.md#apiV2CddriveFoldersFolderIdDelete) | **DELETE** /api/v2/cddrive/folders/{folder-id} | UNDER DEVELOPMENT - Delete a folder.
[**apiV2CddriveFoldersFolderIdGet**](CDDriveApi.md#apiV2CddriveFoldersFolderIdGet) | **GET** /api/v2/cddrive/folders/{folder-id} | UNDER DEVELOPMENT - Get folder information.
[**apiV2CddriveFoldersFolderIdItemsGet**](CDDriveApi.md#apiV2CddriveFoldersFolderIdItemsGet) | **GET** /api/v2/cddrive/folders/{folder-id}/items | Get the items in the folder.
[**apiV2CddriveFoldersPost**](CDDriveApi.md#apiV2CddriveFoldersPost) | **POST** /api/v2/cddrive/folders | Create a folder.



## apiV2CddriveFilesContentPost

> CDDriveFile apiV2CddriveFilesContentPost(opts)

Upload a file.

Upload a file to the customer&#39;s private CD Drive.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.CDDriveApi();
let opts = {
  'contentMD5': "contentMD5_example", // String | If present, the MD5 will be compared against the file received as a message integrity check.
  'file': "/path/to/file", // File | The file content being uploaded.
  'name': "name_example", // String | The name of the file, including extension.
  'parentId': 789 // Number | The ID of the parent folder or 0 for the root folder.
};
apiInstance.apiV2CddriveFilesContentPost(opts, (error, data, response) => {
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
 **contentMD5** | **String**| If present, the MD5 will be compared against the file received as a message integrity check. | [optional] 
 **file** | **File**| The file content being uploaded. | [optional] 
 **name** | **String**| The name of the file, including extension. | [optional] 
 **parentId** | **Number**| The ID of the parent folder or 0 for the root folder. | [optional] 

### Return type

[**CDDriveFile**](CDDriveFile.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## apiV2CddriveFilesFileIdContentGet

> File apiV2CddriveFilesFileIdContentGet(fileId, opts)

UNDER DEVELOPMENT - Download a file.

Download a file from the customer&#39;s private CD Drive.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.CDDriveApi();
let fileId = 789; // Number | The ID of the file to download.
let opts = {
  'range': "range_example" // String | Can be used to limit the range of bytes retrieved. Only a single byte range in the format ```bytes={start-range}-{end-range}``` is supported.
};
apiInstance.apiV2CddriveFilesFileIdContentGet(fileId, opts, (error, data, response) => {
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
 **fileId** | **Number**| The ID of the file to download. | 
 **range** | **String**| Can be used to limit the range of bytes retrieved. Only a single byte range in the format &#x60;&#x60;&#x60;bytes&#x3D;{start-range}-{end-range}&#x60;&#x60;&#x60; is supported. | [optional] 

### Return type

**File**

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## apiV2CddriveFilesFileIdDelete

> apiV2CddriveFilesFileIdDelete(fileId)

Delete a file.

Delete a file from the customer&#39;s private CD Drive.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.CDDriveApi();
let fileId = 789; // Number | The ID of the file to access.
apiInstance.apiV2CddriveFilesFileIdDelete(fileId, (error, data, response) => {
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
 **fileId** | **Number**| The ID of the file to access. | 

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV2CddriveFilesFileIdGet

> CDDriveFile apiV2CddriveFilesFileIdGet(fileId)

Get file information.

Get the information about a file in the customer&#39;s private CD Drive.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.CDDriveApi();
let fileId = 789; // Number | The ID of the file to access.
apiInstance.apiV2CddriveFilesFileIdGet(fileId, (error, data, response) => {
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
 **fileId** | **Number**| The ID of the file to access. | 

### Return type

[**CDDriveFile**](CDDriveFile.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2CddriveFoldersFolderIdDelete

> apiV2CddriveFoldersFolderIdDelete(folderId, opts)

UNDER DEVELOPMENT - Delete a folder.

Delete a file from the customer&#39;s private CD Drive.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.CDDriveApi();
let folderId = 789; // Number | The ID of the folder to get.
let opts = {
  'recursive': true // Boolean | Flag to indicate if the folder should be deleted if it has items inside of it.
};
apiInstance.apiV2CddriveFoldersFolderIdDelete(folderId, opts, (error, data, response) => {
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
 **folderId** | **Number**| The ID of the folder to get. | 
 **recursive** | **Boolean**| Flag to indicate if the folder should be deleted if it has items inside of it. | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV2CddriveFoldersFolderIdGet

> CDDriveFolder apiV2CddriveFoldersFolderIdGet(folderId)

UNDER DEVELOPMENT - Get folder information.

Get the information about a folder in the customer&#39;s private CD Drive.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.CDDriveApi();
let folderId = 789; // Number | The ID of the folder to get.
apiInstance.apiV2CddriveFoldersFolderIdGet(folderId, (error, data, response) => {
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
 **folderId** | **Number**| The ID of the folder to get. | 

### Return type

[**CDDriveFolder**](CDDriveFolder.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2CddriveFoldersFolderIdItemsGet

> ApiV2CddriveFoldersFolderIdItemsGet200Response apiV2CddriveFoldersFolderIdItemsGet(folderId, opts)

Get the items in the folder.

Get the information about a folder in the customer&#39;s private CD Drive.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.CDDriveApi();
let folderId = 789; // Number | The ID of the folder to get. Folder ID 0 represents the uppermost CD drive folder.
let opts = {
  'offset': 0, // Number | The offset into the items to begin the response.
  'limit': 20 // Number | The maximum number of items to return in the response.
};
apiInstance.apiV2CddriveFoldersFolderIdItemsGet(folderId, opts, (error, data, response) => {
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
 **folderId** | **Number**| The ID of the folder to get. Folder ID 0 represents the uppermost CD drive folder. | 
 **offset** | **Number**| The offset into the items to begin the response. | [optional] [default to 0]
 **limit** | **Number**| The maximum number of items to return in the response. | [optional] [default to 20]

### Return type

[**ApiV2CddriveFoldersFolderIdItemsGet200Response**](ApiV2CddriveFoldersFolderIdItemsGet200Response.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2CddriveFoldersPost

> CDDriveFolder apiV2CddriveFoldersPost(opts)

Create a folder.

Create a new folder in the customer&#39;s private CD Drive.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.CDDriveApi();
let opts = {
  'name': "name_example", // String | the name of the folder
  'parentId': 789 // Number | The ID of the parent folder or 0 for the root folder.
};
apiInstance.apiV2CddriveFoldersPost(opts, (error, data, response) => {
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
 **name** | **String**| the name of the folder | [optional] 
 **parentId** | **Number**| The ID of the parent folder or 0 for the root folder. | [optional] 

### Return type

[**CDDriveFolder**](CDDriveFolder.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

