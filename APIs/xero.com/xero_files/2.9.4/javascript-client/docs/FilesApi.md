# XeroFilesApi.FilesApi

All URIs are relative to *https://api.xero.com/files.xro/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFileAssociation**](FilesApi.md#createFileAssociation) | **POST** /Files/{FileId}/Associations | Creates a new file association
[**createFolder**](FilesApi.md#createFolder) | **POST** /Folders | Creates a new folder
[**deleteFile**](FilesApi.md#deleteFile) | **DELETE** /Files/{FileId} | Deletes a specific file
[**deleteFileAssociation**](FilesApi.md#deleteFileAssociation) | **DELETE** /Files/{FileId}/Associations/{ObjectId} | Deletes an existing file association
[**deleteFolder**](FilesApi.md#deleteFolder) | **DELETE** /Folders/{FolderId} | Deletes a folder
[**getAssociationsByObject**](FilesApi.md#getAssociationsByObject) | **GET** /Associations/{ObjectId} | Retrieves an association object using a unique object ID
[**getFile**](FilesApi.md#getFile) | **GET** /Files/{FileId} | Retrieves a file by a unique file ID
[**getFileAssociations**](FilesApi.md#getFileAssociations) | **GET** /Files/{FileId}/Associations | Retrieves a specific file associations
[**getFileContent**](FilesApi.md#getFileContent) | **GET** /Files/{FileId}/Content | Retrieves the content of a specific file
[**getFiles**](FilesApi.md#getFiles) | **GET** /Files | Retrieves files
[**getFolder**](FilesApi.md#getFolder) | **GET** /Folders/{FolderId} | Retrieves specific folder by using a unique folder ID
[**getFolders**](FilesApi.md#getFolders) | **GET** /Folders | Retrieves folders
[**getInbox**](FilesApi.md#getInbox) | **GET** /Inbox | Retrieves inbox folder
[**updateFile**](FilesApi.md#updateFile) | **PUT** /Files/{FileId} | Update a file
[**updateFolder**](FilesApi.md#updateFolder) | **PUT** /Folders/{FolderId} | Updates an existing folder
[**uploadFile**](FilesApi.md#uploadFile) | **POST** /Files | Uploads a File



## createFileAssociation

> Association createFileAssociation(xeroTenantId, fileId, opts)

Creates a new file association

By passing in the appropriate options, you can create a new folder

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let fileId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | File id for single object
let opts = {
  'association': { "ObjectId": "1270bf7c-5d18-473a-9231-1e36c4bd33ed", "ObjectGroup": "Contact", "ObjectType": "Business" } // Association | 
};
apiInstance.createFileAssociation(xeroTenantId, fileId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **fileId** | **String**| File id for single object | 
 **association** | [**Association**](Association.md)|  | [optional] 

### Return type

[**Association**](Association.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFolder

> Folder createFolder(xeroTenantId, opts)

Creates a new folder

By passing in the appropriate properties, you can create a new folder

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'folder': { "Name": "My Docs" } // Folder | 
};
apiInstance.createFolder(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **folder** | [**Folder**](Folder.md)|  | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteFile

> deleteFile(xeroTenantId, fileId)

Deletes a specific file

Delete a specific file

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let fileId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | File id for single object
apiInstance.deleteFile(xeroTenantId, fileId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **fileId** | **String**| File id for single object | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteFileAssociation

> deleteFileAssociation(xeroTenantId, fileId, objectId)

Deletes an existing file association

By passing in the appropriate options, you can create a new folder

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let fileId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | File id for single object
let objectId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Object id for single object
apiInstance.deleteFileAssociation(xeroTenantId, fileId, objectId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **fileId** | **String**| File id for single object | 
 **objectId** | **String**| Object id for single object | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteFolder

> deleteFolder(xeroTenantId, folderId)

Deletes a folder

By passing in the appropriate ID, you can delete a folder

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let folderId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Folder id for single object
apiInstance.deleteFolder(xeroTenantId, folderId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **folderId** | **String**| Folder id for single object | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAssociationsByObject

> [Association] getAssociationsByObject(xeroTenantId, objectId)

Retrieves an association object using a unique object ID

By passing in the appropriate options,

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let objectId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Object id for single object
apiInstance.getAssociationsByObject(xeroTenantId, objectId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **objectId** | **String**| Object id for single object | 

### Return type

[**[Association]**](Association.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFile

> FileObject getFile(xeroTenantId, fileId)

Retrieves a file by a unique file ID

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let fileId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | File id for single object
apiInstance.getFile(xeroTenantId, fileId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **fileId** | **String**| File id for single object | 

### Return type

[**FileObject**](FileObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFileAssociations

> [Association] getFileAssociations(xeroTenantId, fileId)

Retrieves a specific file associations

By passing in the appropriate options,  

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let fileId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | File id for single object
apiInstance.getFileAssociations(xeroTenantId, fileId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **fileId** | **String**| File id for single object | 

### Return type

[**[Association]**](Association.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFileContent

> File getFileContent(xeroTenantId, fileId)

Retrieves the content of a specific file

By passing in the appropriate options, retrieve data for specific file

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let fileId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | File id for single object
apiInstance.getFileContent(xeroTenantId, fileId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **fileId** | **String**| File id for single object | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getFiles

> Files getFiles(xeroTenantId, opts)

Retrieves files

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'pagesize': 50, // Number | pass an optional page size value
  'page': 2, // Number | number of records to skip for pagination
  'sort': "CreatedDateUTC DESC" // String | values to sort by
};
apiInstance.getFiles(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **pagesize** | **Number**| pass an optional page size value | [optional] 
 **page** | **Number**| number of records to skip for pagination | [optional] 
 **sort** | **String**| values to sort by | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFolder

> Folder getFolder(xeroTenantId, folderId)

Retrieves specific folder by using a unique folder ID

By passing in the appropriate ID, you can search for specific folder

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let folderId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Folder id for single object
apiInstance.getFolder(xeroTenantId, folderId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **folderId** | **String**| Folder id for single object | 

### Return type

[**Folder**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFolders

> [Folder] getFolders(xeroTenantId, opts)

Retrieves folders

By passing in the appropriate options, you can search for available folders

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'sort': "CreatedDateUTC DESC" // String | values to sort by
};
apiInstance.getFolders(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **sort** | **String**| values to sort by | [optional] 

### Return type

[**[Folder]**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInbox

> Folder getInbox(xeroTenantId)

Retrieves inbox folder

Search for the user inbox

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
apiInstance.getInbox(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**Folder**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFile

> FileObject updateFile(xeroTenantId, fileId, opts)

Update a file

Updates file properties of a single file

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let fileId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | File id for single object
let opts = {
  'fileObject': { "FolderId": "bf924975-7097-46f2-a143-1ecfbab3c8c3" } // FileObject | 
};
apiInstance.updateFile(xeroTenantId, fileId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **fileId** | **String**| File id for single object | 
 **fileObject** | [**FileObject**](FileObject.md)|  | [optional] 

### Return type

[**FileObject**](FileObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateFolder

> Folder updateFolder(xeroTenantId, folderId, folder)

Updates an existing folder

By passing in the appropriate ID and properties, you can update a folder

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let folderId = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Folder id for single object
let folder = { "Name": "Your Docs" }; // Folder | 
apiInstance.updateFolder(xeroTenantId, folderId, folder, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **folderId** | **String**| Folder id for single object | 
 **folder** | [**Folder**](Folder.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadFile

> FileObject uploadFile(xeroTenantId, opts)

Uploads a File

### Example

```javascript
import XeroFilesApi from 'xero_files_api';
let defaultClient = XeroFilesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroFilesApi.FilesApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'folderId': "4ff1e5cc-9835-40d5-bb18-09fdb118db9c", // String | pass an optional folder id to save file to specific folder
  'body': null, // Blob | 
  'filename': "filename_example", // String | 
  'mimeType': "mimeType_example", // String | 
  'name': "name_example" // String | exact name of the file you are uploading
};
apiInstance.uploadFile(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **folderId** | **String**| pass an optional folder id to save file to specific folder | [optional] 
 **body** | **Blob**|  | [optional] 
 **filename** | **String**|  | [optional] 
 **mimeType** | **String**|  | [optional] 
 **name** | **String**| exact name of the file you are uploading | [optional] 

### Return type

[**FileObject**](FileObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

