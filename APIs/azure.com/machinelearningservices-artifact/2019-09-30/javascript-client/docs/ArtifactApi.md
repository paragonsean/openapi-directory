# Artifact.ArtifactApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifactsBatchCreateEmptyArtifacts**](ArtifactApi.md#artifactsBatchCreateEmptyArtifacts) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/batch/metadata | Create a batch of empty Artifacts.
[**artifactsBatchGetById**](ArtifactApi.md#artifactsBatchGetById) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/batch/metadata | Get Batch Artifacts by Ids.
[**artifactsBatchGetStorageById**](ArtifactApi.md#artifactsBatchGetStorageById) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/storageuri/batch/metadata | Get Batch Artifacts storage by Ids.
[**artifactsBatchIngestFromSas**](ArtifactApi.md#artifactsBatchIngestFromSas) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/batch/ingest/containersas | Batch ingest using shared access signature.
[**artifactsCreate**](ArtifactApi.md#artifactsCreate) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/metadata | Create Artifact.
[**artifactsDeleteBatchMetaData**](ArtifactApi.md#artifactsDeleteBatchMetaData) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/batch/metadata:delete | Delete Batch of Artifact Metadata.
[**artifactsDeleteMetaData**](ArtifactApi.md#artifactsDeleteMetaData) | **DELETE** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/metadata | Delete Artifact Metadata.
[**artifactsDeleteMetaDataInContainer**](ArtifactApi.md#artifactsDeleteMetaDataInContainer) | **DELETE** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/batch | Delete Artifact Metadata.
[**artifactsDownload**](ArtifactApi.md#artifactsDownload) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/content | Get Artifact content by Id.
[**artifactsGet**](ArtifactApi.md#artifactsGet) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/metadata | Get Artifact metadata by Id.
[**artifactsGetContentInformation**](ArtifactApi.md#artifactsGetContentInformation) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/contentinfo | Get Artifact content information.
[**artifactsGetSas**](ArtifactApi.md#artifactsGetSas) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/write | Get writable shared access signature for Artifact.
[**artifactsGetStorageContentInformation**](ArtifactApi.md#artifactsGetStorageContentInformation) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/contentinfo/storageuri | Get Artifact storage content information.
[**artifactsListInContainer**](ArtifactApi.md#artifactsListInContainer) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container} | Get Artifacts metadata in a container or path.
[**artifactsListSasByPrefix**](ArtifactApi.md#artifactsListSasByPrefix) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/prefix/contentinfo | Get shared access signature for an Artifact
[**artifactsListStorageUriByPrefix**](ArtifactApi.md#artifactsListStorageUriByPrefix) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/prefix/contentinfo/storageuri | Get storage Uri for Artifacts in a path.
[**artifactsRegister**](ArtifactApi.md#artifactsRegister) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/register | Create an Artifact for an existing data location.
[**artifactsUpload**](ArtifactApi.md#artifactsUpload) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/content | Upload Artifact content.



## artifactsBatchCreateEmptyArtifacts

> BatchArtifactContentInformationResult artifactsBatchCreateEmptyArtifacts(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactPaths)

Create a batch of empty Artifacts.

Create a Batch of empty Artifacts from the supplied paths.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let artifactPaths = new Artifact.ArtifactPathList(); // ArtifactPathList | The list of Artifact paths to create.
apiInstance.artifactsBatchCreateEmptyArtifacts(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactPaths, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **artifactPaths** | [**ArtifactPathList**](ArtifactPathList.md)| The list of Artifact paths to create. | 

### Return type

[**BatchArtifactContentInformationResult**](BatchArtifactContentInformationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsBatchGetById

> BatchArtifactContentInformationResult artifactsBatchGetById(subscriptionId, resourceGroupName, workspaceName, artifactIds)

Get Batch Artifacts by Ids.

Get Batch Artifacts by the specific Ids.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let artifactIds = new Artifact.ArtifactIdList(); // ArtifactIdList | The command for Batch Artifact get request.
apiInstance.artifactsBatchGetById(subscriptionId, resourceGroupName, workspaceName, artifactIds, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **artifactIds** | [**ArtifactIdList**](ArtifactIdList.md)| The command for Batch Artifact get request. | 

### Return type

[**BatchArtifactContentInformationResult**](BatchArtifactContentInformationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsBatchGetStorageById

> BatchArtifactContentInformationResult artifactsBatchGetStorageById(subscriptionId, resourceGroupName, workspaceName, artifactIds)

Get Batch Artifacts storage by Ids.

Get Batch Artifacts storage by specific Ids.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let artifactIds = new Artifact.ArtifactIdList(); // ArtifactIdList | The list of artifactIds to get.
apiInstance.artifactsBatchGetStorageById(subscriptionId, resourceGroupName, workspaceName, artifactIds, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **artifactIds** | [**ArtifactIdList**](ArtifactIdList.md)| The list of artifactIds to get. | 

### Return type

[**BatchArtifactContentInformationResult**](BatchArtifactContentInformationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsBatchIngestFromSas

> PaginatedArtifactList artifactsBatchIngestFromSas(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactContainerSas)

Batch ingest using shared access signature.

Ingest Batch Artifacts using shared access signature.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let artifactContainerSas = new Artifact.ArtifactContainerSas(); // ArtifactContainerSas | The artifact container shared access signature to use for batch ingest.
apiInstance.artifactsBatchIngestFromSas(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactContainerSas, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **artifactContainerSas** | [**ArtifactContainerSas**](ArtifactContainerSas.md)| The artifact container shared access signature to use for batch ingest. | 

### Return type

[**PaginatedArtifactList**](PaginatedArtifactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsCreate

> Artifact artifactsCreate(subscriptionId, resourceGroupName, workspaceName, artifact)

Create Artifact.

Create an Artifact.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let artifact = new Artifact.Artifact(); // Artifact | The Artifact details.
apiInstance.artifactsCreate(subscriptionId, resourceGroupName, workspaceName, artifact, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **artifact** | [**Artifact**](Artifact.md)| The Artifact details. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsDeleteBatchMetaData

> artifactsDeleteBatchMetaData(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactPaths, opts)

Delete Batch of Artifact Metadata.

Delete a Batch of Artifact Metadata.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let artifactPaths = new Artifact.ArtifactPathList(); // ArtifactPathList | The list of Artifact paths to delete.
let opts = {
  'hardDelete': false // Boolean | If set to true, the delete cannot be reverted at a later time.
};
apiInstance.artifactsDeleteBatchMetaData(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactPaths, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **artifactPaths** | [**ArtifactPathList**](ArtifactPathList.md)| The list of Artifact paths to delete. | 
 **hardDelete** | **Boolean**| If set to true, the delete cannot be reverted at a later time. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsDeleteMetaData

> artifactsDeleteMetaData(subscriptionId, resourceGroupName, workspaceName, origin, container, opts)

Delete Artifact Metadata.

Delete an Artifact Metadata.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let opts = {
  'path': "path_example", // String | The Artifact Path.
  'hardDelete': false // Boolean | If set to true. The delete cannot be revert at later time.
};
apiInstance.artifactsDeleteMetaData(subscriptionId, resourceGroupName, workspaceName, origin, container, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **path** | **String**| The Artifact Path. | [optional] 
 **hardDelete** | **Boolean**| If set to true. The delete cannot be revert at later time. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsDeleteMetaDataInContainer

> artifactsDeleteMetaDataInContainer(subscriptionId, resourceGroupName, workspaceName, origin, container, opts)

Delete Artifact Metadata.

Delete Artifact Metadata in a specific container.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let opts = {
  'hardDelete': false // Boolean | If set to true. The delete cannot be revert at later time.
};
apiInstance.artifactsDeleteMetaDataInContainer(subscriptionId, resourceGroupName, workspaceName, origin, container, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **hardDelete** | **Boolean**| If set to true. The delete cannot be revert at later time. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsDownload

> File artifactsDownload(subscriptionId, resourceGroupName, workspaceName, origin, container, opts)

Get Artifact content by Id.

Get Artifact content of a specific Id.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let opts = {
  'path': "path_example" // String | The Artifact Path.
};
apiInstance.artifactsDownload(subscriptionId, resourceGroupName, workspaceName, origin, container, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **path** | **String**| The Artifact Path. | [optional] 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## artifactsGet

> Artifact artifactsGet(subscriptionId, resourceGroupName, workspaceName, origin, container, path)

Get Artifact metadata by Id.

Get Artifact metadata for a specific Id.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let path = "path_example"; // String | The Artifact Path.
apiInstance.artifactsGet(subscriptionId, resourceGroupName, workspaceName, origin, container, path, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **path** | **String**| The Artifact Path. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsGetContentInformation

> ArtifactContentInformation artifactsGetContentInformation(subscriptionId, resourceGroupName, workspaceName, origin, container, opts)

Get Artifact content information.

Get content information of an Artifact.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let opts = {
  'path': "path_example" // String | The Artifact Path.
};
apiInstance.artifactsGetContentInformation(subscriptionId, resourceGroupName, workspaceName, origin, container, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **path** | **String**| The Artifact Path. | [optional] 

### Return type

[**ArtifactContentInformation**](ArtifactContentInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsGetSas

> ArtifactContentInformation artifactsGetSas(subscriptionId, resourceGroupName, workspaceName, origin, container, opts)

Get writable shared access signature for Artifact.

Get writable shared access signature for a specific Artifact.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let opts = {
  'path': "path_example" // String | The Artifact Path.
};
apiInstance.artifactsGetSas(subscriptionId, resourceGroupName, workspaceName, origin, container, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **path** | **String**| The Artifact Path. | [optional] 

### Return type

[**ArtifactContentInformation**](ArtifactContentInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsGetStorageContentInformation

> ArtifactContentInformation artifactsGetStorageContentInformation(subscriptionId, resourceGroupName, workspaceName, origin, container, opts)

Get Artifact storage content information.

Get storage content information of an Artifact.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let opts = {
  'path': "path_example" // String | The Artifact Path.
};
apiInstance.artifactsGetStorageContentInformation(subscriptionId, resourceGroupName, workspaceName, origin, container, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **path** | **String**| The Artifact Path. | [optional] 

### Return type

[**ArtifactContentInformation**](ArtifactContentInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsListInContainer

> PaginatedArtifactList artifactsListInContainer(subscriptionId, resourceGroupName, workspaceName, origin, container, opts)

Get Artifacts metadata in a container or path.

Get Artifacts metadata in a specific container or path.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let opts = {
  'path': "path_example", // String | The Artifact Path.
  'continuationToken': "continuationToken_example" // String | The continuation token.
};
apiInstance.artifactsListInContainer(subscriptionId, resourceGroupName, workspaceName, origin, container, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **path** | **String**| The Artifact Path. | [optional] 
 **continuationToken** | **String**| The continuation token. | [optional] 

### Return type

[**PaginatedArtifactList**](PaginatedArtifactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsListSasByPrefix

> PaginatedArtifactContentInformationList artifactsListSasByPrefix(subscriptionId, resourceGroupName, workspaceName, origin, container, opts)

Get shared access signature for an Artifact

Get shared access signature for an Artifact in specific path.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let opts = {
  'path': "path_example", // String | The Artifact Path.
  'continuationToken': "continuationToken_example" // String | The continuation token.
};
apiInstance.artifactsListSasByPrefix(subscriptionId, resourceGroupName, workspaceName, origin, container, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **path** | **String**| The Artifact Path. | [optional] 
 **continuationToken** | **String**| The continuation token. | [optional] 

### Return type

[**PaginatedArtifactContentInformationList**](PaginatedArtifactContentInformationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsListStorageUriByPrefix

> PaginatedArtifactContentInformationList artifactsListStorageUriByPrefix(subscriptionId, resourceGroupName, workspaceName, origin, container, opts)

Get storage Uri for Artifacts in a path.

Get storage Uri for Artifacts in a specific path.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let opts = {
  'path': "path_example", // String | The Artifact Path.
  'continuationToken': "continuationToken_example" // String | The continuation token.
};
apiInstance.artifactsListStorageUriByPrefix(subscriptionId, resourceGroupName, workspaceName, origin, container, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **path** | **String**| The Artifact Path. | [optional] 
 **continuationToken** | **String**| The continuation token. | [optional] 

### Return type

[**PaginatedArtifactContentInformationList**](PaginatedArtifactContentInformationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsRegister

> Artifact artifactsRegister(subscriptionId, resourceGroupName, workspaceName, artifact)

Create an Artifact for an existing data location.

Create an Artifact for an existing dataPath.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let artifact = new Artifact.Artifact(); // Artifact | The Artifact creation details.
apiInstance.artifactsRegister(subscriptionId, resourceGroupName, workspaceName, artifact, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **artifact** | [**Artifact**](Artifact.md)| The Artifact creation details. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsUpload

> Artifact artifactsUpload(subscriptionId, resourceGroupName, workspaceName, origin, container, content, opts)

Upload Artifact content.

Upload content to an Artifact.

### Example

```javascript
import Artifact from 'artifact';
let defaultClient = Artifact.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Artifact.ArtifactApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
let workspaceName = "workspaceName_example"; // String | The name of the workspace.
let origin = "origin_example"; // String | The origin of the Artifact.
let container = "container_example"; // String | The container name.
let content = "/path/to/file"; // File | The file upload.
let opts = {
  'path': "path_example", // String | The Artifact Path.
  'index': 56, // Number | The index.
  'append': false, // Boolean | Whether or not to append the content or replace it.
  'allowOverwrite': false // Boolean | whether to allow overwrite if Artifact Content exist already. when set to true, Overwrite happens if Artifact Content already exists
};
apiInstance.artifactsUpload(subscriptionId, resourceGroupName, workspaceName, origin, container, content, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure Subscription ID. | 
 **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | 
 **workspaceName** | **String**| The name of the workspace. | 
 **origin** | **String**| The origin of the Artifact. | 
 **container** | **String**| The container name. | 
 **content** | **File**| The file upload. | 
 **path** | **String**| The Artifact Path. | [optional] 
 **index** | **Number**| The index. | [optional] 
 **append** | **Boolean**| Whether or not to append the content or replace it. | [optional] [default to false]
 **allowOverwrite** | **Boolean**| whether to allow overwrite if Artifact Content exist already. when set to true, Overwrite happens if Artifact Content already exists | [optional] [default to false]

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

