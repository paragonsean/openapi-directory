# HdfsApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**browseHdfsSnapshot**](HdfsApi.md#browseHdfsSnapshot) | **GET** /hdfs/snapshot/{id}/browse | Lists all files and directories in a given path |
| [**createHdfs**](HdfsApi.md#createHdfs) | **POST** /hdfs | Create one HDFS directory for a host |
| [**createHdfsBackupJob**](HdfsApi.md#createHdfsBackupJob) | **POST** /hdfs/{id}/snapshot | Initiate an on-demand backup for a HDFS directory |
| [**createHdfsExportFileJob**](HdfsApi.md#createHdfsExportFileJob) | **POST** /hdfs/snapshot/{id}/export_file | Create export job |
| [**createHdfsRestoreFileJob**](HdfsApi.md#createHdfsRestoreFileJob) | **POST** /hdfs/snapshot/{id}/restore_file | Create restore job |
| [**deleteHdfs**](HdfsApi.md#deleteHdfs) | **DELETE** /hdfs/{id} | Delete a HDFS directory |
| [**deleteHdfsSnapshot**](HdfsApi.md#deleteHdfsSnapshot) | **DELETE** /hdfs/snapshot/{id} | Delete a HDFS directory snapshot |
| [**deleteHdfsSnapshots**](HdfsApi.md#deleteHdfsSnapshots) | **DELETE** /hdfs/{id}/snapshot | Delete all snapshots of a HDFS directory |
| [**getHdfs**](HdfsApi.md#getHdfs) | **GET** /hdfs/{id} | Get information for a single HDFS directory |
| [**getHdfsAsyncRequestStatus**](HdfsApi.md#getHdfsAsyncRequestStatus) | **GET** /hdfs/request/{id} | Get details about an asynchronous request |
| [**getHdfsSnapshot**](HdfsApi.md#getHdfsSnapshot) | **GET** /hdfs/snapshot/{id} | Get information for a HDFS directory snapshot |
| [**getMissedHdfsSnapshots**](HdfsApi.md#getMissedHdfsSnapshots) | **GET** /hdfs/{id}/missed_snapshot | Get missed snapshots for a HDFS directory |
| [**queryHdfs**](HdfsApi.md#queryHdfs) | **GET** /hdfs | Get summary information for all HDFS directories |
| [**searchHdfs**](HdfsApi.md#searchHdfs) | **GET** /hdfs/{id}/search | Search for a file within the HDFS directory |
| [**updateHdfs**](HdfsApi.md#updateHdfs) | **PATCH** /hdfs/{id} | Update a HDFS directory |


<a id="browseHdfsSnapshot"></a>
# **browseHdfsSnapshot**
> BrowseResponseListResponse browseHdfsSnapshot(id, path, offset, limit)

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
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    String path = "path_example"; // String | The absolute path of the starting point for the directory listing.
    Integer offset = 56; // Integer | Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries.
    Integer limit = 56; // Integer | Maximum number of entries in the response.
    try {
      BrowseResponseListResponse result = apiInstance.browseHdfsSnapshot(id, path, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#browseHdfsSnapshot");
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

<a id="createHdfs"></a>
# **createHdfs**
> HdfsDetail createHdfs(hdfsCreate)

Create one HDFS directory for a host

Create a HDFS directory for a network host. A HDFS directory is a HDFS directory template applied to a host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    HdfsCreate hdfsCreate = new HdfsCreate(); // HdfsCreate | Specify a template ID and a host ID.
    try {
      HdfsDetail result = apiInstance.createHdfs(hdfsCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#createHdfs");
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
| **hdfsCreate** | [**HdfsCreate**](HdfsCreate.md)| Specify a template ID and a host ID. | |

### Return type

[**HdfsDetail**](HdfsDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Details of the new HDFS directory. |  -  |

<a id="createHdfsBackupJob"></a>
# **createHdfsBackupJob**
> AsyncRequestStatus createHdfsBackupJob(id, baseOnDemandSnapshotConfig)

Initiate an on-demand backup for a HDFS directory

Create on-demand backup request for HDFS directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of the HDFS directory.
    BaseOnDemandSnapshotConfig baseOnDemandSnapshotConfig = new BaseOnDemandSnapshotConfig(); // BaseOnDemandSnapshotConfig | Configuration for the on-demand backup.
    try {
      AsyncRequestStatus result = apiInstance.createHdfsBackupJob(id, baseOnDemandSnapshotConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#createHdfsBackupJob");
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
| **id** | **String**| ID of the HDFS directory. | |
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

<a id="createHdfsExportFileJob"></a>
# **createHdfsExportFileJob**
> AsyncRequestStatus createHdfsExportFileJob(id, hdfsExportFileJobConfig)

Create export job

Initiate a job to copy a file or folder from a hdfs backup to a destination host other than the source host. Returns the job instance ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    HdfsExportFileJobConfig hdfsExportFileJobConfig = new HdfsExportFileJobConfig(); // HdfsExportFileJobConfig | Configuration for job to export a file or folder from a hdfs backup.
    try {
      AsyncRequestStatus result = apiInstance.createHdfsExportFileJob(id, hdfsExportFileJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#createHdfsExportFileJob");
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
| **hdfsExportFileJobConfig** | [**HdfsExportFileJobConfig**](HdfsExportFileJobConfig.md)| Configuration for job to export a file or folder from a hdfs backup. | |

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

<a id="createHdfsRestoreFileJob"></a>
# **createHdfsRestoreFileJob**
> AsyncRequestStatus createHdfsRestoreFileJob(id, hdfsRestoreFileJobConfig)

Create restore job

Initiate a job to copy a file or folder from a HDFS directory backup to the source host. Returns the job instance ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    HdfsRestoreFileJobConfig hdfsRestoreFileJobConfig = new HdfsRestoreFileJobConfig(); // HdfsRestoreFileJobConfig | Configuration for job to restore a file or folder from a HDFS directory backup.
    try {
      AsyncRequestStatus result = apiInstance.createHdfsRestoreFileJob(id, hdfsRestoreFileJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#createHdfsRestoreFileJob");
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
| **hdfsRestoreFileJobConfig** | [**HdfsRestoreFileJobConfig**](HdfsRestoreFileJobConfig.md)| Configuration for job to restore a file or folder from a HDFS directory backup. | |

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

<a id="deleteHdfs"></a>
# **deleteHdfs**
> deleteHdfs(id, preserveSnapshots)

Delete a HDFS directory

Delete a HDFS directory by specifying the HDFS directory ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | Provide a HDFS directory ID to delete.
    Boolean preserveSnapshots = true; // Boolean | A flag that indicates whether the snapshots of the HDFS directory are preserved or deleted. By default, snapshots are preserved.
    try {
      apiInstance.deleteHdfs(id, preserveSnapshots);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#deleteHdfs");
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
| **id** | **String**| Provide a HDFS directory ID to delete. | |
| **preserveSnapshots** | **Boolean**| A flag that indicates whether the snapshots of the HDFS directory are preserved or deleted. By default, snapshots are preserved. | [optional] |

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
| **204** | Deleted the specified HDFS directory. |  -  |
| **404** | HDFS directory deletion failed. |  -  |

<a id="deleteHdfsSnapshot"></a>
# **deleteHdfsSnapshot**
> deleteHdfsSnapshot(id)

Delete a HDFS directory snapshot

Delete a HDFS directory snapshot. A snapshot is deleted only if it is an on-demand snapshot, or a snapshot of an unprotected HDFS directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    try {
      apiInstance.deleteHdfsSnapshot(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#deleteHdfsSnapshot");
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

<a id="deleteHdfsSnapshots"></a>
# **deleteHdfsSnapshots**
> deleteHdfsSnapshots(id)

Delete all snapshots of a HDFS directory

Delete all snapshots that were created based on a hdfs by providing the HDFS directory ID. Requires an unprotected HDFS directory. Remove the HDFS directory from all SLA Domains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of the HDFS directory.
    try {
      apiInstance.deleteHdfsSnapshots(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#deleteHdfsSnapshots");
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
| **id** | **String**| ID of the HDFS directory. | |

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
| **204** | Successfully removed all snapshots for the HDFS directory. |  -  |

<a id="getHdfs"></a>
# **getHdfs**
> HdfsDetail getHdfs(id)

Get information for a single HDFS directory

Retrieve summary information for a HDFS directory by specifying the HDFS directory ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | Specify the HDFS directory ID.
    try {
      HdfsDetail result = apiInstance.getHdfs(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#getHdfs");
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
| **id** | **String**| Specify the HDFS directory ID. | |

### Return type

[**HdfsDetail**](HdfsDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information for the specified HDFS directory. |  -  |

<a id="getHdfsAsyncRequestStatus"></a>
# **getHdfsAsyncRequestStatus**
> AsyncRequestStatus getHdfsAsyncRequestStatus(id)

Get details about an asynchronous request

Get details about a hdfs related asynchronous request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of the request.
    try {
      AsyncRequestStatus result = apiInstance.getHdfsAsyncRequestStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#getHdfsAsyncRequestStatus");
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
| **200** | Status for the asynchronous request. |  -  |

<a id="getHdfsSnapshot"></a>
# **getHdfsSnapshot**
> HdfsSnapshotDetail getHdfsSnapshot(id)

Get information for a HDFS directory snapshot

Retrieve summary information for a HDFS directory snapshot by specifying the snapshot ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    try {
      HdfsSnapshotDetail result = apiInstance.getHdfsSnapshot(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#getHdfsSnapshot");
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

[**HdfsSnapshotDetail**](HdfsSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information for the specified HDFS directory snapshot. |  -  |

<a id="getMissedHdfsSnapshots"></a>
# **getMissedHdfsSnapshots**
> MissedSnapshotListResponse getMissedHdfsSnapshots(id)

Get missed snapshots for a HDFS directory

Retrieve summary information about all missed snapshots for a HDFS directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of the HDFS directory.
    try {
      MissedSnapshotListResponse result = apiInstance.getMissedHdfsSnapshots(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#getMissedHdfsSnapshots");
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
| **id** | **String**| ID of the HDFS directory. | |

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
| **200** | Summary information about missed snapshots for the specified HDFS directory. |  -  |

<a id="queryHdfs"></a>
# **queryHdfs**
> HdfsSummaryListResponse queryHdfs(primaryClusterId, hostId, isRelic, effectiveSlaDomainId, templateId, limit, offset, name, hostName, sortBy, sortOrder)

Get summary information for all HDFS directories

Retrieve summary information for each HDFS directory. Optionally, filter the retrieved information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String primaryClusterId = "primaryClusterId_example"; // String | Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
    String hostId = "hostId_example"; // String | Filter the summary information based on the ID of the host referenced by the HDFS directory (name node).
    Boolean isRelic = true; // Boolean | Filter the summary information based on the relic status of the HDFS directory. When this parameter is not set, the returned HDFS directory summary information is not filtered by relic status.
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter the summary information based on the ID of the effective SLA Domain inherited by a HDFS directory. Use **_UNPROTECTED_** to only return information for HDFS directories that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for HDFS directories that have an effective SLA Domain.
    String templateId = "templateId_example"; // String | Filter the summary information based on the ID of a HDFS directory template. Use **_NONE_** to only return information for HDFS directories that were not created from a HDFS directory template. Use **_ANY_** to only return information for HDFS directories that were created from a HDFS directory template.
    Integer limit = 56; // Integer | Limit the summary information to a specified maximum number of HDFS directories. Optionally, use with **_offset_** to start the count at a specified point. Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort.
    Integer offset = 56; // Integer | Starting position in the list of HDFS directory entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as a collection of grouped entries for paging.
    String name = "name_example"; // String | Retrieve HDFS directories with a name matching the provided name. The search is performed as a case-insensitive infix search.
    String hostName = "hostName_example"; // String | Retrieve HDFS directories with a host name (name node) matching the provided name. The search is performed as a case-insensitive infix search.
    String sortBy = "name"; // String | Specifies a comma-separated list of HDFS directory attributes to use in sorting the HDFS directory summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified. Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      HdfsSummaryListResponse result = apiInstance.queryHdfs(primaryClusterId, hostId, isRelic, effectiveSlaDomainId, templateId, limit, offset, name, hostName, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#queryHdfs");
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
| **hostId** | **String**| Filter the summary information based on the ID of the host referenced by the HDFS directory (name node). | [optional] |
| **isRelic** | **Boolean**| Filter the summary information based on the relic status of the HDFS directory. When this parameter is not set, the returned HDFS directory summary information is not filtered by relic status. | [optional] |
| **effectiveSlaDomainId** | **String**| Filter the summary information based on the ID of the effective SLA Domain inherited by a HDFS directory. Use **_UNPROTECTED_** to only return information for HDFS directories that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for HDFS directories that have an effective SLA Domain. | [optional] |
| **templateId** | **String**| Filter the summary information based on the ID of a HDFS directory template. Use **_NONE_** to only return information for HDFS directories that were not created from a HDFS directory template. Use **_ANY_** to only return information for HDFS directories that were created from a HDFS directory template. | [optional] |
| **limit** | **Integer**| Limit the summary information to a specified maximum number of HDFS directories. Optionally, use with **_offset_** to start the count at a specified point. Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort. | [optional] |
| **offset** | **Integer**| Starting position in the list of HDFS directory entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as a collection of grouped entries for paging. | [optional] |
| **name** | **String**| Retrieve HDFS directories with a name matching the provided name. The search is performed as a case-insensitive infix search. | [optional] |
| **hostName** | **String**| Retrieve HDFS directories with a host name (name node) matching the provided name. The search is performed as a case-insensitive infix search. | [optional] |
| **sortBy** | **String**| Specifies a comma-separated list of HDFS directory attributes to use in sorting the HDFS directory summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified. Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**. | [optional] [default to name] [enum: name, hostName, templateId, effectiveSlaDomainName, includes, excludes, exceptions] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**HdfsSummaryListResponse**](HdfsSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for HDFS directories. |  -  |

<a id="searchHdfs"></a>
# **searchHdfs**
> SearchResponseListResponse searchHdfs(id, path, limit, cursor)

Search for a file within the HDFS directory

Search for a file within the HDFS directory. Search using full path prefix or filename prefix.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | HDFS directory ID to search.
    String path = "path_example"; // String | The path query. The query can be a path refix or a filename prefix.
    Integer limit = 56; // Integer | Maximum number of entries in the response.
    String cursor = "cursor_example"; // String | Pagination cursor returned by the previous request.
    try {
      SearchResponseListResponse result = apiInstance.searchHdfs(id, path, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#searchHdfs");
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
| **id** | **String**| HDFS directory ID to search. | |
| **path** | **String**| The path query. The query can be a path refix or a filename prefix. | |
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

<a id="updateHdfs"></a>
# **updateHdfs**
> HdfsDetail updateHdfs(id, hdfsUpdate)

Update a HDFS directory

Update a HDFS directory with the specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HdfsApi;

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

    HdfsApi apiInstance = new HdfsApi(defaultClient);
    String id = "id_example"; // String | ID of the HDFS directory to update.
    HdfsUpdate hdfsUpdate = new HdfsUpdate(); // HdfsUpdate | Properties to update.
    try {
      HdfsDetail result = apiInstance.updateHdfs(id, hdfsUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HdfsApi#updateHdfs");
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
| **id** | **String**| ID of the HDFS directory to update. | |
| **hdfsUpdate** | [**HdfsUpdate**](HdfsUpdate.md)| Properties to update. | |

### Return type

[**HdfsDetail**](HdfsDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the update was successful. |  -  |

