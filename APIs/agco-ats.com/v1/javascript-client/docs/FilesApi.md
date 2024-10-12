# AgcoApi.FilesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filesDeleteFile**](FilesApi.md#filesDeleteFile) | **DELETE** /api/v2/Files/{ID} | Mark a file as &#39;Removed&#39;. Disables download of the file and hides metadata from GET all method
[**filesGetFile**](FilesApi.md#filesGetFile) | **GET** /api/v2/Files/{ID} | Gets a file&#39;s metadata.
[**filesGetFileContents**](FilesApi.md#filesGetFileContents) | **GET** /api/v2/Files/{ID}/FileContents | Download the contents of a file. The current State of the File should be &#39;Available&#39;.
[**filesGetFiles**](FilesApi.md#filesGetFiles) | **GET** /api/v2/Files | Get a paged response of file metadata.
[**filesPostFile**](FilesApi.md#filesPostFile) | **POST** /api/v2/Files | Create the metadata for a file before uploading. The State of the File should be &#39;Created&#39;.
[**filesPutFile**](FilesApi.md#filesPutFile) | **PUT** /api/v2/Files/{ID} | Update the metadata for a file. Size may not be modified by the client.
[**filesPutFileContents**](FilesApi.md#filesPutFileContents) | **PUT** /api/v2/Files/{ID}/FileContents | Upload the contents of a file. The current State of the File should be &#39;Created&#39;.



## filesDeleteFile

> filesDeleteFile(ID)

Mark a file as &#39;Removed&#39;. Disables download of the file and hides metadata from GET all method

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.FilesApi();
let ID = "ID_example"; // String | The file's id.
apiInstance.filesDeleteFile(ID, (error, data, response) => {
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
 **ID** | **String**| The file&#39;s id. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## filesGetFile

> GlobalResourcesSharedModelsFileDownload filesGetFile(ID)

Gets a file&#39;s metadata.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.FilesApi();
let ID = "ID_example"; // String | 
apiInstance.filesGetFile(ID, (error, data, response) => {
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
 **ID** | **String**|  | 

### Return type

[**GlobalResourcesSharedModelsFileDownload**](GlobalResourcesSharedModelsFileDownload.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## filesGetFileContents

> Object filesGetFileContents(ID)

Download the contents of a file. The current State of the File should be &#39;Available&#39;.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.FilesApi();
let ID = "ID_example"; // String | The file's metadata.
apiInstance.filesGetFileContents(ID, (error, data, response) => {
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
 **ID** | **String**| The file&#39;s metadata. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## filesGetFiles

> APIIPagedResponseGlobalResourcesSharedModelsFileDownload filesGetFiles(opts)

Get a paged response of file metadata.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.FilesApi();
let opts = {
  'includeDeleted': true, // Boolean | Indicates whether to include files marked as removed.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.filesGetFiles(opts, (error, data, response) => {
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
 **includeDeleted** | **Boolean**| Indicates whether to include files marked as removed. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsFileDownload**](APIIPagedResponseGlobalResourcesSharedModelsFileDownload.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## filesPostFile

> String filesPostFile(globalResourcesSharedModelsFileDownload)

Create the metadata for a file before uploading. The State of the File should be &#39;Created&#39;.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.FilesApi();
let globalResourcesSharedModelsFileDownload = new AgcoApi.GlobalResourcesSharedModelsFileDownload(); // GlobalResourcesSharedModelsFileDownload | The file's metadata.
apiInstance.filesPostFile(globalResourcesSharedModelsFileDownload, (error, data, response) => {
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
 **globalResourcesSharedModelsFileDownload** | [**GlobalResourcesSharedModelsFileDownload**](GlobalResourcesSharedModelsFileDownload.md)| The file&#39;s metadata. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## filesPutFile

> filesPutFile(ID, globalResourcesSharedModelsFileDownload)

Update the metadata for a file. Size may not be modified by the client.

Update the metadata for a file. Size may not be modified by the client.                   Set status to &#39;Available&#39; to publish a file. The file must be uploaded.                  Set status to &#39;Created&#39; to reset a file&#39;s contents and re-upload.                   A file may only be &#39;Removed&#39; by the DELETE method.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.FilesApi();
let ID = "ID_example"; // String | The file's id
let globalResourcesSharedModelsFileDownload = new AgcoApi.GlobalResourcesSharedModelsFileDownload(); // GlobalResourcesSharedModelsFileDownload | The file's metadata
apiInstance.filesPutFile(ID, globalResourcesSharedModelsFileDownload, (error, data, response) => {
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
 **ID** | **String**| The file&#39;s id | 
 **globalResourcesSharedModelsFileDownload** | [**GlobalResourcesSharedModelsFileDownload**](GlobalResourcesSharedModelsFileDownload.md)| The file&#39;s metadata | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## filesPutFileContents

> Object filesPutFileContents(ID)

Upload the contents of a file. The current State of the File should be &#39;Created&#39;.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.FilesApi();
let ID = "ID_example"; // String | The file's metadata.
apiInstance.filesPutFileContents(ID, (error, data, response) => {
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
 **ID** | **String**| The file&#39;s metadata. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

