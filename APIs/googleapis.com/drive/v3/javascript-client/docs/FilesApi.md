# GoogleDriveApi.FilesApi

All URIs are relative to *https://www.googleapis.com/drive/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**driveFilesCopy**](FilesApi.md#driveFilesCopy) | **POST** /files/{fileId}/copy | 
[**driveFilesCreate**](FilesApi.md#driveFilesCreate) | **POST** /files | 
[**driveFilesDelete**](FilesApi.md#driveFilesDelete) | **DELETE** /files/{fileId} | 
[**driveFilesEmptyTrash**](FilesApi.md#driveFilesEmptyTrash) | **DELETE** /files/trash | 
[**driveFilesExport**](FilesApi.md#driveFilesExport) | **GET** /files/{fileId}/export | 
[**driveFilesGenerateIds**](FilesApi.md#driveFilesGenerateIds) | **GET** /files/generateIds | 
[**driveFilesGet**](FilesApi.md#driveFilesGet) | **GET** /files/{fileId} | 
[**driveFilesList**](FilesApi.md#driveFilesList) | **GET** /files | 
[**driveFilesListLabels**](FilesApi.md#driveFilesListLabels) | **GET** /files/{fileId}/listLabels | 
[**driveFilesModifyLabels**](FilesApi.md#driveFilesModifyLabels) | **POST** /files/{fileId}/modifyLabels | 
[**driveFilesUpdate**](FilesApi.md#driveFilesUpdate) | **PATCH** /files/{fileId} | 
[**driveFilesWatch**](FilesApi.md#driveFilesWatch) | **POST** /files/{fileId}/watch | 



## driveFilesCopy

> File driveFilesCopy(fileId, opts)



Creates a copy of a file and applies any requested updates with patch semantics.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let fileId = "fileId_example"; // String | The ID of the file.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'enforceSingleParent': true, // Boolean | Deprecated. Copying files into multiple folders is no longer supported. Use shortcuts instead.
  'ignoreDefaultVisibility': true, // Boolean | Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
  'keepRevisionForever': true, // Boolean | Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.
  'ocrLanguage': "ocrLanguage_example", // String | A language hint for OCR processing during image import (ISO 639-1 code).
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'file': null // File | 
};
apiInstance.driveFilesCopy(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **enforceSingleParent** | **Boolean**| Deprecated. Copying files into multiple folders is no longer supported. Use shortcuts instead. | [optional] 
 **ignoreDefaultVisibility** | **Boolean**| Whether to ignore the domain&#39;s default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] 
 **keepRevisionForever** | **Boolean**| Whether to set the &#39;keepForever&#39; field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. | [optional] 
 **ocrLanguage** | **String**| A language hint for OCR processing during image import (ISO 639-1 code). | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **file** | [**File**](File.md)|  | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driveFilesCreate

> File driveFilesCreate(opts)



 Creates a new file. This method supports an *_/upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*_/_*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*_/_*&#x60; value. The literal &#x60;*_/_*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads). Apps creating shortcuts with &#x60;files.create&#x60; must specify the MIME type &#x60;application/vnd.google-apps.shortcut&#x60;. Apps should specify a file extension in the &#x60;name&#x60; property when inserting files with the API. For example, an operation to insert a JPEG file should specify something like &#x60;\&quot;name\&quot;: \&quot;cat.jpg\&quot;&#x60; in the metadata. Subsequent &#x60;GET&#x60; requests include the read-only &#x60;fileExtension&#x60; property populated with the extension originally specified in the &#x60;title&#x60; property. When a Google Drive user requests to download a file, or when the file is downloaded through the sync client, Drive builds a full filename (with extension) based on the title. In cases where the extension is missing, Drive attempts to determine the extension based on the file&#39;s MIME type.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'enforceSingleParent': true, // Boolean | Deprecated. Creating files in multiple folders is no longer supported.
  'ignoreDefaultVisibility': true, // Boolean | Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
  'keepRevisionForever': true, // Boolean | Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.
  'ocrLanguage': "ocrLanguage_example", // String | A language hint for OCR processing during image import (ISO 639-1 code).
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'useContentAsIndexableText': true, // Boolean | Whether to use the uploaded content as indexable text.
  'file': null // File | 
};
apiInstance.driveFilesCreate(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **enforceSingleParent** | **Boolean**| Deprecated. Creating files in multiple folders is no longer supported. | [optional] 
 **ignoreDefaultVisibility** | **Boolean**| Whether to ignore the domain&#39;s default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] 
 **keepRevisionForever** | **Boolean**| Whether to set the &#39;keepForever&#39; field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. | [optional] 
 **ocrLanguage** | **String**| A language hint for OCR processing during image import (ISO 639-1 code). | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **useContentAsIndexableText** | **Boolean**| Whether to use the uploaded content as indexable text. | [optional] 
 **file** | [**File**](File.md)|  | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## driveFilesDelete

> driveFilesDelete(fileId, opts)



Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a shared drive, the user must be an &#x60;organizer&#x60; on the parent folder. If the target is a folder, all descendants owned by the user are also deleted.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let fileId = "fileId_example"; // String | The ID of the file.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'enforceSingleParent': true, // Boolean | Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner's root.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true // Boolean | Deprecated: Use `supportsAllDrives` instead.
};
apiInstance.driveFilesDelete(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **enforceSingleParent** | **Boolean**| Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner&#39;s root. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## driveFilesEmptyTrash

> driveFilesEmptyTrash(opts)



Permanently deletes all of the user&#39;s trashed files.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'driveId': "driveId_example", // String | If set, empties the trash of the provided shared drive.
  'enforceSingleParent': true // Boolean | Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner's root.
};
apiInstance.driveFilesEmptyTrash(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **driveId** | **String**| If set, empties the trash of the provided shared drive. | [optional] 
 **enforceSingleParent** | **Boolean**| Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner&#39;s root. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## driveFilesExport

> driveFilesExport(fileId, mimeType, opts)



Exports a Google Workspace document to the requested MIME type and returns exported byte content. Note that the exported content is limited to 10MB.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let fileId = "fileId_example"; // String | The ID of the file.
let mimeType = "mimeType_example"; // String | Required. The MIME type of the format requested for this export.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.driveFilesExport(fileId, mimeType, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file. | 
 **mimeType** | **String**| Required. The MIME type of the format requested for this export. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## driveFilesGenerateIds

> GeneratedIds driveFilesGenerateIds(opts)



Generates a set of file IDs which can be provided in create or copy requests.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'count': 56, // Number | The number of IDs to return.
  'space': "space_example", // String | The space in which the IDs can be used to create new files. Supported values are 'drive' and 'appDataFolder'. (Default: 'drive')
  'type': "type_example" // String | The type of items which the IDs can be used for. Supported values are 'files' and 'shortcuts'. Note that 'shortcuts' are only supported in the `drive` 'space'. (Default: 'files')
};
apiInstance.driveFilesGenerateIds(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **count** | **Number**| The number of IDs to return. | [optional] 
 **space** | **String**| The space in which the IDs can be used to create new files. Supported values are &#39;drive&#39; and &#39;appDataFolder&#39;. (Default: &#39;drive&#39;) | [optional] 
 **type** | **String**| The type of items which the IDs can be used for. Supported values are &#39;files&#39; and &#39;shortcuts&#39;. Note that &#39;shortcuts&#39; are only supported in the &#x60;drive&#x60; &#39;space&#39;. (Default: &#39;files&#39;) | [optional] 

### Return type

[**GeneratedIds**](GeneratedIds.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## driveFilesGet

> File driveFilesGet(fileId, opts)



 Gets a file&#39;s metadata or content by ID. If you provide the URL parameter &#x60;alt&#x3D;media&#x60;, then the response includes the file contents in the response body. Downloading content with &#x60;alt&#x3D;media&#x60; only works if the file is stored in Drive. To download Google Docs, Sheets, and Slides use [&#x60;files.export&#x60;](/drive/api/reference/rest/v3/files/export) instead. For more information, see [Download &amp; export files](/drive/api/guides/manage-downloads).

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let fileId = "fileId_example"; // String | The ID of the file.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'acknowledgeAbuse': true, // Boolean | Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true // Boolean | Deprecated: Use `supportsAllDrives` instead.
};
apiInstance.driveFilesGet(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **acknowledgeAbuse** | **Boolean**| Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt&#x3D;media. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## driveFilesList

> FileList driveFilesList(opts)



 Lists the user&#39;s files. This method accepts the &#x60;q&#x60; parameter, which is a search query combining one or more search terms. For more information, see the [Search for files &amp; folders](/drive/api/guides/search-files) guide. *Note:* This method returns *all* files by default, including trashed files. If you don&#39;t want trashed files to appear in the list, use the &#x60;trashed&#x3D;false&#x60; query parameter to remove trashed files from the results.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'corpora': "corpora_example", // String | Bodies of items (files/documents) to which the query applies. Supported bodies are 'user', 'domain', 'drive', and 'allDrives'. Prefer 'user' or 'drive' to 'allDrives' for efficiency. By default, corpora is set to 'user'. However, this can change depending on the filter set through the 'q' parameter.
  'corpus': "corpus_example", // String | Deprecated: The source of files to list. Use 'corpora' instead.
  'driveId': "driveId_example", // String | ID of the shared drive to search.
  'includeItemsFromAllDrives': true, // Boolean | Whether both My Drive and shared drive items should be included in results.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
  'includeTeamDriveItems': true, // Boolean | Deprecated: Use `includeItemsFromAllDrives` instead.
  'orderBy': "orderBy_example", // String | A comma-separated list of sort keys. Valid keys are 'createdTime', 'folder', 'modifiedByMeTime', 'modifiedTime', 'name', 'name_natural', 'quotaBytesUsed', 'recency', 'sharedWithMeTime', 'starred', and 'viewedByMeTime'. Each key sorts ascending by default, but can be reversed with the 'desc' modifier. Example usage: ?orderBy=folder,modifiedTime desc,name.
  'pageSize': 56, // Number | The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached.
  'pageToken': "pageToken_example", // String | The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.
  'q': "q_example", // String | A query for filtering the file results. See the \"Search for files & folders\" guide for supported syntax.
  'spaces': "spaces_example", // String | A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'teamDriveId': "teamDriveId_example" // String | Deprecated: Use `driveId` instead.
};
apiInstance.driveFilesList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **corpora** | **String**| Bodies of items (files/documents) to which the query applies. Supported bodies are &#39;user&#39;, &#39;domain&#39;, &#39;drive&#39;, and &#39;allDrives&#39;. Prefer &#39;user&#39; or &#39;drive&#39; to &#39;allDrives&#39; for efficiency. By default, corpora is set to &#39;user&#39;. However, this can change depending on the filter set through the &#39;q&#39; parameter. | [optional] 
 **corpus** | **String**| Deprecated: The source of files to list. Use &#39;corpora&#39; instead. | [optional] 
 **driveId** | **String**| ID of the shared drive to search. | [optional] 
 **includeItemsFromAllDrives** | **Boolean**| Whether both My Drive and shared drive items should be included in results. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] 
 **includeTeamDriveItems** | **Boolean**| Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead. | [optional] 
 **orderBy** | **String**| A comma-separated list of sort keys. Valid keys are &#39;createdTime&#39;, &#39;folder&#39;, &#39;modifiedByMeTime&#39;, &#39;modifiedTime&#39;, &#39;name&#39;, &#39;name_natural&#39;, &#39;quotaBytesUsed&#39;, &#39;recency&#39;, &#39;sharedWithMeTime&#39;, &#39;starred&#39;, and &#39;viewedByMeTime&#39;. Each key sorts ascending by default, but can be reversed with the &#39;desc&#39; modifier. Example usage: ?orderBy&#x3D;folder,modifiedTime desc,name. | [optional] 
 **pageSize** | **Number**| The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached. | [optional] 
 **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response. | [optional] 
 **q** | **String**| A query for filtering the file results. See the \&quot;Search for files &amp; folders\&quot; guide for supported syntax. | [optional] 
 **spaces** | **String**| A comma-separated list of spaces to query within the corpora. Supported values are &#39;drive&#39; and &#39;appDataFolder&#39;. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **teamDriveId** | **String**| Deprecated: Use &#x60;driveId&#x60; instead. | [optional] 

### Return type

[**FileList**](FileList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## driveFilesListLabels

> LabelList driveFilesListLabels(fileId, opts)



Lists the labels on a file.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let fileId = "fileId_example"; // String | The ID for the file.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'maxResults': 56, // Number | The maximum number of labels to return per page. When not set, defaults to 100.
  'pageToken': "pageToken_example" // String | The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.
};
apiInstance.driveFilesListLabels(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID for the file. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **maxResults** | **Number**| The maximum number of labels to return per page. When not set, defaults to 100. | [optional] 
 **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response. | [optional] 

### Return type

[**LabelList**](LabelList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## driveFilesModifyLabels

> ModifyLabelsResponse driveFilesModifyLabels(fileId, opts)



Modifies the set of labels applied to a file. Returns a list of the labels that were added or modified.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let fileId = "fileId_example"; // String | The ID of the file to which the labels belong.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'modifyLabelsRequest': new GoogleDriveApi.ModifyLabelsRequest() // ModifyLabelsRequest | 
};
apiInstance.driveFilesModifyLabels(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file to which the labels belong. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **modifyLabelsRequest** | [**ModifyLabelsRequest**](ModifyLabelsRequest.md)|  | [optional] 

### Return type

[**ModifyLabelsResponse**](ModifyLabelsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driveFilesUpdate

> File driveFilesUpdate(fileId, opts)



 Updates a file&#39;s metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might be changed automatically, such as &#x60;modifiedDate&#x60;. This method supports patch semantics. This method supports an *_/upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*_/_*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*_/_*&#x60; value. The literal &#x60;*_/_*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads).

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let fileId = "fileId_example"; // String | The ID of the file.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'addParents': "addParents_example", // String | A comma-separated list of parent IDs to add.
  'enforceSingleParent': true, // Boolean | Deprecated: Adding files to multiple folders is no longer supported. Use shortcuts instead.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
  'keepRevisionForever': true, // Boolean | Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.
  'ocrLanguage': "ocrLanguage_example", // String | A language hint for OCR processing during image import (ISO 639-1 code).
  'removeParents': "removeParents_example", // String | A comma-separated list of parent IDs to remove.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'useContentAsIndexableText': true, // Boolean | Whether to use the uploaded content as indexable text.
  'file': null // File | 
};
apiInstance.driveFilesUpdate(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **addParents** | **String**| A comma-separated list of parent IDs to add. | [optional] 
 **enforceSingleParent** | **Boolean**| Deprecated: Adding files to multiple folders is no longer supported. Use shortcuts instead. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] 
 **keepRevisionForever** | **Boolean**| Whether to set the &#39;keepForever&#39; field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions. | [optional] 
 **ocrLanguage** | **String**| A language hint for OCR processing during image import (ISO 639-1 code). | [optional] 
 **removeParents** | **String**| A comma-separated list of parent IDs to remove. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **useContentAsIndexableText** | **Boolean**| Whether to use the uploaded content as indexable text. | [optional] 
 **file** | [**File**](File.md)|  | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## driveFilesWatch

> Channel driveFilesWatch(fileId, opts)



Subscribes to changes to a file.

### Example

```javascript
import GoogleDriveApi from 'google_drive_api';
let defaultClient = GoogleDriveApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleDriveApi.FilesApi();
let fileId = "fileId_example"; // String | The ID of the file.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'acknowledgeAbuse': true, // Boolean | Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only 'published' is supported.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'channel': new GoogleDriveApi.Channel() // Channel | 
};
apiInstance.driveFilesWatch(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **acknowledgeAbuse** | **Boolean**| Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt&#x3D;media. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **channel** | [**Channel**](Channel.md)|  | [optional] 

### Return type

[**Channel**](Channel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

