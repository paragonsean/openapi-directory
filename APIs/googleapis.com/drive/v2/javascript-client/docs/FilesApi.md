# GoogleDriveApi.FilesApi

All URIs are relative to *https://www.googleapis.com/drive/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**driveFilesCopy**](FilesApi.md#driveFilesCopy) | **POST** /files/{fileId}/copy | 
[**driveFilesDelete**](FilesApi.md#driveFilesDelete) | **DELETE** /files/{fileId} | 
[**driveFilesEmptyTrash**](FilesApi.md#driveFilesEmptyTrash) | **DELETE** /files/trash | 
[**driveFilesExport**](FilesApi.md#driveFilesExport) | **GET** /files/{fileId}/export | 
[**driveFilesGenerateIds**](FilesApi.md#driveFilesGenerateIds) | **GET** /files/generateIds | 
[**driveFilesGet**](FilesApi.md#driveFilesGet) | **GET** /files/{fileId} | 
[**driveFilesInsert**](FilesApi.md#driveFilesInsert) | **POST** /files | 
[**driveFilesList**](FilesApi.md#driveFilesList) | **GET** /files | 
[**driveFilesListLabels**](FilesApi.md#driveFilesListLabels) | **GET** /files/{fileId}/listLabels | 
[**driveFilesModifyLabels**](FilesApi.md#driveFilesModifyLabels) | **POST** /files/{fileId}/modifyLabels | 
[**driveFilesPatch**](FilesApi.md#driveFilesPatch) | **PATCH** /files/{fileId} | 
[**driveFilesTouch**](FilesApi.md#driveFilesTouch) | **POST** /files/{fileId}/touch | 
[**driveFilesTrash**](FilesApi.md#driveFilesTrash) | **POST** /files/{fileId}/trash | 
[**driveFilesUntrash**](FilesApi.md#driveFilesUntrash) | **POST** /files/{fileId}/untrash | 
[**driveFilesUpdate**](FilesApi.md#driveFilesUpdate) | **PUT** /files/{fileId} | 
[**driveFilesWatch**](FilesApi.md#driveFilesWatch) | **POST** /files/{fileId}/watch | 



## driveFilesCopy

> File driveFilesCopy(fileId, opts)



Creates a copy of the specified file.

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
let fileId = "fileId_example"; // String | The ID of the file to copy.
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
  'convert': true, // Boolean | Whether to convert this file to the corresponding Docs Editors format.
  'enforceSingleParent': true, // Boolean | Deprecated: Copying files into multiple folders is no longer supported. Use shortcuts instead.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'ocr': true, // Boolean | Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
  'ocrLanguage': "ocrLanguage_example", // String | If `ocr` is true, hints at the language to use. Valid values are BCP 47 codes.
  'pinned': true, // Boolean | Whether to pin the head revision of the new copy. A file can have a maximum of 200 pinned revisions.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'timedTextLanguage': "timedTextLanguage_example", // String | The language of the timed text.
  'timedTextTrackName': "timedTextTrackName_example", // String | The timed text track name.
  'visibility': "visibility_example", // String | The visibility of the new file. This parameter is only relevant when the source is not a native Google Doc and convert=false.
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
 **fileId** | **String**| The ID of the file to copy. | 
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
 **convert** | **Boolean**| Whether to convert this file to the corresponding Docs Editors format. | [optional] 
 **enforceSingleParent** | **Boolean**| Deprecated: Copying files into multiple folders is no longer supported. Use shortcuts instead. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **ocr** | **Boolean**| Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. | [optional] 
 **ocrLanguage** | **String**| If &#x60;ocr&#x60; is true, hints at the language to use. Valid values are BCP 47 codes. | [optional] 
 **pinned** | **Boolean**| Whether to pin the head revision of the new copy. A file can have a maximum of 200 pinned revisions. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **timedTextLanguage** | **String**| The language of the timed text. | [optional] 
 **timedTextTrackName** | **String**| The timed text track name. | [optional] 
 **visibility** | **String**| The visibility of the new file. This parameter is only relevant when the source is not a native Google Doc and convert&#x3D;false. | [optional] 
 **file** | [**File**](File.md)|  | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
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
let fileId = "fileId_example"; // String | The ID of the file to delete.
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
  'enforceSingleParent': true, // Boolean | Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner's root.
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
 **fileId** | **String**| The ID of the file to delete. | 
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
 **enforceSingleParent** | **Boolean**| Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner&#39;s root. | [optional] 
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
  'enforceSingleParent': true // Boolean | Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner's root.
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
 **enforceSingleParent** | **Boolean**| Deprecated: If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item is placed under its owner&#39;s root. | [optional] 

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



Generates a set of file IDs which can be provided in insert or copy requests.

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
  'maxResults': 56, // Number | Maximum number of IDs to return.
  'space': "space_example", // String | The space in which the IDs can be used to create new files. Supported values are `drive` and `appDataFolder`. (Default: `drive`)
  'type': "type_example" // String | The type of items which the IDs can be used for. Supported values are `files` and `shortcuts`. Note that `shortcuts` are only supported in the `drive` `space`. (Default: `files`)
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
 **maxResults** | **Number**| Maximum number of IDs to return. | [optional] 
 **space** | **String**| The space in which the IDs can be used to create new files. Supported values are &#x60;drive&#x60; and &#x60;appDataFolder&#x60;. (Default: &#x60;drive&#x60;) | [optional] 
 **type** | **String**| The type of items which the IDs can be used for. Supported values are &#x60;files&#x60; and &#x60;shortcuts&#x60;. Note that &#x60;shortcuts&#x60; are only supported in the &#x60;drive&#x60; &#x60;space&#x60;. (Default: &#x60;files&#x60;) | [optional] 

### Return type

[**GeneratedIds**](GeneratedIds.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## driveFilesGet

> File driveFilesGet(fileId, opts)



 Gets a file&#39;s metadata or content by ID. If you provide the URL parameter &#x60;alt&#x3D;media&#x60;, then the response includes the file contents in the response body. Downloading content with &#x60;alt&#x3D;media&#x60; only works if the file is stored in Drive. To download Google Docs, Sheets, and Slides use [&#x60;files.export&#x60;](/drive/api/reference/rest/v2/files/export) instead. For more information, see [Download &amp; export files](/drive/api/guides/manage-downloads).

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
let fileId = "fileId_example"; // String | The ID for the file in question.
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
  'acknowledgeAbuse': true, // Boolean | Whether the user is acknowledging the risk of downloading known malware or other abusive files.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'projection': "projection_example", // String | Deprecated: This parameter has no function.
  'revisionId': "revisionId_example", // String | Specifies the Revision ID that should be downloaded. Ignored unless alt=media is specified.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'updateViewedDate': true // Boolean | Deprecated: Use `files.update` with `modifiedDateBehavior=noChange, updateViewedDate=true` and an empty request body.
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
 **fileId** | **String**| The ID for the file in question. | 
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
 **acknowledgeAbuse** | **Boolean**| Whether the user is acknowledging the risk of downloading known malware or other abusive files. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **projection** | **String**| Deprecated: This parameter has no function. | [optional] 
 **revisionId** | **String**| Specifies the Revision ID that should be downloaded. Ignored unless alt&#x3D;media is specified. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **updateViewedDate** | **Boolean**| Deprecated: Use &#x60;files.update&#x60; with &#x60;modifiedDateBehavior&#x3D;noChange, updateViewedDate&#x3D;true&#x60; and an empty request body. | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## driveFilesInsert

> File driveFilesInsert(opts)



 Inserts a new file. This method supports an *_/upload* URI and accepts uploaded media with the following characteristics: - *Maximum file size:* 5,120 GB - *Accepted Media MIME types:*&#x60;*_/_*&#x60; Note: Specify a valid MIME type, rather than the literal &#x60;*_/_*&#x60; value. The literal &#x60;*_/_*&#x60; is only used to indicate that any valid MIME type can be uploaded. For more information on uploading files, see [Upload file data](/drive/api/guides/manage-uploads). Apps creating shortcuts with &#x60;files.insert&#x60; must specify the MIME type &#x60;application/vnd.google-apps.shortcut&#x60;. Apps should specify a file extension in the &#x60;title&#x60; property when inserting files with the API. For example, an operation to insert a JPEG file should specify something like &#x60;\&quot;title\&quot;: \&quot;cat.jpg\&quot;&#x60; in the metadata. Subsequent &#x60;GET&#x60; requests include the read-only &#x60;fileExtension&#x60; property populated with the extension originally specified in the &#x60;title&#x60; property. When a Google Drive user requests to download a file, or when the file is downloaded through the sync client, Drive builds a full filename (with extension) based on the title. In cases where the extension is missing, Drive attempts to determine the extension based on the file&#39;s MIME type.

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
  'convert': true, // Boolean | Whether to convert this file to the corresponding Docs Editors format.
  'enforceSingleParent': true, // Boolean | Deprecated: Creating files in multiple folders is no longer supported.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'ocr': true, // Boolean | Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
  'ocrLanguage': "ocrLanguage_example", // String | If ocr is true, hints at the language to use. Valid values are BCP 47 codes.
  'pinned': true, // Boolean | Whether to pin the head revision of the uploaded file. A file can have a maximum of 200 pinned revisions.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'timedTextLanguage': "timedTextLanguage_example", // String | The language of the timed text.
  'timedTextTrackName': "timedTextTrackName_example", // String | The timed text track name.
  'useContentAsIndexableText': true, // Boolean | Whether to use the content as indexable text.
  'visibility': "visibility_example", // String | The visibility of the new file. This parameter is only relevant when convert=false.
  'file': null // File | 
};
apiInstance.driveFilesInsert(opts, (error, data, response) => {
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
 **convert** | **Boolean**| Whether to convert this file to the corresponding Docs Editors format. | [optional] 
 **enforceSingleParent** | **Boolean**| Deprecated: Creating files in multiple folders is no longer supported. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **ocr** | **Boolean**| Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. | [optional] 
 **ocrLanguage** | **String**| If ocr is true, hints at the language to use. Valid values are BCP 47 codes. | [optional] 
 **pinned** | **Boolean**| Whether to pin the head revision of the uploaded file. A file can have a maximum of 200 pinned revisions. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **timedTextLanguage** | **String**| The language of the timed text. | [optional] 
 **timedTextTrackName** | **String**| The timed text track name. | [optional] 
 **useContentAsIndexableText** | **Boolean**| Whether to use the content as indexable text. | [optional] 
 **visibility** | **String**| The visibility of the new file. This parameter is only relevant when convert&#x3D;false. | [optional] 
 **file** | [**File**](File.md)|  | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
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
  'corpora': "corpora_example", // String | Bodies of items (files/documents) to which the query applies. Supported bodies are `default`, `domain`, `drive` and `allDrives`. Prefer `default` or `drive` to `allDrives` for efficiency.
  'corpus': "corpus_example", // String | Deprecated: The body of items (files/documents) to which the query applies. Use `corpora` instead.
  'driveId': "driveId_example", // String | ID of the shared drive to search.
  'includeItemsFromAllDrives': true, // Boolean | Whether both My Drive and shared drive items should be included in results.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'includeTeamDriveItems': true, // Boolean | Deprecated: Use `includeItemsFromAllDrives` instead.
  'maxResults': 56, // Number | The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached.
  'orderBy': "orderBy_example", // String | A comma-separated list of sort keys. Valid keys are `createdDate`, `folder`, `lastViewedByMeDate`, `modifiedByMeDate`, `modifiedDate`, `quotaBytesUsed`, `recency`, `sharedWithMeDate`, `starred`, `title`, and `title_natural`. Each key sorts ascending by default, but may be reversed with the `desc` modifier. Example usage: ?orderBy=folder,modifiedDate desc,title. Please note that there is a current limitation for users with approximately one million files in which the requested sort order is ignored.
  'pageToken': "pageToken_example", // String | Page token for files.
  'projection': "projection_example", // String | Deprecated: This parameter has no function.
  'q': "q_example", // String | Query string for searching files.
  'spaces': "spaces_example", // String | A comma-separated list of spaces to query. Supported values are `drive`, and `appDataFolder`.
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
 **corpora** | **String**| Bodies of items (files/documents) to which the query applies. Supported bodies are &#x60;default&#x60;, &#x60;domain&#x60;, &#x60;drive&#x60; and &#x60;allDrives&#x60;. Prefer &#x60;default&#x60; or &#x60;drive&#x60; to &#x60;allDrives&#x60; for efficiency. | [optional] 
 **corpus** | **String**| Deprecated: The body of items (files/documents) to which the query applies. Use &#x60;corpora&#x60; instead. | [optional] 
 **driveId** | **String**| ID of the shared drive to search. | [optional] 
 **includeItemsFromAllDrives** | **Boolean**| Whether both My Drive and shared drive items should be included in results. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **includeTeamDriveItems** | **Boolean**| Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead. | [optional] 
 **maxResults** | **Number**| The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached. | [optional] 
 **orderBy** | **String**| A comma-separated list of sort keys. Valid keys are &#x60;createdDate&#x60;, &#x60;folder&#x60;, &#x60;lastViewedByMeDate&#x60;, &#x60;modifiedByMeDate&#x60;, &#x60;modifiedDate&#x60;, &#x60;quotaBytesUsed&#x60;, &#x60;recency&#x60;, &#x60;sharedWithMeDate&#x60;, &#x60;starred&#x60;, &#x60;title&#x60;, and &#x60;title_natural&#x60;. Each key sorts ascending by default, but may be reversed with the &#x60;desc&#x60; modifier. Example usage: ?orderBy&#x3D;folder,modifiedDate desc,title. Please note that there is a current limitation for users with approximately one million files in which the requested sort order is ignored. | [optional] 
 **pageToken** | **String**| Page token for files. | [optional] 
 **projection** | **String**| Deprecated: This parameter has no function. | [optional] 
 **q** | **String**| Query string for searching files. | [optional] 
 **spaces** | **String**| A comma-separated list of spaces to query. Supported values are &#x60;drive&#x60;, and &#x60;appDataFolder&#x60;. | [optional] 
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
  'pageToken': "pageToken_example" // String | The token for continuing a previous list request on the next page. This should be set to the value of `nextPageToken` from the previous response.
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
 **pageToken** | **String**| The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from the previous response. | [optional] 

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


## driveFilesPatch

> File driveFilesPatch(fileId, opts)



Updates a file&#39;s metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might change automatically, such as modifiedDate. This method supports patch semantics.

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
let fileId = "fileId_example"; // String | The ID of the file to update.
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
  'addParents': "addParents_example", // String | Comma-separated list of parent IDs to add.
  'convert': true, // Boolean | Deprecated: This parameter has no function.
  'enforceSingleParent': true, // Boolean | Deprecated: Adding files to multiple folders is no longer supported. Use `shortcuts` instead.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'modifiedDateBehavior': "modifiedDateBehavior_example", // String | Determines the behavior in which `modifiedDate` is updated. This overrides `setModifiedDate`.
  'newRevision': true, // Boolean | Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045). Note that this field is ignored if there is no payload in the request.
  'ocr': true, // Boolean | Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
  'ocrLanguage': "ocrLanguage_example", // String | If ocr is true, hints at the language to use. Valid values are BCP 47 codes.
  'pinned': true, // Boolean | Whether to pin the new revision. A file can have a maximum of 200 pinned revisions. Note that this field is ignored if there is no payload in the request.
  'removeParents': "removeParents_example", // String | Comma-separated list of parent IDs to remove.
  'setModifiedDate': true, // Boolean | Whether to set the modified date using the value supplied in the request body. Setting this field to `true` is equivalent to `modifiedDateBehavior=fromBodyOrNow`, and `false` is equivalent to `modifiedDateBehavior=now`. To prevent any changes to the modified date set `modifiedDateBehavior=noChange`.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'timedTextLanguage': "timedTextLanguage_example", // String | The language of the timed text.
  'timedTextTrackName': "timedTextTrackName_example", // String | The timed text track name.
  'updateViewedDate': true, // Boolean | Whether to update the view date after successfully updating the file.
  'useContentAsIndexableText': true, // Boolean | Whether to use the content as indexable text.
  'file': null // File | 
};
apiInstance.driveFilesPatch(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file to update. | 
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
 **addParents** | **String**| Comma-separated list of parent IDs to add. | [optional] 
 **convert** | **Boolean**| Deprecated: This parameter has no function. | [optional] 
 **enforceSingleParent** | **Boolean**| Deprecated: Adding files to multiple folders is no longer supported. Use &#x60;shortcuts&#x60; instead. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **modifiedDateBehavior** | **String**| Determines the behavior in which &#x60;modifiedDate&#x60; is updated. This overrides &#x60;setModifiedDate&#x60;. | [optional] 
 **newRevision** | **Boolean**| Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045). Note that this field is ignored if there is no payload in the request. | [optional] 
 **ocr** | **Boolean**| Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. | [optional] 
 **ocrLanguage** | **String**| If ocr is true, hints at the language to use. Valid values are BCP 47 codes. | [optional] 
 **pinned** | **Boolean**| Whether to pin the new revision. A file can have a maximum of 200 pinned revisions. Note that this field is ignored if there is no payload in the request. | [optional] 
 **removeParents** | **String**| Comma-separated list of parent IDs to remove. | [optional] 
 **setModifiedDate** | **Boolean**| Whether to set the modified date using the value supplied in the request body. Setting this field to &#x60;true&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;fromBodyOrNow&#x60;, and &#x60;false&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;now&#x60;. To prevent any changes to the modified date set &#x60;modifiedDateBehavior&#x3D;noChange&#x60;. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **timedTextLanguage** | **String**| The language of the timed text. | [optional] 
 **timedTextTrackName** | **String**| The timed text track name. | [optional] 
 **updateViewedDate** | **Boolean**| Whether to update the view date after successfully updating the file. | [optional] 
 **useContentAsIndexableText** | **Boolean**| Whether to use the content as indexable text. | [optional] 
 **file** | [**File**](File.md)|  | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## driveFilesTouch

> File driveFilesTouch(fileId, opts)



Set the file&#39;s updated time to the current server time.

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
let fileId = "fileId_example"; // String | The ID of the file to update.
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
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true // Boolean | Deprecated: Use `supportsAllDrives` instead.
};
apiInstance.driveFilesTouch(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file to update. | 
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
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## driveFilesTrash

> File driveFilesTrash(fileId, opts)



Moves a file to the trash. The currently authenticated user must own the file or be at least a &#x60;fileOrganizer&#x60; on the parent for shared drive files.

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
let fileId = "fileId_example"; // String | The ID of the file to trash.
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
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true // Boolean | Deprecated: Use `supportsAllDrives` instead.
};
apiInstance.driveFilesTrash(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file to trash. | 
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
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## driveFilesUntrash

> File driveFilesUntrash(fileId, opts)



Restores a file from the trash. The currently authenticated user must own the file or be at least a &#x60;fileOrganizer&#x60; on the parent for shared drive files.

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
let fileId = "fileId_example"; // String | The ID of the file to untrash.
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
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true // Boolean | Deprecated: Use `supportsAllDrives` instead.
};
apiInstance.driveFilesUntrash(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The ID of the file to untrash. | 
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
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 

### Return type

**File**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
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
let fileId = "fileId_example"; // String | The ID of the file to update.
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
  'addParents': "addParents_example", // String | Comma-separated list of parent IDs to add.
  'convert': true, // Boolean | Deprecated: This parameter has no function.
  'enforceSingleParent': true, // Boolean | Deprecated: Adding files to multiple folders is no longer supported. Use `shortcuts` instead.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'modifiedDateBehavior': "modifiedDateBehavior_example", // String | Determines the behavior in which `modifiedDate` is updated. This overrides `setModifiedDate`.
  'newRevision': true, // Boolean | Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045).
  'ocr': true, // Boolean | Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads.
  'ocrLanguage': "ocrLanguage_example", // String | If ocr is true, hints at the language to use. Valid values are BCP 47 codes.
  'pinned': true, // Boolean | Whether to pin the new revision. A file can have a maximum of 200 pinned revisions.
  'removeParents': "removeParents_example", // String | Comma-separated list of parent IDs to remove.
  'setModifiedDate': true, // Boolean | Whether to set the modified date using the value supplied in the request body. Setting this field to `true` is equivalent to `modifiedDateBehavior=fromBodyOrNow`, and `false` is equivalent to `modifiedDateBehavior=now`. To prevent any changes to the modified date set `modifiedDateBehavior=noChange`.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'timedTextLanguage': "timedTextLanguage_example", // String | The language of the timed text.
  'timedTextTrackName': "timedTextTrackName_example", // String | The timed text track name.
  'updateViewedDate': true, // Boolean | Whether to update the view date after successfully updating the file.
  'useContentAsIndexableText': true, // Boolean | Whether to use the content as indexable text.
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
 **fileId** | **String**| The ID of the file to update. | 
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
 **addParents** | **String**| Comma-separated list of parent IDs to add. | [optional] 
 **convert** | **Boolean**| Deprecated: This parameter has no function. | [optional] 
 **enforceSingleParent** | **Boolean**| Deprecated: Adding files to multiple folders is no longer supported. Use &#x60;shortcuts&#x60; instead. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **modifiedDateBehavior** | **String**| Determines the behavior in which &#x60;modifiedDate&#x60; is updated. This overrides &#x60;setModifiedDate&#x60;. | [optional] 
 **newRevision** | **Boolean**| Whether a blob upload should create a new revision. If false, the blob data in the current head revision is replaced. If true or not set, a new blob is created as head revision, and previous unpinned revisions are preserved for a short period of time. Pinned revisions are stored indefinitely, using additional storage quota, up to a maximum of 200 revisions. For details on how revisions are retained, see the [Drive Help Center](https://support.google.com/drive/answer/2409045). | [optional] 
 **ocr** | **Boolean**| Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. | [optional] 
 **ocrLanguage** | **String**| If ocr is true, hints at the language to use. Valid values are BCP 47 codes. | [optional] 
 **pinned** | **Boolean**| Whether to pin the new revision. A file can have a maximum of 200 pinned revisions. | [optional] 
 **removeParents** | **String**| Comma-separated list of parent IDs to remove. | [optional] 
 **setModifiedDate** | **Boolean**| Whether to set the modified date using the value supplied in the request body. Setting this field to &#x60;true&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;fromBodyOrNow&#x60;, and &#x60;false&#x60; is equivalent to &#x60;modifiedDateBehavior&#x3D;now&#x60;. To prevent any changes to the modified date set &#x60;modifiedDateBehavior&#x3D;noChange&#x60;. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **timedTextLanguage** | **String**| The language of the timed text. | [optional] 
 **timedTextTrackName** | **String**| The timed text track name. | [optional] 
 **updateViewedDate** | **Boolean**| Whether to update the view date after successfully updating the file. | [optional] 
 **useContentAsIndexableText** | **Boolean**| Whether to use the content as indexable text. | [optional] 
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
let fileId = "fileId_example"; // String | The ID for the file in question.
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
  'acknowledgeAbuse': true, // Boolean | Whether the user is acknowledging the risk of downloading known malware or other abusive files.
  'includeLabels': "includeLabels_example", // String | A comma-separated list of IDs of labels to include in the `labelInfo` part of the response.
  'includePermissionsForView': "includePermissionsForView_example", // String | Specifies which additional view's permissions to include in the response. Only `published` is supported.
  'projection': "projection_example", // String | Deprecated: This parameter has no function.
  'revisionId': "revisionId_example", // String | Specifies the Revision ID that should be downloaded. Ignored unless alt=media is specified.
  'supportsAllDrives': true, // Boolean | Whether the requesting application supports both My Drives and shared drives.
  'supportsTeamDrives': true, // Boolean | Deprecated: Use `supportsAllDrives` instead.
  'updateViewedDate': true, // Boolean | Deprecated: Use files.update with modifiedDateBehavior=noChange, updateViewedDate=true and an empty request body.
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
 **fileId** | **String**| The ID for the file in question. | 
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
 **acknowledgeAbuse** | **Boolean**| Whether the user is acknowledging the risk of downloading known malware or other abusive files. | [optional] 
 **includeLabels** | **String**| A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response. | [optional] 
 **includePermissionsForView** | **String**| Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported. | [optional] 
 **projection** | **String**| Deprecated: This parameter has no function. | [optional] 
 **revisionId** | **String**| Specifies the Revision ID that should be downloaded. Ignored unless alt&#x3D;media is specified. | [optional] 
 **supportsAllDrives** | **Boolean**| Whether the requesting application supports both My Drives and shared drives. | [optional] 
 **supportsTeamDrives** | **Boolean**| Deprecated: Use &#x60;supportsAllDrives&#x60; instead. | [optional] 
 **updateViewedDate** | **Boolean**| Deprecated: Use files.update with modifiedDateBehavior&#x3D;noChange, updateViewedDate&#x3D;true and an empty request body. | [optional] 
 **channel** | [**Channel**](Channel.md)|  | [optional] 

### Return type

[**Channel**](Channel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

