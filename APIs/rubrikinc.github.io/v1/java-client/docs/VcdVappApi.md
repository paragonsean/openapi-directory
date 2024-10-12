# VcdVappApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOnDemandSnapshotV1**](VcdVappApi.md#createOnDemandSnapshotV1) | **POST** /vcd/vapp/{id}/snapshot | Create an on-demand snapshot for a vApp |
| [**createVappExportV1**](VcdVappApi.md#createVappExportV1) | **POST** /vcd/vapp/snapshot/{snapshot_id}/export | Export vApp snapshot |
| [**createVappInstantRecoveryV1**](VcdVappApi.md#createVappInstantRecoveryV1) | **POST** /vcd/vapp/snapshot/{snapshot_id}/instant_recover | Instant Recovery of vApp virtual machines |
| [**createVappTemplateSnapshotExport**](VcdVappApi.md#createVappTemplateSnapshotExport) | **POST** /vcd/vapp/template/snapshot/{snapshot_id}/export | Export of a vApp template snapshot |
| [**createVcdVappDownloadSnapshotFromCloudV1**](VcdVappApi.md#createVcdVappDownloadSnapshotFromCloudV1) | **POST** /vcd/vapp/snapshot/{id}/download | Download snapshot from archive |
| [**deleteVappSnapshotV1**](VcdVappApi.md#deleteVappSnapshotV1) | **DELETE** /vcd/vapp/snapshot/{id} | Delete a vApp snapshot |
| [**deleteVappSnapshotsV1**](VcdVappApi.md#deleteVappSnapshotsV1) | **DELETE** /vcd/vapp/{id}/snapshot | Delete all snapshots of vApp |
| [**getVappAsyncRequestStatusV1**](VcdVappApi.md#getVappAsyncRequestStatusV1) | **GET** /vcd/vapp/request/{id} | Get vApp job status |
| [**getVappSnapshotExportOptionsV1**](VcdVappApi.md#getVappSnapshotExportOptionsV1) | **GET** /vcd/vapp/snapshot/{snapshot_id}/export/options | Get exportable network configurations |
| [**getVappSnapshotInstantRecoveryOptionsV1**](VcdVappApi.md#getVappSnapshotInstantRecoveryOptionsV1) | **GET** /vcd/vapp/snapshot/{snapshot_id}/instant_recover/options | Get Instant Recovery information |
| [**getVappSnapshotV1**](VcdVappApi.md#getVappSnapshotV1) | **GET** /vcd/vapp/snapshot/{id} | Get vApp snapshot details |
| [**getVappTemplateSnapshotExportOptions**](VcdVappApi.md#getVappTemplateSnapshotExportOptions) | **GET** /vcd/vapp/template/snapshot/{snapshot_id}/export/options | Get Export information for a vApp template snapshot |
| [**getVcdVappV1**](VcdVappApi.md#getVcdVappV1) | **GET** /vcd/vapp/{id} | Get details of a specific vApp |
| [**queryVappSnapshotV1**](VcdVappApi.md#queryVappSnapshotV1) | **GET** /vcd/vapp/{id}/snapshot | Get list of snapshots of vApp |
| [**queryVcdVappsV1**](VcdVappApi.md#queryVcdVappsV1) | **GET** /vcd/vapp | Get summary for vApps |
| [**searchVappV1**](VcdVappApi.md#searchVappV1) | **GET** /vcd/vapp/{id}/search | Search for a file in a vApp |
| [**updateVcdVappV1**](VcdVappApi.md#updateVcdVappV1) | **PATCH** /vcd/vapp/{id} | Update vApp |
| [**vcdMissedSnapshotsV1**](VcdVappApi.md#vcdMissedSnapshotsV1) | **GET** /vcd/vapp/{id}/missed_snapshot | Get details about missed snapshots for a vApp |


<a id="createOnDemandSnapshotV1"></a>
# **createOnDemandSnapshotV1**
> AsyncRequestStatus createOnDemandSnapshotV1(id, baseOnDemandSnapshotConfig)

Create an on-demand snapshot for a vApp

Start an asynchronous job to create an on-demand snapshot for a specified vApp object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vApp object.
    BaseOnDemandSnapshotConfig baseOnDemandSnapshotConfig = new BaseOnDemandSnapshotConfig(); // BaseOnDemandSnapshotConfig | Configuration for the on-demand backup of a specified vApp object.
    try {
      AsyncRequestStatus result = apiInstance.createOnDemandSnapshotV1(id, baseOnDemandSnapshotConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#createOnDemandSnapshotV1");
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
| **id** | **String**| ID assigned to a vApp object. | |
| **baseOnDemandSnapshotConfig** | [**BaseOnDemandSnapshotConfig**](BaseOnDemandSnapshotConfig.md)| Configuration for the on-demand backup of a specified vApp object. | [optional] |

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
| **202** | Status of the async job for the on-demand snapshot of a vApp. |  -  |

<a id="createVappExportV1"></a>
# **createVappExportV1**
> AsyncRequestStatus createVappExportV1(snapshotId, vappExportSnapshotJobConfig)

Export vApp snapshot

Export the specified vApp snapshot into a new vApp or an existing vApp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String snapshotId = "snapshotId_example"; // String | ID assigned to the vApp snapshot object.
    VappExportSnapshotJobConfig vappExportSnapshotJobConfig = new VappExportSnapshotJobConfig(); // VappExportSnapshotJobConfig | Configuration for the request to export the specified vApp snapshot.
    try {
      AsyncRequestStatus result = apiInstance.createVappExportV1(snapshotId, vappExportSnapshotJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#createVappExportV1");
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
| **snapshotId** | **String**| ID assigned to the vApp snapshot object. | |
| **vappExportSnapshotJobConfig** | [**VappExportSnapshotJobConfig**](VappExportSnapshotJobConfig.md)| Configuration for the request to export the specified vApp snapshot. | |

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
| **202** | Accepted request for asynchronous job to export a vApp snapshot. |  -  |

<a id="createVappInstantRecoveryV1"></a>
# **createVappInstantRecoveryV1**
> AsyncRequestStatus createVappInstantRecoveryV1(snapshotId, vappInstantRecoveryJobConfig)

Instant Recovery of vApp virtual machines

Use Instant Recovery to recover specified vApp virtual machines.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String snapshotId = "snapshotId_example"; // String | ID assigned to the vApp snapshot object.
    VappInstantRecoveryJobConfig vappInstantRecoveryJobConfig = new VappInstantRecoveryJobConfig(); // VappInstantRecoveryJobConfig | Configuration for a request to recover specified virtual machines from a vApp snapshot.
    try {
      AsyncRequestStatus result = apiInstance.createVappInstantRecoveryV1(snapshotId, vappInstantRecoveryJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#createVappInstantRecoveryV1");
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
| **snapshotId** | **String**| ID assigned to the vApp snapshot object. | |
| **vappInstantRecoveryJobConfig** | [**VappInstantRecoveryJobConfig**](VappInstantRecoveryJobConfig.md)| Configuration for a request to recover specified virtual machines from a vApp snapshot. | |

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
| **202** | Status of the async request initiated for the Instant Recovery job for virtual machines in a vApp snapshot. |  -  |

<a id="createVappTemplateSnapshotExport"></a>
# **createVappTemplateSnapshotExport**
> AsyncRequestStatus createVappTemplateSnapshotExport(snapshotId, vappTemplateExportJobConfig)

Export of a vApp template snapshot

Export a vApp template snapashot to a catalog. Use the options endpoint to confirm that exporting to the catalog defaults or the original organization vDC storage profile is possible.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String snapshotId = "snapshotId_example"; // String | ID assigned to a vApp snapshot object.
    VappTemplateExportJobConfig vappTemplateExportJobConfig = new VappTemplateExportJobConfig(); // VappTemplateExportJobConfig | Configuration for a request to export a vApp template snapshot to a specific catalog.
    try {
      AsyncRequestStatus result = apiInstance.createVappTemplateSnapshotExport(snapshotId, vappTemplateExportJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#createVappTemplateSnapshotExport");
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
| **snapshotId** | **String**| ID assigned to a vApp snapshot object. | |
| **vappTemplateExportJobConfig** | [**VappTemplateExportJobConfig**](VappTemplateExportJobConfig.md)| Configuration for a request to export a vApp template snapshot to a specific catalog. | |

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
| **202** | Request status for asynchronous Export job for vApp template snapshot. |  -  |

<a id="createVcdVappDownloadSnapshotFromCloudV1"></a>
# **createVcdVappDownloadSnapshotFromCloudV1**
> AsyncRequestStatus createVcdVappDownloadSnapshotFromCloudV1(id)

Download snapshot from archive

Provides a method for retrieving a snapshot that is not available locally, from an archival location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    try {
      AsyncRequestStatus result = apiInstance.createVcdVappDownloadSnapshotFromCloudV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#createVcdVappDownloadSnapshotFromCloudV1");
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
| **202** | Status of the download request. |  -  |

<a id="deleteVappSnapshotV1"></a>
# **deleteVappSnapshotV1**
> deleteVappSnapshotV1(id, location)

Delete a vApp snapshot

Designate a vApp snapshot as expired and available for garbage collection. The snapshot must be an on-demand snapshot or a snapshot from a vApp that is not assigned to an SLA Domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a snapshot object.
    String location = "all"; // String | Location of the snapshot to delete. Use _local_ to delete only the local copy of the snapshot. Use _all_ to delete the snapshot locally, on a replication target, and at an archival location.
    try {
      apiInstance.deleteVappSnapshotV1(id, location);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#deleteVappSnapshotV1");
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
| **id** | **String**| ID assigned to a snapshot object. | |
| **location** | **String**| Location of the snapshot to delete. Use _local_ to delete only the local copy of the snapshot. Use _all_ to delete the snapshot locally, on a replication target, and at an archival location. | [enum: all, local] |

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
| **204** | Snapshot successfully deleted. |  -  |

<a id="deleteVappSnapshotsV1"></a>
# **deleteVappSnapshotsV1**
> deleteVappSnapshotsV1(id)

Delete all snapshots of vApp

Delete all snapshots for a specified vApp object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vApp object.
    try {
      apiInstance.deleteVappSnapshotsV1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#deleteVappSnapshotsV1");
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
| **id** | **String**| ID assigned to a vApp object. | |

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
| **204** | Snapshots deleted successfully. |  -  |

<a id="getVappAsyncRequestStatusV1"></a>
# **getVappAsyncRequestStatusV1**
> AsyncRequestStatus getVappAsyncRequestStatusV1(id)

Get vApp job status

Retrieve the details of a specified asynchronous job for a vApp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID assigned to an asynchronous job.
    try {
      AsyncRequestStatus result = apiInstance.getVappAsyncRequestStatusV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#getVappAsyncRequestStatusV1");
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
| **id** | **String**| ID assigned to an asynchronous job. | |

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
| **202** | Status of a vApp asynchronous job. |  -  |

<a id="getVappSnapshotExportOptionsV1"></a>
# **getVappSnapshotExportOptionsV1**
> VappExportOptions getVappSnapshotExportOptionsV1(snapshotId, exportMode, targetVappId, targetOrgVdcId)

Get exportable network configurations

Retrieve summary information for the vApp networks that are available for network connections from the virtual machines in the exported vApp snapshot. The summary also specifies the default vApp network for each virtual machine network connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String snapshotId = "snapshotId_example"; // String | ID assigned to the vApp snapshot object to export.
    String exportMode = "ExportToNewVapp"; // String | Target type for the specified vApp export.
    String targetVappId = "targetVappId_example"; // String | ID assigned to the target vApp object, when the export is into an existing vApp. When the export is not into a target vApp, remove the 'target_vapp_id' member.
    String targetOrgVdcId = "targetOrgVdcId_example"; // String | ID assigned to a target organization VDC object. Use the ID when exporting a vApp snapshot to create a new vApp on the specified target organization VDC. When the exported vApp snapshot is not used to create a new vApp on a target organization VDC, remove the 'target_org_vdc_id' member.
    try {
      VappExportOptions result = apiInstance.getVappSnapshotExportOptionsV1(snapshotId, exportMode, targetVappId, targetOrgVdcId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#getVappSnapshotExportOptionsV1");
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
| **snapshotId** | **String**| ID assigned to the vApp snapshot object to export. | |
| **exportMode** | **String**| Target type for the specified vApp export. | [enum: ExportToNewVapp, ExportToTargetVapp] |
| **targetVappId** | **String**| ID assigned to the target vApp object, when the export is into an existing vApp. When the export is not into a target vApp, remove the &#39;target_vapp_id&#39; member. | [optional] |
| **targetOrgVdcId** | **String**| ID assigned to a target organization VDC object. Use the ID when exporting a vApp snapshot to create a new vApp on the specified target organization VDC. When the exported vApp snapshot is not used to create a new vApp on a target organization VDC, remove the &#39;target_org_vdc_id&#39; member. | [optional] |

### Return type

[**VappExportOptions**](VappExportOptions.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | vApp snapshot export options. |  -  |

<a id="getVappSnapshotInstantRecoveryOptionsV1"></a>
# **getVappSnapshotInstantRecoveryOptionsV1**
> VappInstantRecoveryOptions getVappSnapshotInstantRecoveryOptionsV1(snapshotId)

Get Instant Recovery information

Retrieve the available vApp network connections and the default vApp network connection for the virtual machines in a vApp snapshot. Use this information to configure an Instant Recovery of specified virtual machines in the vApp snapshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String snapshotId = "snapshotId_example"; // String | ID assigned to a vApp snapshot object.
    try {
      VappInstantRecoveryOptions result = apiInstance.getVappSnapshotInstantRecoveryOptionsV1(snapshotId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#getVappSnapshotInstantRecoveryOptionsV1");
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
| **snapshotId** | **String**| ID assigned to a vApp snapshot object. | |

### Return type

[**VappInstantRecoveryOptions**](VappInstantRecoveryOptions.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | vApp Instant Recovery options. |  -  |

<a id="getVappSnapshotV1"></a>
# **getVappSnapshotV1**
> VcdVappSnapshotDetail getVappSnapshotV1(id)

Get vApp snapshot details

Retrieve detailed information about a specified snapshot for a vApp object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a snapshot object.
    try {
      VcdVappSnapshotDetail result = apiInstance.getVappSnapshotV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#getVappSnapshotV1");
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
| **id** | **String**| ID assigned to a snapshot object. | |

### Return type

[**VcdVappSnapshotDetail**](VcdVappSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details for a vApp snapshot. |  -  |

<a id="getVappTemplateSnapshotExportOptions"></a>
# **getVappTemplateSnapshotExportOptions**
> VappTemplateExportOptionsUnion getVappTemplateSnapshotExportOptions(snapshotId, catalogId, name, orgVdcId)

Get Export information for a vApp template snapshot

Retrieve the available choices vApp template storage profile and organization vDC choices in case of exporting to either original organization vDC defaults of the target catalog. In case advanced option of manually deciding org vdc is preferred, this also provides available storage profile choices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String snapshotId = "snapshotId_example"; // String | ID assigned to a vApp snapshot object.
    String catalogId = "catalogId_example"; // String | ID of the target catalog object.
    String name = "name_example"; // String | Name of template object to create. This is used to verify the existence of a template with the given name. Templates must have unique names.
    String orgVdcId = "orgVdcId_example"; // String | ID assigned to a target organization vDC object. Use the ID when exporting a vApp template snapshot to a specified organization VDC. This ID is used to fetch the avaiable choices to pick the storage profile of the template. Leave this field empty to use the options from the original organization vDC or the target catalog defaults.
    try {
      VappTemplateExportOptionsUnion result = apiInstance.getVappTemplateSnapshotExportOptions(snapshotId, catalogId, name, orgVdcId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#getVappTemplateSnapshotExportOptions");
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
| **snapshotId** | **String**| ID assigned to a vApp snapshot object. | |
| **catalogId** | **String**| ID of the target catalog object. | |
| **name** | **String**| Name of template object to create. This is used to verify the existence of a template with the given name. Templates must have unique names. | |
| **orgVdcId** | **String**| ID assigned to a target organization vDC object. Use the ID when exporting a vApp template snapshot to a specified organization VDC. This ID is used to fetch the avaiable choices to pick the storage profile of the template. Leave this field empty to use the options from the original organization vDC or the target catalog defaults. | [optional] |

### Return type

[**VappTemplateExportOptionsUnion**](VappTemplateExportOptionsUnion.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | vApp template snapshot export options. |  -  |

<a id="getVcdVappV1"></a>
# **getVcdVappV1**
> VcdVappDetail getVcdVappV1(id)

Get details of a specific vApp

Retrieve detailed information for a specified vApp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vApp object.
    try {
      VcdVappDetail result = apiInstance.getVcdVappV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#getVcdVappV1");
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
| **id** | **String**| ID assigned to a vApp object. | |

### Return type

[**VcdVappDetail**](VcdVappDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information about a vApp object. |  -  |

<a id="queryVappSnapshotV1"></a>
# **queryVappSnapshotV1**
> VcdVappSnapshotSummaryListResponse queryVappSnapshotV1(id)

Get list of snapshots of vApp

Retrieve summary information for each of the snapshot objects of a specified vApp object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vApp object.
    try {
      VcdVappSnapshotSummaryListResponse result = apiInstance.queryVappSnapshotV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#queryVappSnapshotV1");
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
| **id** | **String**| ID assigned to a vApp object. | |

### Return type

[**VcdVappSnapshotSummaryListResponse**](VcdVappSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for all snapshots for a vApp object. |  -  |

<a id="queryVcdVappsV1"></a>
# **queryVcdVappsV1**
> VcdVappSummaryListResponse queryVcdVappsV1(sortBy, sortOrder, limit, offset, name, isRelic, effectiveSlaDomainId, primaryClusterId, slaAssignment, includeBackupTaskInfo)

Get summary for vApps

Retrieve summary information for all vCD vApp objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String sortBy = "Name"; // String | Attribute to sort the vCD vApp list on.
    String sortOrder = "asc"; // String | Order for sorting the results, either ascending or descending.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Number of matches to ignore from the beginning of the results.
    String name = "name_example"; // String | Search for a vCD vApp object by name.
    Boolean isRelic = true; // Boolean | Filter by isRelic field of vCD vApp object. Return both relic and non-relic vApps when this value is not specified.
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter by ID of the effective SLA domain.
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster ID, or **local**.
    String slaAssignment = "Derived"; // String | Filter by SLA assignment type.
    Boolean includeBackupTaskInfo = false; // Boolean | Include backup task information in response.
    try {
      VcdVappSummaryListResponse result = apiInstance.queryVcdVappsV1(sortBy, sortOrder, limit, offset, name, isRelic, effectiveSlaDomainId, primaryClusterId, slaAssignment, includeBackupTaskInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#queryVcdVappsV1");
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
| **sortBy** | **String**| Attribute to sort the vCD vApp list on. | [optional] [enum: Name, EffectiveSlaDomainName, SlaAssignment] |
| **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Number of matches to ignore from the beginning of the results. | [optional] |
| **name** | **String**| Search for a vCD vApp object by name. | [optional] |
| **isRelic** | **Boolean**| Filter by isRelic field of vCD vApp object. Return both relic and non-relic vApps when this value is not specified. | [optional] |
| **effectiveSlaDomainId** | **String**| Filter by ID of the effective SLA domain. | [optional] |
| **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] |
| **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **includeBackupTaskInfo** | **Boolean**| Include backup task information in response. | [optional] [default to false] |

### Return type

[**VcdVappSummaryListResponse**](VcdVappSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for vCD vApps. |  -  |

<a id="searchVappV1"></a>
# **searchVappV1**
> AppSearchResponseListResponse searchVappV1(id, path)

Search for a file in a vApp

Aggregated search for a file through snapshots of all virtual machines that are presently part of the vApp. Specify the file using a full path prefix or a filename prefix.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID of the vApp.
    String path = "path_example"; // String | The path query. Use either a path prefix or a filename prefix.
    try {
      AppSearchResponseListResponse result = apiInstance.searchVappV1(id, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#searchVappV1");
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
| **id** | **String**| ID of the vApp. | |
| **path** | **String**| The path query. Use either a path prefix or a filename prefix. | |

### Return type

[**AppSearchResponseListResponse**](AppSearchResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File search results. |  -  |

<a id="updateVcdVappV1"></a>
# **updateVcdVappV1**
> VcdVappDetail updateVcdVappV1(id, vcdVappPatch)

Update vApp

Make changes to the parameters of a specified vApp object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vApp object.
    VcdVappPatch vcdVappPatch = new VcdVappPatch(); // VcdVappPatch | Parameters to use to update the specified vApp object.
    try {
      VcdVappDetail result = apiInstance.updateVcdVappV1(id, vcdVappPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#updateVcdVappV1");
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
| **id** | **String**| ID assigned to a vApp object. | |
| **vcdVappPatch** | [**VcdVappPatch**](VcdVappPatch.md)| Parameters to use to update the specified vApp object. | |

### Return type

[**VcdVappDetail**](VcdVappDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of an updated vApp object. |  -  |

<a id="vcdMissedSnapshotsV1"></a>
# **vcdMissedSnapshotsV1**
> MissedSnapshotListResponse vcdMissedSnapshotsV1(id)

Get details about missed snapshots for a vApp

Retrieve the timestamp for each missed snapshot for a specified vApp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdVappApi;

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

    VcdVappApi apiInstance = new VcdVappApi(defaultClient);
    String id = "id_example"; // String | ID of the vApp.
    try {
      MissedSnapshotListResponse result = apiInstance.vcdMissedSnapshotsV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdVappApi#vcdMissedSnapshotsV1");
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
| **id** | **String**| ID of the vApp. | |

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
| **200** | Details for missed snapshots for a vApp. |  -  |

