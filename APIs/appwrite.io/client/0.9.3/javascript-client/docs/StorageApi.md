# Appwrite.StorageApi

All URIs are relative to *https://appwrite.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageCreateFile**](StorageApi.md#storageCreateFile) | **POST** /storage/files | Create File
[**storageDeleteFile**](StorageApi.md#storageDeleteFile) | **DELETE** /storage/files/{fileId} | Delete File
[**storageGetFile**](StorageApi.md#storageGetFile) | **GET** /storage/files/{fileId} | Get File
[**storageGetFileDownload**](StorageApi.md#storageGetFileDownload) | **GET** /storage/files/{fileId}/download | Get File for Download
[**storageGetFilePreview**](StorageApi.md#storageGetFilePreview) | **GET** /storage/files/{fileId}/preview | Get File Preview
[**storageGetFileView**](StorageApi.md#storageGetFileView) | **GET** /storage/files/{fileId}/view | Get File for View
[**storageListFiles**](StorageApi.md#storageListFiles) | **GET** /storage/files | List Files
[**storageUpdateFile**](StorageApi.md#storageUpdateFile) | **PUT** /storage/files/{fileId} | Update File



## storageCreateFile

> File storageCreateFile(file, opts)

Create File

Create a new file. The user who creates the file will automatically be assigned to read and write access unless he has passed custom values for read and write arguments.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.StorageApi();
let file = "file_example"; // String | Binary file.
let opts = {
  'read': ["null"], // [String] | An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
  'write': ["null"] // [String] | An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
};
apiInstance.storageCreateFile(file, opts, (error, data, response) => {
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
 **file** | **String**| Binary file. | 
 **read** | [**[String]**](String.md)| An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions. | [optional] 
 **write** | [**[String]**](String.md)| An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions. | [optional] 

### Return type

**File**

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## storageDeleteFile

> storageDeleteFile(fileId)

Delete File

Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.StorageApi();
let fileId = "fileId_example"; // String | File unique ID.
apiInstance.storageDeleteFile(fileId, (error, data, response) => {
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
 **fileId** | **String**| File unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageGetFile

> File storageGetFile(fileId)

Get File

Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.StorageApi();
let fileId = "fileId_example"; // String | File unique ID.
apiInstance.storageGetFile(fileId, (error, data, response) => {
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
 **fileId** | **String**| File unique ID. | 

### Return type

**File**

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageGetFileDownload

> storageGetFileDownload(fileId)

Get File for Download

Get a file content by its unique ID. The endpoint response return with a &#39;Content-Disposition: attachment&#39; header that tells the browser to start downloading the file to user downloads directory.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.StorageApi();
let fileId = "fileId_example"; // String | File unique ID.
apiInstance.storageGetFileDownload(fileId, (error, data, response) => {
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
 **fileId** | **String**| File unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageGetFilePreview

> storageGetFilePreview(fileId, opts)

Get File Preview

Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.StorageApi();
let fileId = "fileId_example"; // String | File unique ID
let opts = {
  'width': 0, // Number | Resize preview image width, Pass an integer between 0 to 4000.
  'height': 0, // Number | Resize preview image height, Pass an integer between 0 to 4000.
  'gravity': "'center'", // String | Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right
  'quality': 100, // Number | Preview image quality. Pass an integer between 0 to 100. Defaults to 100.
  'borderWidth': 0, // Number | Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.
  'borderColor': "''", // String | Preview image border color. Use a valid HEX color, no # is needed for prefix.
  'borderRadius': 0, // Number | Preview image border radius in pixels. Pass an integer between 0 to 4000.
  'opacity': 1, // Number | Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.
  'rotation': 0, // Number | Preview image rotation in degrees. Pass an integer between 0 and 360.
  'background': "''", // String | Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.
  'output': "''" // String | Output format type (jpeg, jpg, png, gif and webp).
};
apiInstance.storageGetFilePreview(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| File unique ID | 
 **width** | **Number**| Resize preview image width, Pass an integer between 0 to 4000. | [optional] [default to 0]
 **height** | **Number**| Resize preview image height, Pass an integer between 0 to 4000. | [optional] [default to 0]
 **gravity** | **String**| Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right | [optional] [default to &#39;center&#39;]
 **quality** | **Number**| Preview image quality. Pass an integer between 0 to 100. Defaults to 100. | [optional] [default to 100]
 **borderWidth** | **Number**| Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0. | [optional] [default to 0]
 **borderColor** | **String**| Preview image border color. Use a valid HEX color, no # is needed for prefix. | [optional] [default to &#39;&#39;]
 **borderRadius** | **Number**| Preview image border radius in pixels. Pass an integer between 0 to 4000. | [optional] [default to 0]
 **opacity** | **Number**| Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1. | [optional] [default to 1]
 **rotation** | **Number**| Preview image rotation in degrees. Pass an integer between 0 and 360. | [optional] [default to 0]
 **background** | **String**| Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix. | [optional] [default to &#39;&#39;]
 **output** | **String**| Output format type (jpeg, jpg, png, gif and webp). | [optional] [default to &#39;&#39;]

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageGetFileView

> storageGetFileView(fileId)

Get File for View

Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  &#39;Content-Disposition: attachment&#39; header.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.StorageApi();
let fileId = "fileId_example"; // String | File unique ID.
apiInstance.storageGetFileView(fileId, (error, data, response) => {
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
 **fileId** | **String**| File unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageListFiles

> FileList storageListFiles(opts)

List Files

Get a list of all the user files. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s files. [Learn more about different API modes](/docs/admin).

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.StorageApi();
let opts = {
  'search': "''", // String | Search term to filter your list results. Max length: 256 chars.
  'limit': 25, // Number | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
  'offset': 0, // Number | Results offset. The default value is 0. Use this param to manage pagination.
  'orderType': "'ASC'" // String | Order result by ASC or DESC order.
};
apiInstance.storageListFiles(opts, (error, data, response) => {
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
 **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to &#39;&#39;]
 **limit** | **Number**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25]
 **offset** | **Number**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0]
 **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to &#39;ASC&#39;]

### Return type

[**FileList**](FileList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageUpdateFile

> File storageUpdateFile(fileId, opts)

Update File

Update a file by its unique ID. Only users with write permissions have access to update this resource.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.StorageApi();
let fileId = "fileId_example"; // String | File unique ID.
let opts = {
  'storageUpdateFileRequest': new Appwrite.StorageUpdateFileRequest() // StorageUpdateFileRequest | 
};
apiInstance.storageUpdateFile(fileId, opts, (error, data, response) => {
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
 **fileId** | **String**| File unique ID. | 
 **storageUpdateFileRequest** | [**StorageUpdateFileRequest**](StorageUpdateFileRequest.md)|  | [optional] 

### Return type

**File**

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

