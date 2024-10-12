# OsfApiv2Documentation.FilesApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filesDetail**](FilesApi.md#filesDetail) | **GET** /files/{file_id}/ | Retrieve a file
[**filesPatch**](FilesApi.md#filesPatch) | **PATCH** /files/{file_id}/ | Update a file
[**filesVersionDetail**](FilesApi.md#filesVersionDetail) | **GET** /files/{file_id}/versions/{version_id}/ | Retrieve a file version
[**filesVersions**](FilesApi.md#filesVersions) | **GET** /files/{file_id}/versions/ | List all file versions



## filesDetail

> [File] filesDetail(fileId)

Retrieve a file

Retrieves the details of a file (or folder) #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested file, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. ### Waterbutler API actions  Files can be modified through the Waterbutler API routes found in &#x60;links&#x60; (&#x60;new_folder&#x60;, &#x60;move&#x60;, &#x60;upload&#x60;, &#x60;download&#x60;, and &#x60;delete&#x60;).  #### Download (files)  To download a file, issue a GET request against the download link. The response will have the Content-Disposition header set, which will will trigger a download in a browser.  #### Create Subfolder (folders)  You can create a subfolder of an existing folder by issuing a PUT request against the new_folder link. The ?kind&#x3D;folder portion of the query parameter is already included in the new_folder link. The name of the new subfolder should be provided in the name query parameter. The response will contain a WaterButler folder entity. If a folder with that name already exists in the parent directory, the server will return a 409 Conflict error response.  #### Upload New File (folders)     To upload a file to a folder, issue a PUT request to the folder&#39;s upload link with the raw file data in the request body, and the kind and name query parameters set to &#39;file&#39; and the desired name of the file. The response will contain a WaterButler file entity that describes the new file. If a file with the same name already exists in the folder, the server will return a 409 Conflict error response.   #### Update Existing File (file)  To update an existing file, issue a PUT request to the file&#39;s upload link with the raw file data in the request body and the kind query parameter set to \&quot;file\&quot;. The update action will create a new version of the file. The response will contain a WaterButler file entity that describes the updated file.  #### Rename (files, folders)  To rename a file or folder, issue a POST request to the move link with the action body parameter set to \&quot;rename\&quot; and the rename body parameter set to the desired name. The response will contain either a folder entity or file entity with the new name.  #### Move &amp; Copy (files, folders)  Move and copy actions both use the same request structure, a POST to the move url, but with different values for the action body parameters. The path parameter is also required and should be the OSF path attribute of the folder being written to. The rename and conflict parameters are optional. If you wish to change the name of the file or folder at its destination, set the rename parameter to the new name. The conflict param governs how name clashes are resolved. Possible values are replace and keep. replace is the default and will overwrite the file that already exists in the target folder. keep will attempt to keep both by adding a suffix to the new file&#39;s name until it no longer conflicts. The suffix will be &#39; (x)&#39; where x is a increasing integer starting from 1. This behavior is intended to mimic that of the OS X Finder. The response will contain either a folder entity or file entity with the new name. Files and folders can also be moved between nodes and providers. The resource parameter is the id of the node under which the file/folder should be moved. It must agree with the path parameter, that is the path must identify a valid folder under the node identified by resource. Likewise, the provider parameter may be used to move the file/folder to another storage provider, but both the resource and path parameters must belong to a node and folder already extant on that provider. Both resource and provider default to the current node and providers. If a moved/copied file is overwriting an existing file, a 200 OK response will be returned. Otherwise, a 201 Created will be returned.  #### Delete (file, folders)  To delete a file or folder send a DELETE request to the delete link. Nothing will be returned in the response body.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.FilesApi();
let fileId = "fileId_example"; // String | The unique identifier of the file you wish to retrieve.
apiInstance.filesDetail(fileId, (error, data, response) => {
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
 **fileId** | **String**| The unique identifier of the file you wish to retrieve. | 

### Return type

**[File]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## filesPatch

> filesPatch(fileId, body)

Update a file

Updates the specified file by setting the values of the parameters passed. Any parameters not provided will be left unchanged. #### Returns Returns JSON with a &#x60;data&#x60; key containing the new representation of the updated file, if the request is successful.  If the request is unsuccessful, JSON with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.FilesApi();
let fileId = "fileId_example"; // String | The unique identifier of the file you wish to update.
let body = {key: null}; // Object | 
apiInstance.filesPatch(fileId, body, (error, data, response) => {
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
 **fileId** | **String**| The unique identifier of the file you wish to update. | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## filesVersionDetail

> [FileVersion] filesVersionDetail(fileId, versionId)

Retrieve a file version

Retrieves the details of a file version #### Returns  Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested file, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.FilesApi();
let fileId = "fileId_example"; // String | The unique identifier of the file from which you want to retrieve versions.
let versionId = "versionId_example"; // String | The file version number you want to retrieve.
apiInstance.filesVersionDetail(fileId, versionId, (error, data, response) => {
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
 **fileId** | **String**| The unique identifier of the file from which you want to retrieve versions. | 
 **versionId** | **String**| The file version number you want to retrieve. | 

### Return type

[**[FileVersion]**](FileVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## filesVersions

> [FileVersion] filesVersions(fileId)

List all file versions

 A paginated list of all file versions. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 file versions. Each resource in the array is a separate file version object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.FilesApi();
let fileId = "fileId_example"; // String | The unique identifier of the file from which you want to retrieve versions.
apiInstance.filesVersions(fileId, (error, data, response) => {
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
 **fileId** | **String**| The unique identifier of the file from which you want to retrieve versions. | 

### Return type

[**[FileVersion]**](FileVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

