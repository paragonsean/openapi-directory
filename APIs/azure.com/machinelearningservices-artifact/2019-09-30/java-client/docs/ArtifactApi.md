# ArtifactApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**artifactsBatchCreateEmptyArtifacts**](ArtifactApi.md#artifactsBatchCreateEmptyArtifacts) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/batch/metadata | Create a batch of empty Artifacts. |
| [**artifactsBatchGetById**](ArtifactApi.md#artifactsBatchGetById) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/batch/metadata | Get Batch Artifacts by Ids. |
| [**artifactsBatchGetStorageById**](ArtifactApi.md#artifactsBatchGetStorageById) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/storageuri/batch/metadata | Get Batch Artifacts storage by Ids. |
| [**artifactsBatchIngestFromSas**](ArtifactApi.md#artifactsBatchIngestFromSas) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/batch/ingest/containersas | Batch ingest using shared access signature. |
| [**artifactsCreate**](ArtifactApi.md#artifactsCreate) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/metadata | Create Artifact. |
| [**artifactsDeleteBatchMetaData**](ArtifactApi.md#artifactsDeleteBatchMetaData) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/batch/metadata:delete | Delete Batch of Artifact Metadata. |
| [**artifactsDeleteMetaData**](ArtifactApi.md#artifactsDeleteMetaData) | **DELETE** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/metadata | Delete Artifact Metadata. |
| [**artifactsDeleteMetaDataInContainer**](ArtifactApi.md#artifactsDeleteMetaDataInContainer) | **DELETE** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/batch | Delete Artifact Metadata. |
| [**artifactsDownload**](ArtifactApi.md#artifactsDownload) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/content | Get Artifact content by Id. |
| [**artifactsGet**](ArtifactApi.md#artifactsGet) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/metadata | Get Artifact metadata by Id. |
| [**artifactsGetContentInformation**](ArtifactApi.md#artifactsGetContentInformation) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/contentinfo | Get Artifact content information. |
| [**artifactsGetSas**](ArtifactApi.md#artifactsGetSas) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/write | Get writable shared access signature for Artifact. |
| [**artifactsGetStorageContentInformation**](ArtifactApi.md#artifactsGetStorageContentInformation) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/contentinfo/storageuri | Get Artifact storage content information. |
| [**artifactsListInContainer**](ArtifactApi.md#artifactsListInContainer) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container} | Get Artifacts metadata in a container or path. |
| [**artifactsListSasByPrefix**](ArtifactApi.md#artifactsListSasByPrefix) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/prefix/contentinfo | Get shared access signature for an Artifact |
| [**artifactsListStorageUriByPrefix**](ArtifactApi.md#artifactsListStorageUriByPrefix) | **GET** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/prefix/contentinfo/storageuri | Get storage Uri for Artifacts in a path. |
| [**artifactsRegister**](ArtifactApi.md#artifactsRegister) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/register | Create an Artifact for an existing data location. |
| [**artifactsUpload**](ArtifactApi.md#artifactsUpload) | **POST** /artifact/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/artifacts/{origin}/{container}/content | Upload Artifact content. |


<a id="artifactsBatchCreateEmptyArtifacts"></a>
# **artifactsBatchCreateEmptyArtifacts**
> BatchArtifactContentInformationResult artifactsBatchCreateEmptyArtifacts(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactPaths)

Create a batch of empty Artifacts.

Create a Batch of empty Artifacts from the supplied paths.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    ArtifactPathList artifactPaths = new ArtifactPathList(); // ArtifactPathList | The list of Artifact paths to create.
    try {
      BatchArtifactContentInformationResult result = apiInstance.artifactsBatchCreateEmptyArtifacts(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactPaths);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsBatchCreateEmptyArtifacts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **artifactPaths** | [**ArtifactPathList**](ArtifactPathList.md)| The list of Artifact paths to create. | |

### Return type

[**BatchArtifactContentInformationResult**](BatchArtifactContentInformationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Batch of empty Artifacts created successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsBatchGetById"></a>
# **artifactsBatchGetById**
> BatchArtifactContentInformationResult artifactsBatchGetById(subscriptionId, resourceGroupName, workspaceName, artifactIds)

Get Batch Artifacts by Ids.

Get Batch Artifacts by the specific Ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    ArtifactIdList artifactIds = new ArtifactIdList(); // ArtifactIdList | The command for Batch Artifact get request.
    try {
      BatchArtifactContentInformationResult result = apiInstance.artifactsBatchGetById(subscriptionId, resourceGroupName, workspaceName, artifactIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsBatchGetById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **artifactIds** | [**ArtifactIdList**](ArtifactIdList.md)| The command for Batch Artifact get request. | |

### Return type

[**BatchArtifactContentInformationResult**](BatchArtifactContentInformationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Batch Artifacts are returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsBatchGetStorageById"></a>
# **artifactsBatchGetStorageById**
> BatchArtifactContentInformationResult artifactsBatchGetStorageById(subscriptionId, resourceGroupName, workspaceName, artifactIds)

Get Batch Artifacts storage by Ids.

Get Batch Artifacts storage by specific Ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    ArtifactIdList artifactIds = new ArtifactIdList(); // ArtifactIdList | The list of artifactIds to get.
    try {
      BatchArtifactContentInformationResult result = apiInstance.artifactsBatchGetStorageById(subscriptionId, resourceGroupName, workspaceName, artifactIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsBatchGetStorageById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **artifactIds** | [**ArtifactIdList**](ArtifactIdList.md)| The list of artifactIds to get. | |

### Return type

[**BatchArtifactContentInformationResult**](BatchArtifactContentInformationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Batch Artifact&#39;s storage are returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsBatchIngestFromSas"></a>
# **artifactsBatchIngestFromSas**
> PaginatedArtifactList artifactsBatchIngestFromSas(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactContainerSas)

Batch ingest using shared access signature.

Ingest Batch Artifacts using shared access signature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    ArtifactContainerSas artifactContainerSas = new ArtifactContainerSas(); // ArtifactContainerSas | The artifact container shared access signature to use for batch ingest.
    try {
      PaginatedArtifactList result = apiInstance.artifactsBatchIngestFromSas(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactContainerSas);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsBatchIngestFromSas");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **artifactContainerSas** | [**ArtifactContainerSas**](ArtifactContainerSas.md)| The artifact container shared access signature to use for batch ingest. | |

### Return type

[**PaginatedArtifactList**](PaginatedArtifactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Batch is ingested using shared access signature successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsCreate"></a>
# **artifactsCreate**
> Artifact artifactsCreate(subscriptionId, resourceGroupName, workspaceName, artifact)

Create Artifact.

Create an Artifact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    Artifact artifact = new Artifact(); // Artifact | The Artifact details.
    try {
      Artifact result = apiInstance.artifactsCreate(subscriptionId, resourceGroupName, workspaceName, artifact);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **artifact** | [**Artifact**](Artifact.md)| The Artifact details. | |

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact is created successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsDeleteBatchMetaData"></a>
# **artifactsDeleteBatchMetaData**
> artifactsDeleteBatchMetaData(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactPaths, hardDelete)

Delete Batch of Artifact Metadata.

Delete a Batch of Artifact Metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    ArtifactPathList artifactPaths = new ArtifactPathList(); // ArtifactPathList | The list of Artifact paths to delete.
    Boolean hardDelete = false; // Boolean | If set to true, the delete cannot be reverted at a later time.
    try {
      apiInstance.artifactsDeleteBatchMetaData(subscriptionId, resourceGroupName, workspaceName, origin, container, artifactPaths, hardDelete);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsDeleteBatchMetaData");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **artifactPaths** | [**ArtifactPathList**](ArtifactPathList.md)| The list of Artifact paths to delete. | |
| **hardDelete** | **Boolean**| If set to true, the delete cannot be reverted at a later time. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The batch delete of Artifact metadata completed successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsDeleteMetaData"></a>
# **artifactsDeleteMetaData**
> artifactsDeleteMetaData(subscriptionId, resourceGroupName, workspaceName, origin, container, path, hardDelete)

Delete Artifact Metadata.

Delete an Artifact Metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    String path = "path_example"; // String | The Artifact Path.
    Boolean hardDelete = false; // Boolean | If set to true. The delete cannot be revert at later time.
    try {
      apiInstance.artifactsDeleteMetaData(subscriptionId, resourceGroupName, workspaceName, origin, container, path, hardDelete);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsDeleteMetaData");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **path** | **String**| The Artifact Path. | [optional] |
| **hardDelete** | **Boolean**| If set to true. The delete cannot be revert at later time. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact metadata deleted successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsDeleteMetaDataInContainer"></a>
# **artifactsDeleteMetaDataInContainer**
> artifactsDeleteMetaDataInContainer(subscriptionId, resourceGroupName, workspaceName, origin, container, hardDelete)

Delete Artifact Metadata.

Delete Artifact Metadata in a specific container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    Boolean hardDelete = false; // Boolean | If set to true. The delete cannot be revert at later time.
    try {
      apiInstance.artifactsDeleteMetaDataInContainer(subscriptionId, resourceGroupName, workspaceName, origin, container, hardDelete);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsDeleteMetaDataInContainer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **hardDelete** | **Boolean**| If set to true. The delete cannot be revert at later time. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact metadata deleted successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsDownload"></a>
# **artifactsDownload**
> File artifactsDownload(subscriptionId, resourceGroupName, workspaceName, origin, container, path)

Get Artifact content by Id.

Get Artifact content of a specific Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    String path = "path_example"; // String | The Artifact Path.
    try {
      File result = apiInstance.artifactsDownload(subscriptionId, resourceGroupName, workspaceName, origin, container, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsDownload");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **path** | **String**| The Artifact Path. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File Response |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsGet"></a>
# **artifactsGet**
> Artifact artifactsGet(subscriptionId, resourceGroupName, workspaceName, origin, container, path)

Get Artifact metadata by Id.

Get Artifact metadata for a specific Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    String path = "path_example"; // String | The Artifact Path.
    try {
      Artifact result = apiInstance.artifactsGet(subscriptionId, resourceGroupName, workspaceName, origin, container, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **path** | **String**| The Artifact Path. | |

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The details of the Artifact are returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsGetContentInformation"></a>
# **artifactsGetContentInformation**
> ArtifactContentInformation artifactsGetContentInformation(subscriptionId, resourceGroupName, workspaceName, origin, container, path)

Get Artifact content information.

Get content information of an Artifact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    String path = "path_example"; // String | The Artifact Path.
    try {
      ArtifactContentInformation result = apiInstance.artifactsGetContentInformation(subscriptionId, resourceGroupName, workspaceName, origin, container, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsGetContentInformation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **path** | **String**| The Artifact Path. | [optional] |

### Return type

[**ArtifactContentInformation**](ArtifactContentInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact content information is returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsGetSas"></a>
# **artifactsGetSas**
> ArtifactContentInformation artifactsGetSas(subscriptionId, resourceGroupName, workspaceName, origin, container, path)

Get writable shared access signature for Artifact.

Get writable shared access signature for a specific Artifact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    String path = "path_example"; // String | The Artifact Path.
    try {
      ArtifactContentInformation result = apiInstance.artifactsGetSas(subscriptionId, resourceGroupName, workspaceName, origin, container, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsGetSas");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **path** | **String**| The Artifact Path. | [optional] |

### Return type

[**ArtifactContentInformation**](ArtifactContentInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact writable shared access signature is returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsGetStorageContentInformation"></a>
# **artifactsGetStorageContentInformation**
> ArtifactContentInformation artifactsGetStorageContentInformation(subscriptionId, resourceGroupName, workspaceName, origin, container, path)

Get Artifact storage content information.

Get storage content information of an Artifact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    String path = "path_example"; // String | The Artifact Path.
    try {
      ArtifactContentInformation result = apiInstance.artifactsGetStorageContentInformation(subscriptionId, resourceGroupName, workspaceName, origin, container, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsGetStorageContentInformation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **path** | **String**| The Artifact Path. | [optional] |

### Return type

[**ArtifactContentInformation**](ArtifactContentInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact storage content information is returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsListInContainer"></a>
# **artifactsListInContainer**
> PaginatedArtifactList artifactsListInContainer(subscriptionId, resourceGroupName, workspaceName, origin, container, path, continuationToken)

Get Artifacts metadata in a container or path.

Get Artifacts metadata in a specific container or path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    String path = "path_example"; // String | The Artifact Path.
    String continuationToken = "continuationToken_example"; // String | The continuation token.
    try {
      PaginatedArtifactList result = apiInstance.artifactsListInContainer(subscriptionId, resourceGroupName, workspaceName, origin, container, path, continuationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsListInContainer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **path** | **String**| The Artifact Path. | [optional] |
| **continuationToken** | **String**| The continuation token. | [optional] |

### Return type

[**PaginatedArtifactList**](PaginatedArtifactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The details of the Artifacts are returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsListSasByPrefix"></a>
# **artifactsListSasByPrefix**
> PaginatedArtifactContentInformationList artifactsListSasByPrefix(subscriptionId, resourceGroupName, workspaceName, origin, container, path, continuationToken)

Get shared access signature for an Artifact

Get shared access signature for an Artifact in specific path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    String path = "path_example"; // String | The Artifact Path.
    String continuationToken = "continuationToken_example"; // String | The continuation token.
    try {
      PaginatedArtifactContentInformationList result = apiInstance.artifactsListSasByPrefix(subscriptionId, resourceGroupName, workspaceName, origin, container, path, continuationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsListSasByPrefix");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **path** | **String**| The Artifact Path. | [optional] |
| **continuationToken** | **String**| The continuation token. | [optional] |

### Return type

[**PaginatedArtifactContentInformationList**](PaginatedArtifactContentInformationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact writable shared access signature is returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsListStorageUriByPrefix"></a>
# **artifactsListStorageUriByPrefix**
> PaginatedArtifactContentInformationList artifactsListStorageUriByPrefix(subscriptionId, resourceGroupName, workspaceName, origin, container, path, continuationToken)

Get storage Uri for Artifacts in a path.

Get storage Uri for Artifacts in a specific path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    String path = "path_example"; // String | The Artifact Path.
    String continuationToken = "continuationToken_example"; // String | The continuation token.
    try {
      PaginatedArtifactContentInformationList result = apiInstance.artifactsListStorageUriByPrefix(subscriptionId, resourceGroupName, workspaceName, origin, container, path, continuationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsListStorageUriByPrefix");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **path** | **String**| The Artifact Path. | [optional] |
| **continuationToken** | **String**| The continuation token. | [optional] |

### Return type

[**PaginatedArtifactContentInformationList**](PaginatedArtifactContentInformationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact storage uri is returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsRegister"></a>
# **artifactsRegister**
> Artifact artifactsRegister(subscriptionId, resourceGroupName, workspaceName, artifact)

Create an Artifact for an existing data location.

Create an Artifact for an existing dataPath.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    Artifact artifact = new Artifact(); // Artifact | The Artifact creation details.
    try {
      Artifact result = apiInstance.artifactsRegister(subscriptionId, resourceGroupName, workspaceName, artifact);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsRegister");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **artifact** | [**Artifact**](Artifact.md)| The Artifact creation details. | |

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact is created successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="artifactsUpload"></a>
# **artifactsUpload**
> Artifact artifactsUpload(subscriptionId, resourceGroupName, workspaceName, origin, container, content, path, index, append, allowOverwrite)

Upload Artifact content.

Upload content to an Artifact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String origin = "origin_example"; // String | The origin of the Artifact.
    String container = "container_example"; // String | The container name.
    File content = new File("/path/to/file"); // File | The file upload.
    String path = "path_example"; // String | The Artifact Path.
    Integer index = 56; // Integer | The index.
    Boolean append = false; // Boolean | Whether or not to append the content or replace it.
    Boolean allowOverwrite = false; // Boolean | whether to allow overwrite if Artifact Content exist already. when set to true, Overwrite happens if Artifact Content already exists
    try {
      Artifact result = apiInstance.artifactsUpload(subscriptionId, resourceGroupName, workspaceName, origin, container, content, path, index, append, allowOverwrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsUpload");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **origin** | **String**| The origin of the Artifact. | |
| **container** | **String**| The container name. | |
| **content** | **File**| The file upload. | |
| **path** | **String**| The Artifact Path. | [optional] |
| **index** | **Integer**| The index. | [optional] |
| **append** | **Boolean**| Whether or not to append the content or replace it. | [optional] [default to false] |
| **allowOverwrite** | **Boolean**| whether to allow overwrite if Artifact Content exist already. when set to true, Overwrite happens if Artifact Content already exists | [optional] [default to false] |

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Artifact content is uploaded successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

