# VmwareVmApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchMountSnapshot**](VmwareVmApi.md#batchMountSnapshot) | **POST** /vmware/vm/batch_mount | Live mount a snapshot each from a set of virtual machines |
| [**browseVmwareSnapshot**](VmwareVmApi.md#browseVmwareSnapshot) | **GET** /vmware/vm/snapshot/{id}/browse | List files in VM snapshot |
| [**bulkCreateOnDemandBackup**](VmwareVmApi.md#bulkCreateOnDemandBackup) | **POST** /vmware/vm/snapshot/bulk | Take an on-demand snapshot of multiple virtual machines |
| [**createDownloadFileJob**](VmwareVmApi.md#createDownloadFileJob) | **POST** /vmware/vm/snapshot/{id}/download_file | Download file from VM snapshot |
| [**createDownloadSnapshotFromCloud**](VmwareVmApi.md#createDownloadSnapshotFromCloud) | **POST** /vmware/vm/snapshot/{id}/download | Download snapshot from archive |
| [**createExportV1**](VmwareVmApi.md#createExportV1) | **POST** /vmware/vm/snapshot/{id}/export | Export VM snapshot |
| [**createExportWithDownloadFromCloudV1**](VmwareVmApi.md#createExportWithDownloadFromCloudV1) | **POST** /vmware/vm/snapshot/{id}/export_with_download | Download a snapshot from an archival location, then export a virtual machine using the downloaded snapshot |
| [**createInstantRecovery**](VmwareVmApi.md#createInstantRecovery) | **POST** /vmware/vm/snapshot/{id}/instant_recover | Instantly recover a VM |
| [**createMountV1**](VmwareVmApi.md#createMountV1) | **POST** /vmware/vm/snapshot/{id}/mount | Live mount a VM from a snapshot |
| [**createOnDemandBackup**](VmwareVmApi.md#createOnDemandBackup) | **POST** /vmware/vm/{id}/snapshot | Create an on-demand snapshot for a VM |
| [**createRestoreFileJob**](VmwareVmApi.md#createRestoreFileJob) | **POST** /vmware/vm/snapshot/{id}/restore_file | Restore file from VM snapshot |
| [**createUnmount**](VmwareVmApi.md#createUnmount) | **DELETE** /vmware/vm/snapshot/mount/{id} | Delete a Live Mount VM |
| [**deleteVmwareSnapshot**](VmwareVmApi.md#deleteVmwareSnapshot) | **DELETE** /vmware/vm/snapshot/{id} | Delete VM snapshot |
| [**deleteVmwareSnapshots**](VmwareVmApi.md#deleteVmwareSnapshots) | **DELETE** /vmware/vm/{id}/snapshot | Delete all snapshots of VM |
| [**getAsyncRequestStatus**](VmwareVmApi.md#getAsyncRequestStatus) | **GET** /vmware/vm/request/{id} | Get asynchronous request details for VM |
| [**getMountV1**](VmwareVmApi.md#getMountV1) | **GET** /vmware/vm/snapshot/mount/{id} | Get information for a Live Mount |
| [**getSnapshot**](VmwareVmApi.md#getSnapshot) | **GET** /vmware/vm/snapshot/{id} | Get VM snapshot details |
| [**getVirtualDisk**](VmwareVmApi.md#getVirtualDisk) | **GET** /vmware/vm/virtual_disk/{id} | Details about the specific Virtual Disk |
| [**getVm**](VmwareVmApi.md#getVm) | **GET** /vmware/vm/{id} | Get VM details |
| [**getVmForceFullSpec**](VmwareVmApi.md#getVmForceFullSpec) | **GET** /vmware/vm/{id}/request/force_full_snapshot | Retrieve the configuration for forcing a full snapshot of a VMware virtual machine |
| [**getVmwareCdpLiveInfo**](VmwareVmApi.md#getVmwareCdpLiveInfo) | **POST** /vmware/vm/cdp | Returns the live CDP info for a set of CDP-enabled virtual machines |
| [**getVmwareCdpStateInfo**](VmwareVmApi.md#getVmwareCdpStateInfo) | **POST** /vmware/vm/cdp_state | Returns CDP state info for a set of virtual machines |
| [**getVmwareMissedRecoverableRanges**](VmwareVmApi.md#getVmwareMissedRecoverableRanges) | **GET** /vmware/vm/{id}/missed_recoverable_range | Get missed time ranges for point in time recovery |
| [**getVmwareRecoverableRanges**](VmwareVmApi.md#getVmwareRecoverableRanges) | **GET** /vmware/vm/{id}/recoverable_range | Get available time ranges for point in time recovery |
| [**getVmwareVmMissedRecoverableRangesInBatch**](VmwareVmApi.md#getVmwareVmMissedRecoverableRangesInBatch) | **POST** /vmware/vm/missed_recoverable_range | Returns the recoverable ranges that were missed for a set of CDP-enabled virtual machines |
| [**getVmwareVmRecoverableRangesInBatch**](VmwareVmApi.md#getVmwareVmRecoverableRangesInBatch) | **POST** /vmware/vm/recoverable_range | Returns the recoverable ranges for a set of CDP-enabled virtual machines |
| [**missedSnapshots**](VmwareVmApi.md#missedSnapshots) | **GET** /vmware/vm/{id}/missed_snapshot | Get details about missed snapshots for a VM |
| [**queryMountV1**](VmwareVmApi.md#queryMountV1) | **GET** /vmware/vm/snapshot/mount | Get Live Mount information |
| [**querySnapshot**](VmwareVmApi.md#querySnapshot) | **GET** /vmware/vm/{id}/snapshot | Get list of snapshots of VM |
| [**querySnapshotsForVms**](VmwareVmApi.md#querySnapshotsForVms) | **POST** /vmware/vm/snapshots | Get snapshot information for a list of virtual machines |
| [**queryVm**](VmwareVmApi.md#queryVm) | **GET** /vmware/vm | Get list of VMs |
| [**relocateMount**](VmwareVmApi.md#relocateMount) | **POST** /vmware/vm/snapshot/mount/{id}/relocate | Relocate a virtual machine to another datastore |
| [**requestVmForceFullSnapshot**](VmwareVmApi.md#requestVmForceFullSnapshot) | **POST** /vmware/vm/{id}/request/force_full_snapshot | Request a full snapshot for the next backup job of a VMware virtual machine |
| [**runGuestOsScript**](VmwareVmApi.md#runGuestOsScript) | **POST** /vmware/vm/{id}/guest_script/run | Run guest OS script |
| [**searchVm**](VmwareVmApi.md#searchVm) | **GET** /vmware/vm/{id}/search | Search for a file from a VM |
| [**updateMount**](VmwareVmApi.md#updateMount) | **PATCH** /vmware/vm/snapshot/mount/{id} | Power a Live Mount on and off |
| [**updateVirtualDisk**](VmwareVmApi.md#updateVirtualDisk) | **PATCH** /vmware/vm/virtual_disk/{id} | Update a specific Virtual Disk |
| [**updateVm**](VmwareVmApi.md#updateVm) | **PATCH** /vmware/vm/{id} | Update VM |
| [**vmMakePrimary**](VmwareVmApi.md#vmMakePrimary) | **POST** /vmware/vm/make_primary | Make this cluster the primary for agents on a set of VMs |
| [**vmRegisterAgent**](VmwareVmApi.md#vmRegisterAgent) | **POST** /vmware/vm/{id}/register_agent | Register Rubrik Backup Service |


<a id="batchMountSnapshot"></a>
# **batchMountSnapshot**
> BatchAsyncRequestStatus batchMountSnapshot(batchMountSnapshotJobConfig)

Live mount a snapshot each from a set of virtual machines

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    BatchMountSnapshotJobConfig batchMountSnapshotJobConfig = new BatchMountSnapshotJobConfig(); // BatchMountSnapshotJobConfig | Configuration object containing an array of virtual machine IDs, a way to indicate the snapshot to be chosen and mount configs.
    try {
      BatchAsyncRequestStatus result = apiInstance.batchMountSnapshot(batchMountSnapshotJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#batchMountSnapshot");
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
| **batchMountSnapshotJobConfig** | [**BatchMountSnapshotJobConfig**](BatchMountSnapshotJobConfig.md)| Configuration object containing an array of virtual machine IDs, a way to indicate the snapshot to be chosen and mount configs. | |

### Return type

[**BatchAsyncRequestStatus**](BatchAsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status of the Live Mount requests. |  -  |

<a id="browseVmwareSnapshot"></a>
# **browseVmwareSnapshot**
> BrowseResponseListResponse browseVmwareSnapshot(id, path, offset, limit)

List files in VM snapshot

For a virtual machine snapshot, list the directories and files that are beneath a specified file system path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    String path = "path_example"; // String | The absolute path of the starting point for the directory listing.
    Integer offset = 56; // Integer | Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries.
    Integer limit = 56; // Integer | Maximum number of entries in the response.
    try {
      BrowseResponseListResponse result = apiInstance.browseVmwareSnapshot(id, path, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#browseVmwareSnapshot");
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

<a id="bulkCreateOnDemandBackup"></a>
# **bulkCreateOnDemandBackup**
> BatchAsyncRequestStatus bulkCreateOnDemandBackup(bulkOnDemandSnapshotJobConfig)

Take an on-demand snapshot of multiple virtual machines

Bulk operation of taking on-demand snapshot for given virtual machines.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    BulkOnDemandSnapshotJobConfig bulkOnDemandSnapshotJobConfig = new BulkOnDemandSnapshotJobConfig(); // BulkOnDemandSnapshotJobConfig | The IDs of the virtual machines for which to take an on-demand snapshot and the ID of the SLA Domain to assign to the resulting snapshot.
    try {
      BatchAsyncRequestStatus result = apiInstance.bulkCreateOnDemandBackup(bulkOnDemandSnapshotJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#bulkCreateOnDemandBackup");
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
| **bulkOnDemandSnapshotJobConfig** | [**BulkOnDemandSnapshotJobConfig**](BulkOnDemandSnapshotJobConfig.md)| The IDs of the virtual machines for which to take an on-demand snapshot and the ID of the SLA Domain to assign to the resulting snapshot. | |

### Return type

[**BatchAsyncRequestStatus**](BatchAsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status of the on-demand backup requests. |  -  |

<a id="createDownloadFileJob"></a>
# **createDownloadFileJob**
> AsyncRequestStatus createDownloadFileJob(id, downloadFileJobConfig)

Download file from VM snapshot

Create a request to download a file from a virtual machine snapshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a snapshot.
    DownloadFileJobConfig downloadFileJobConfig = new DownloadFileJobConfig(); // DownloadFileJobConfig | Configuration for the file download request.
    try {
      AsyncRequestStatus result = apiInstance.createDownloadFileJob(id, downloadFileJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#createDownloadFileJob");
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
| **id** | **String**| ID of a snapshot. | |
| **downloadFileJobConfig** | [**DownloadFileJobConfig**](DownloadFileJobConfig.md)| Configuration for the file download request. | |

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
| **202** | Status of the file download request. |  -  |

<a id="createDownloadSnapshotFromCloud"></a>
# **createDownloadSnapshotFromCloud**
> AsyncRequestStatus createDownloadSnapshotFromCloud(id)

Download snapshot from archive

Provides a method for retrieving a snapshot, that is not available locally, from an archival location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    try {
      AsyncRequestStatus result = apiInstance.createDownloadSnapshotFromCloud(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#createDownloadSnapshotFromCloud");
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

<a id="createExportV1"></a>
# **createExportV1**
> AsyncRequestStatus createExportV1(id, exportSnapshotJobConfigV1)

Export VM snapshot

Export a virtual machine from a snapshot, using a specified hypervisor host as the datastore.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a snapshot.
    ExportSnapshotJobConfigV1 exportSnapshotJobConfigV1 = new ExportSnapshotJobConfigV1(); // ExportSnapshotJobConfigV1 | Configuration for the export request.
    try {
      AsyncRequestStatus result = apiInstance.createExportV1(id, exportSnapshotJobConfigV1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#createExportV1");
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
| **id** | **String**| ID of a snapshot. | |
| **exportSnapshotJobConfigV1** | [**ExportSnapshotJobConfigV1**](ExportSnapshotJobConfigV1.md)| Configuration for the export request. | |

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
| **202** | Status of the export request. |  -  |

<a id="createExportWithDownloadFromCloudV1"></a>
# **createExportWithDownloadFromCloudV1**
> AsyncRequestStatus createExportWithDownloadFromCloudV1(id, exportSnapshotJobConfigV1)

Download a snapshot from an archival location, then export a virtual machine using the downloaded snapshot

Download a snapshot from an archival location and then export a virtual machine using the downloaded snapshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a snapshot.
    ExportSnapshotJobConfigV1 exportSnapshotJobConfigV1 = new ExportSnapshotJobConfigV1(); // ExportSnapshotJobConfigV1 | Configuration for the export request.
    try {
      AsyncRequestStatus result = apiInstance.createExportWithDownloadFromCloudV1(id, exportSnapshotJobConfigV1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#createExportWithDownloadFromCloudV1");
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
| **id** | **String**| ID of a snapshot. | |
| **exportSnapshotJobConfigV1** | [**ExportSnapshotJobConfigV1**](ExportSnapshotJobConfigV1.md)| Configuration for the export request. | |

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
| **202** | Status of the download request. |  -  |

<a id="createInstantRecovery"></a>
# **createInstantRecovery**
> AsyncRequestStatus createInstantRecovery(id, instantRecoveryJobConfig)

Instantly recover a VM

Instantly recovery a virtual machine from a snapshot. The Instant Recovery request starts the virtual machine with networking enabled and renames and powers off the source virtual machine, if it still exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of Snapshot.
    InstantRecoveryJobConfig instantRecoveryJobConfig = new InstantRecoveryJobConfig(); // InstantRecoveryJobConfig | Configuration for the Instant Recovery request.
    try {
      AsyncRequestStatus result = apiInstance.createInstantRecovery(id, instantRecoveryJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#createInstantRecovery");
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
| **id** | **String**| ID of Snapshot. | |
| **instantRecoveryJobConfig** | [**InstantRecoveryJobConfig**](InstantRecoveryJobConfig.md)| Configuration for the Instant Recovery request. | |

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
| **202** | Status of the Instant Recovery request. |  -  |

<a id="createMountV1"></a>
# **createMountV1**
> AsyncRequestStatus createMountV1(id, mountSnapshotJobConfigV1)

Live mount a VM from a snapshot

Create a request to Live Mount a virtual machine from a snapshot using a specified configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a snapshot.
    MountSnapshotJobConfigV1 mountSnapshotJobConfigV1 = new MountSnapshotJobConfigV1(); // MountSnapshotJobConfigV1 | Configuration for the Live Mount request.
    try {
      AsyncRequestStatus result = apiInstance.createMountV1(id, mountSnapshotJobConfigV1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#createMountV1");
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
| **id** | **String**| ID of a snapshot. | |
| **mountSnapshotJobConfigV1** | [**MountSnapshotJobConfigV1**](MountSnapshotJobConfigV1.md)| Configuration for the Live Mount request. | [optional] |

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
| **202** | Status of the Live Mount request. |  -  |

<a id="createOnDemandBackup"></a>
# **createOnDemandBackup**
> AsyncRequestStatus createOnDemandBackup(id, baseOnDemandSnapshotConfig)

Create an on-demand snapshot for a VM

Use the ID of a virtual machine to create an on-demand snapshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the virtual machine.
    BaseOnDemandSnapshotConfig baseOnDemandSnapshotConfig = new BaseOnDemandSnapshotConfig(); // BaseOnDemandSnapshotConfig | Configuration for the on-demand snapshot.
    try {
      AsyncRequestStatus result = apiInstance.createOnDemandBackup(id, baseOnDemandSnapshotConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#createOnDemandBackup");
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
| **id** | **String**| ID of the virtual machine. | |
| **baseOnDemandSnapshotConfig** | [**BaseOnDemandSnapshotConfig**](BaseOnDemandSnapshotConfig.md)| Configuration for the on-demand snapshot. | [optional] |

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
| **202** | On-demand snapshot status. |  -  |

<a id="createRestoreFileJob"></a>
# **createRestoreFileJob**
> AsyncRequestStatus createRestoreFileJob(id, restoreFileJobConfig)

Restore file from VM snapshot

Create a request to restore a file or folder to the source virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a snapshot.
    RestoreFileJobConfig restoreFileJobConfig = new RestoreFileJobConfig(); // RestoreFileJobConfig | Configuration for the restore request.
    try {
      AsyncRequestStatus result = apiInstance.createRestoreFileJob(id, restoreFileJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#createRestoreFileJob");
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
| **id** | **String**| ID of a snapshot. | |
| **restoreFileJobConfig** | [**RestoreFileJobConfig**](RestoreFileJobConfig.md)| Configuration for the restore request. | |

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
| **202** | Status of the restore request. |  -  |

<a id="createUnmount"></a>
# **createUnmount**
> AsyncRequestStatus createUnmount(id, force)

Delete a Live Mount VM

Create a request to delete a Live Mount virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a Live Mount.
    Boolean force = true; // Boolean | Force unmount to remove metadata when the datastore of the Live Mount virtual machine was moved off of the Rubrik cluster.
    try {
      AsyncRequestStatus result = apiInstance.createUnmount(id, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#createUnmount");
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
| **id** | **String**| ID of a Live Mount. | |
| **force** | **Boolean**| Force unmount to remove metadata when the datastore of the Live Mount virtual machine was moved off of the Rubrik cluster. | [optional] |

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
| **202** | Status of the delete request. |  -  |

<a id="deleteVmwareSnapshot"></a>
# **deleteVmwareSnapshot**
> deleteVmwareSnapshot(id, location)

Delete VM snapshot

Designate a snapshot as expired and available for garbage collection. The snapshot must be an on-demand snapshot or a snapshot from a virtual machine that is not assigned to an SLA Domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    String location = "all"; // String | Location of the snapshot. Use **_local_** to delete only the local copy of the snapshot. Or use **_all_** to delete the snapshot locally, on a replication target, and at an archival location.
    try {
      apiInstance.deleteVmwareSnapshot(id, location);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#deleteVmwareSnapshot");
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
| **location** | **String**| Location of the snapshot. Use **_local_** to delete only the local copy of the snapshot. Or use **_all_** to delete the snapshot locally, on a replication target, and at an archival location. | [enum: all, local] |

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

<a id="deleteVmwareSnapshots"></a>
# **deleteVmwareSnapshots**
> deleteVmwareSnapshots(id)

Delete all snapshots of VM

Delete all of the snapshots from a virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | Virtual machine ID.
    try {
      apiInstance.deleteVmwareSnapshots(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#deleteVmwareSnapshots");
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
| **id** | **String**| Virtual machine ID. | |

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
| **204** | Snapshots successfully deleted. |  -  |

<a id="getAsyncRequestStatus"></a>
# **getAsyncRequestStatus**
> AsyncRequestStatus getAsyncRequestStatus(id)

Get asynchronous request details for VM

Get the details of an asynchronous request that involves a VMware virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of an asynchronous request.
    try {
      AsyncRequestStatus result = apiInstance.getAsyncRequestStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getAsyncRequestStatus");
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
| **id** | **String**| ID of an asynchronous request. | |

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
| **200** | Status of an asynchronous request. |  -  |

<a id="getMountV1"></a>
# **getMountV1**
> VmwareVmMountDetailV1 getMountV1(id)

Get information for a Live Mount

Retrieve detailed information for a specified Live Mount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a Live Mount.
    try {
      VmwareVmMountDetailV1 result = apiInstance.getMountV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getMountV1");
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
| **id** | **String**| ID of a Live Mount. | |

### Return type

[**VmwareVmMountDetailV1**](VmwareVmMountDetailV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information for the specified Live Mount. |  -  |

<a id="getSnapshot"></a>
# **getSnapshot**
> VmSnapshotDetail getSnapshot(id)

Get VM snapshot details

Retrieve detailed information about a virtual machine snapshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a snapshot.
    try {
      VmSnapshotDetail result = apiInstance.getSnapshot(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getSnapshot");
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
| **id** | **String**| ID of a snapshot. | |

### Return type

[**VmSnapshotDetail**](VmSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Snapshot details. |  -  |

<a id="getVirtualDisk"></a>
# **getVirtualDisk**
> VirtualDiskDetail getVirtualDisk(id)

Details about the specific Virtual Disk

Detailed about the specific Virtual Disk.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the Virtual Disk.
    try {
      VirtualDiskDetail result = apiInstance.getVirtualDisk(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getVirtualDisk");
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
| **id** | **String**| ID of the Virtual Disk. | |

### Return type

[**VirtualDiskDetail**](VirtualDiskDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return details about the virtual disk. |  -  |

<a id="getVm"></a>
# **getVm**
> VirtualMachineDetail getVm(id)

Get VM details

Retrieve details for a virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the virtual machine.
    try {
      VirtualMachineDetail result = apiInstance.getVm(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getVm");
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
| **id** | **String**| ID of the virtual machine. | |

### Return type

[**VirtualMachineDetail**](VirtualMachineDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Virtual machine details. |  -  |

<a id="getVmForceFullSpec"></a>
# **getVmForceFullSpec**
> VmForceFullResponse getVmForceFullSpec(id)

Retrieve the configuration for forcing a full snapshot of a VMware virtual machine

Retrieve the configuration that has been set for forcing a full snapshot for a VMware virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the VMware virtual machine.
    try {
      VmForceFullResponse result = apiInstance.getVmForceFullSpec(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getVmForceFullSpec");
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
| **id** | **String**| ID of the VMware virtual machine. | |

### Return type

[**VmForceFullResponse**](VmForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the configuration for forcing a full snapshot for the VMware virtual machine. |  -  |

<a id="getVmwareCdpLiveInfo"></a>
# **getVmwareCdpLiveInfo**
> BatchVmwareCdpLiveInfo getVmwareCdpLiveInfo(requestBody)

Returns the live CDP info for a set of CDP-enabled virtual machines

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    List<String> requestBody = Arrays.asList(); // List<String> | The ID of each CDP-enabled virtual machine for which live info is being retrieved.
    try {
      BatchVmwareCdpLiveInfo result = apiInstance.getVmwareCdpLiveInfo(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getVmwareCdpLiveInfo");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)| The ID of each CDP-enabled virtual machine for which live info is being retrieved. | |

### Return type

[**BatchVmwareCdpLiveInfo**](BatchVmwareCdpLiveInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the live CDP info for the CDP-enabled virtual machines. |  -  |

<a id="getVmwareCdpStateInfo"></a>
# **getVmwareCdpStateInfo**
> BatchVmwareCdpStateInfo getVmwareCdpStateInfo(requestBody)

Returns CDP state info for a set of virtual machines

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    List<String> requestBody = Arrays.asList(); // List<String> | The ID of each virtual machine for which CDP state info is being retrieved.
    try {
      BatchVmwareCdpStateInfo result = apiInstance.getVmwareCdpStateInfo(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getVmwareCdpStateInfo");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)| The ID of each virtual machine for which CDP state info is being retrieved. | |

### Return type

[**BatchVmwareCdpStateInfo**](BatchVmwareCdpStateInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns CDP state info for the virtual machines. |  -  |

<a id="getVmwareMissedRecoverableRanges"></a>
# **getVmwareMissedRecoverableRanges**
> VmwareRecoverableRangeListResponse getVmwareMissedRecoverableRanges(id, afterTime, beforeTime)

Get missed time ranges for point in time recovery

Gets a list of time ranges to which a CDP-enabled virtual machine cannot perform a point-in-time recovery. The time ranges are indicated by start and end timestamps listed as date-time strings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | The virtual machine ID.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as `2018-01-01T01:23:45.678Z`.
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as `2018-01-01T01:23:45.678Z`.
    try {
      VmwareRecoverableRangeListResponse result = apiInstance.getVmwareMissedRecoverableRanges(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getVmwareMissedRecoverableRanges");
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
| **id** | **String**| The virtual machine ID. | |
| **afterTime** | **OffsetDateTime**| Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] |

### Return type

[**VmwareRecoverableRangeListResponse**](VmwareRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the missed recoverable ranges for the virtual machine. |  -  |

<a id="getVmwareRecoverableRanges"></a>
# **getVmwareRecoverableRanges**
> VmwareRecoverableRangeListResponse getVmwareRecoverableRanges(id, afterTime, beforeTime)

Get available time ranges for point in time recovery

Gets time ranges available for point-in-time recovery. The time ranges are indicated by start and end date-time strings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | The virtual machine ID.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as `2018-01-01T01:23:45.678Z`.
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as `2018-01-01T01:23:45.678Z`.
    try {
      VmwareRecoverableRangeListResponse result = apiInstance.getVmwareRecoverableRanges(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getVmwareRecoverableRanges");
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
| **id** | **String**| The virtual machine ID. | |
| **afterTime** | **OffsetDateTime**| Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] |

### Return type

[**VmwareRecoverableRangeListResponse**](VmwareRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the recoverable ranges for the virtual machine. |  -  |

<a id="getVmwareVmMissedRecoverableRangesInBatch"></a>
# **getVmwareVmMissedRecoverableRangesInBatch**
> BatchVmwareVmMissedRecoverableRanges getVmwareVmMissedRecoverableRangesInBatch(batchVmwareVmMissedRecoverableRangesRequest)

Returns the recoverable ranges that were missed for a set of CDP-enabled virtual machines

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    BatchVmwareVmMissedRecoverableRangesRequest batchVmwareVmMissedRecoverableRangesRequest = new BatchVmwareVmMissedRecoverableRangesRequest(); // BatchVmwareVmMissedRecoverableRangesRequest | The batch request and the date ranges (optional) as a filter. The batch request includes the ID of each CDP-enabled virtual machine for which missed recoverable ranges are being retrieved.
    try {
      BatchVmwareVmMissedRecoverableRanges result = apiInstance.getVmwareVmMissedRecoverableRangesInBatch(batchVmwareVmMissedRecoverableRangesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getVmwareVmMissedRecoverableRangesInBatch");
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
| **batchVmwareVmMissedRecoverableRangesRequest** | [**BatchVmwareVmMissedRecoverableRangesRequest**](BatchVmwareVmMissedRecoverableRangesRequest.md)| The batch request and the date ranges (optional) as a filter. The batch request includes the ID of each CDP-enabled virtual machine for which missed recoverable ranges are being retrieved. | |

### Return type

[**BatchVmwareVmMissedRecoverableRanges**](BatchVmwareVmMissedRecoverableRanges.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the missed recoverable ranges for a set of CDP-enabled virtual machines. |  -  |

<a id="getVmwareVmRecoverableRangesInBatch"></a>
# **getVmwareVmRecoverableRangesInBatch**
> BatchVmwareVmRecoverableRanges getVmwareVmRecoverableRangesInBatch(batchVmwareVmRecoverableRangesRequest)

Returns the recoverable ranges for a set of CDP-enabled virtual machines

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    BatchVmwareVmRecoverableRangesRequest batchVmwareVmRecoverableRangesRequest = new BatchVmwareVmRecoverableRangesRequest(); // BatchVmwareVmRecoverableRangesRequest | The batch request, which includes the ID of each CDP-enabled virtual machine for which recoverable ranges are being retrieved, and optionally the date ranges as a filter.
    try {
      BatchVmwareVmRecoverableRanges result = apiInstance.getVmwareVmRecoverableRangesInBatch(batchVmwareVmRecoverableRangesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#getVmwareVmRecoverableRangesInBatch");
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
| **batchVmwareVmRecoverableRangesRequest** | [**BatchVmwareVmRecoverableRangesRequest**](BatchVmwareVmRecoverableRangesRequest.md)| The batch request, which includes the ID of each CDP-enabled virtual machine for which recoverable ranges are being retrieved, and optionally the date ranges as a filter. | |

### Return type

[**BatchVmwareVmRecoverableRanges**](BatchVmwareVmRecoverableRanges.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the recoverable ranges for a set of CDP-enabled virtual machines. |  -  |

<a id="missedSnapshots"></a>
# **missedSnapshots**
> MissedSnapshotListResponse missedSnapshots(id)

Get details about missed snapshots for a VM

Retrieve details about the missed snapshots for a virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a virtual machine.
    try {
      MissedSnapshotListResponse result = apiInstance.missedSnapshots(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#missedSnapshots");
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
| **id** | **String**| ID of a virtual machine. | |

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
| **200** | Missed snapshot details for a virtual machine. |  -  |

<a id="queryMountV1"></a>
# **queryMountV1**
> VmwareVmMountSummaryV1ListResponse queryMountV1(vmId, offset, limit)

Get Live Mount information

Retrieve summary information about Live Mount activity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String vmId = "vmId_example"; // String | Filters information by virtual machine ID.
    Integer offset = 56; // Integer | Starting position in the list of Live Mount entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of the results.
    Integer limit = 56; // Integer | Limit the summary information to a specified maximum number of entries. Optionally, use with **_offset_** to start the count at a specified point. Default is 25.
    try {
      VmwareVmMountSummaryV1ListResponse result = apiInstance.queryMountV1(vmId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#queryMountV1");
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
| **vmId** | **String**| Filters information by virtual machine ID. | [optional] |
| **offset** | **Integer**| Starting position in the list of Live Mount entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of the results. | [optional] |
| **limit** | **Integer**| Limit the summary information to a specified maximum number of entries. Optionally, use with **_offset_** to start the count at a specified point. Default is 25. | [optional] |

### Return type

[**VmwareVmMountSummaryV1ListResponse**](VmwareVmMountSummaryV1ListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for all Live Mounts. |  -  |

<a id="querySnapshot"></a>
# **querySnapshot**
> VmSnapshotSummaryListResponse querySnapshot(id)

Get list of snapshots of VM

Retrieve summary information for the snapshots of a virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the virtual machine.
    try {
      VmSnapshotSummaryListResponse result = apiInstance.querySnapshot(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#querySnapshot");
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
| **id** | **String**| ID of the virtual machine. | |

### Return type

[**VmSnapshotSummaryListResponse**](VmSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary snapshot information for a virtual machine. |  -  |

<a id="querySnapshotsForVms"></a>
# **querySnapshotsForVms**
> BatchVmSnapshotSummaries querySnapshotsForVms(requestBody)

Get snapshot information for a list of virtual machines

Retrieve snapshot summaries for a list of virtual machines.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    List<String> requestBody = Arrays.asList(); // List<String> | IDs of the virtual machines.
    try {
      BatchVmSnapshotSummaries result = apiInstance.querySnapshotsForVms(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#querySnapshotsForVms");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)| IDs of the virtual machines. | |

### Return type

[**BatchVmSnapshotSummaries**](BatchVmSnapshotSummaries.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Snapshot summaries for a list of virtual machines. |  -  |

<a id="queryVm"></a>
# **queryVm**
> VirtualMachineSummaryListResponse queryVm(effectiveSlaDomainId, primaryClusterId, limit, offset, isRelic, name, moid, slaAssignment, guestOsName, sortBy, sortOrder)

Get list of VMs

Get summary of all the VMs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter by ID of effective SLA Domain.
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster ID, or **local**.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Ignore these many matches in the beginning.
    Boolean isRelic = true; // Boolean | Filter by the isRelic field of the virtual machine. When this parameter is not set, return both relic and non-relic virtual machines.
    String name = "name_example"; // String | Search by using a virtual machine name.
    String moid = "moid_example"; // String | Search by using a virtual machine managed object ID.
    String slaAssignment = "Derived"; // String | Filter by SLA Domain assignment type.
    String guestOsName = "guestOsName_example"; // String | Filters by the name of operating system using infix search.
    String sortBy = "effectiveSlaDomainName"; // String | Sort results based on the specified attribute.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      VirtualMachineSummaryListResponse result = apiInstance.queryVm(effectiveSlaDomainId, primaryClusterId, limit, offset, isRelic, name, moid, slaAssignment, guestOsName, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#queryVm");
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
| **effectiveSlaDomainId** | **String**| Filter by ID of effective SLA Domain. | [optional] |
| **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Ignore these many matches in the beginning. | [optional] |
| **isRelic** | **Boolean**| Filter by the isRelic field of the virtual machine. When this parameter is not set, return both relic and non-relic virtual machines. | [optional] |
| **name** | **String**| Search by using a virtual machine name. | [optional] |
| **moid** | **String**| Search by using a virtual machine managed object ID. | [optional] |
| **slaAssignment** | **String**| Filter by SLA Domain assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **guestOsName** | **String**| Filters by the name of operating system using infix search. | [optional] |
| **sortBy** | **String**| Sort results based on the specified attribute. | [optional] [enum: effectiveSlaDomainName, name, moid, folderPath, infraPath] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |

### Return type

[**VirtualMachineSummaryListResponse**](VirtualMachineSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Virtual machine summary. |  -  |

<a id="relocateMount"></a>
# **relocateMount**
> AsyncRequestStatus relocateMount(id, relocateMountConfig)

Relocate a virtual machine to another datastore

Run storage VMotion to relocate a specified Live Mount into another data store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the live mount.
    RelocateMountConfig relocateMountConfig = new RelocateMountConfig(); // RelocateMountConfig | Configuration for the RelocateMount request to another data store.
    try {
      AsyncRequestStatus result = apiInstance.relocateMount(id, relocateMountConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#relocateMount");
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
| **id** | **String**| ID of the live mount. | |
| **relocateMountConfig** | [**RelocateMountConfig**](RelocateMountConfig.md)| Configuration for the RelocateMount request to another data store. | |

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
| **202** | Status of an asynchronous request to migrate datastore. |  -  |

<a id="requestVmForceFullSnapshot"></a>
# **requestVmForceFullSnapshot**
> VmForceFullResponse requestVmForceFullSnapshot(id, vmForceFullRequest)

Request a full snapshot for the next backup job of a VMware virtual machine

Request a full snapshot to be taken for the next backup job of a VMware virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the VMware virtual machine.
    VmForceFullRequest vmForceFullRequest = new VmForceFullRequest(); // VmForceFullRequest | Configuration for forcing a full snapshot on the VMware virtual machine.
    try {
      VmForceFullResponse result = apiInstance.requestVmForceFullSnapshot(id, vmForceFullRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#requestVmForceFullSnapshot");
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
| **id** | **String**| ID of the VMware virtual machine. | |
| **vmForceFullRequest** | [**VmForceFullRequest**](VmForceFullRequest.md)| Configuration for forcing a full snapshot on the VMware virtual machine. | |

### Return type

[**VmForceFullResponse**](VmForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the response to the request for a forced full snapshot. |  -  |

<a id="runGuestOsScript"></a>
# **runGuestOsScript**
> runGuestOsScript(id, vmGuestScriptRunConfig)

Run guest OS script

Run the specified preBackup, postSnap, or postBackup script in the guest OS of a virtual machine. The script must exist and meet requirements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the virtual machine.
    VmGuestScriptRunConfig vmGuestScriptRunConfig = new VmGuestScriptRunConfig(); // VmGuestScriptRunConfig | Configuration used to run the specified preBackup, postSnap, or postBackup guest OS script.
    try {
      apiInstance.runGuestOsScript(id, vmGuestScriptRunConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#runGuestOsScript");
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
| **id** | **String**| ID of the virtual machine. | |
| **vmGuestScriptRunConfig** | [**VmGuestScriptRunConfig**](VmGuestScriptRunConfig.md)| Configuration used to run the specified preBackup, postSnap, or postBackup guest OS script. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Guest OS script ran successfully and returned a 0 exit code. |  -  |

<a id="searchVm"></a>
# **searchVm**
> SearchResponseListResponse searchVm(id, path, limit, cursor)

Search for a file from a VM

Search for a file in the snapshots of a a virtual machine. Specify the file by full path prefix or filename prefix.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the virtual machine.
    String path = "path_example"; // String | The path query. Use either a path prefix or a filename prefix.
    Integer limit = 56; // Integer | Maximum number of entries in the response.
    String cursor = "cursor_example"; // String | Pagination cursor returned by the previous request.
    try {
      SearchResponseListResponse result = apiInstance.searchVm(id, path, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#searchVm");
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
| **id** | **String**| ID of the virtual machine. | |
| **path** | **String**| The path query. Use either a path prefix or a filename prefix. | |
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
| **200** | File search results. |  -  |

<a id="updateMount"></a>
# **updateMount**
> VmwareVmMountDetailV1 updateMount(id, updateMountConfig)

Power a Live Mount on and off

Power a specified Live Mount virtual machine on or off. Pass **_true_** to power the virtual machine on and pass **_false_** to power the virtual machine off.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of a Live Mount.
    UpdateMountConfig updateMountConfig = new UpdateMountConfig(); // UpdateMountConfig | Power state configuration.
    try {
      VmwareVmMountDetailV1 result = apiInstance.updateMount(id, updateMountConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#updateMount");
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
| **id** | **String**| ID of a Live Mount. | |
| **updateMountConfig** | [**UpdateMountConfig**](UpdateMountConfig.md)| Power state configuration. | |

### Return type

[**VmwareVmMountDetailV1**](VmwareVmMountDetailV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the Live Mount. |  -  |

<a id="updateVirtualDisk"></a>
# **updateVirtualDisk**
> VirtualDiskDetail updateVirtualDisk(id, virtualDiskUpdate)

Update a specific Virtual Disk

Update a specific Virtual Disk.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of the Virtual Disk.
    VirtualDiskUpdate virtualDiskUpdate = new VirtualDiskUpdate(); // VirtualDiskUpdate | Virtual Disk update information.
    try {
      VirtualDiskDetail result = apiInstance.updateVirtualDisk(id, virtualDiskUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#updateVirtualDisk");
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
| **id** | **String**| ID of the Virtual Disk. | |
| **virtualDiskUpdate** | [**VirtualDiskUpdate**](VirtualDiskUpdate.md)| Virtual Disk update information. | |

### Return type

[**VirtualDiskDetail**](VirtualDiskDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated Virtual Disk. |  -  |

<a id="updateVm"></a>
# **updateVm**
> VirtualMachineDetail updateVm(id, virtualMachineUpdateWithSecret)

Update VM

Update a virtual machine with specified properties. Use the guestCredential field to update the guest credential for a specified virtual machine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID of virtual machine.
    VirtualMachineUpdateWithSecret virtualMachineUpdateWithSecret = new VirtualMachineUpdateWithSecret(); // VirtualMachineUpdateWithSecret | Properties to update.
    try {
      VirtualMachineDetail result = apiInstance.updateVm(id, virtualMachineUpdateWithSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#updateVm");
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
| **id** | **String**| ID of virtual machine. | |
| **virtualMachineUpdateWithSecret** | [**VirtualMachineUpdateWithSecret**](VirtualMachineUpdateWithSecret.md)| Properties to update. | |

### Return type

[**VirtualMachineDetail**](VirtualMachineDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Virtual machine details. |  -  |

<a id="vmMakePrimary"></a>
# **vmMakePrimary**
> AsyncRequestStatus vmMakePrimary(requestBody)

Make this cluster the primary for agents on a set of VMs

Migrate the primary cluster with which the agent is able to communicate. For disaster recovery when migrating everything over from another cluster, the /host/make_primary endpoint can be used with the oldPrimaryClusterUuid parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    List<String> requestBody = Arrays.asList(); // List<String> | IDs of hosts to migrate.
    try {
      AsyncRequestStatus result = apiInstance.vmMakePrimary(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#vmMakePrimary");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)| IDs of hosts to migrate. | |

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
| **202** | Asynchronous request for making this cluster primary. |  -  |

<a id="vmRegisterAgent"></a>
# **vmRegisterAgent**
> vmRegisterAgent(id)

Register Rubrik Backup Service

Register the Rubrik Backup Service that is running on a specified host with the specified Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVmApi;

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

    VmwareVmApi apiInstance = new VmwareVmApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a virtual machine object.
    try {
      apiInstance.vmRegisterAgent(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVmApi#vmRegisterAgent");
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
| **id** | **String**| ID assigned to a virtual machine object. | |

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
| **204** | Successfully registered the Rubrik Backup Service for a specified virtual machine. |  -  |

