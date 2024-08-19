# OpenChannelMarketApi.FilesUploadFilesApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filesByIdOrUrlGet**](FilesUploadFilesApi.md#filesByIdOrUrlGet) | **GET** /files/byIdOrUrl | Get the details for a file.
[**filesDownloadGet**](FilesUploadFilesApi.md#filesDownloadGet) | **GET** /files/download | A signed URL for downloading a private file can be returned by providing the fileId.
[**filesGet**](FilesUploadFilesApi.md#filesGet) | **GET** /files | Returns a paginated list of files
[**filesPost**](FilesUploadFilesApi.md#filesPost) | **POST** /files | Uploads a file.
[**filesUrlPost**](FilesUploadFilesApi.md#filesUrlPost) | **POST** /files/url | Uploads a file from a URL



## filesByIdOrUrlGet

> File filesByIdOrUrlGet(fileIdOrUrl)

Get the details for a file.

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.FilesUploadFilesApi();
let fileIdOrUrl = "fileIdOrUrl_example"; // String | The fileId or fileUrl of the file to be returned
apiInstance.filesByIdOrUrlGet(fileIdOrUrl, (error, data, response) => {
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
 **fileIdOrUrl** | **String**| The fileId or fileUrl of the file to be returned | 

### Return type

**File**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## filesDownloadGet

> FileDownload filesDownloadGet(fileId, opts)

A signed URL for downloading a private file can be returned by providing the fileId.

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.FilesUploadFilesApi();
let fileId = "fileId_example"; // String | The URL of the file to be uploaded
let opts = {
  'validSeconds': 56 // Number | The number of seconds that this signed URL should be valid for. The default is 60.
};
apiInstance.filesDownloadGet(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| The URL of the file to be uploaded | 
 **validSeconds** | **Number**| The number of seconds that this signed URL should be valid for. The default is 60. | [optional] 

### Return type

[**FileDownload**](FileDownload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## filesGet

> File filesGet(opts)

Returns a paginated list of files

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.FilesUploadFilesApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'name':'file.txt'} matches all the files that have the name 'file.txt'
  'sort': "sort_example", // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56 // Number | The maximum number of results to return per page
};
apiInstance.filesGet(opts, (error, data, response) => {
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
 **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;file.txt&#39;} matches all the files that have the name &#39;file.txt&#39; | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 

### Return type

**File**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## filesPost

> File filesPost(file, opts)

Uploads a file.

- WARNING: File URLs or fileIds must be stored somewhere within the customData field for an app, review, developer or user. Unused files will be removed after a few days.  - This method is called on behalf of a developer. 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.FilesUploadFilesApi();
let file = "/path/to/file"; // File | The file to be uploaded
let opts = {
  'isPrivate': true, // Boolean | If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false.
  'hash': "hash_example" // String | A comma separated list of hashes to return in order to verify file integrity.
};
apiInstance.filesPost(file, opts, (error, data, response) => {
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
 **file** | **File**| The file to be uploaded | 
 **isPrivate** | **Boolean**| If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false. | [optional] 
 **hash** | **String**| A comma separated list of hashes to return in order to verify file integrity. | [optional] 

### Return type

**File**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## filesUrlPost

> File filesUrlPost(url, opts)

Uploads a file from a URL

- WARNING: File URLs or fileIds must be stored somewhere within the customData field for an app, review, developer or user. Unused files will be removed after a few days. - This method is called on behalf of a developer. 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.FilesUploadFilesApi();
let url = "url_example"; // String | The URL of the file to be uploaded
let opts = {
  'isPrivate': true // Boolean | If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false.
};
apiInstance.filesUrlPost(url, opts, (error, data, response) => {
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
 **url** | **String**| The URL of the file to be uploaded | 
 **isPrivate** | **Boolean**| If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false. | [optional] 

### Return type

**File**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

