# CloudStorageJsonApi.FoldersApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageFoldersDelete**](FoldersApi.md#storageFoldersDelete) | **DELETE** /b/{bucket}/folders/{folder} | 
[**storageFoldersGet**](FoldersApi.md#storageFoldersGet) | **GET** /b/{bucket}/folders/{folder} | 
[**storageFoldersInsert**](FoldersApi.md#storageFoldersInsert) | **POST** /b/{bucket}/folders | 
[**storageFoldersList**](FoldersApi.md#storageFoldersList) | **GET** /b/{bucket}/folders | 
[**storageFoldersRename**](FoldersApi.md#storageFoldersRename) | **POST** /b/{bucket}/folders/{sourceFolder}/renameTo/folders/{destinationFolder} | 



## storageFoldersDelete

> storageFoldersDelete(bucket, folder, opts)



Permanently deletes a folder. Only applicable to buckets with hierarchical namespace enabled.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.FoldersApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the folder resides.
let folder = "folder_example"; // String | Name of a folder.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | If set, only deletes the folder if its metageneration matches this value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example" // String | If set, only deletes the folder if its metageneration does not match this value.
};
apiInstance.storageFoldersDelete(bucket, folder, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the folder resides. | 
 **folder** | **String**| Name of a folder. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| If set, only deletes the folder if its metageneration matches this value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| If set, only deletes the folder if its metageneration does not match this value. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageFoldersGet

> Folder storageFoldersGet(bucket, folder, opts)



Returns metadata for the specified folder. Only applicable to buckets with hierarchical namespace enabled.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.FoldersApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the folder resides.
let folder = "folder_example"; // String | Name of a folder.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the return of the folder metadata conditional on whether the folder's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example" // String | Makes the return of the folder metadata conditional on whether the folder's current metageneration does not match the given value.
};
apiInstance.storageFoldersGet(bucket, folder, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the folder resides. | 
 **folder** | **String**| Name of a folder. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the return of the folder metadata conditional on whether the folder&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the return of the folder metadata conditional on whether the folder&#39;s current metageneration does not match the given value. | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageFoldersInsert

> Folder storageFoldersInsert(bucket, opts)



Creates a new folder. Only applicable to buckets with hierarchical namespace enabled.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.FoldersApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the folder resides.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'recursive': true, // Boolean | If true, any parent folder which doesn’t exist will be created automatically.
  'folder': new CloudStorageJsonApi.Folder() // Folder | 
};
apiInstance.storageFoldersInsert(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the folder resides. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **recursive** | **Boolean**| If true, any parent folder which doesn’t exist will be created automatically. | [optional] 
 **folder** | [**Folder**](Folder.md)|  | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageFoldersList

> Folders storageFoldersList(bucket, opts)



Retrieves a list of folders matching the criteria. Only applicable to buckets with hierarchical namespace enabled.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.FoldersApi();
let bucket = "bucket_example"; // String | Name of the bucket in which to look for folders.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'delimiter': "delimiter_example", // String | Returns results in a directory-like mode. The only supported value is '/'. If set, items will only contain folders that either exactly match the prefix, or are one level below the prefix.
  'endOffset': "endOffset_example", // String | Filter results to folders whose names are lexicographically before endOffset. If startOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive).
  'pageSize': 56, // Number | Maximum number of items to return in a single page of responses.
  'pageToken': "pageToken_example", // String | A previously-returned page token representing part of the larger set of results to view.
  'prefix': "prefix_example", // String | Filter results to folders whose paths begin with this prefix. If set, the value must either be an empty string or end with a '/'.
  'startOffset': "startOffset_example" // String | Filter results to folders whose names are lexicographically equal to or after startOffset. If endOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive).
};
apiInstance.storageFoldersList(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which to look for folders. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **delimiter** | **String**| Returns results in a directory-like mode. The only supported value is &#39;/&#39;. If set, items will only contain folders that either exactly match the prefix, or are one level below the prefix. | [optional] 
 **endOffset** | **String**| Filter results to folders whose names are lexicographically before endOffset. If startOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] 
 **pageSize** | **Number**| Maximum number of items to return in a single page of responses. | [optional] 
 **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] 
 **prefix** | **String**| Filter results to folders whose paths begin with this prefix. If set, the value must either be an empty string or end with a &#39;/&#39;. | [optional] 
 **startOffset** | **String**| Filter results to folders whose names are lexicographically equal to or after startOffset. If endOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] 

### Return type

[**Folders**](Folders.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageFoldersRename

> GoogleLongrunningOperation storageFoldersRename(bucket, sourceFolder, destinationFolder, opts)



Renames a source folder to a destination folder. Only applicable to buckets with hierarchical namespace enabled.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.FoldersApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the folders are in.
let sourceFolder = "sourceFolder_example"; // String | Name of the source folder.
let destinationFolder = "destinationFolder_example"; // String | Name of the destination folder.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifSourceMetagenerationMatch': "ifSourceMetagenerationMatch_example", // String | Makes the operation conditional on whether the source object's current metageneration matches the given value.
  'ifSourceMetagenerationNotMatch': "ifSourceMetagenerationNotMatch_example" // String | Makes the operation conditional on whether the source object's current metageneration does not match the given value.
};
apiInstance.storageFoldersRename(bucket, sourceFolder, destinationFolder, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the folders are in. | 
 **sourceFolder** | **String**| Name of the source folder. | 
 **destinationFolder** | **String**| Name of the destination folder. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifSourceMetagenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value. | [optional] 
 **ifSourceMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value. | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

