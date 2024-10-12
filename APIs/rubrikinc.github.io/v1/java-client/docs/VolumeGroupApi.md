# VolumeGroupApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOnDemandVolumeGroupBackup**](VolumeGroupApi.md#createOnDemandVolumeGroupBackup) | **POST** /volume_group/{id}/snapshot | Create on-demand snapshot for the Volume Group |
| [**getVolumeGroup**](VolumeGroupApi.md#getVolumeGroup) | **GET** /volume_group/{id} | Get Volume Group details |
| [**getVolumeGroupForceFullSpec**](VolumeGroupApi.md#getVolumeGroupForceFullSpec) | **GET** /volume_group/{id}/request/force_full_snapshot | Retrieve the configuration for forcing a full snapshot |
| [**getVolumeGroupSnapshot**](VolumeGroupApi.md#getVolumeGroupSnapshot) | **GET** /volume_group/snapshot/{id} | Get Volume Group snapshot details |
| [**getVolumeGroupSnapshotMount**](VolumeGroupApi.md#getVolumeGroupSnapshotMount) | **GET** /volume_group/snapshot/mount/{id} | Get summary information for a mount |
| [**patchVolumeGroup**](VolumeGroupApi.md#patchVolumeGroup) | **PATCH** /volume_group/{id} | Update Volume Group properties |
| [**queryVolumeGroup**](VolumeGroupApi.md#queryVolumeGroup) | **GET** /volume_group | Get list of Volume Groups |
| [**queryVolumeGroupLatestSnapshot**](VolumeGroupApi.md#queryVolumeGroupLatestSnapshot) | **GET** /volume_group/{id}/latest_snapshot | Get the latest snapshot of the Volume Group |
| [**queryVolumeGroupSnapshot**](VolumeGroupApi.md#queryVolumeGroupSnapshot) | **GET** /volume_group/{id}/snapshot | Get list of snapshots of the Volume Group |
| [**queryVolumeGroupSnapshotMount**](VolumeGroupApi.md#queryVolumeGroupSnapshotMount) | **GET** /volume_group/snapshot/mount | Get summary information for all mounts |
| [**requestVolumeGroupForceFullSnapshot**](VolumeGroupApi.md#requestVolumeGroupForceFullSnapshot) | **POST** /volume_group/{id}/request/force_full_snapshot | Request a full snapshot on the next backup job of a Volume Group |


<a id="createOnDemandVolumeGroupBackup"></a>
# **createOnDemandVolumeGroupBackup**
> AsyncRequestStatus createOnDemandVolumeGroupBackup(id, volumeGroupOnDemandSnapshotConfig)

Create on-demand snapshot for the Volume Group

Create an on-demand snapshot for the given Volume Group ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String id = "id_example"; // String | The ID of the Volume Group.
    VolumeGroupOnDemandSnapshotConfig volumeGroupOnDemandSnapshotConfig = new VolumeGroupOnDemandSnapshotConfig(); // VolumeGroupOnDemandSnapshotConfig | Configuration for the on-demand backup. Configuration values are `volumeIdsIncludedInSnapshot`, which specifies the unique ID of each volume that is part of this snapshot of the Volume Group, and `slaID`, the ID of the SLA Domain for the snapshot.
    try {
      AsyncRequestStatus result = apiInstance.createOnDemandVolumeGroupBackup(id, volumeGroupOnDemandSnapshotConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#createOnDemandVolumeGroupBackup");
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
| **id** | **String**| The ID of the Volume Group. | |
| **volumeGroupOnDemandSnapshotConfig** | [**VolumeGroupOnDemandSnapshotConfig**](VolumeGroupOnDemandSnapshotConfig.md)| Configuration for the on-demand backup. Configuration values are &#x60;volumeIdsIncludedInSnapshot&#x60;, which specifies the unique ID of each volume that is part of this snapshot of the Volume Group, and &#x60;slaID&#x60;, the ID of the SLA Domain for the snapshot. | [optional] |

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

<a id="getVolumeGroup"></a>
# **getVolumeGroup**
> VolumeGroupDetail getVolumeGroup(id)

Get Volume Group details

Detailed view of a Volume Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String id = "id_example"; // String | The ID of the Volume Group.
    try {
      VolumeGroupDetail result = apiInstance.getVolumeGroup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#getVolumeGroup");
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
| **id** | **String**| The ID of the Volume Group. | |

### Return type

[**VolumeGroupDetail**](VolumeGroupDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return details about the Volume Group. |  -  |

<a id="getVolumeGroupForceFullSpec"></a>
# **getVolumeGroupForceFullSpec**
> VolumeGroupForceFullResponse getVolumeGroupForceFullSpec(id)

Retrieve the configuration for forcing a full snapshot

Retrieve the configuration for forcing a full snapshot for a Volume Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String id = "id_example"; // String | The ID of the Volume Group.
    try {
      VolumeGroupForceFullResponse result = apiInstance.getVolumeGroupForceFullSpec(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#getVolumeGroupForceFullSpec");
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
| **id** | **String**| The ID of the Volume Group. | |

### Return type

[**VolumeGroupForceFullResponse**](VolumeGroupForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the configuration for forcing a full snapshot on the Volume Group. |  -  |

<a id="getVolumeGroupSnapshot"></a>
# **getVolumeGroupSnapshot**
> VolumeGroupSnapshotDetail getVolumeGroupSnapshot(id)

Get Volume Group snapshot details

Retrieve detailed information about a snapshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String id = "id_example"; // String | The ID of the Volume Group snapshot.
    try {
      VolumeGroupSnapshotDetail result = apiInstance.getVolumeGroupSnapshot(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#getVolumeGroupSnapshot");
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
| **id** | **String**| The ID of the Volume Group snapshot. | |

### Return type

[**VolumeGroupSnapshotDetail**](VolumeGroupSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns details about a snapshot. |  -  |

<a id="getVolumeGroupSnapshotMount"></a>
# **getVolumeGroupSnapshotMount**
> VolumeGroupMountSummary getVolumeGroupSnapshotMount(id)

Get summary information for a mount

Retrieve information on a Volume Group mount. The information returned includes the following items, when available. id (the unique ID of the mount), name (the name of the Volume Group), snapshotDate (the snapshot date), sourceVolumeGroupId (The ID of the Volume Group from which this snapshot was created), sourceHostId (the ID of the source host), sourceHostName (the name of the source host), mountedDate (the date when the mount was created), mountedVolumes (the mounted volumes information), targetHostId (the ID of the mounted volumes host), targetHostName (the name of the mounted volumes host), mountRequestId (the ID of the job instance that initiated the mount), unmountRequestId (the ID of the job instance that intiated the request to remove the mount), isReady (whether the Volume Group mount is ready to use), and restoreScriptSmbPath (the link to the script that can perform bare-metal recovery).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String id = "id_example"; // String | The ID of the Volume Group mount.
    try {
      VolumeGroupMountSummary result = apiInstance.getVolumeGroupSnapshotMount(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#getVolumeGroupSnapshotMount");
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
| **id** | **String**| The ID of the Volume Group mount. | |

### Return type

[**VolumeGroupMountSummary**](VolumeGroupMountSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns detail information for a specified live mount. |  -  |

<a id="patchVolumeGroup"></a>
# **patchVolumeGroup**
> VolumeGroupDetail patchVolumeGroup(id, volumeGroupPatch)

Update Volume Group properties

Patch Volume Group with specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String id = "id_example"; // String | The ID of Volume Group.
    VolumeGroupPatch volumeGroupPatch = new VolumeGroupPatch(); // VolumeGroupPatch | Properties to update for this Volume Group.
    try {
      VolumeGroupDetail result = apiInstance.patchVolumeGroup(id, volumeGroupPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#patchVolumeGroup");
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
| **id** | **String**| The ID of Volume Group. | |
| **volumeGroupPatch** | [**VolumeGroupPatch**](VolumeGroupPatch.md)| Properties to update for this Volume Group. | |

### Return type

[**VolumeGroupDetail**](VolumeGroupDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return details about the Volume Group. |  -  |

<a id="queryVolumeGroup"></a>
# **queryVolumeGroup**
> VolumeGroupSummaryListResponse queryVolumeGroup(effectiveSlaDomainId, primaryClusterId, limit, offset, isRelic, name, slaAssignment, sortBy, sortOrder)

Get list of Volume Groups

Get summary of all Volume Groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | The ID of the SLA Domain that controls the protection of the Volume Group.
    String primaryClusterId = "primaryClusterId_example"; // String | The ID of the Rubrik cluster that provides primary protection for the Volume Group.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Ignore these many matches in the beginning.
    Boolean isRelic = true; // Boolean | Specifies whether the results should contain only Volume Groups that are accessible on the Rubrik cluster.
    String name = "name_example"; // String | The name of the Volume Group.
    String slaAssignment = "Derived"; // String | The type of SLA assigned to the Volume Group.
    String sortBy = "name"; // String | The Volume Group attribute to use in storing the responses. Valid attributes are `name` and `effectiveSlaDomainName`.
    String sortOrder = "asc"; // String | The order to sort the responses. Valid choices are asc (ascending) or desc (descending).
    try {
      VolumeGroupSummaryListResponse result = apiInstance.queryVolumeGroup(effectiveSlaDomainId, primaryClusterId, limit, offset, isRelic, name, slaAssignment, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#queryVolumeGroup");
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
| **effectiveSlaDomainId** | **String**| The ID of the SLA Domain that controls the protection of the Volume Group. | [optional] |
| **primaryClusterId** | **String**| The ID of the Rubrik cluster that provides primary protection for the Volume Group. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Ignore these many matches in the beginning. | [optional] |
| **isRelic** | **Boolean**| Specifies whether the results should contain only Volume Groups that are accessible on the Rubrik cluster. | [optional] |
| **name** | **String**| The name of the Volume Group. | [optional] |
| **slaAssignment** | **String**| The type of SLA assigned to the Volume Group. | [optional] [enum: Derived, Direct, Unassigned] |
| **sortBy** | **String**| The Volume Group attribute to use in storing the responses. Valid attributes are &#x60;name&#x60; and &#x60;effectiveSlaDomainName&#x60;. | [optional] [default to name] [enum: name, effectiveSlaDomainName] |
| **sortOrder** | **String**| The order to sort the responses. Valid choices are asc (ascending) or desc (descending). | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**VolumeGroupSummaryListResponse**](VolumeGroupSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Volume Groups summary list. |  -  |

<a id="queryVolumeGroupLatestSnapshot"></a>
# **queryVolumeGroupLatestSnapshot**
> List&lt;VolumeGroupSnapshotSummary&gt; queryVolumeGroupLatestSnapshot(id)

Get the latest snapshot of the Volume Group

Retrieve the latest snapshot summary of a Volume Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String id = "id_example"; // String | ID of the Volume Group.
    try {
      List<VolumeGroupSnapshotSummary> result = apiInstance.queryVolumeGroupLatestSnapshot(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#queryVolumeGroupLatestSnapshot");
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
| **id** | **String**| ID of the Volume Group. | |

### Return type

[**List&lt;VolumeGroupSnapshotSummary&gt;**](VolumeGroupSnapshotSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a summary of a Volume Group&#39;s latest snapshot. Returns an empty array if there is no snapshot summary.  |  -  |

<a id="queryVolumeGroupSnapshot"></a>
# **queryVolumeGroupSnapshot**
> VolumeGroupSnapshotSummaryListResponse queryVolumeGroupSnapshot(id)

Get list of snapshots of the Volume Group

Retrieve snapshot details for a Volume Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String id = "id_example"; // String | The ID of the Volume Group.
    try {
      VolumeGroupSnapshotSummaryListResponse result = apiInstance.queryVolumeGroupSnapshot(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#queryVolumeGroupSnapshot");
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
| **id** | **String**| The ID of the Volume Group. | |

### Return type

[**VolumeGroupSnapshotSummaryListResponse**](VolumeGroupSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns summary information for all snapshots. |  -  |

<a id="queryVolumeGroupSnapshotMount"></a>
# **queryVolumeGroupSnapshotMount**
> VolumeGroupMountSummaryListResponse queryVolumeGroupSnapshotMount(sourceVolumeGroupId, sourceHostName, sortBy, sortOrder, offset, limit)

Get summary information for all mounts

Retrieves information for each Volume Group mount. The information returned includes the following items, when available. id (the unique ID of the mount), name (the name of the Volume Group), snapshotDate (the snapshot date), sourceVolumeGroupId (the ID of the Volume Group from which this snapshot was created), sourceHostId (the ID of the source host), sourceHostName (the name of the source host), mountedDate (the date when the mount was created), mountedVolumes (information on the mounted volumes), targetHostId (the ID of the mounted volumes host), targetHostName (the name of the mounted volumes host), mountRequestId (the ID of the job instance that initiated the mount), unmountRequestId (the ID of the job instance that initiated the request to remove the mount), isReady (whether the Volume Group mount is ready to use), and restoreScriptSmbPath (the link to the script that can perform bare-metal recovery).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String sourceVolumeGroupId = "sourceVolumeGroupId_example"; // String | The ID of the source Volume Group.
    String sourceHostName = "sourceHostName_example"; // String | A prefix of the source host name. The prefix is used as a response filter when available.
    String sortBy = "name"; // String | The Volume Group mount attribute used in sorting the responses. Valid choices are name, sourceHostName, snapshotDate, and mountedDate.
    String sortOrder = "asc"; // String | The order to sort the responses. Valid choices are asc (ascending) or desc (descending).
    Integer offset = 56; // Integer | Ignore these many matches in the beginning.
    Integer limit = 56; // Integer | Limit the number of matches returned. The default value is 25.
    try {
      VolumeGroupMountSummaryListResponse result = apiInstance.queryVolumeGroupSnapshotMount(sourceVolumeGroupId, sourceHostName, sortBy, sortOrder, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#queryVolumeGroupSnapshotMount");
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
| **sourceVolumeGroupId** | **String**| The ID of the source Volume Group. | [optional] |
| **sourceHostName** | **String**| A prefix of the source host name. The prefix is used as a response filter when available. | [optional] |
| **sortBy** | **String**| The Volume Group mount attribute used in sorting the responses. Valid choices are name, sourceHostName, snapshotDate, and mountedDate. | [optional] [enum: name, sourceHostName, snapshotDate, mountedDate] |
| **sortOrder** | **String**| The order to sort the responses. Valid choices are asc (ascending) or desc (descending). | [optional] [default to asc] [enum: asc, desc] |
| **offset** | **Integer**| Ignore these many matches in the beginning. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. The default value is 25. | [optional] |

### Return type

[**VolumeGroupMountSummaryListResponse**](VolumeGroupMountSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns summary information for all mounts. |  -  |

<a id="requestVolumeGroupForceFullSnapshot"></a>
# **requestVolumeGroupForceFullSnapshot**
> VolumeGroupForceFullResponse requestVolumeGroupForceFullSnapshot(id, volumeGroupForceFullRequest)

Request a full snapshot on the next backup job of a Volume Group

Request a full snapshot to be taken during the next backup job of a Volume Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumeGroupApi;

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

    VolumeGroupApi apiInstance = new VolumeGroupApi(defaultClient);
    String id = "id_example"; // String | The ID of the Volume Group.
    VolumeGroupForceFullRequest volumeGroupForceFullRequest = new VolumeGroupForceFullRequest(); // VolumeGroupForceFullRequest | Configuration for forcing a full snapshot on the Volume Group.
    try {
      VolumeGroupForceFullResponse result = apiInstance.requestVolumeGroupForceFullSnapshot(id, volumeGroupForceFullRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumeGroupApi#requestVolumeGroupForceFullSnapshot");
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
| **id** | **String**| The ID of the Volume Group. | |
| **volumeGroupForceFullRequest** | [**VolumeGroupForceFullRequest**](VolumeGroupForceFullRequest.md)| Configuration for forcing a full snapshot on the Volume Group. | |

### Return type

[**VolumeGroupForceFullResponse**](VolumeGroupForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the configuration for forcing a full snapshot on the Volume Group. |  -  |

