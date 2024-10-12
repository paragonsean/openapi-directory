# MssqlApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignMssqlSlaProperties**](MssqlApi.md#assignMssqlSlaProperties) | **POST** /mssql/sla_domain/assign | Assign SLA properties to SQL Server objects |
| [**browseMssqlBackupFiles**](MssqlApi.md#browseMssqlBackupFiles) | **POST** /mssql/db/{id}/browse | List snapshots and logs from a Microsoft SQL database |
| [**bulkUpdateMssqlDbV1**](MssqlApi.md#bulkUpdateMssqlDbV1) | **PATCH** /mssql/db/bulk | Update multiple Microsoft SQL databases |
| [**countMssqlDbV1**](MssqlApi.md#countMssqlDbV1) | **GET** /mssql/db/count | Returns a count of Microsoft SQL databases |
| [**countMssqlInstanceV1**](MssqlApi.md#countMssqlInstanceV1) | **GET** /mssql/instance/count | Returns a count of Microsoft SQL instances |
| [**createDownloadMssqlBackupFiles**](MssqlApi.md#createDownloadMssqlBackupFiles) | **POST** /mssql/db/{id}/download_files | Download snapshots and logs backups from a Microsoft SQL Database |
| [**createDownloadMssqlBackupFilesById**](MssqlApi.md#createDownloadMssqlBackupFilesById) | **POST** /mssql/db/{id}/download_files_by_id | Downloads a list of snapshot and log backups from a Microsoft SQL database |
| [**createExportMssqlDb**](MssqlApi.md#createExportMssqlDb) | **POST** /mssql/db/{id}/export | Export a Microsoft SQL database to a new location |
| [**createLogShippingConfiguration**](MssqlApi.md#createLogShippingConfiguration) | **POST** /mssql/db/{id}/log_shipping | Create a log shipping configuration |
| [**createMssqlHostConfig**](MssqlApi.md#createMssqlHostConfig) | **POST** /mssql/host/configuration | Create a SQL Server host configuration |
| [**createMssqlMount**](MssqlApi.md#createMssqlMount) | **POST** /mssql/db/{id}/mount | Live Mount SQL Server database from a point in time copy |
| [**createMssqlUnmount**](MssqlApi.md#createMssqlUnmount) | **DELETE** /mssql/db/mount/{id} | Delete a Live Mount of a SQL Server database |
| [**createOnDemandMssqlBackup**](MssqlApi.md#createOnDemandMssqlBackup) | **POST** /mssql/db/{id}/snapshot | Take an on-demand backup of a Microsoft SQL database |
| [**createOnDemandMssqlBatchBackupV1**](MssqlApi.md#createOnDemandMssqlBatchBackupV1) | **POST** /mssql/db/bulk/snapshot | Take an on-demand backup of multiple Microsoft SQL databases |
| [**createOnDemandMssqlLogBackup**](MssqlApi.md#createOnDemandMssqlLogBackup) | **POST** /mssql/db/{id}/log_backup | Take an on-demand log backup for a Microsoft SQL database |
| [**createRestoreMssqlDb**](MssqlApi.md#createRestoreMssqlDb) | **POST** /mssql/db/{id}/restore | Restore a Microsoft SQL database |
| [**deleteDownloadedMssqlDbRecoverableRangesV1**](MssqlApi.md#deleteDownloadedMssqlDbRecoverableRangesV1) | **DELETE** /mssql/db/{id}/recoverable_range/download | Delete downloaded recoverable ranges of a Microsoft SQL database |
| [**deleteLogShippingConfiguration**](MssqlApi.md#deleteLogShippingConfiguration) | **DELETE** /mssql/db/log_shipping/{id} | Delete a specified log shipping configuration |
| [**deleteMssqlDbSnapshots**](MssqlApi.md#deleteMssqlDbSnapshots) | **DELETE** /mssql/db/{id}/snapshot | Delete all snapshots of a Microsoft SQL database |
| [**deleteMssqlHostConfig**](MssqlApi.md#deleteMssqlHostConfig) | **DELETE** /mssql/host/configuration/{host_id} | Delete the SQL Server host configuration |
| [**downloadFromArchive**](MssqlApi.md#downloadFromArchive) | **POST** /mssql/db/{id}/download | Download snapshots and log backups from archival |
| [**getCompatibleMssqlInstancesV1**](MssqlApi.md#getCompatibleMssqlInstancesV1) | **GET** /mssql/db/{id}/compatible_instance | Get compatible instances for the recovery of a Microsoft SQL database |
| [**getDefaultDbPropertiesV1**](MssqlApi.md#getDefaultDbPropertiesV1) | **GET** /mssql/db/defaults | Returns the current default properties for Microsoft SQL databases |
| [**getDeleteMssqlDbRecoverableRangesStatusV1**](MssqlApi.md#getDeleteMssqlDbRecoverableRangesStatusV1) | **GET** /mssql/db/recoverable_range/download/{id} | Get the deletion status of downloaded recoverable ranges |
| [**getLogShippingConfiguration**](MssqlApi.md#getLogShippingConfiguration) | **GET** /mssql/db/log_shipping/{id} | Get a log shipping configuration |
| [**getMissedMssqlDbSnapshots**](MssqlApi.md#getMissedMssqlDbSnapshots) | **GET** /mssql/db/{id}/missed_snapshot | Get summary information for missed snapshots of a SQL database |
| [**getMssqlAsyncRequestStatus**](MssqlApi.md#getMssqlAsyncRequestStatus) | **GET** /mssql/request/{id} | Get details for an async request |
| [**getMssqlAvailabilityGroupV1**](MssqlApi.md#getMssqlAvailabilityGroupV1) | **GET** /mssql/availability_group/{id} | Returns detailed information for a Microsoft SQL availability group |
| [**getMssqlDb**](MssqlApi.md#getMssqlDb) | **GET** /mssql/db/{id} | Get detailed information for a Microsoft SQL database |
| [**getMssqlDbMissedRecoverableRanges**](MssqlApi.md#getMssqlDbMissedRecoverableRanges) | **GET** /mssql/db/{id}/missed_recoverable_range | Get missed recoverable ranges of a Microsoft SQL database |
| [**getMssqlDbRecoverableRanges**](MssqlApi.md#getMssqlDbRecoverableRanges) | **GET** /mssql/db/{id}/recoverable_range | Get recoverable ranges of a Microsoft SQL database |
| [**getMssqlDbSnapshot**](MssqlApi.md#getMssqlDbSnapshot) | **GET** /mssql/db/snapshot/{id} | Get details information about a Microsoft SQL database snapshot |
| [**getMssqlHierarchyChildren**](MssqlApi.md#getMssqlHierarchyChildren) | **GET** /mssql/hierarchy/{id}/children | Get list of immediate descendant objects |
| [**getMssqlHierarchyDescendants**](MssqlApi.md#getMssqlHierarchyDescendants) | **GET** /mssql/hierarchy/{id}/descendants | Get list of descendant objects |
| [**getMssqlHierarchyObject**](MssqlApi.md#getMssqlHierarchyObject) | **GET** /mssql/hierarchy/{id} | Get summary of a SQL Server hierarchy object |
| [**getMssqlHostConfig**](MssqlApi.md#getMssqlHostConfig) | **GET** /mssql/host/configuration/{host_id} | Get the configuration for a specific host |
| [**getMssqlInstance**](MssqlApi.md#getMssqlInstance) | **GET** /mssql/instance/{id} | Get detailed information for a Microsoft SQL instance |
| [**getMssqlMount**](MssqlApi.md#getMssqlMount) | **GET** /mssql/db/mount/{id} | Get detailed information for a Live Mount of a SQL Server database |
| [**getOnDemandMssqlBatchBackupResultV1**](MssqlApi.md#getOnDemandMssqlBatchBackupResultV1) | **GET** /mssql/db/bulk/snapshot/{id} | Returns details for an on-demand backup of multiple Microsoft SQL databases |
| [**mssqlGetRestoreFilesV1**](MssqlApi.md#mssqlGetRestoreFilesV1) | **GET** /mssql/db/{id}/restore_files | Returns a list all database files to be restored |
| [**mssqlGetSnappableIdV1**](MssqlApi.md#mssqlGetSnappableIdV1) | **GET** /mssql/db/{id}/snappable_id | Returns the snappableId for a Microsoft SQL database |
| [**mssqlRestoreEstimateV1**](MssqlApi.md#mssqlRestoreEstimateV1) | **GET** /mssql/db/{id}/restore_estimate | Returns a size estimate for a restore or export |
| [**queryLogShippingConfigurations**](MssqlApi.md#queryLogShippingConfigurations) | **GET** /mssql/db/log_shipping | Get log shipping configurations |
| [**queryMssqlAvailabilityGroupV1**](MssqlApi.md#queryMssqlAvailabilityGroupV1) | **GET** /mssql/availability_group | Returns summary information for Microsoft SQL availability groups |
| [**queryMssqlDb**](MssqlApi.md#queryMssqlDb) | **GET** /mssql/db | Get summary information for SQL Server databases |
| [**queryMssqlDbSnapshot**](MssqlApi.md#queryMssqlDbSnapshot) | **GET** /mssql/db/{id}/snapshot | Get summary information for snapshots of a Microsoft SQL database |
| [**queryMssqlHostConfig**](MssqlApi.md#queryMssqlHostConfig) | **GET** /mssql/host/configuration | Get the summary of SQL Server host configurations |
| [**queryMssqlInstance**](MssqlApi.md#queryMssqlInstance) | **GET** /mssql/instance | Get summary information for Microsoft SQL instances |
| [**queryMssqlMount**](MssqlApi.md#queryMssqlMount) | **GET** /mssql/db/mount | Get summary information for all Live Mounts SQL Server databases |
| [**reseedSecondary**](MssqlApi.md#reseedSecondary) | **POST** /mssql/db/log_shipping/{id}/reseed | Reseed a secondary database |
| [**updateDefaultDbPropertiesV1**](MssqlApi.md#updateDefaultDbPropertiesV1) | **PATCH** /mssql/db/defaults | Update the default properties for Microsoft SQL databases |
| [**updateLogShippingConfiguration**](MssqlApi.md#updateLogShippingConfiguration) | **PATCH** /mssql/db/log_shipping/{id} | Update a specified log shipping configuration |
| [**updateMssqlAvailabilityGroupV1**](MssqlApi.md#updateMssqlAvailabilityGroupV1) | **PATCH** /mssql/availability_group/{id} | Update a Microsoft SQL availability group |
| [**updateMssqlDb**](MssqlApi.md#updateMssqlDb) | **PATCH** /mssql/db/{id} | Update a Microsoft SQL database |
| [**updateMssqlHostConfig**](MssqlApi.md#updateMssqlHostConfig) | **PATCH** /mssql/host/configuration/{host_id} | Update host configuration |
| [**updateMssqlInstance**](MssqlApi.md#updateMssqlInstance) | **PATCH** /mssql/instance/{id} | Update a Microsoft SQL instance |


<a id="assignMssqlSlaProperties"></a>
# **assignMssqlSlaProperties**
> assignMssqlSlaProperties(mssqlSlaDomainAssignInfo)

Assign SLA properties to SQL Server objects

Assigns SLA Domain properties to SQL Server objects. Hosts and Windows clusters cannot be assigned SLA Domains directly. The SLA Domains are instead applied to the SQL Server child objects within the Host or Windows Cluster object. Newly discovered SQL Server objects within a given Host or Windows Cluster object do not inherit SLA Domain properties from other child SQL Server objects with the same parent object. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    MssqlSlaDomainAssignInfo mssqlSlaDomainAssignInfo = new MssqlSlaDomainAssignInfo(); // MssqlSlaDomainAssignInfo | Update information.
    try {
      apiInstance.assignMssqlSlaProperties(mssqlSlaDomainAssignInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#assignMssqlSlaProperties");
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
| **mssqlSlaDomainAssignInfo** | [**MssqlSlaDomainAssignInfo**](MssqlSlaDomainAssignInfo.md)| Update information. | |

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
| **204** | Successfully assigned SLA Domain properties. |  -  |

<a id="browseMssqlBackupFiles"></a>
# **browseMssqlBackupFiles**
> MssqlBackups browseMssqlBackupFiles(id, mssqlBackupSelection)

List snapshots and logs from a Microsoft SQL database

When a recovery point is set, this API endpoint returns the snapshot and list of logs needed to restore the database to the recovery point. When a time range or LSN range is specified, this API endpoint returns the snapshots and logs that overlap the specified range. Specify only a recovery point or a range. Specify only LSNs or times. This endpoint is only used to fetch data, but uses POST instead of GET due to limitations on parameters used in the body of a GET request. The parameter set for this endpoint is shared with the download_file endpoint. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    MssqlBackupSelection mssqlBackupSelection = new MssqlBackupSelection(); // MssqlBackupSelection | Configuration for the browse request.
    try {
      MssqlBackups result = apiInstance.browseMssqlBackupFiles(id, mssqlBackupSelection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#browseMssqlBackupFiles");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **mssqlBackupSelection** | [**MssqlBackupSelection**](MssqlBackupSelection.md)| Configuration for the browse request. | |

### Return type

[**MssqlBackups**](MssqlBackups.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of backups requested. |  -  |

<a id="bulkUpdateMssqlDbV1"></a>
# **bulkUpdateMssqlDbV1**
> List&lt;MssqlDbDetail&gt; bulkUpdateMssqlDbV1(mssqlDbUpdateId)

Update multiple Microsoft SQL databases

Update multiple Microsoft SQL databases with the specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    List<MssqlDbUpdateId> mssqlDbUpdateId = Arrays.asList(); // List<MssqlDbUpdateId> | Properties to update for each database.
    try {
      List<MssqlDbDetail> result = apiInstance.bulkUpdateMssqlDbV1(mssqlDbUpdateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#bulkUpdateMssqlDbV1");
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
| **mssqlDbUpdateId** | [**List&lt;MssqlDbUpdateId&gt;**](MssqlDbUpdateId.md)| Properties to update for each database. | |

### Return type

[**List&lt;MssqlDbDetail&gt;**](MssqlDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a detailed view of all updated databases. |  -  |

<a id="countMssqlDbV1"></a>
# **countMssqlDbV1**
> ProtectedObjectsCount countMssqlDbV1(rootId)

Returns a count of Microsoft SQL databases

Returns a count of Microsoft SQL databases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String rootId = "rootId_example"; // String | Include only instances that belong to this root.
    try {
      ProtectedObjectsCount result = apiInstance.countMssqlDbV1(rootId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#countMssqlDbV1");
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
| **rootId** | **String**| Include only instances that belong to this root. | [optional] |

### Return type

[**ProtectedObjectsCount**](ProtectedObjectsCount.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

<a id="countMssqlInstanceV1"></a>
# **countMssqlInstanceV1**
> CountResponse countMssqlInstanceV1()

Returns a count of Microsoft SQL instances

Returns a count of all Microsoft SQL instances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    try {
      CountResponse result = apiInstance.countMssqlInstanceV1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#countMssqlInstanceV1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountResponse**](CountResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

<a id="createDownloadMssqlBackupFiles"></a>
# **createDownloadMssqlBackupFiles**
> AsyncRequestStatus createDownloadMssqlBackupFiles(id, mssqlBackupSelection)

Download snapshots and logs backups from a Microsoft SQL Database

Starts an asynchronous request to download a set of backup files as a single compressed zipfile. When a recovery point is set, this API endpoint returns the snapshot and list of logs that Rubrik CDM would use to restore the database to the recovery point. When a time range or LSN range is specified, this API endpoint returns the snapshots and logs that overlap the specified range. Specify only a point in time or a range. Specify only LSNs or times. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    MssqlBackupSelection mssqlBackupSelection = new MssqlBackupSelection(); // MssqlBackupSelection | Configuration for a download files job.
    try {
      AsyncRequestStatus result = apiInstance.createDownloadMssqlBackupFiles(id, mssqlBackupSelection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createDownloadMssqlBackupFiles");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **mssqlBackupSelection** | [**MssqlBackupSelection**](MssqlBackupSelection.md)| Configuration for a download files job. | |

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

<a id="createDownloadMssqlBackupFilesById"></a>
# **createDownloadMssqlBackupFilesById**
> AsyncRequestStatus createDownloadMssqlBackupFilesById(id, downloadMssqlBackupFilesByIdJobConfig)

Downloads a list of snapshot and log backups from a Microsoft SQL database

Downloads a list of snapshot and log backups from a Microsoft SQL database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    DownloadMssqlBackupFilesByIdJobConfig downloadMssqlBackupFilesByIdJobConfig = new DownloadMssqlBackupFilesByIdJobConfig(); // DownloadMssqlBackupFilesByIdJobConfig | Configuration for a download files by id job.
    try {
      AsyncRequestStatus result = apiInstance.createDownloadMssqlBackupFilesById(id, downloadMssqlBackupFilesByIdJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createDownloadMssqlBackupFilesById");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **downloadMssqlBackupFilesByIdJobConfig** | [**DownloadMssqlBackupFilesByIdJobConfig**](DownloadMssqlBackupFilesByIdJobConfig.md)| Configuration for a download files by id job. | |

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

<a id="createExportMssqlDb"></a>
# **createExportMssqlDb**
> AsyncRequestStatus createExportMssqlDb(id, exportMssqlDbJobConfig)

Export a Microsoft SQL database to a new location

Create a request to export a Microsoft SQL database. To check the result of the request, poll /mssql/request/{id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    ExportMssqlDbJobConfig exportMssqlDbJobConfig = new ExportMssqlDbJobConfig(); // ExportMssqlDbJobConfig | Configuration for the export.
    try {
      AsyncRequestStatus result = apiInstance.createExportMssqlDb(id, exportMssqlDbJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createExportMssqlDb");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **exportMssqlDbJobConfig** | [**ExportMssqlDbJobConfig**](ExportMssqlDbJobConfig.md)| Configuration for the export. | |

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
| **202** | Returns the async request for the initiated export. |  -  |

<a id="createLogShippingConfiguration"></a>
# **createLogShippingConfiguration**
> AsyncRequestStatus createLogShippingConfiguration(id, mssqlLogShippingCreateConfig)

Create a log shipping configuration

Create a log shipping configuration between a specified primary database and a specified secondary database. The transaction logs from the primary database are regularly restored to the secondary database in order to maintain the secondary database as a point-in-time copy of the primary database. The primary database must have log backups configured, and it must be in the full or bulk-logged recovery model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the primary database object.
    MssqlLogShippingCreateConfig mssqlLogShippingCreateConfig = new MssqlLogShippingCreateConfig(); // MssqlLogShippingCreateConfig | Object containing the values of a log shipping configuration.
    try {
      AsyncRequestStatus result = apiInstance.createLogShippingConfiguration(id, mssqlLogShippingCreateConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createLogShippingConfiguration");
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
| **id** | **String**| ID of the primary database object. | |
| **mssqlLogShippingCreateConfig** | [**MssqlLogShippingCreateConfig**](MssqlLogShippingCreateConfig.md)| Object containing the values of a log shipping configuration. | |

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
| **202** | Returned when the specified log shipping configuration is successfully applied. |  -  |

<a id="createMssqlHostConfig"></a>
# **createMssqlHostConfig**
> MssqlHostConfiguration createMssqlHostConfig(mssqlHostConfigurationWithHostId)

Create a SQL Server host configuration

Creates a SQL Server host configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    MssqlHostConfigurationWithHostId mssqlHostConfigurationWithHostId = new MssqlHostConfigurationWithHostId(); // MssqlHostConfigurationWithHostId | Parameters for creating a SQL Server host configuration.
    try {
      MssqlHostConfiguration result = apiInstance.createMssqlHostConfig(mssqlHostConfigurationWithHostId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createMssqlHostConfig");
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
| **mssqlHostConfigurationWithHostId** | [**MssqlHostConfigurationWithHostId**](MssqlHostConfigurationWithHostId.md)| Parameters for creating a SQL Server host configuration. | |

### Return type

[**MssqlHostConfiguration**](MssqlHostConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Details of the new SQL Server host configuration. |  -  |

<a id="createMssqlMount"></a>
# **createMssqlMount**
> AsyncRequestStatus createMssqlMount(id, mountMssqlDbConfig)

Live Mount SQL Server database from a point in time copy

Create an asynchronous request to create a Live Mount SQL Server database. Poll the task status by using /mssql/request/{id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the SQL Server database.
    MountMssqlDbConfig mountMssqlDbConfig = new MountMssqlDbConfig(); // MountMssqlDbConfig | Configuration for the Live Mount.
    try {
      AsyncRequestStatus result = apiInstance.createMssqlMount(id, mountMssqlDbConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createMssqlMount");
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
| **id** | **String**| ID of the SQL Server database. | |
| **mountMssqlDbConfig** | [**MountMssqlDbConfig**](MountMssqlDbConfig.md)| Configuration for the Live Mount. | |

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
| **202** | Returns the asynchronous task object for the Live Mount request. |  -  |

<a id="createMssqlUnmount"></a>
# **createMssqlUnmount**
> AsyncRequestStatus createMssqlUnmount(id, force)

Delete a Live Mount of a SQL Server database

Create an async request to delete a Live Mount of a SQL Server database. Poll the task status by using /mssql/request/{id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Live Mount to delete.
    Boolean force = true; // Boolean | Remove all data within the Rubrik cluster related to the Live Mount, even if the SQL Server database cannot be contacted. Default value is false.
    try {
      AsyncRequestStatus result = apiInstance.createMssqlUnmount(id, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createMssqlUnmount");
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
| **id** | **String**| ID of the Live Mount to delete. | |
| **force** | **Boolean**| Remove all data within the Rubrik cluster related to the Live Mount, even if the SQL Server database cannot be contacted. Default value is false. | [optional] |

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
| **202** | Returns the task object for the async request to delete the Live Mount of a SQL Server database. |  -  |

<a id="createOnDemandMssqlBackup"></a>
# **createOnDemandMssqlBackup**
> AsyncRequestStatus createOnDemandMssqlBackup(id, mssqlBackupJobConfig)

Take an on-demand backup of a Microsoft SQL database

Take an on-demand backup of a Microsoft SQL database. The forceFullSnapshot property can be set to true to force a full snapshot. To check the result of the request, poll /mssql/request/{id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    MssqlBackupJobConfig mssqlBackupJobConfig = new MssqlBackupJobConfig(); // MssqlBackupJobConfig | Configuration for the on-demand backup.
    try {
      AsyncRequestStatus result = apiInstance.createOnDemandMssqlBackup(id, mssqlBackupJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createOnDemandMssqlBackup");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **mssqlBackupJobConfig** | [**MssqlBackupJobConfig**](MssqlBackupJobConfig.md)| Configuration for the on-demand backup. | |

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
| **202** | Returns the async request for the initiated on-demand backup. |  -  |

<a id="createOnDemandMssqlBatchBackupV1"></a>
# **createOnDemandMssqlBatchBackupV1**
> AsyncRequestStatus createOnDemandMssqlBatchBackupV1(mssqlBatchBackupJobConfig)

Take an on-demand backup of multiple Microsoft SQL databases

Take an on-demand backup of one or more Microsoft SQL databases. Set the forceFullSnapshot property to true to force a full snapshot for every database that is specified. Only one snapshot will be taken for each database, even if a database is included multiple times in the fields of the request body. To check the result of the request, poll /mssql/request/{id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    MssqlBatchBackupJobConfig mssqlBatchBackupJobConfig = new MssqlBatchBackupJobConfig(); // MssqlBatchBackupJobConfig | Configuration for the on-demand backups.
    try {
      AsyncRequestStatus result = apiInstance.createOnDemandMssqlBatchBackupV1(mssqlBatchBackupJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createOnDemandMssqlBatchBackupV1");
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
| **mssqlBatchBackupJobConfig** | [**MssqlBatchBackupJobConfig**](MssqlBatchBackupJobConfig.md)| Configuration for the on-demand backups. | |

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
| **202** | Returns the async request for the initiated on-demand backups. |  -  |

<a id="createOnDemandMssqlLogBackup"></a>
# **createOnDemandMssqlLogBackup**
> AsyncRequestStatus createOnDemandMssqlLogBackup(id)

Take an on-demand log backup for a Microsoft SQL database

Take an on-demand log backup for a Microsoft SQL database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    try {
      AsyncRequestStatus result = apiInstance.createOnDemandMssqlLogBackup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createOnDemandMssqlLogBackup");
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
| **id** | **String**| ID of the Microsoft SQL database. | |

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
| **202** | Returns the async request for the initiated on-demand log backup. |  -  |

<a id="createRestoreMssqlDb"></a>
# **createRestoreMssqlDb**
> AsyncRequestStatus createRestoreMssqlDb(id, restoreMssqlDbJobConfig)

Restore a Microsoft SQL database

Create a request to restore a SQL Server database. To check the result of the request, poll /mssql/request/{id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    RestoreMssqlDbJobConfig restoreMssqlDbJobConfig = new RestoreMssqlDbJobConfig(); // RestoreMssqlDbJobConfig | Restore configuration.
    try {
      AsyncRequestStatus result = apiInstance.createRestoreMssqlDb(id, restoreMssqlDbJobConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#createRestoreMssqlDb");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **restoreMssqlDbJobConfig** | [**RestoreMssqlDbJobConfig**](RestoreMssqlDbJobConfig.md)| Restore configuration. | |

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
| **202** | Returns the async request for the initiated restore. |  -  |

<a id="deleteDownloadedMssqlDbRecoverableRangesV1"></a>
# **deleteDownloadedMssqlDbRecoverableRangesV1**
> JobScheduledResponse deleteDownloadedMssqlDbRecoverableRangesV1(id, afterTime, beforeTime)

Delete downloaded recoverable ranges of a Microsoft SQL database

Deletes all local snapshots and logs that have previously been downloaded. Provide a begin or end time to delete only the downloaded snapshots and logs that fall within this time frame. The time is relative to when the snapshot or log backup was originally taken, not downloaded. Parts of the window may not be deleted if certain log files must be kept to preserve times outside the window. Data is deleted in the background. To check the status of the deletion, poll /mssql/db/recoverable_range/download/{id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Delete only the downloaded snapshots and logs taken after this time. The date-time string should be in ISO8601 format. For example, \"2016-01-01T01:23:45.678\".
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Delete only the downloaded snapshots and logs taken before this time. The date-time string should be in ISO8601 format. For example, \"2016-01-01T01:23:45.678\".
    try {
      JobScheduledResponse result = apiInstance.deleteDownloadedMssqlDbRecoverableRangesV1(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#deleteDownloadedMssqlDbRecoverableRangesV1");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **afterTime** | **OffsetDateTime**| Delete only the downloaded snapshots and logs taken after this time. The date-time string should be in ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Delete only the downloaded snapshots and logs taken before this time. The date-time string should be in ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |

### Return type

[**JobScheduledResponse**](JobScheduledResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Returns the job ID to check the progress of deleting the downloaded snapshots and logs. |  -  |

<a id="deleteLogShippingConfiguration"></a>
# **deleteLogShippingConfiguration**
> AsyncRequestStatus deleteLogShippingConfiguration(id, deleteSecondaryDatabase)

Delete a specified log shipping configuration

Deletes the specified log shipping configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of a log shipping configuration object.
    Boolean deleteSecondaryDatabase = true; // Boolean | Boolean value that determines whether to attempt to delete the secondary database associated with the specified log shipping configuration. The default value is false. When set to false, no attempt is made to delete the secondary database. When set to true, starts an asynchronous job to delete the secondary database.
    try {
      AsyncRequestStatus result = apiInstance.deleteLogShippingConfiguration(id, deleteSecondaryDatabase);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#deleteLogShippingConfiguration");
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
| **id** | **String**| ID of a log shipping configuration object. | |
| **deleteSecondaryDatabase** | **Boolean**| Boolean value that determines whether to attempt to delete the secondary database associated with the specified log shipping configuration. The default value is false. When set to false, no attempt is made to delete the secondary database. When set to true, starts an asynchronous job to delete the secondary database. | [optional] |

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
| **202** | Returns with the request ID of an async job to delete a log shipping configuration object and, if specified, a secondary database. |  -  |

<a id="deleteMssqlDbSnapshots"></a>
# **deleteMssqlDbSnapshots**
> deleteMssqlDbSnapshots(id)

Delete all snapshots of a Microsoft SQL database

Deletes all snapshots of a Microsoft SQL database. The database must be unprotected for the operation to succeed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    try {
      apiInstance.deleteMssqlDbSnapshots(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#deleteMssqlDbSnapshots");
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
| **id** | **String**| ID of the Microsoft SQL database. | |

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
| **204** | Returned if all snapshots for the Microsoft SQL database were successfully removed. |  -  |

<a id="deleteMssqlHostConfig"></a>
# **deleteMssqlHostConfig**
> deleteMssqlHostConfig(hostId)

Delete the SQL Server host configuration

Deletes the SQL Server host configuration. The host falls back to use values from the global configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String hostId = "hostId_example"; // String | ID of the host.
    try {
      apiInstance.deleteMssqlHostConfig(hostId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#deleteMssqlHostConfig");
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
| **hostId** | **String**| ID of the host. | |

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
| **204** | SQL Server host configuration deleted successfully. |  -  |

<a id="downloadFromArchive"></a>
# **downloadFromArchive**
> AsyncRequestStatus downloadFromArchive(id, mssqlDownloadFromArchiveConfig)

Download snapshots and log backups from archival

Starts an asynchronous request to download snapshots and logs from archival for a given database and recovery point. If the specified point in time is already available locally, this endpoint throws an error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    MssqlDownloadFromArchiveConfig mssqlDownloadFromArchiveConfig = new MssqlDownloadFromArchiveConfig(); // MssqlDownloadFromArchiveConfig | Configuration for the archive download request.
    try {
      AsyncRequestStatus result = apiInstance.downloadFromArchive(id, mssqlDownloadFromArchiveConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#downloadFromArchive");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **mssqlDownloadFromArchiveConfig** | [**MssqlDownloadFromArchiveConfig**](MssqlDownloadFromArchiveConfig.md)| Configuration for the archive download request. | |

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

<a id="getCompatibleMssqlInstancesV1"></a>
# **getCompatibleMssqlInstancesV1**
> MssqlInstanceSummaryListResponse getCompatibleMssqlInstancesV1(id, recoveryType, recoveryTime)

Get compatible instances for the recovery of a Microsoft SQL database

Returns all compatible instances for export for the specified recovery time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    String recoveryType = "Mount"; // String | Recovery type.
    OffsetDateTime recoveryTime = OffsetDateTime.now(); // OffsetDateTime | Time, in ISO8601 format, to recover to. For example \"2016-01-01T01:23:45.678Z\". If this is not specified, the latest recoverable time is used.
    try {
      MssqlInstanceSummaryListResponse result = apiInstance.getCompatibleMssqlInstancesV1(id, recoveryType, recoveryTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getCompatibleMssqlInstancesV1");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **recoveryType** | **String**| Recovery type. | [enum: Mount, Export, Restore] |
| **recoveryTime** | **OffsetDateTime**| Time, in ISO8601 format, to recover to. For example \&quot;2016-01-01T01:23:45.678Z\&quot;. If this is not specified, the latest recoverable time is used. | [optional] |

### Return type

[**MssqlInstanceSummaryListResponse**](MssqlInstanceSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns summary information for all compatible Microsoft SQL instances for export. |  -  |

<a id="getDefaultDbPropertiesV1"></a>
# **getDefaultDbPropertiesV1**
> MssqlDbDefaults getDefaultDbPropertiesV1()

Returns the current default properties for Microsoft SQL databases

The default properties are Log Backup Frequency (in seconds), Log Retention Time (in hours) and CBT status. New databases added to the Rubrik cluster are provided the log backup frequency value and log backup retention value by default. New hosts added to the Rubrik cluster are provided the CBT status by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    try {
      MssqlDbDefaults result = apiInstance.getDefaultDbPropertiesV1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getDefaultDbPropertiesV1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MssqlDbDefaults**](MssqlDbDefaults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the current default properties. |  -  |

<a id="getDeleteMssqlDbRecoverableRangesStatusV1"></a>
# **getDeleteMssqlDbRecoverableRangesStatusV1**
> InternalJobInstanceDetail getDeleteMssqlDbRecoverableRangesStatusV1(id)

Get the deletion status of downloaded recoverable ranges

Get the details of the progress made in deleting recoverable ranges. The recoverable ranges to delete are those specified by the DELETE request to /mssql/db/{id}/recoverable_range/download which yielded the response with the job id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | Job ID of the deletion for which to check progress.
    try {
      InternalJobInstanceDetail result = apiInstance.getDeleteMssqlDbRecoverableRangesStatusV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getDeleteMssqlDbRecoverableRangesStatusV1");
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
| **id** | **String**| Job ID of the deletion for which to check progress. | |

### Return type

[**InternalJobInstanceDetail**](InternalJobInstanceDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the progress made in deleting the recoverable ranges. |  -  |

<a id="getLogShippingConfiguration"></a>
# **getLogShippingConfiguration**
> MssqlLogShippingDetail getLogShippingConfiguration(id)

Get a log shipping configuration

Retrieves a particular log shipping configuration with all the details of the configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of a log shipping configuration.
    try {
      MssqlLogShippingDetail result = apiInstance.getLogShippingConfiguration(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getLogShippingConfiguration");
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
| **id** | **String**| ID of a log shipping configuration. | |

### Return type

[**MssqlLogShippingDetail**](MssqlLogShippingDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned when the request for the log shipping configuration details is successful. |  -  |

<a id="getMissedMssqlDbSnapshots"></a>
# **getMissedMssqlDbSnapshots**
> MissedSnapshotListResponse getMissedMssqlDbSnapshots(id, afterTime, beforeTime)

Get summary information for missed snapshots of a SQL database

Returns a list of summary information for the missed snapshots of a Microsoft SQL database, including the time of day and the locations where the snapshot was missed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter snapshots to those missed on or after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter snapshots to those missed on or before this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
    try {
      MissedSnapshotListResponse result = apiInstance.getMissedMssqlDbSnapshots(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMissedMssqlDbSnapshots");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **afterTime** | **OffsetDateTime**| Filter snapshots to those missed on or after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter snapshots to those missed on or before this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |

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
| **200** | Returns details about the missed snapshots. |  -  |

<a id="getMssqlAsyncRequestStatus"></a>
# **getMssqlAsyncRequestStatus**
> AsyncRequestStatus getMssqlAsyncRequestStatus(id)

Get details for an async request

Returns the task object for an async request related to SQL Server databases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the async request.
    try {
      AsyncRequestStatus result = apiInstance.getMssqlAsyncRequestStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlAsyncRequestStatus");
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
| **id** | **String**| ID of the async request. | |

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
| **200** | Status of the async request. |  -  |

<a id="getMssqlAvailabilityGroupV1"></a>
# **getMssqlAvailabilityGroupV1**
> MssqlAvailabilityGroupDetail getMssqlAvailabilityGroupV1(id)

Returns detailed information for a Microsoft SQL availability group

Returns a detailed view of a Microsoft SQL availability group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL availability group to fetch.
    try {
      MssqlAvailabilityGroupDetail result = apiInstance.getMssqlAvailabilityGroupV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlAvailabilityGroupV1");
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
| **id** | **String**| ID of the Microsoft SQL availability group to fetch. | |

### Return type

[**MssqlAvailabilityGroupDetail**](MssqlAvailabilityGroupDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

<a id="getMssqlDb"></a>
# **getMssqlDb**
> MssqlDbDetail getMssqlDb(id)

Get detailed information for a Microsoft SQL database

Returns a detailed view of a Microsoft SQL database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database to fetch.
    try {
      MssqlDbDetail result = apiInstance.getMssqlDb(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlDb");
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
| **id** | **String**| ID of the Microsoft SQL database to fetch. | |

### Return type

[**MssqlDbDetail**](MssqlDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

<a id="getMssqlDbMissedRecoverableRanges"></a>
# **getMssqlDbMissedRecoverableRanges**
> MssqlMissedRecoverableRangeListResponse getMssqlDbMissedRecoverableRanges(id, afterTime, beforeTime)

Get missed recoverable ranges of a Microsoft SQL database

Retrieve a list of missed recoverable ranges for a Microsoft SQL database. For each run of one type of error, the first and last occurrence of the error are given.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter the missed ranges to end after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter the missed ranges to start before this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
    try {
      MssqlMissedRecoverableRangeListResponse result = apiInstance.getMssqlDbMissedRecoverableRanges(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlDbMissedRecoverableRanges");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **afterTime** | **OffsetDateTime**| Filter the missed ranges to end after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter the missed ranges to start before this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |

### Return type

[**MssqlMissedRecoverableRangeListResponse**](MssqlMissedRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the missed recoverable ranges for the Microsoft SQL database. |  -  |

<a id="getMssqlDbRecoverableRanges"></a>
# **getMssqlDbRecoverableRanges**
> MssqlRecoverableRangeListResponse getMssqlDbRecoverableRanges(id, afterTime, beforeTime)

Get recoverable ranges of a Microsoft SQL database

Retrieve the recoverable ranges for a specified Microsoft SQL database. A begin and/or end timestamp can be provided to retrieve only the ranges that fall within the window.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678Z\".
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
    try {
      MssqlRecoverableRangeListResponse result = apiInstance.getMssqlDbRecoverableRanges(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlDbRecoverableRanges");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **afterTime** | **OffsetDateTime**| Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678Z\&quot;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |

### Return type

[**MssqlRecoverableRangeListResponse**](MssqlRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the recoverable ranges for the Microsoft SQL database. |  -  |

<a id="getMssqlDbSnapshot"></a>
# **getMssqlDbSnapshot**
> MssqlDbSnapshotDetail getMssqlDbSnapshot(id)

Get details information about a Microsoft SQL database snapshot

Returns detailed information about a Microsoft SQL database snapshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the snapshot.
    try {
      MssqlDbSnapshotDetail result = apiInstance.getMssqlDbSnapshot(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlDbSnapshot");
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
| **id** | **String**| ID of the snapshot. | |

### Return type

[**MssqlDbSnapshotDetail**](MssqlDbSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns details about a Microsoft SQL database snapshot. |  -  |

<a id="getMssqlHierarchyChildren"></a>
# **getMssqlHierarchyChildren**
> MssqlHierarchyObjectSummaryListResponse getMssqlHierarchyChildren(id, effectiveSlaDomainId, objectType, primaryClusterId, limit, offset, name, isRelic, isLiveMount, isLogShippingSecondary, isClustered, hasInstances, slaAssignment, sortBy, sortOrder, snappableStatus)

Get list of immediate descendant objects

Retrieve the list of immediate descendant objects for the specified parent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the parent SQL Server hierarchy object. To get top-level nodes, use **root** as the ID. 
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter by the ID of the effective SLA Domain.
    List<String> objectType = Arrays.asList(); // List<String> | Filter by a comma-separated list of node object types. 
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster ID, or **local**.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | An integer that specifies the number of initial matches to ignore. 
    String name = "name_example"; // String | Filter children by provided name.
    Boolean isRelic = true; // Boolean | Filter by the value of the `isRelic` field for nodes with object type MssqlDatabase.
    Boolean isLiveMount = true; // Boolean | Filter database by the value of the `isLiveMount` field for nodes with object type MssqlDatabase.
    Boolean isLogShippingSecondary = true; // Boolean | Filter by the value of the `isLogShippingSecondary` field for nodes with object type MssqlDatabase.
    Boolean isClustered = true; // Boolean | Filter by the value of the `isClustered` field for nodes with object type MssqlDatabase or MssqlInstance.
    Boolean hasInstances = true; // Boolean | Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is 'true,' the filter shows only nodes with children MssqlInstance nodes. When this value is 'false,' the filter shows only nodes without children MssqlInstance nodes.
    String slaAssignment = "Derived"; // String | Filter by SLA assignment type.
    String sortBy = "name"; // String | Attribute to sort the results on.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    String snappableStatus = "Protectable"; // String | Determines whether SQL Server instances are fetched with additional privilege checks.
    try {
      MssqlHierarchyObjectSummaryListResponse result = apiInstance.getMssqlHierarchyChildren(id, effectiveSlaDomainId, objectType, primaryClusterId, limit, offset, name, isRelic, isLiveMount, isLogShippingSecondary, isClustered, hasInstances, slaAssignment, sortBy, sortOrder, snappableStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlHierarchyChildren");
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
| **id** | **String**| ID of the parent SQL Server hierarchy object. To get top-level nodes, use **root** as the ID.  | |
| **effectiveSlaDomainId** | **String**| Filter by the ID of the effective SLA Domain. | [optional] |
| **objectType** | [**List&lt;String&gt;**](String.md)| Filter by a comma-separated list of node object types.  | [optional] [enum: Host, MssqlInstance, MssqlDatabase, WindowsCluster, MssqlAvailabilityGroup] |
| **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| An integer that specifies the number of initial matches to ignore.  | [optional] |
| **name** | **String**| Filter children by provided name. | [optional] |
| **isRelic** | **Boolean**| Filter by the value of the &#x60;isRelic&#x60; field for nodes with object type MssqlDatabase. | [optional] |
| **isLiveMount** | **Boolean**| Filter database by the value of the &#x60;isLiveMount&#x60; field for nodes with object type MssqlDatabase. | [optional] |
| **isLogShippingSecondary** | **Boolean**| Filter by the value of the &#x60;isLogShippingSecondary&#x60; field for nodes with object type MssqlDatabase. | [optional] |
| **isClustered** | **Boolean**| Filter by the value of the &#x60;isClustered&#x60; field for nodes with object type MssqlDatabase or MssqlInstance. | [optional] |
| **hasInstances** | **Boolean**| Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is &#39;true,&#39; the filter shows only nodes with children MssqlInstance nodes. When this value is &#39;false,&#39; the filter shows only nodes without children MssqlInstance nodes. | [optional] |
| **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **sortBy** | **String**| Attribute to sort the results on. | [optional] [enum: name, descendantCount.MssqlInstance, descendantCount.MssqlDatabase, logBackupRetentionHours, copyOnly, effectiveSlaDomainName] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |
| **snappableStatus** | **String**| Determines whether SQL Server instances are fetched with additional privilege checks. | [optional] [enum: Protectable] |

### Return type

[**MssqlHierarchyObjectSummaryListResponse**](MssqlHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary list of children objects. |  -  |

<a id="getMssqlHierarchyDescendants"></a>
# **getMssqlHierarchyDescendants**
> MssqlHierarchyObjectSummaryListResponse getMssqlHierarchyDescendants(id, effectiveSlaDomainId, objectType, primaryClusterId, limit, offset, name, isRelic, isLiveMount, isLogShippingSecondary, isClustered, hasInstances, slaAssignment, sortBy, sortOrder, snappableStatus)

Get list of descendant objects

Retrieve the list of descendant objects for the specified parent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the parent SQL server hierarchy object. To get top-level nodes, use **root** as the ID. 
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter by the ID of the effective SLA Domain.
    List<String> objectType = Arrays.asList(); // List<String> | Filter by a comma-separated list of node object types. 
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster ID, or **local**.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | An integer that specifies the number of initial matches to ignore. 
    String name = "name_example"; // String | Filter descendants by provided name.
    Boolean isRelic = true; // Boolean | Filter by the value of the `isRelic` field for nodes with MssqlDatabase as the value of the object type field.
    Boolean isLiveMount = true; // Boolean | Filter database by the value of the `isLiveMount` field for nodes with MssqlDatabase as the value of the object type field.
    Boolean isLogShippingSecondary = true; // Boolean | Filter by the value of the `isLogShippingSecondary` field for nodes with MssqlDatabase as the value of the object type field.
    Boolean isClustered = true; // Boolean | Filter by the value of the `isClustered` field for nodes with object type MssqlDatabase or MssqlInstance.
    Boolean hasInstances = true; // Boolean | Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is 'true,' the filter shows only nodes with children MssqlInstance nodes. When this value is 'false,' the filter shows only nodes without children MssqlInstance nodes.
    String slaAssignment = "Derived"; // String | Filter by SLA Domain assignment type.
    String sortBy = "name"; // String | Attribute to sort the results on.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    String snappableStatus = "Protectable"; // String | Determines whether SQL Server instances are fetched with additional privilege checks.
    try {
      MssqlHierarchyObjectSummaryListResponse result = apiInstance.getMssqlHierarchyDescendants(id, effectiveSlaDomainId, objectType, primaryClusterId, limit, offset, name, isRelic, isLiveMount, isLogShippingSecondary, isClustered, hasInstances, slaAssignment, sortBy, sortOrder, snappableStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlHierarchyDescendants");
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
| **id** | **String**| ID of the parent SQL server hierarchy object. To get top-level nodes, use **root** as the ID.  | |
| **effectiveSlaDomainId** | **String**| Filter by the ID of the effective SLA Domain. | [optional] |
| **objectType** | [**List&lt;String&gt;**](String.md)| Filter by a comma-separated list of node object types.  | [optional] [enum: Host, MssqlInstance, MssqlDatabase, WindowsCluster, MssqlAvailabilityGroup] |
| **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| An integer that specifies the number of initial matches to ignore.  | [optional] |
| **name** | **String**| Filter descendants by provided name. | [optional] |
| **isRelic** | **Boolean**| Filter by the value of the &#x60;isRelic&#x60; field for nodes with MssqlDatabase as the value of the object type field. | [optional] |
| **isLiveMount** | **Boolean**| Filter database by the value of the &#x60;isLiveMount&#x60; field for nodes with MssqlDatabase as the value of the object type field. | [optional] |
| **isLogShippingSecondary** | **Boolean**| Filter by the value of the &#x60;isLogShippingSecondary&#x60; field for nodes with MssqlDatabase as the value of the object type field. | [optional] |
| **isClustered** | **Boolean**| Filter by the value of the &#x60;isClustered&#x60; field for nodes with object type MssqlDatabase or MssqlInstance. | [optional] |
| **hasInstances** | **Boolean**| Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is &#39;true,&#39; the filter shows only nodes with children MssqlInstance nodes. When this value is &#39;false,&#39; the filter shows only nodes without children MssqlInstance nodes. | [optional] |
| **slaAssignment** | **String**| Filter by SLA Domain assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **sortBy** | **String**| Attribute to sort the results on. | [optional] [enum: name, descendantCount.MssqlInstance, descendantCount.MssqlDatabase, logBackupRetentionHours, copyOnly, effectiveSlaDomainName] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |
| **snappableStatus** | **String**| Determines whether SQL Server instances are fetched with additional privilege checks. | [optional] [enum: Protectable] |

### Return type

[**MssqlHierarchyObjectSummaryListResponse**](MssqlHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary list of descendant objects. |  -  |

<a id="getMssqlHierarchyObject"></a>
# **getMssqlHierarchyObject**
> MssqlHierarchyObjectSummary getMssqlHierarchyObject(id)

Get summary of a SQL Server hierarchy object

Retrieve details for the specified object in the SQL Server hierarchy. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the SQL Server hierarchy object.
    try {
      MssqlHierarchyObjectSummary result = apiInstance.getMssqlHierarchyObject(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlHierarchyObject");
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
| **id** | **String**| ID of the SQL Server hierarchy object. | |

### Return type

[**MssqlHierarchyObjectSummary**](MssqlHierarchyObjectSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the hierarchy object. |  -  |

<a id="getMssqlHostConfig"></a>
# **getMssqlHostConfig**
> MssqlHostConfiguration getMssqlHostConfig(hostId)

Get the configuration for a specific host

Returns the configuration for the specified SQL Server host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String hostId = "hostId_example"; // String | ID of the host.
    try {
      MssqlHostConfiguration result = apiInstance.getMssqlHostConfig(hostId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlHostConfig");
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
| **hostId** | **String**| ID of the host. | |

### Return type

[**MssqlHostConfiguration**](MssqlHostConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Configuration details of the specified SQL Server host. |  -  |

<a id="getMssqlInstance"></a>
# **getMssqlInstance**
> MssqlInstanceDetail getMssqlInstance(id)

Get detailed information for a Microsoft SQL instance

Returns a detailed view of a Microsoft SQL instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL instance.
    try {
      MssqlInstanceDetail result = apiInstance.getMssqlInstance(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlInstance");
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
| **id** | **String**| ID of the Microsoft SQL instance. | |

### Return type

[**MssqlInstanceDetail**](MssqlInstanceDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

<a id="getMssqlMount"></a>
# **getMssqlMount**
> MssqlMountDetail getMssqlMount(id)

Get detailed information for a Live Mount of a SQL Server database

Returns detailed information for the specified Live Mount of a SQL Server database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Live Mount to fetch.
    try {
      MssqlMountDetail result = apiInstance.getMssqlMount(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getMssqlMount");
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
| **id** | **String**| ID of the Live Mount to fetch. | |

### Return type

[**MssqlMountDetail**](MssqlMountDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns detailed information for a specified Live Mount of a SQL Server database. |  -  |

<a id="getOnDemandMssqlBatchBackupResultV1"></a>
# **getOnDemandMssqlBatchBackupResultV1**
> MssqlBatchBackupSummary getOnDemandMssqlBatchBackupResultV1(id)

Returns details for an on-demand backup of multiple Microsoft SQL databases

Returns the details for an on-demand backup of multiple Microsoft SQL databases. This only returns details for requests that have finished successfully. To check the status of the request, poll /mssql/request/{id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the on-demand backup request.
    try {
      MssqlBatchBackupSummary result = apiInstance.getOnDemandMssqlBatchBackupResultV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#getOnDemandMssqlBatchBackupResultV1");
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
| **id** | **String**| ID of the on-demand backup request. | |

### Return type

[**MssqlBatchBackupSummary**](MssqlBatchBackupSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of the on-demand backup request. |  -  |

<a id="mssqlGetRestoreFilesV1"></a>
# **mssqlGetRestoreFilesV1**
> List&lt;MssqlRestoreFile&gt; mssqlGetRestoreFilesV1(id, time, lsn, recoveryForkGuid)

Returns a list all database files to be restored

Provides a list of database files to be restored for the specified restore or export operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    OffsetDateTime time = OffsetDateTime.now(); // OffsetDateTime | Time, in ISO8601 date-time format, to recover to. For example, \"2016-01-01T01:23:45.678\". This value or the LSN are required.
    String lsn = "lsn_example"; // String | LSN to recover to. This value or the time are required.
    String recoveryForkGuid = "recoveryForkGuid_example"; // String | Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified.
    try {
      List<MssqlRestoreFile> result = apiInstance.mssqlGetRestoreFilesV1(id, time, lsn, recoveryForkGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#mssqlGetRestoreFilesV1");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **time** | **OffsetDateTime**| Time, in ISO8601 date-time format, to recover to. For example, \&quot;2016-01-01T01:23:45.678\&quot;. This value or the LSN are required. | [optional] |
| **lsn** | **String**| LSN to recover to. This value or the time are required. | [optional] |
| **recoveryForkGuid** | **String**| Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified. | [optional] |

### Return type

[**List&lt;MssqlRestoreFile&gt;**](MssqlRestoreFile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database files to be restored. |  -  |

<a id="mssqlGetSnappableIdV1"></a>
# **mssqlGetSnappableIdV1**
> MssqlSnappableId mssqlGetSnappableIdV1(id)

Returns the snappableId for a Microsoft SQL database

Returns the snappableId for a Microsoft SQL database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    try {
      MssqlSnappableId result = apiInstance.mssqlGetSnappableIdV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#mssqlGetSnappableIdV1");
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
| **id** | **String**| ID of the Microsoft SQL database. | |

### Return type

[**MssqlSnappableId**](MssqlSnappableId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the snappableId. |  -  |

<a id="mssqlRestoreEstimateV1"></a>
# **mssqlRestoreEstimateV1**
> MssqlRestoreEstimateResult mssqlRestoreEstimateV1(id, time, lsn, recoveryForkGuid)

Returns a size estimate for a restore or export

Provides an estimate of resources needed for the specified restore or export operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    OffsetDateTime time = OffsetDateTime.now(); // OffsetDateTime | Time, in ISO8601 date-time format, to recover to. For example, \"2016-01-01T01:23:45.678\". This value or the LSN are required.
    String lsn = "lsn_example"; // String | LSN to recover to. This value or the LSN are required.
    String recoveryForkGuid = "recoveryForkGuid_example"; // String | Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified.
    try {
      MssqlRestoreEstimateResult result = apiInstance.mssqlRestoreEstimateV1(id, time, lsn, recoveryForkGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#mssqlRestoreEstimateV1");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **time** | **OffsetDateTime**| Time, in ISO8601 date-time format, to recover to. For example, \&quot;2016-01-01T01:23:45.678\&quot;. This value or the LSN are required. | [optional] |
| **lsn** | **String**| LSN to recover to. This value or the LSN are required. | [optional] |
| **recoveryForkGuid** | **String**| Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified. | [optional] |

### Return type

[**MssqlRestoreEstimateResult**](MssqlRestoreEstimateResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the esimate for a restore or export to the specified recovery point. |  -  |

<a id="queryLogShippingConfigurations"></a>
# **queryLogShippingConfigurations**
> MssqlLogShippingSummaryListResponse queryLogShippingConfigurations(primaryDatabaseId, primaryDatabaseName, secondaryDatabaseName, location, status, limit, offset, sortBy, sortOrder)

Get log shipping configurations

Retrieves all log shipping configuration objects. Results can be filtered and sorted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String primaryDatabaseId = "primaryDatabaseId_example"; // String | ID of a primary database object.
    String primaryDatabaseName = "primaryDatabaseName_example"; // String | Filter log shipping configuration objects by performing an infix search using the name of a primary database.
    String secondaryDatabaseName = "secondaryDatabaseName_example"; // String | Filter log shipping configuration objects by performing an infix search using the name of a secondary database.
    String location = "location_example"; // String | Filter log shipping configuration objects by performing an infix search using the location string value (host/instance) for a secondary database.
    String status = "OK"; // String | Filter log shipping configuration objects based on the status value for the secondary database.
    Integer limit = 56; // Integer | Limit the summary information to a specified maximum number of results.
    Integer offset = 56; // Integer | Starting position in the list of results contained in the response. The summary information includes the specified numbered result and all higher numbered results.
    String sortBy = "secondaryDatabaseName"; // String | Specifies an attribute used to ASCII-sort the results. Sorting by the last_applied attribute represents the timestamp as an ISO 8601-encoded string.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      MssqlLogShippingSummaryListResponse result = apiInstance.queryLogShippingConfigurations(primaryDatabaseId, primaryDatabaseName, secondaryDatabaseName, location, status, limit, offset, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#queryLogShippingConfigurations");
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
| **primaryDatabaseId** | **String**| ID of a primary database object. | [optional] |
| **primaryDatabaseName** | **String**| Filter log shipping configuration objects by performing an infix search using the name of a primary database. | [optional] |
| **secondaryDatabaseName** | **String**| Filter log shipping configuration objects by performing an infix search using the name of a secondary database. | [optional] |
| **location** | **String**| Filter log shipping configuration objects by performing an infix search using the location string value (host/instance) for a secondary database. | [optional] |
| **status** | **String**| Filter log shipping configuration objects based on the status value for the secondary database. | [optional] [enum: OK, Broken, Initializing, Stale] |
| **limit** | **Integer**| Limit the summary information to a specified maximum number of results. | [optional] |
| **offset** | **Integer**| Starting position in the list of results contained in the response. The summary information includes the specified numbered result and all higher numbered results. | [optional] |
| **sortBy** | **String**| Specifies an attribute used to ASCII-sort the results. Sorting by the last_applied attribute represents the timestamp as an ISO 8601-encoded string. | [optional] [enum: secondaryDatabaseName, primaryDatabaseName, lastAppliedPoint, location] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |

### Return type

[**MssqlLogShippingSummaryListResponse**](MssqlLogShippingSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary list of descendant objects. |  -  |

<a id="queryMssqlAvailabilityGroupV1"></a>
# **queryMssqlAvailabilityGroupV1**
> MssqlAvailabilityGroupSummaryListResponse queryMssqlAvailabilityGroupV1(primaryClusterId)

Returns summary information for Microsoft SQL availability groups

Returns a list of summary information for Microsoft SQL availability groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster.
    try {
      MssqlAvailabilityGroupSummaryListResponse result = apiInstance.queryMssqlAvailabilityGroupV1(primaryClusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#queryMssqlAvailabilityGroupV1");
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
| **primaryClusterId** | **String**| Filter by primary cluster. | [optional] |

### Return type

[**MssqlAvailabilityGroupSummaryListResponse**](MssqlAvailabilityGroupSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

<a id="queryMssqlDb"></a>
# **queryMssqlDb**
> MssqlDbSummaryListResponse queryMssqlDb(instanceId, availabilityGroupId, effectiveSlaDomainId, primaryClusterId, name, slaAssignment, limit, offset, isRelic, isLiveMount, isLogShippingSecondary, sortBy, sortOrder, includeBackupTaskInfo)

Get summary information for SQL Server databases

Returns a list of summary information for Microsoft SQL databases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String instanceId = "instanceId_example"; // String | Filter by Microsoft SQL instance.
    String availabilityGroupId = "availabilityGroupId_example"; // String | Filter by the `id` of an Always On Availability Group.
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter by effective SLA domain.
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster.
    String name = "name_example"; // String | Filter by a substring of the database name.
    String slaAssignment = "slaAssignment_example"; // String | SLA Assignment of the database.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | An integer that specifies a number of initial matches to ignore.
    Boolean isRelic = true; // Boolean | Filter database summary information by the value of the `isRelic` field.
    Boolean isLiveMount = true; // Boolean | Filter database summary information by the value of the `isLiveMount` field.
    Boolean isLogShippingSecondary = true; // Boolean | Filter database summary information by the value of the `isLogShippingSecondary` field.
    String sortBy = "copyOnly"; // String | Specifies the SQL Server Database attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    Boolean includeBackupTaskInfo = false; // Boolean | Include backup task information in response.
    try {
      MssqlDbSummaryListResponse result = apiInstance.queryMssqlDb(instanceId, availabilityGroupId, effectiveSlaDomainId, primaryClusterId, name, slaAssignment, limit, offset, isRelic, isLiveMount, isLogShippingSecondary, sortBy, sortOrder, includeBackupTaskInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#queryMssqlDb");
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
| **instanceId** | **String**| Filter by Microsoft SQL instance. | [optional] |
| **availabilityGroupId** | **String**| Filter by the &#x60;id&#x60; of an Always On Availability Group. | [optional] |
| **effectiveSlaDomainId** | **String**| Filter by effective SLA domain. | [optional] |
| **primaryClusterId** | **String**| Filter by primary cluster. | [optional] |
| **name** | **String**| Filter by a substring of the database name. | [optional] |
| **slaAssignment** | **String**| SLA Assignment of the database. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| An integer that specifies a number of initial matches to ignore. | [optional] |
| **isRelic** | **Boolean**| Filter database summary information by the value of the &#x60;isRelic&#x60; field. | [optional] |
| **isLiveMount** | **Boolean**| Filter database summary information by the value of the &#x60;isLiveMount&#x60; field. | [optional] |
| **isLogShippingSecondary** | **Boolean**| Filter database summary information by the value of the &#x60;isLogShippingSecondary&#x60; field. | [optional] |
| **sortBy** | **String**| Specifies the SQL Server Database attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order. | [optional] [enum: copyOnly, effectiveSlaDomainName, logBackupRetentionHours, name] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |
| **includeBackupTaskInfo** | **Boolean**| Include backup task information in response. | [optional] [default to false] |

### Return type

[**MssqlDbSummaryListResponse**](MssqlDbSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

<a id="queryMssqlDbSnapshot"></a>
# **queryMssqlDbSnapshot**
> MssqlDbSnapshotSummaryListResponse queryMssqlDbSnapshot(id, afterTime, beforeTime)

Get summary information for snapshots of a Microsoft SQL database

Returns a list of summary information for snapshots of a Microsoft SQL database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
    try {
      MssqlDbSnapshotSummaryListResponse result = apiInstance.queryMssqlDbSnapshot(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#queryMssqlDbSnapshot");
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
| **id** | **String**| ID of the Microsoft SQL database. | |
| **afterTime** | **OffsetDateTime**| Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |

### Return type

[**MssqlDbSnapshotSummaryListResponse**](MssqlDbSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns summary information for snapshots. |  -  |

<a id="queryMssqlHostConfig"></a>
# **queryMssqlHostConfig**
> MssqlHostConfigurationWithHostIdListResponse queryMssqlHostConfig(hostId)

Get the summary of SQL Server host configurations

Returns a list of customized SQL Server host configurations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    List<String> hostId = Arrays.asList(); // List<String> | IDs of the hosts.
    try {
      MssqlHostConfigurationWithHostIdListResponse result = apiInstance.queryMssqlHostConfig(hostId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#queryMssqlHostConfig");
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
| **hostId** | [**List&lt;String&gt;**](String.md)| IDs of the hosts. | [optional] |

### Return type

[**MssqlHostConfigurationWithHostIdListResponse**](MssqlHostConfigurationWithHostIdListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of SQL Server host configurations. |  -  |

<a id="queryMssqlInstance"></a>
# **queryMssqlInstance**
> MssqlInstanceSummaryListResponse queryMssqlInstance(rootId, primaryClusterId, snappableStatus)

Get summary information for Microsoft SQL instances

Returns a list of summary information for Microsoft SQL instances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String rootId = "rootId_example"; // String | Include only instances that belong to this root.
    String primaryClusterId = "primaryClusterId_example"; // String | Limits the instances returned within one cluster specified by primary_cluster_id.
    String snappableStatus = "Protectable"; // String | Determines whether SQL Server instances are fetched with additional privilege checks.
    try {
      MssqlInstanceSummaryListResponse result = apiInstance.queryMssqlInstance(rootId, primaryClusterId, snappableStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#queryMssqlInstance");
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
| **rootId** | **String**| Include only instances that belong to this root. | [optional] |
| **primaryClusterId** | **String**| Limits the instances returned within one cluster specified by primary_cluster_id. | [optional] |
| **snappableStatus** | **String**| Determines whether SQL Server instances are fetched with additional privilege checks. | [optional] [enum: Protectable] |

### Return type

[**MssqlInstanceSummaryListResponse**](MssqlInstanceSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

<a id="queryMssqlMount"></a>
# **queryMssqlMount**
> MssqlMountSummaryListResponse queryMssqlMount(sourceDatabaseId, sourceDatabaseName, targetInstanceId, mountedDatabaseName, sortBy, sortOrder, offset, limit)

Get summary information for all Live Mounts SQL Server databases

Returns a list with summary information for all Live Mount SQL Server databases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String sourceDatabaseId = "sourceDatabaseId_example"; // String | Filters by the ID of the source SQL Server database.
    String sourceDatabaseName = "sourceDatabaseName_example"; // String | Filters by the name of the source SQL Server database using infix search.
    String targetInstanceId = "targetInstanceId_example"; // String | Filters by the ID of the target SQL Server instance.
    String mountedDatabaseName = "mountedDatabaseName_example"; // String | Filters by the name of the mounted SQL Server database using infix search.
    String sortBy = "sourceDatabaseName"; // String | Specifies the SQL Server Live Mount attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order.
    String sortOrder = "asc"; // String | Specifies the sort order, either ascending or descending. Default order is ascending.
    Integer offset = 56; // Integer | Returns the portion of the ordered list that starts after the element specified by the offset number.
    Integer limit = 56; // Integer | Sets the maximum number of a elements to include in the data array of the response.
    try {
      MssqlMountSummaryListResponse result = apiInstance.queryMssqlMount(sourceDatabaseId, sourceDatabaseName, targetInstanceId, mountedDatabaseName, sortBy, sortOrder, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#queryMssqlMount");
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
| **sourceDatabaseId** | **String**| Filters by the ID of the source SQL Server database. | [optional] |
| **sourceDatabaseName** | **String**| Filters by the name of the source SQL Server database using infix search. | [optional] |
| **targetInstanceId** | **String**| Filters by the ID of the target SQL Server instance. | [optional] |
| **mountedDatabaseName** | **String**| Filters by the name of the mounted SQL Server database using infix search. | [optional] |
| **sortBy** | **String**| Specifies the SQL Server Live Mount attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order. | [optional] [enum: sourceDatabaseName, sourceRecoveryPoint, mountedDatabaseName, creationDate] |
| **sortOrder** | **String**| Specifies the sort order, either ascending or descending. Default order is ascending. | [optional] [enum: asc, desc] |
| **offset** | **Integer**| Returns the portion of the ordered list that starts after the element specified by the offset number. | [optional] |
| **limit** | **Integer**| Sets the maximum number of a elements to include in the data array of the response. | [optional] |

### Return type

[**MssqlMountSummaryListResponse**](MssqlMountSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns summary information for all Live Mounts. |  -  |

<a id="reseedSecondary"></a>
# **reseedSecondary**
> AsyncRequestStatus reseedSecondary(id, mssqlLogShippingReseedConfig)

Reseed a secondary database

Starts an asynchronous job to reseed a secondary database. Reseeding restores the data in the secondary database based on a log shipping configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the log shipping configuration object for the specified secondary database.
    MssqlLogShippingReseedConfig mssqlLogShippingReseedConfig = new MssqlLogShippingReseedConfig(); // MssqlLogShippingReseedConfig | Configuration parameters for the reseed operation.
    try {
      AsyncRequestStatus result = apiInstance.reseedSecondary(id, mssqlLogShippingReseedConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#reseedSecondary");
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
| **id** | **String**| ID of the log shipping configuration object for the specified secondary database. | |
| **mssqlLogShippingReseedConfig** | [**MssqlLogShippingReseedConfig**](MssqlLogShippingReseedConfig.md)| Configuration parameters for the reseed operation. | |

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
| **202** | Returns with a request ID for the async job to reseed a secondary database. |  -  |

<a id="updateDefaultDbPropertiesV1"></a>
# **updateDefaultDbPropertiesV1**
> MssqlDbDefaults updateDefaultDbPropertiesV1(mssqlDbDefaultsUpdate)

Update the default properties for Microsoft SQL databases

The default properties are Log Backup Frequency (in seconds), Log Retention Time (in hours) and CBT status. New databases added to the Rubrik cluster are provided the log backup frequency value and log backup retention value by default. New hosts added to the Rubrik cluster are provided the CBT status by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    MssqlDbDefaultsUpdate mssqlDbDefaultsUpdate = new MssqlDbDefaultsUpdate(); // MssqlDbDefaultsUpdate | Updated default properties.
    try {
      MssqlDbDefaults result = apiInstance.updateDefaultDbPropertiesV1(mssqlDbDefaultsUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#updateDefaultDbPropertiesV1");
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
| **mssqlDbDefaultsUpdate** | [**MssqlDbDefaultsUpdate**](MssqlDbDefaultsUpdate.md)| Updated default properties. | |

### Return type

[**MssqlDbDefaults**](MssqlDbDefaults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the updated default properties. |  -  |

<a id="updateLogShippingConfiguration"></a>
# **updateLogShippingConfiguration**
> AsyncRequestStatus updateLogShippingConfiguration(id, mssqlLogShippingUpdate)

Update a specified log shipping configuration

Updates a specified log shipping configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of a log shipping configuration object.
    MssqlLogShippingUpdate mssqlLogShippingUpdate = new MssqlLogShippingUpdate(); // MssqlLogShippingUpdate | Configuration parameters for the update operation.
    try {
      AsyncRequestStatus result = apiInstance.updateLogShippingConfiguration(id, mssqlLogShippingUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#updateLogShippingConfiguration");
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
| **id** | **String**| ID of a log shipping configuration object. | |
| **mssqlLogShippingUpdate** | [**MssqlLogShippingUpdate**](MssqlLogShippingUpdate.md)| Configuration parameters for the update operation. | |

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
| **202** | Returns the request ID of an asynchronous job that updates a log shipping configuration object. |  -  |

<a id="updateMssqlAvailabilityGroupV1"></a>
# **updateMssqlAvailabilityGroupV1**
> MssqlAvailabilityGroupDetail updateMssqlAvailabilityGroupV1(id, mssqlAvailabilityGroupUpdate)

Update a Microsoft SQL availability group

Update a Microsoft SQL availability group with the specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL availability group to update.
    MssqlAvailabilityGroupUpdate mssqlAvailabilityGroupUpdate = new MssqlAvailabilityGroupUpdate(); // MssqlAvailabilityGroupUpdate | Properties to update.
    try {
      MssqlAvailabilityGroupDetail result = apiInstance.updateMssqlAvailabilityGroupV1(id, mssqlAvailabilityGroupUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#updateMssqlAvailabilityGroupV1");
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
| **id** | **String**| ID of the Microsoft SQL availability group to update. | |
| **mssqlAvailabilityGroupUpdate** | [**MssqlAvailabilityGroupUpdate**](MssqlAvailabilityGroupUpdate.md)| Properties to update. | |

### Return type

[**MssqlAvailabilityGroupDetail**](MssqlAvailabilityGroupDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the update was successful. |  -  |

<a id="updateMssqlDb"></a>
# **updateMssqlDb**
> MssqlDbDetail updateMssqlDb(id, mssqlDbUpdate)

Update a Microsoft SQL database

Update a Microsoft SQL database with the specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL database to update.
    MssqlDbUpdate mssqlDbUpdate = new MssqlDbUpdate(); // MssqlDbUpdate | Properties to update.
    try {
      MssqlDbDetail result = apiInstance.updateMssqlDb(id, mssqlDbUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#updateMssqlDb");
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
| **id** | **String**| ID of the Microsoft SQL database to update. | |
| **mssqlDbUpdate** | [**MssqlDbUpdate**](MssqlDbUpdate.md)| Properties to update. | |

### Return type

[**MssqlDbDetail**](MssqlDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the update was successful. |  -  |

<a id="updateMssqlHostConfig"></a>
# **updateMssqlHostConfig**
> MssqlHostConfiguration updateMssqlHostConfig(hostId, mssqlHostConfiguration)

Update host configuration

Updates the configuration for a specified host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String hostId = "hostId_example"; // String | ID of the SQL Server host to update the host configuration.
    MssqlHostConfiguration mssqlHostConfiguration = new MssqlHostConfiguration(); // MssqlHostConfiguration | SQL Server host configuration properties to update.
    try {
      MssqlHostConfiguration result = apiInstance.updateMssqlHostConfig(hostId, mssqlHostConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#updateMssqlHostConfig");
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
| **hostId** | **String**| ID of the SQL Server host to update the host configuration. | |
| **mssqlHostConfiguration** | [**MssqlHostConfiguration**](MssqlHostConfiguration.md)| SQL Server host configuration properties to update. | |

### Return type

[**MssqlHostConfiguration**](MssqlHostConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the updated SQL Server host configuration. |  -  |

<a id="updateMssqlInstance"></a>
# **updateMssqlInstance**
> MssqlInstanceDetail updateMssqlInstance(id, mssqlInstanceUpdate)

Update a Microsoft SQL instance

Update a Microsoft SQL instance with specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MssqlApi;

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

    MssqlApi apiInstance = new MssqlApi(defaultClient);
    String id = "id_example"; // String | ID of the Microsoft SQL instance.
    MssqlInstanceUpdate mssqlInstanceUpdate = new MssqlInstanceUpdate(); // MssqlInstanceUpdate | Properties to update.
    try {
      MssqlInstanceDetail result = apiInstance.updateMssqlInstance(id, mssqlInstanceUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MssqlApi#updateMssqlInstance");
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
| **id** | **String**| ID of the Microsoft SQL instance. | |
| **mssqlInstanceUpdate** | [**MssqlInstanceUpdate**](MssqlInstanceUpdate.md)| Properties to update. | |

### Return type

[**MssqlInstanceDetail**](MssqlInstanceDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the update was successful. |  -  |

