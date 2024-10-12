# ExaVault.ResourcesApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFolder**](ResourcesApi.md#addFolder) | **POST** /resources | Create a folder
[**compressFiles**](ResourcesApi.md#compressFiles) | **POST** /resources/compress | Compress resources
[**copyResources**](ResourcesApi.md#copyResources) | **POST** /resources/copy | Copy resources
[**deleteResourceById**](ResourcesApi.md#deleteResourceById) | **DELETE** /resources/{id} | Delete a Resource
[**deleteResources**](ResourcesApi.md#deleteResources) | **DELETE** /resources | Delete Resources
[**download**](ResourcesApi.md#download) | **GET** /resources/download | Download a file
[**extractFiles**](ResourcesApi.md#extractFiles) | **POST** /resources/extract | Extract resources
[**getPreviewImage**](ResourcesApi.md#getPreviewImage) | **GET** /resources/preview | Preview a file
[**getResourceInfo**](ResourcesApi.md#getResourceInfo) | **GET** /resources | Get Resource Properties
[**getResourceInfoById**](ResourcesApi.md#getResourceInfoById) | **GET** /resources/{id} | Get resource metadata
[**listResourceContents**](ResourcesApi.md#listResourceContents) | **GET** /resources/list/{id} | List contents of folder
[**listResources**](ResourcesApi.md#listResources) | **GET** /resources/list | Get a list of all resources
[**moveResources**](ResourcesApi.md#moveResources) | **POST** /resources/move | Move resources
[**updateResourceById**](ResourcesApi.md#updateResourceById) | **PATCH** /resources/{id} | Rename a resource.
[**uploadFile**](ResourcesApi.md#uploadFile) | **POST** /resources/upload | Upload a file



## addFolder

> ResourceResponse addFolder(evApiKey, evAccessToken, opts)

Create a folder

Create a new empty folder at the specified path. New files can be uploaded via the [/resources/upload](#operation/uploadFile) endpoint.  **Notes:** - Authenticated user should have modify permission. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'addFolderRequestBody': {"path":"/exavault/exampleFile.txt"} // AddFolderRequestBody | 
};
apiInstance.addFolder(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **addFolderRequestBody** | [**AddFolderRequestBody**](AddFolderRequestBody.md)|  | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## compressFiles

> ResourceResponse compressFiles(evApiKey, evAccessToken, opts)

Compress resources

Create a zip archive containing the files from given set of paths. Note that this can be a very slow operation if you have indicated many files should be included in the archive.  **Notes:** - Authenticated user should have modify permission. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'compressFilesRequestBody': {"archiveName":"exampleFiles.zip","parentResource":"/exavault","resources":["exampleFile1.txt","exampleFile2.txt","id:234222"]} // CompressFilesRequestBody | 
};
apiInstance.compressFiles(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **compressFilesRequestBody** | [**CompressFilesRequestBody**](CompressFilesRequestBody.md)|  | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## copyResources

> ResourceCopyMove copyResources(evApiKey, evAccessToken, opts)

Copy resources

Copies a set of exisiting files/folders (provided by an array &#x60;resources&#x60;) to the requested &#x60;parentResource&#x60; in your account. In the &#x60;resources&#x60; array, you may specify paths pointing files/folders throughout the account, but everything will be copied to the  root of the &#x60;parentResource&#x60;.  **Notes:** - Authenticated user should have modify permission. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'copyResourcesRequestBody': {"parentResource":"/exavault/exampleFileFolder","resources":["/exavault/exampleFile.txt","/exavault/otherFile.txt","id:28282828"]} // CopyResourcesRequestBody | 
};
apiInstance.copyResources(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **copyResourcesRequestBody** | [**CopyResourcesRequestBody**](CopyResourcesRequestBody.md)|  | [optional] 

### Return type

[**ResourceCopyMove**](ResourceCopyMove.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteResourceById

> EmptyResponse deleteResourceById(id, evApiKey, evAccessToken)

Delete a Resource

Delete a single file or folder resource. Deleting a folder will also delete all of the contents.  **Notes:** - Authenticated user should have [delete permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - There is no way to un-delete a deleted resource. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let id = 789; // Number | ID number of the resource
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
apiInstance.deleteResourceById(id, evApiKey, evAccessToken, (error, data, response) => {
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
 **id** | **Number**| ID number of the resource | 
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteResources

> EmptyResponse deleteResources(evApiKey, evAccessToken, opts)

Delete Resources

Delete multiple file or folder resourcess. Deleting a folder resource will also delete any resources in that folder.  **Notes:** - Authenticated user should have [delete permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - It is not possible to un-delete a deleted resource. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
let evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
let opts = {
  'deleteResourcesRequestBody': {"resources":["exampleFile1.txt","exampleFile2.txt"]} // DeleteResourcesRequestBody | 
};
apiInstance.deleteResources(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key | 
 **evAccessToken** | **String**| Access Token | 
 **deleteResourcesRequestBody** | [**DeleteResourcesRequestBody**](DeleteResourcesRequestBody.md)|  | [optional] 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## download

> File download(evApiKey, evAccessToken, resources, opts)

Download a file

Downloads a file from the server. Whenever more than one file is being downloaded, the file are first zipped into  a single file before the download starts, and the resulting zip file is named to match the &#x60;downloadArchiveName&#x60; parameter.  **NOTE**: Downloading many files at once  may result in a long delay before the API will return a response. You may need to override default timeout values in your API client, or download files individually.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let resources = ["null"]; // [String] | Path of file or folder to be downloaded, starting from the root. Can also be an array of paths.
let opts = {
  'downloadArchiveName': "downloadArchiveName_example" // String | When downloading multiple files, this will be used as the name of the zip file that is created.
};
apiInstance.download(evApiKey, evAccessToken, resources, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **resources** | [**[String]**](String.md)| Path of file or folder to be downloaded, starting from the root. Can also be an array of paths. | 
 **downloadArchiveName** | **String**| When downloading multiple files, this will be used as the name of the zip file that is created. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/zip


## extractFiles

> ResourceCollectionResponse extractFiles(evApiKey, evAccessToken, opts)

Extract resources

Extract the contents of a zip archive to a specified directory. Note that this can be a very slow operation.  **Notes:** - You must have  [modify permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to do this. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'extractFilesRequestBody': {"parentResource":"/extractFolder","resource":"/exavault/exampleFiles.zip"} // ExtractFilesRequestBody | 
};
apiInstance.extractFiles(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **extractFilesRequestBody** | [**ExtractFilesRequestBody**](ExtractFilesRequestBody.md)|  | [optional] 

### Return type

[**ResourceCollectionResponse**](ResourceCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPreviewImage

> PreviewFileResponse getPreviewImage(evApiKey, evAccessToken, resource, size, opts)

Preview a file

Returns a resized image of the specified document for supported file types.  Image data returned is encoded in base64 format and can be viewed using the &#x60;&lt;img&gt;&#x60; element.   &#x60;&#x60;&#x60;&lt;img src&#x3D;&#39;data:image/jpeg;base64&#39; + meta.image/&gt;&#x60;&#x60;&#x60;  **Notes:** - Supported files types are &#x60;&#39;jpg&#39;&#x60;, &#x60;&#39;jpeg&#39;&#x60;, &#x60;&#39;gif&#39;&#x60;, &#x60;&#39;png&#39;&#x60;, &#x60;&#39;bmp&#39;&#x60;, &#x60;&#39;pdf&#39;&#x60;, &#x60;&#39;psd&#39;&#x60;, &#x60;&#39;doc&#39;&#x60; 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
let evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
let resource = "resource_example"; // String | Resource identifier for the image file.
let size = "size_example"; // String | The size of the image.
let opts = {
  'width': 56, // Number | Overrides sizes. Sets to a specific width.
  'height': 56, // Number | Overrides sizes. Sets to a specific height.
  'page': 0 // Number | Page number to extract from a multi-page document (0 is the first page). Vaild for **.pdf** or **.doc** files.
};
apiInstance.getPreviewImage(evApiKey, evAccessToken, resource, size, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key | 
 **evAccessToken** | **String**| Access Token | 
 **resource** | **String**| Resource identifier for the image file. | 
 **size** | **String**| The size of the image. | 
 **width** | **Number**| Overrides sizes. Sets to a specific width. | [optional] 
 **height** | **Number**| Overrides sizes. Sets to a specific height. | [optional] 
 **page** | **Number**| Page number to extract from a multi-page document (0 is the first page). Vaild for **.pdf** or **.doc** files. | [optional] [default to 0]

### Return type

[**PreviewFileResponse**](PreviewFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResourceInfo

> ResourceResponse getResourceInfo(evApiKey, evAccessToken, resource, opts)

Get Resource Properties

Returns details for specified file/folder id or hash, including upload date, size and type. For the full list of returned properties, see the response syntax, below.  **Notes:** - Authenticated user should have list permission. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let resource = "resource_example"; // String | Resource identifier of the file or folder to get metadata for.
let opts = {
  'include': "include_example" // String | Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**.
};
apiInstance.getResourceInfo(evApiKey, evAccessToken, resource, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **resource** | **String**| Resource identifier of the file or folder to get metadata for. | 
 **include** | **String**| Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**. | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResourceInfoById

> ResourceResponse getResourceInfoById(id, evApiKey, evAccessToken, opts)

Get resource metadata

Returns metadata for specified file/folder path, including upload date, size and type. For the full list of returned properties, see the response syntax, below.  **Notes:** - Authenticated user should have list permission. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let id = 789; // Number | ID number of the resource
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'include': "include_example" // String | Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**.
};
apiInstance.getResourceInfoById(id, evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **id** | **Number**| ID number of the resource | 
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **include** | **String**| Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**. | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listResourceContents

> ResourceCollectionResponse listResourceContents(evApiKey, evAccessToken, id, opts)

List contents of folder

Returns a list of files/folders for the parent resource ID.   You can use this API call to get information about all files and folders at a specified path. By default, the API returns basic metadata on each file/folder. An optional &#x60;include&#x60; parameter forces the return of additional metadata. As with all API calls, the path should be the full path relative to the user&#39;s home directory (e.g. **_/myfiles/some_folder**).  **Notes:** - Authenticated user should have list permission. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call. 
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let id = 789; // Number | ID of the parent resource to get a list of resources for.
let opts = {
  'sort': "name", // String | Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.
  'offset': 0, // Number | Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list.
  'limit': 56, // Number | The number of files to limit the result. Cannot be set higher than 100. If you have more than one hundred files in your directory, make multiple calls, incrementing the `offset parameter, above.
  'type': "type_example", // String | Limit types of resources returned to \"file\" or \"dir\" only.
  'include': "include_example" // String | Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**.
};
apiInstance.listResourceContents(evApiKey, evAccessToken, id, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call.  | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **id** | **Number**| ID of the parent resource to get a list of resources for. | 
 **sort** | **String**| Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending. | [optional] 
 **offset** | **Number**| Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list. | [optional] [default to 0]
 **limit** | **Number**| The number of files to limit the result. Cannot be set higher than 100. If you have more than one hundred files in your directory, make multiple calls, incrementing the &#x60;offset parameter, above. | [optional] 
 **type** | **String**| Limit types of resources returned to \&quot;file\&quot; or \&quot;dir\&quot; only. | [optional] 
 **include** | **String**| Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**. | [optional] 

### Return type

[**ResourceCollectionResponse**](ResourceCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listResources

> ResourceCollectionResponse listResources(evApiKey, evAccessToken, resource, opts)

Get a list of all resources

Returns a list of files and folders in the account. Use the &#x60;resource&#x60; query parameter to indicate the folder you wish to search in (which can be /).   **Searching for Files and Folders**  Using the &#x60;name&#x60; parameter triggers search mode, which will search the entire directory structure under the provided &#x60;resource&#x60; for files or folders with names matching the provided &#x60;name&#x60;. This supports wildcard matching such as:  - \\*Report\\* would find any files or folders with \&quot;Report\&quot; in the name. - Data\\_202?-09-30.xlsx would match items such as \&quot;Data\\_2020-09-30.xlsx\&quot;, \&quot;DATA\\_2021-09-30.xlsx\&quot;, \&quot;data\\_2022-09-30.xlsx\&quot; etc. - sales\\* would find any files or folders starting with the word \&quot;Sales\&quot; - \\*.csv would locate any files ending in \&quot;.csv\&quot; - \\* matches everything within the directory tree starting at your given &#x60;resource&#x60;  The search is not case-sensitive. Searching for Clients\\* or clients\\* or CLIENTS\\*, etc. will provide identical results  If you are using the &#x60;name&#x60; parameter to run a search, the &#x60;type&#x60; parameter will be ignored by the server.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let resource = "resource_example"; // String | Resource identifier to get resources for. Can be path/id/name.
let opts = {
  'sort': "name", // String | Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.
  'offset': 0, // Number | Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list. e.g, setting `offset=200` would trigger the server to skip the first 200 matching entries when returning the results.
  'limit': 56, // Number | The number of files to limit the result. If you have more files in your directory than this limit, make multiple calls, incrementing the `offset` parameter, above.
  'type': "type_example", // String | Limit types of resources returned to \"file\" or \"dir\" only. This is ignored if you are using the `name` parameter to trigger a search.
  'name': "name_example", // String | Text to match resource names. This allows you to filter the results returned. For example, to locate only zip archive files, you can enter `*zip` and only resources ending in \"zip\" will be included in the list of results.
  'include': "include_example" // String | Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**.
};
apiInstance.listResources(evApiKey, evAccessToken, resource, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **resource** | **String**| Resource identifier to get resources for. Can be path/id/name. | 
 **sort** | **String**| Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending. | [optional] 
 **offset** | **Number**| Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list. e.g, setting &#x60;offset&#x3D;200&#x60; would trigger the server to skip the first 200 matching entries when returning the results. | [optional] [default to 0]
 **limit** | **Number**| The number of files to limit the result. If you have more files in your directory than this limit, make multiple calls, incrementing the &#x60;offset&#x60; parameter, above. | [optional] 
 **type** | **String**| Limit types of resources returned to \&quot;file\&quot; or \&quot;dir\&quot; only. This is ignored if you are using the &#x60;name&#x60; parameter to trigger a search. | [optional] 
 **name** | **String**| Text to match resource names. This allows you to filter the results returned. For example, to locate only zip archive files, you can enter &#x60;*zip&#x60; and only resources ending in \&quot;zip\&quot; will be included in the list of results. | [optional] 
 **include** | **String**| Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**. | [optional] 

### Return type

[**ResourceCollectionResponse**](ResourceCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## moveResources

> ResourceCopyMove moveResources(evApiKey, evAccessToken, opts)

Move resources

Moves a set of exisiting files/folders (provided by an array &#x60;resources&#x60;) to the requested &#x60;parentResource&#x60; in your account. In the &#x60;resources&#x60; array, you may specify paths pointing files/folders throughout the account, but everything will be moved to the root of the &#x60;parentResource&#x60;.  **Notes:** - Authenticated user should have modify permission. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'moveResourcesRequestBody': {"parentResource":"/copyhere","resources":["/testone.jpg","/folder"]} // MoveResourcesRequestBody | 
};
apiInstance.moveResources(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **moveResourcesRequestBody** | [**MoveResourcesRequestBody**](MoveResourcesRequestBody.md)|  | [optional] 

### Return type

[**ResourceCopyMove**](ResourceCopyMove.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateResourceById

> ResourceResponse updateResourceById(id, evAccessToken, evApiKey, opts)

Rename a resource.

Update the specified file or folder resource record&#39;s \&quot;name\&quot; parameter. The resource is identified by the numeric resource ID that is passed in as the last segment of the URI. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let id = 789; // Number | ID number of the resource
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let opts = {
  'updateResourceByIdRequestBody': {"name":"my-renamed-file.txt"} // UpdateResourceByIdRequestBody | 
};
apiInstance.updateResourceById(id, evAccessToken, evApiKey, opts, (error, data, response) => {
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
 **id** | **Number**| ID number of the resource | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **updateResourceByIdRequestBody** | [**UpdateResourceByIdRequestBody**](UpdateResourceByIdRequestBody.md)|  | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadFile

> ResourceResponse uploadFile(evApiKey, evAccessToken, path, fileSize, opts)

Upload a file

Uploads a file to a specified path, with optional support for resuming a partially uploaded existing file. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.ResourcesApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let path = "path_example"; // String | Destination path for the file being uploaded, including the file name.
let fileSize = 2935; // Number | File size, in bits, of the file being uploaded.
let opts = {
  'offsetBytes': 4852, // Number | Allows a file upload to resume at a certain number of bytes.
  'resume': true, // Boolean | True if upload resume is supported, false if it isn't. 
  'allowOverwrite': true, // Boolean | True if a file with the same name is found in the designated path, should be overwritten. False if different file names should be generated. 
  'file': "/path/to/file" // File | 
};
apiInstance.uploadFile(evApiKey, evAccessToken, path, fileSize, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **path** | **String**| Destination path for the file being uploaded, including the file name. | 
 **fileSize** | **Number**| File size, in bits, of the file being uploaded. | 
 **offsetBytes** | **Number**| Allows a file upload to resume at a certain number of bytes. | [optional] 
 **resume** | **Boolean**| True if upload resume is supported, false if it isn&#39;t.  | [optional] [default to true]
 **allowOverwrite** | **Boolean**| True if a file with the same name is found in the designated path, should be overwritten. False if different file names should be generated.  | [optional] [default to false]
 **file** | **File**|  | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

