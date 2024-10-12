# FilesetApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**browseFilesetSnapshot**](FilesetApi.md#browseFilesetSnapshot) | **GET** /fileset/snapshot/{id}/browse | Lists all files and directories in a given path |
| [**createDownloadFilesetSnapshotFromCloud**](FilesetApi.md#createDownloadFilesetSnapshotFromCloud) | **POST** /fileset/snapshot/{id}/download | Create a download fileset snapshot from archival request |
| [**createFileset**](FilesetApi.md#createFileset) | **POST** /fileset | Create one fileset for a host |
| [**createFilesetBackupJob**](FilesetApi.md#createFilesetBackupJob) | **POST** /fileset/{id}/snapshot | Initiate an on-demand backup for a fileset |
| [**createFilesetDownloadFileJob**](FilesetApi.md#createFilesetDownloadFileJob) | **POST** /fileset/snapshot/{id}/download_file | Create a file download job from a fileset backup |
| [**createFilesetExportFileJob**](FilesetApi.md#createFilesetExportFileJob) | **POST** /fileset/snapshot/{id}/export_file | Create export job |
| [**createFilesetRestoreFileJob**](FilesetApi.md#createFilesetRestoreFileJob) | **POST** /fileset/snapshot/{id}/restore_file | Create restore job |
| [**deleteFileset**](FilesetApi.md#deleteFileset) | **DELETE** /fileset/{id} | Delete a fileset |
| [**deleteFilesetSnapshot**](FilesetApi.md#deleteFilesetSnapshot) | **DELETE** /fileset/snapshot/{id} | Delete a fileset snapshot |
| [**deleteFilesetSnapshots**](FilesetApi.md#deleteFilesetSnapshots) | **DELETE** /fileset/{id}/snapshot | Delete all snapshots of a fileset |
| [**getFileset**](FilesetApi.md#getFileset) | **GET** /fileset/{id} | Get information for a single fileset |
| [**getFilesetAsyncRequestStatus**](FilesetApi.md#getFilesetAsyncRequestStatus) | **GET** /fileset/request/{id} | Get details about an async request |
| [**getFilesetSnapshot**](FilesetApi.md#getFilesetSnapshot) | **GET** /fileset/snapshot/{id} | Get information for a fileset snapshot |
| [**getMissedFilesetSnapshots**](FilesetApi.md#getMissedFilesetSnapshots) | **GET** /fileset/{id}/missed_snapshot | Get missed snapshots for a fileset |
| [**queryFileset**](FilesetApi.md#queryFileset) | **GET** /fileset | Get summary information for all filesets |
| [**searchFileset**](FilesetApi.md#searchFileset) | **GET** /fileset/{id}/search | Search for a file within the fileset |
| [**updateFileset**](FilesetApi.md#updateFileset) | **PATCH** /fileset/{id} | Update a Fileset |


<a id="browseFilesetSnapshot"></a>
# **browseFilesetSnapshot**
> BrowseResponseListResponse browseFilesetSnapshot(id, path, offset, limit)

Lists all files and directories in a given path

Lists all files and directories in a given path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    String path = "path_example"; // String | The absolute path of the starting point for the directory listing.
    Integer offset = 56; // Integer | Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries.
    Integer limit = 56; // Integer | Maximum number of entries in the response.
    try {
      BrowseResponseListResponse result = apiInstance.browseFilesetSnapshot(id, path, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#browseFilesetSnapshot");
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
| **id** | **String**| ID of snapshot. | |
| **path** | **String**| The absolute path of the starting point for the directory listing. | |
| **offset** | **Integer**| Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries. | [optional] |
| **limit** | **Integer**| Maximum number of entries in the response. | [optional] |

### Return type

[**BrowseResponseListResponse**](BrowseResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of files and directories at the specified path. |  -  |

<a id="createDownloadFilesetSnapshotFromCloud"></a>
# **createDownloadFilesetSnapshotFromCloud**
> AsyncRequestStatus createDownloadFilesetSnapshotFromCloud(id)

Create a download fileset snapshot from archival request

Create a download fileset snapshot from archival request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    try {
      AsyncRequestStatus result = apiInstance.createDownloadFilesetSnapshotFromCloud(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#createDownloadFilesetSnapshotFromCloud");
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
| **id** | **String**| ID of snapshot. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status for the download request. |  -  |

<a id="createFileset"></a>
# **createFileset**
> FilesetDetail createFileset(filesetCreate)

Create one fileset for a host

Create a fileset for a network host. A fileset is a fileset template applied to a host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    FilesetCreate filesetCreate = new FilesetCreate(); // FilesetCreate | Specify a template ID and either a host ID or a share ID. When a share ID is provided, the host ID is derived from the host share. Also specify whether or not this backup is a direct archive backup.
    try {
      FilesetDetail result = apiInstance.createFileset(filesetCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#createFileset");
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
| **filesetCreate** | [**FilesetCreate**](FilesetCreate.md)| Specify a template ID and either a host ID or a share ID. When a share ID is provided, the host ID is derived from the host share. Also specify whether or not this backup is a direct archive backup. | |

### Return type

[**FilesetDetail**](FilesetDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Details of the new fileset. |  -  |

<a id="createFilesetBackupJob"></a>
# **createFilesetBackupJob**
> AsyncRequestStatus createFilesetBackupJob(id, baseOnDemandSnapshotConfig)

Initiate an on-demand backup for a fileset

Create an on-demand backup request for the given fileset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of the Fileset.
    BaseOnDemandSnapshotConfig baseOnDemandSnapshotConfig = new BaseOnDemandSnapshotConfig(); // BaseOnDemandSnapshotConfig | Configuration for the on-demand backup.
    try {
      AsyncRequestStatus result = apiInstance.createFilesetBackupJob(id, baseOnDemandSnapshotConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#createFilesetBackupJob");
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
| **id** | **String**| ID of the Fileset. | |
| **baseOnDemandSnapshotConfig** | [**BaseOnDemandSnapshotConfig**](BaseOnDemandSnapshotConfig.md)| Configuration for the on-demand backup. | [optional] |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status for the backup request. |  -  |

<a id="createFilesetDownloadFileJob"></a>
# **createFilesetDownloadFileJob**
> AsyncRequestStatus createFilesetDownloadFileJob(id, filesetDownloadFileJobConfig)

Create a file download job from a fileset backup

Initiate a job to download a file from a backup of a fileset. Returns a job instance ID. An email notification will be sent out when the download is ready. When the download is ready, the file can be downloaded from the corresponding event which includes the job instance ID as the value of **jobInstanceId**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    FilesetDownloadFileJobConfig filesetDownloadFileJobConfig = new FilesetDownloadFileJobConfig(); // FilesetDownloadFileJobConfig | Configuration for a download job.
    try {
      AsyncRequestStatus result = apiInstance.createFilesetDownloadFileJob(id, filesetDownloadFileJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#createFilesetDownloadFileJob");
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
| **id** | **String**| ID of snapshot. | |
| **filesetDownloadFileJobConfig** | [**FilesetDownloadFileJobConfig**](FilesetDownloadFileJobConfig.md)| Configuration for a download job. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status for the download request. |  -  |

<a id="createFilesetExportFileJob"></a>
# **createFilesetExportFileJob**
> AsyncRequestStatus createFilesetExportFileJob(id, filesetExportFileJobConfig)

Create export job

Initiate a job to copy a file or folder from a fileset backup to a destination host other than the source host. Returns the job instance ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    FilesetExportFileJobConfig filesetExportFileJobConfig = new FilesetExportFileJobConfig(); // FilesetExportFileJobConfig | Configuration for job to export a file or folder from a fileset backup.
    try {
      AsyncRequestStatus result = apiInstance.createFilesetExportFileJob(id, filesetExportFileJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#createFilesetExportFileJob");
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
| **id** | **String**| ID of snapshot. | |
| **filesetExportFileJobConfig** | [**FilesetExportFileJobConfig**](FilesetExportFileJobConfig.md)| Configuration for job to export a file or folder from a fileset backup. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status for the export request. |  -  |

<a id="createFilesetRestoreFileJob"></a>
# **createFilesetRestoreFileJob**
> AsyncRequestStatus createFilesetRestoreFileJob(id, filesetRestoreFileJobConfig)

Create restore job

Initiate a job to copy a file or folder from a fileset backup to the source host. Returns the job instance ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    FilesetRestoreFileJobConfig filesetRestoreFileJobConfig = new FilesetRestoreFileJobConfig(); // FilesetRestoreFileJobConfig | Configuration for job to restore a file or folder from a fileset backup.
    try {
      AsyncRequestStatus result = apiInstance.createFilesetRestoreFileJob(id, filesetRestoreFileJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#createFilesetRestoreFileJob");
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
| **id** | **String**| ID of snapshot. | |
| **filesetRestoreFileJobConfig** | [**FilesetRestoreFileJobConfig**](FilesetRestoreFileJobConfig.md)| Configuration for job to restore a file or folder from a fileset backup. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status for the restore request. |  -  |

<a id="deleteFileset"></a>
# **deleteFileset**
> deleteFileset(id, preserveSnapshots)

Delete a fileset

Delete a fileset by specifying the fileset ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | Provide a fileset ID to delete.
    Boolean preserveSnapshots = true; // Boolean | Flag to indicate whether to preserve snapshots of the fileset or to delete them. Default behavior is to preserve them.
    try {
      apiInstance.deleteFileset(id, preserveSnapshots);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#deleteFileset");
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
| **id** | **String**| Provide a fileset ID to delete. | |
| **preserveSnapshots** | **Boolean**| Flag to indicate whether to preserve snapshots of the fileset or to delete them. Default behavior is to preserve them. | [optional] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted the specified fileset. |  -  |
| **404** | Fileset deletion failed. |  -  |

<a id="deleteFilesetSnapshot"></a>
# **deleteFilesetSnapshot**
> deleteFilesetSnapshot(id, location)

Delete a fileset snapshot

Delete a fileset snapshot. A snapshot is deleted only if it is an on-demand snapshot, a snapshot of an unprotected fileset or a local snapshot that was downloaded from an archive location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    String location = "all"; // String | Snapshot location to delete. Use **_local_** to delete all local snapshots and **_all_** to delete the snapshot in all locations.
    try {
      apiInstance.deleteFilesetSnapshot(id, location);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#deleteFilesetSnapshot");
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
| **id** | **String**| ID of snapshot. | |
| **location** | **String**| Snapshot location to delete. Use **_local_** to delete all local snapshots and **_all_** to delete the snapshot in all locations. | [enum: all, local] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Snapshot sucessfully deleted. |  -  |

<a id="deleteFilesetSnapshots"></a>
# **deleteFilesetSnapshots**
> deleteFilesetSnapshots(id)

Delete all snapshots of a fileset

Delete all snapshots that were created based on a fileset by providing the fileset ID. Requires an unprotected fileset. Remove the fileset from all SLA Domains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of the fileset.
    try {
      apiInstance.deleteFilesetSnapshots(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#deleteFilesetSnapshots");
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
| **id** | **String**| ID of the fileset. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully removed all snapshots for the fileset. |  -  |

<a id="getFileset"></a>
# **getFileset**
> FilesetDetail getFileset(id)

Get information for a single fileset

Retrieve summary information for a fileset by specifying the fileset ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | Specify the fileset ID.
    try {
      FilesetDetail result = apiInstance.getFileset(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#getFileset");
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
| **id** | **String**| Specify the fileset ID. | |

### Return type

[**FilesetDetail**](FilesetDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information for the specified fileset. |  -  |

<a id="getFilesetAsyncRequestStatus"></a>
# **getFilesetAsyncRequestStatus**
> AsyncRequestStatus getFilesetAsyncRequestStatus(id)

Get details about an async request

Get details about a fileset related async request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of the request.
    try {
      AsyncRequestStatus result = apiInstance.getFilesetAsyncRequestStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#getFilesetAsyncRequestStatus");
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
| **id** | **String**| ID of the request. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status for the async request. |  -  |

<a id="getFilesetSnapshot"></a>
# **getFilesetSnapshot**
> FilesetSnapshotDetail getFilesetSnapshot(id, verbose)

Get information for a fileset snapshot

Retrieve summary information for a fileset snapshot by specifying the snapshot ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    Boolean verbose = false; // Boolean | Whether or not to fetch verbose fileset snapshot information. The performance of this endpoint will decrease if set to true.
    try {
      FilesetSnapshotDetail result = apiInstance.getFilesetSnapshot(id, verbose);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#getFilesetSnapshot");
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
| **id** | **String**| ID of snapshot. | |
| **verbose** | **Boolean**| Whether or not to fetch verbose fileset snapshot information. The performance of this endpoint will decrease if set to true. | [optional] [default to false] |

### Return type

[**FilesetSnapshotDetail**](FilesetSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information for the specified fileset snapshot. |  -  |

<a id="getMissedFilesetSnapshots"></a>
# **getMissedFilesetSnapshots**
> MissedSnapshotListResponse getMissedFilesetSnapshots(id)

Get missed snapshots for a fileset

Retrieve summary information about all missed snapshots for a fileset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of the fileset.
    try {
      MissedSnapshotListResponse result = apiInstance.getMissedFilesetSnapshots(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#getMissedFilesetSnapshots");
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
| **id** | **String**| ID of the fileset. | |

### Return type

[**MissedSnapshotListResponse**](MissedSnapshotListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information about missed snapshots for the specified fileset. |  -  |

<a id="queryFileset"></a>
# **queryFileset**
> FilesetSummaryListResponse queryFileset(primaryClusterId, hostId, shareId, isRelic, effectiveSlaDomainId, templateId, limit, offset, name, hostName, sortBy, sortOrder)

Get summary information for all filesets

Retrieve summary information for each fileset. Optionally, filter the retrieved information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String primaryClusterId = "primaryClusterId_example"; // String | Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
    String hostId = "hostId_example"; // String | Filter the summary information based on the ID of the host referenced by the fileset.
    String shareId = "shareId_example"; // String | Filter the summary information based on the ID of the host share referenced by the fileset. Use **_NONE_** to only return information for filesets that were not created based on a host share. Use **_ANY_** to only return information for filesets that were created based on a host share.
    Boolean isRelic = true; // Boolean | Filter the summary information based on the relic status of the fileset. Returns both relic and non relic if the parameter is not set.
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter the summary information based on the ID of the effective SLA Domain inherited by a fileset. Use **_UNPROTECTED_** to only return information for filesets that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for filesets that do have an effective SLA Domain.
    String templateId = "templateId_example"; // String | Filter the summary information based on the ID of a fileset template.  Use **_NONE_** to only return information for filesets that were not created from a fileset template.  Use **_ANY_** to only return information for filesets that were created from a fileset template.
    Integer limit = 56; // Integer | Limit the summary information to a specified maximum number of filesets.  Optionally, use with **_offset_** to start the count at a specified point.  Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort.
    Integer offset = 56; // Integer | Starting position in the list of fileset entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of results.
    String name = "name_example"; // String | Retrieve filesets with a name matching the provided name. The search is performed as a case-insensitive infix search.
    String hostName = "hostName_example"; // String | Retrieve filesets with a host name matching the provided name. The search is performed as a case-insensitive infix search.
    String sortBy = "name"; // String | Specifies a comma-separated list of fileset attributes to use in sorting the fileset summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified.  Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      FilesetSummaryListResponse result = apiInstance.queryFileset(primaryClusterId, hostId, shareId, isRelic, effectiveSlaDomainId, templateId, limit, offset, name, hostName, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#queryFileset");
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
| **primaryClusterId** | **String**| Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session. | [optional] |
| **hostId** | **String**| Filter the summary information based on the ID of the host referenced by the fileset. | [optional] |
| **shareId** | **String**| Filter the summary information based on the ID of the host share referenced by the fileset. Use **_NONE_** to only return information for filesets that were not created based on a host share. Use **_ANY_** to only return information for filesets that were created based on a host share. | [optional] |
| **isRelic** | **Boolean**| Filter the summary information based on the relic status of the fileset. Returns both relic and non relic if the parameter is not set. | [optional] |
| **effectiveSlaDomainId** | **String**| Filter the summary information based on the ID of the effective SLA Domain inherited by a fileset. Use **_UNPROTECTED_** to only return information for filesets that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for filesets that do have an effective SLA Domain. | [optional] |
| **templateId** | **String**| Filter the summary information based on the ID of a fileset template.  Use **_NONE_** to only return information for filesets that were not created from a fileset template.  Use **_ANY_** to only return information for filesets that were created from a fileset template. | [optional] |
| **limit** | **Integer**| Limit the summary information to a specified maximum number of filesets.  Optionally, use with **_offset_** to start the count at a specified point.  Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort. | [optional] |
| **offset** | **Integer**| Starting position in the list of fileset entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of results. | [optional] |
| **name** | **String**| Retrieve filesets with a name matching the provided name. The search is performed as a case-insensitive infix search. | [optional] |
| **hostName** | **String**| Retrieve filesets with a host name matching the provided name. The search is performed as a case-insensitive infix search. | [optional] |
| **sortBy** | **String**| Specifies a comma-separated list of fileset attributes to use in sorting the fileset summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified.  Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**. | [optional] [enum: name, hostName, templateId, effectiveSlaDomainName, includes, excludes, exceptions] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |

### Return type

[**FilesetSummaryListResponse**](FilesetSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for filesets. |  -  |

<a id="searchFileset"></a>
# **searchFileset**
> SearchResponseListResponse searchFileset(id, path, limit, cursor)

Search for a file within the fileset

Search for a file within the fileset. Search via full path prefix or filename prefix.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | Fileset ID to search.
    String path = "path_example"; // String | The path query. Either path prefix or filename prefix.
    Integer limit = 56; // Integer | Maximum number of entries in the response.
    String cursor = "cursor_example"; // String | Pagination cursor returned by the previous request.
    try {
      SearchResponseListResponse result = apiInstance.searchFileset(id, path, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#searchFileset");
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
| **id** | **String**| Fileset ID to search. | |
| **path** | **String**| The path query. Either path prefix or filename prefix. | |
| **limit** | **Integer**| Maximum number of entries in the response. | [optional] |
| **cursor** | **String**| Pagination cursor returned by the previous request. | [optional] |

### Return type

[**SearchResponseListResponse**](SearchResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search results. |  -  |

<a id="updateFileset"></a>
# **updateFileset**
> FilesetDetail updateFileset(id, filesetUpdate)

Update a Fileset

Update a Fileset with the specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    FilesetApi apiInstance = new FilesetApi(defaultClient);
    String id = "id_example"; // String | ID of the Fileset. to update.
    FilesetUpdate filesetUpdate = new FilesetUpdate(); // FilesetUpdate | Properties to update.
    try {
      FilesetDetail result = apiInstance.updateFileset(id, filesetUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesetApi#updateFileset");
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
| **id** | **String**| ID of the Fileset. to update. | |
| **filesetUpdate** | [**FilesetUpdate**](FilesetUpdate.md)| Properties to update. | |

### Return type

[**FilesetDetail**](FilesetDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the update was successful. |  -  |

