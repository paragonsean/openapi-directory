# UnmanagedObjectApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignToRetentionSlaAsync**](UnmanagedObjectApi.md#assignToRetentionSlaAsync) | **POST** /unmanaged_object/assign_retention_sla | Assign relic/unmanaged entities to an SLA Domain for managing retention asynchronously |
| [**bulkTierExistingSnapshots**](UnmanagedObjectApi.md#bulkTierExistingSnapshots) | **POST** /unmanaged_object/snapshot/bulk_archive_tier | Bulk tier existing snapshots to cold storage |
| [**queryUnmanagedObjectSnapshotsV1**](UnmanagedObjectApi.md#queryUnmanagedObjectSnapshotsV1) | **GET** /unmanaged_object/{id}/snapshot | Get summary of all the snapshots for a given object |
| [**queryUnmanagedObjectV1**](UnmanagedObjectApi.md#queryUnmanagedObjectV1) | **GET** /unmanaged_object | Get summary of all the objects with unmanaged snapshots |
| [**queryUnmanagedReaderObject**](UnmanagedObjectApi.md#queryUnmanagedReaderObject) | **GET** /unmanaged_object/reader_object | Get summary of all unmanaged reader objects |


<a id="assignToRetentionSlaAsync"></a>
# **assignToRetentionSlaAsync**
> List&lt;ManagedObjectPendingSlaInfo&gt; assignToRetentionSlaAsync(unmanagedObjectSlaAssignmentInfo)

Assign relic/unmanaged entities to an SLA Domain for managing retention asynchronously

Assign relic/unmanaged entities to the specified SLA Domain for managing retention. The assignment event runs asynchronously.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UnmanagedObjectApi;

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

    UnmanagedObjectApi apiInstance = new UnmanagedObjectApi(defaultClient);
    UnmanagedObjectSlaAssignmentInfo unmanagedObjectSlaAssignmentInfo = new UnmanagedObjectSlaAssignmentInfo(); // UnmanagedObjectSlaAssignmentInfo | Object with SLA Domain ID and a comma-separated list of the IDs of the relic/unmanaged entities being assigned to the SLA Domain.
    try {
      List<ManagedObjectPendingSlaInfo> result = apiInstance.assignToRetentionSlaAsync(unmanagedObjectSlaAssignmentInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UnmanagedObjectApi#assignToRetentionSlaAsync");
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
| **unmanagedObjectSlaAssignmentInfo** | [**UnmanagedObjectSlaAssignmentInfo**](UnmanagedObjectSlaAssignmentInfo.md)| Object with SLA Domain ID and a comma-separated list of the IDs of the relic/unmanaged entities being assigned to the SLA Domain. | |

### Return type

[**List&lt;ManagedObjectPendingSlaInfo&gt;**](ManagedObjectPendingSlaInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pending SLA Domains resulting from this assignment. |  -  |

<a id="bulkTierExistingSnapshots"></a>
# **bulkTierExistingSnapshots**
> AsyncRequestStatus bulkTierExistingSnapshots(bulkTierSnapshotsConfig)

Bulk tier existing snapshots to cold storage

Schedules a job to tier existing snapshots of the specified objects to cold storage.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UnmanagedObjectApi;

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

    UnmanagedObjectApi apiInstance = new UnmanagedObjectApi(defaultClient);
    BulkTierSnapshotsConfig bulkTierSnapshotsConfig = new BulkTierSnapshotsConfig(); // BulkTierSnapshotsConfig | A list of object IDs to tier. Optionally specifies a location ID.
    try {
      AsyncRequestStatus result = apiInstance.bulkTierExistingSnapshots(bulkTierSnapshotsConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UnmanagedObjectApi#bulkTierExistingSnapshots");
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
| **bulkTierSnapshotsConfig** | [**BulkTierSnapshotsConfig**](BulkTierSnapshotsConfig.md)| A list of object IDs to tier. Optionally specifies a location ID. | |

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
| **202** | Job ID of the TIER_EXISTING_SNAPSHOTS job scheduled. |  -  |

<a id="queryUnmanagedObjectSnapshotsV1"></a>
# **queryUnmanagedObjectSnapshotsV1**
> SnapshotSummaryListResponse queryUnmanagedObjectSnapshotsV1(id, limit, offset, searchValue, snapshotType, beforeDate, afterDate, sortBy, sortOrder)

Get summary of all the snapshots for a given object

Gets summary information for all snapshots of the object with the specified object ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UnmanagedObjectApi;

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

    UnmanagedObjectApi apiInstance = new UnmanagedObjectApi(defaultClient);
    String id = "id_example"; // String | ID of a object.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Ignore these many matches in the beginning.
    String searchValue = "searchValue_example"; // String | Search snapshot by date and time.
    String snapshotType = "OnDemand"; // String | Filter by snapshot type. Valid types are OnDemand, PolicyBased, Retrieved.
    OffsetDateTime beforeDate = OffsetDateTime.now(); // OffsetDateTime | Filter all the snapshots before a date.
    OffsetDateTime afterDate = OffsetDateTime.now(); // OffsetDateTime | Filter all the snapshots after a date.
    String sortBy = "SnapshotDateAndTime"; // String | Sort by given attribute.
    String sortOrder = "asc"; // String | The sort order. The default sort order is ascending.
    try {
      SnapshotSummaryListResponse result = apiInstance.queryUnmanagedObjectSnapshotsV1(id, limit, offset, searchValue, snapshotType, beforeDate, afterDate, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UnmanagedObjectApi#queryUnmanagedObjectSnapshotsV1");
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
| **id** | **String**| ID of a object. | |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Ignore these many matches in the beginning. | [optional] |
| **searchValue** | **String**| Search snapshot by date and time. | [optional] |
| **snapshotType** | **String**| Filter by snapshot type. Valid types are OnDemand, PolicyBased, Retrieved. | [optional] [enum: OnDemand, PolicyBased, Retrieved] |
| **beforeDate** | **OffsetDateTime**| Filter all the snapshots before a date. | [optional] |
| **afterDate** | **OffsetDateTime**| Filter all the snapshots after a date. | [optional] |
| **sortBy** | **String**| Sort by given attribute. | [optional] [enum: SnapshotDateAndTime, LocalExpirationDate, ArchivalLocation] |
| **sortOrder** | **String**| The sort order. The default sort order is ascending. | [optional] [enum: asc, desc] |

### Return type

[**SnapshotSummaryListResponse**](SnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get page summary about snapshots for a given object. |  -  |

<a id="queryUnmanagedObjectV1"></a>
# **queryUnmanagedObjectV1**
> UnmanagedObjectDetailsListResponse queryUnmanagedObjectV1(limit, afterId, searchValue, unmanagedStatus, objectType, sortBy, sortOrder)

Get summary of all the objects with unmanaged snapshots

Get summary of all the objects with unmanaged snapshots.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UnmanagedObjectApi;

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

    UnmanagedObjectApi apiInstance = new UnmanagedObjectApi(defaultClient);
    Integer limit = 56; // Integer | Limit the number of matches returned.
    String afterId = "afterId_example"; // String | First unmanaged object after which objects should be retrieved.
    String searchValue = "searchValue_example"; // String | Filters by the object name using infix search.
    String unmanagedStatus = "Protected"; // String | Filters by object status. Valid status are Protected, Unprotected, and Relic.
    String objectType = "VirtualMachine"; // String | Filter by the type of the unmanaged object.
    String sortBy = "Name"; // String | Sort the result by given attribute.
    String sortOrder = "asc"; // String | The sort order. The default sort order is ascending.
    try {
      UnmanagedObjectDetailsListResponse result = apiInstance.queryUnmanagedObjectV1(limit, afterId, searchValue, unmanagedStatus, objectType, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UnmanagedObjectApi#queryUnmanagedObjectV1");
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
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **afterId** | **String**| First unmanaged object after which objects should be retrieved. | [optional] |
| **searchValue** | **String**| Filters by the object name using infix search. | [optional] |
| **unmanagedStatus** | **String**| Filters by object status. Valid status are Protected, Unprotected, and Relic. | [optional] [enum: Protected, Relic, Unprotected, ReplicatedRelic, RemoteUnprotected] |
| **objectType** | **String**| Filter by the type of the unmanaged object. | [optional] [enum: VirtualMachine, MssqlDatabase, LinuxFileset, WindowsFileset, ShareFileset, NutanixVirtualMachine, HypervVirtualMachine, ManagedVolume, Ec2Instance, StorageArrayVolumeGroup, VcdVapp, LinuxHost, WindowsHost, OracleDatabase, VolumeGroup, AppBlueprint] |
| **sortBy** | **String**| Sort the result by given attribute. | [optional] [enum: Name, UnmanagedStatus, Location, UnmanagedSnapshotCount, LocalStorage, ArchiveStorage, RetentionSlaDomainName, ObjectType, SnapshotCount, AutoSnapshotCount, ManualSnapshotCount] |
| **sortOrder** | **String**| The sort order. The default sort order is ascending. | [optional] [enum: asc, desc] |

### Return type

[**UnmanagedObjectDetailsListResponse**](UnmanagedObjectDetailsListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get page summary about objects with unmanaged snapshots. |  -  |

<a id="queryUnmanagedReaderObject"></a>
# **queryUnmanagedReaderObject**
> UnmanagedObjectSummaryListResponse queryUnmanagedReaderObject(limit, afterId, objectName, unmanagedStatus, objectType, sortBy, sortOrder)

Get summary of all unmanaged reader objects

A summary of all unmanaged objects recovered from reader archival locations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UnmanagedObjectApi;

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

    UnmanagedObjectApi apiInstance = new UnmanagedObjectApi(defaultClient);
    Integer limit = 56; // Integer | Limit the number of matches returned.
    String afterId = "afterId_example"; // String | Retrieve objects after the unmanaged object with the specified ID.
    String objectName = "objectName_example"; // String | Search object by object name.
    String unmanagedStatus = "Protected"; // String | Filters by object status. Valid status are Protected, Unprotected, and Relic.
    String objectType = "VirtualMachine"; // String | Filter by the type of the unmanaged object.
    String sortBy = "Name"; // String | Sort the result by given attribute.
    String sortOrder = "asc"; // String | The sort order. The default sort order is ascending.
    try {
      UnmanagedObjectSummaryListResponse result = apiInstance.queryUnmanagedReaderObject(limit, afterId, objectName, unmanagedStatus, objectType, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UnmanagedObjectApi#queryUnmanagedReaderObject");
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
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **afterId** | **String**| Retrieve objects after the unmanaged object with the specified ID. | [optional] |
| **objectName** | **String**| Search object by object name. | [optional] |
| **unmanagedStatus** | **String**| Filters by object status. Valid status are Protected, Unprotected, and Relic. | [optional] [enum: Protected, Relic, Unprotected, ReplicatedRelic, RemoteUnprotected] |
| **objectType** | **String**| Filter by the type of the unmanaged object. | [optional] [enum: VirtualMachine, MssqlDatabase, LinuxFileset, WindowsFileset, ShareFileset, NutanixVirtualMachine, HypervVirtualMachine, ManagedVolume, Ec2Instance, StorageArrayVolumeGroup, VcdVapp, LinuxHost, WindowsHost, OracleDatabase, VolumeGroup, AppBlueprint] |
| **sortBy** | **String**| Sort the result by given attribute. | [optional] [enum: Name, UnmanagedStatus, Location, UnmanagedSnapshotCount, LocalStorage, ArchiveStorage, RetentionSlaDomainName, ObjectType, SnapshotCount, AutoSnapshotCount, ManualSnapshotCount] |
| **sortOrder** | **String**| The sort order. The default sort order is ascending. | [optional] [enum: asc, desc] |

### Return type

[**UnmanagedObjectSummaryListResponse**](UnmanagedObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a page summary of the unmanaged objects recovered from reader archival locations. |  -  |

