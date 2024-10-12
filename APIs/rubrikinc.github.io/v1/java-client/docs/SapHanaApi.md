# SapHanaApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSapHanaSystem**](SapHanaApi.md#addSapHanaSystem) | **POST** /sap_hana/system | Add a SAP HANA system |
| [**configureSapHanaRestore**](SapHanaApi.md#configureSapHanaRestore) | **POST** /sap_hana/db/{id}/configure_restore | Configure the target database for system copy restore |
| [**createOnDemandSapHanaBackup**](SapHanaApi.md#createOnDemandSapHanaBackup) | **POST** /sap_hana/db/{id}/snapshot | Create on demand database snapshot |
| [**createSapHanaSystemRefresh**](SapHanaApi.md#createSapHanaSystemRefresh) | **POST** /sap_hana/system/{id}/refresh | Refresh SAP HANA system metadata |
| [**deleteSapHanaDbSnapshot**](SapHanaApi.md#deleteSapHanaDbSnapshot) | **DELETE** /sap_hana/db/snapshot/{id} | Delete a particular full snapshot of a SAP HANA database |
| [**deleteSapHanaSystem**](SapHanaApi.md#deleteSapHanaSystem) | **DELETE** /sap_hana/system/{id} | Delete a SAP HANA system |
| [**getMissedSapHanaDbSnapshots**](SapHanaApi.md#getMissedSapHanaDbSnapshots) | **GET** /sap_hana/db/{id}/missed_snapshot | Retrieve summary information for missed snapshots of a SAP HANA database |
| [**getSapHanaDatabase**](SapHanaApi.md#getSapHanaDatabase) | **GET** /sap_hana/db/{id} | Get detailed information for an SAP HANA database |
| [**getSapHanaDbAsyncRequestStatus**](SapHanaApi.md#getSapHanaDbAsyncRequestStatus) | **GET** /sap_hana/db/request/{id} | Get the status of a SAP HANA database request |
| [**getSapHanaDbRecoverableRanges**](SapHanaApi.md#getSapHanaDbRecoverableRanges) | **GET** /sap_hana/db/{id}/recoverable_range | Get recoverable ranges of a SAP HANA database |
| [**getSapHanaDbSnapshot**](SapHanaApi.md#getSapHanaDbSnapshot) | **GET** /sap_hana/db/snapshot/{id} | Get SAP HANA database snapshot details |
| [**getSapHanaSystem**](SapHanaApi.md#getSapHanaSystem) | **GET** /sap_hana/system/{id} | Get summary information for a SAP HANA system |
| [**getSapHanaSystemAsyncRequestStatus**](SapHanaApi.md#getSapHanaSystemAsyncRequestStatus) | **GET** /sap_hana/system/request/{id} | Get the status of a SAP HANA system request |
| [**patchSapHanaDatabase**](SapHanaApi.md#patchSapHanaDatabase) | **PATCH** /sap_hana/db/{id} | Update the SLA Domain for an SAP HANA database |
| [**patchSapHanaSystem**](SapHanaApi.md#patchSapHanaSystem) | **PATCH** /sap_hana/system/{id} | Update the SLA Domain for a SAP HANA system |
| [**querySapHanaDatabases**](SapHanaApi.md#querySapHanaDatabases) | **GET** /sap_hana/db | Get summary information for discovered SAP HANA databases |
| [**querySapHanaDbSnapshot**](SapHanaApi.md#querySapHanaDbSnapshot) | **GET** /sap_hana/db/{id}/snapshot | Get a summary list of snapshots for a SAP HANA database |
| [**querySapHanaSystems**](SapHanaApi.md#querySapHanaSystems) | **GET** /sap_hana/system | Get summary information for added SAP HANA systems |
| [**unconfigureSapHanaRestore**](SapHanaApi.md#unconfigureSapHanaRestore) | **POST** /sap_hana/db/{id}/unconfigure_restore | Reset the configuration for system copy restore on target database |


<a id="addSapHanaSystem"></a>
# **addSapHanaSystem**
> SapHanaAddSystemResponse addSapHanaSystem(sapHanaSystemConfig)

Add a SAP HANA system

Add a SAP HANA system to the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    SapHanaSystemConfig sapHanaSystemConfig = new SapHanaSystemConfig(); // SapHanaSystemConfig | Add a SAP HANA system to the Rubrik cluster. Contains parameters like username, list of hosts, password required while adding a SAP HANA system.
    try {
      SapHanaAddSystemResponse result = apiInstance.addSapHanaSystem(sapHanaSystemConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#addSapHanaSystem");
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
| **sapHanaSystemConfig** | [**SapHanaSystemConfig**](SapHanaSystemConfig.md)| Add a SAP HANA system to the Rubrik cluster. Contains parameters like username, list of hosts, password required while adding a SAP HANA system. | |

### Return type

[**SapHanaAddSystemResponse**](SapHanaAddSystemResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Adds the SAP HANA system and returns its ID and the status of the scheduled system refresh job. |  -  |

<a id="configureSapHanaRestore"></a>
# **configureSapHanaRestore**
> AsyncRequestStatus configureSapHanaRestore(id, sapHanaRestoreSourceConfig)

Configure the target database for system copy restore

Initiates a job to configure the specified target database for a system copy restore by sending metadata about the source database. System copy restore in SAP HANA is done across different databases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | ID of the target SAP HANA database to be configured.
    SapHanaRestoreSourceConfig sapHanaRestoreSourceConfig = new SapHanaRestoreSourceConfig(); // SapHanaRestoreSourceConfig | The object containing configuration related metadata for the source SAP HANA database.
    try {
      AsyncRequestStatus result = apiInstance.configureSapHanaRestore(id, sapHanaRestoreSourceConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#configureSapHanaRestore");
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
| **id** | **String**| ID of the target SAP HANA database to be configured. | |
| **sapHanaRestoreSourceConfig** | [**SapHanaRestoreSourceConfig**](SapHanaRestoreSourceConfig.md)| The object containing configuration related metadata for the source SAP HANA database. | |

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
| **202** | Status of the request. |  -  |

<a id="createOnDemandSapHanaBackup"></a>
# **createOnDemandSapHanaBackup**
> AsyncRequestStatus createOnDemandSapHanaBackup(id, baseOnDemandSnapshotConfig)

Create on demand database snapshot

Initiates a job to take an on demand full snapshot of a specified SAP HANA database object. The GET /sap_hana/db/request/{id} endpoint can be used to monitor the progress of the job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a SAP HANA database object.
    BaseOnDemandSnapshotConfig baseOnDemandSnapshotConfig = new BaseOnDemandSnapshotConfig(); // BaseOnDemandSnapshotConfig | Configuration for the on demand backup.
    try {
      AsyncRequestStatus result = apiInstance.createOnDemandSapHanaBackup(id, baseOnDemandSnapshotConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#createOnDemandSapHanaBackup");
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
| **id** | **String**| ID assigned to a SAP HANA database object. | |
| **baseOnDemandSnapshotConfig** | [**BaseOnDemandSnapshotConfig**](BaseOnDemandSnapshotConfig.md)| Configuration for the on demand backup. | [optional] |

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

<a id="createSapHanaSystemRefresh"></a>
# **createSapHanaSystemRefresh**
> AsyncRequestStatus createSapHanaSystemRefresh(id)

Refresh SAP HANA system metadata

Initiates a job to refresh metadata of a SAP HANA system object. The GET /sap_hana/system/request/{id} endpoint can be used to monitor the progress of the job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | The ID of the SAP HANA system.
    try {
      AsyncRequestStatus result = apiInstance.createSapHanaSystemRefresh(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#createSapHanaSystemRefresh");
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
| **id** | **String**| The ID of the SAP HANA system. | |

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
| **202** | Status for the request. |  -  |

<a id="deleteSapHanaDbSnapshot"></a>
# **deleteSapHanaDbSnapshot**
> deleteSapHanaDbSnapshot(id)

Delete a particular full snapshot of a SAP HANA database

Initiates a request to delete a particular full snapshot of a SAP HANA database. If the log retention period for the database is still in effect, the snapshot will be deleted when the log retention period ends.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a SAP HANA database full snapshot.
    try {
      apiInstance.deleteSapHanaDbSnapshot(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#deleteSapHanaDbSnapshot");
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
| **id** | **String**| ID assigned to a SAP HANA database full snapshot. | |

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
| **204** | Successfully initiated the request to delete the specified SAP HANA database snapshot and there is nothing to return. |  -  |

<a id="deleteSapHanaSystem"></a>
# **deleteSapHanaSystem**
> AsyncRequestStatus deleteSapHanaSystem(id)

Delete a SAP HANA system

Initiates a job to delete a SAP HANA system object. GET /sap_hana/system/request/{id} endpoint can be used to monitor the progress of the job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | The ID of the SAP HANA system.
    try {
      AsyncRequestStatus result = apiInstance.deleteSapHanaSystem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#deleteSapHanaSystem");
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
| **id** | **String**| The ID of the SAP HANA system. | |

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
| **202** | Status for the request. |  -  |

<a id="getMissedSapHanaDbSnapshots"></a>
# **getMissedSapHanaDbSnapshots**
> MissedSnapshotListResponse getMissedSapHanaDbSnapshots(id, afterTime, beforeTime)

Retrieve summary information for missed snapshots of a SAP HANA database

Returns a summary of information for the missed snapshots of a SAP HANA database. Retrieve only the missed snapshots that occur between the beginning and ending timestamps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | ID of the SAP HANA database.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter for snapshots that are missed on or after this time. The date-time string must be in ISO8601 format, for example, \"2016-01-01T01:23:45.678\".
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter for snapshots that are missed on or before this time. The date-time string must be in ISO8601 format, for example, \"2016-01-01T01:23:45.678\".
    try {
      MissedSnapshotListResponse result = apiInstance.getMissedSapHanaDbSnapshots(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#getMissedSapHanaDbSnapshots");
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
| **id** | **String**| ID of the SAP HANA database. | |
| **afterTime** | **OffsetDateTime**| Filter for snapshots that are missed on or after this time. The date-time string must be in ISO8601 format, for example, \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter for snapshots that are missed on or before this time. The date-time string must be in ISO8601 format, for example, \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |

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
| **200** | Returns details about missed snapshots. |  -  |

<a id="getSapHanaDatabase"></a>
# **getSapHanaDatabase**
> SapHanaDatabaseDetail getSapHanaDatabase(id)

Get detailed information for an SAP HANA database

Returns a detailed view of the SAP HANA database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | The ID of the SAP HANA database.
    try {
      SapHanaDatabaseDetail result = apiInstance.getSapHanaDatabase(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#getSapHanaDatabase");
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
| **id** | **String**| The ID of the SAP HANA database. | |

### Return type

[**SapHanaDatabaseDetail**](SapHanaDatabaseDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the query is successful, returns a detailed view of the SAP HANA database. |  -  |

<a id="getSapHanaDbAsyncRequestStatus"></a>
# **getSapHanaDbAsyncRequestStatus**
> AsyncRequestStatus getSapHanaDbAsyncRequestStatus(id)

Get the status of a SAP HANA database request

Get details about a SAP HANA database related request which includes the status of data backup job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | ID of the request.
    try {
      AsyncRequestStatus result = apiInstance.getSapHanaDbAsyncRequestStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#getSapHanaDbAsyncRequestStatus");
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

<a id="getSapHanaDbRecoverableRanges"></a>
# **getSapHanaDbRecoverableRanges**
> SapHanaRecoverableRangeListResponse getSapHanaDbRecoverableRanges(id, afterTime, beforeTime)

Get recoverable ranges of a SAP HANA database

Retrieve the recoverable ranges for a specified SAP HANA database. Provide a beginning and/or ending timestamp to retrieve only the recoverable ranges that fall within this period of time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | ID of the SAP HANA database.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter ranges to end after this time. The date-time string should be in an ISO8601 format. For example, \"2016-01-01T01:23:45.678Z\".
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter ranges to start before this time. The date-time string should be in an ISO8601 format. For example, \"2016-01-01T01:23:45.678Z\".
    try {
      SapHanaRecoverableRangeListResponse result = apiInstance.getSapHanaDbRecoverableRanges(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#getSapHanaDbRecoverableRanges");
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
| **id** | **String**| ID of the SAP HANA database. | |
| **afterTime** | **OffsetDateTime**| Filter ranges to end after this time. The date-time string should be in an ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678Z\&quot;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter ranges to start before this time. The date-time string should be in an ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678Z\&quot;. | [optional] |

### Return type

[**SapHanaRecoverableRangeListResponse**](SapHanaRecoverableRangeListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the recoverable ranges for the SAP HANA database. |  -  |

<a id="getSapHanaDbSnapshot"></a>
# **getSapHanaDbSnapshot**
> SapHanaDatabaseSnapshotDetail getSapHanaDbSnapshot(id)

Get SAP HANA database snapshot details

Retrieve detailed information about a full or an incremental snapshot of a SAP HANA database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | ID of snapshot.
    try {
      SapHanaDatabaseSnapshotDetail result = apiInstance.getSapHanaDbSnapshot(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#getSapHanaDbSnapshot");
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

[**SapHanaDatabaseSnapshotDetail**](SapHanaDatabaseSnapshotDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns details about a snapshot. |  -  |

<a id="getSapHanaSystem"></a>
# **getSapHanaSystem**
> SapHanaSystemSummary getSapHanaSystem(id)

Get summary information for a SAP HANA system

Returns a summary view of a SAP HANA system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | The ID of the SAP HANA system.
    try {
      SapHanaSystemSummary result = apiInstance.getSapHanaSystem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#getSapHanaSystem");
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
| **id** | **String**| The ID of the SAP HANA system. | |

### Return type

[**SapHanaSystemSummary**](SapHanaSystemSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns summary information. |  -  |

<a id="getSapHanaSystemAsyncRequestStatus"></a>
# **getSapHanaSystemAsyncRequestStatus**
> AsyncRequestStatus getSapHanaSystemAsyncRequestStatus(id)

Get the status of a SAP HANA system request

Get details about a SAP HANA system related request which includes the status of delete or refresh system job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | The ID of the request object used to poll the status.
    try {
      AsyncRequestStatus result = apiInstance.getSapHanaSystemAsyncRequestStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#getSapHanaSystemAsyncRequestStatus");
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
| **id** | **String**| The ID of the request object used to poll the status. | |

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
| **200** | Status for the request. |  -  |

<a id="patchSapHanaDatabase"></a>
# **patchSapHanaDatabase**
> SapHanaDatabaseDetail patchSapHanaDatabase(id, sapHanaDatabasePatch)

Update the SLA Domain for an SAP HANA database

Update the SLA Domain that is configured for an SAP HANA database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | The ID of the SAP HANA database.
    SapHanaDatabasePatch sapHanaDatabasePatch = new SapHanaDatabasePatch(); // SapHanaDatabasePatch | Object containing updated SAP HANA database SLA Domain ID.
    try {
      SapHanaDatabaseDetail result = apiInstance.patchSapHanaDatabase(id, sapHanaDatabasePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#patchSapHanaDatabase");
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
| **id** | **String**| The ID of the SAP HANA database. | |
| **sapHanaDatabasePatch** | [**SapHanaDatabasePatch**](SapHanaDatabasePatch.md)| Object containing updated SAP HANA database SLA Domain ID. | |

### Return type

[**SapHanaDatabaseDetail**](SapHanaDatabaseDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the API call is successful, the SAP HANA database object is updated and summary of the object is returned. |  -  |

<a id="patchSapHanaSystem"></a>
# **patchSapHanaSystem**
> SapHanaPatchSystemResponse patchSapHanaSystem(id, sapHanaSystemPatch)

Update the SLA Domain for a SAP HANA system

Update the SLA Domain that is configured for a SAP HANA system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | The ID of the SAP HANA system.
    SapHanaSystemPatch sapHanaSystemPatch = new SapHanaSystemPatch(); // SapHanaSystemPatch | An object that contains the updated SLA Domain ID for the SAP HANA system.
    try {
      SapHanaPatchSystemResponse result = apiInstance.patchSapHanaSystem(id, sapHanaSystemPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#patchSapHanaSystem");
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
| **id** | **String**| The ID of the SAP HANA system. | |
| **sapHanaSystemPatch** | [**SapHanaSystemPatch**](SapHanaSystemPatch.md)| An object that contains the updated SLA Domain ID for the SAP HANA system. | |

### Return type

[**SapHanaPatchSystemResponse**](SapHanaPatchSystemResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Updates the SAP HANA system and returns its summary and the status of the scheduled system refresh job. |  -  |

<a id="querySapHanaDatabases"></a>
# **querySapHanaDatabases**
> SapHanaDatabaseSummaryListResponse querySapHanaDatabases(effectiveSlaDomainId, primaryClusterId, name, slaAssignment, limit, offset, isRelic, sortBy, sortOrder)

Get summary information for discovered SAP HANA databases

Returns summary information for SAP HANA databases connected to the CDM cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | The ID of the SLA Domain that controls the protection of the host.
    String primaryClusterId = "primaryClusterId_example"; // String | The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases.
    String name = "name_example"; // String | The name of the SAP HANA database.
    String slaAssignment = "slaAssignment_example"; // String | The name of the SLA Domain that controls the protection of the SAP HANA database.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | An integer that specifies a number of initial matches to ignore.
    Boolean isRelic = true; // Boolean | Specify whether the SAP HANA database is accessible on the Rubrik cluster.
    String sortBy = "effectiveSlaDomainName"; // String | Specifies the SAP HANA Database attribute to use in sorting the summary information.
    String sortOrder = "asc"; // String | The order to sort the responses by. Valid choices are asc (ascending) and desc (descending).
    try {
      SapHanaDatabaseSummaryListResponse result = apiInstance.querySapHanaDatabases(effectiveSlaDomainId, primaryClusterId, name, slaAssignment, limit, offset, isRelic, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#querySapHanaDatabases");
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
| **effectiveSlaDomainId** | **String**| The ID of the SLA Domain that controls the protection of the host. | [optional] |
| **primaryClusterId** | **String**| The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases. | [optional] |
| **name** | **String**| The name of the SAP HANA database. | [optional] |
| **slaAssignment** | **String**| The name of the SLA Domain that controls the protection of the SAP HANA database. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| An integer that specifies a number of initial matches to ignore. | [optional] |
| **isRelic** | **Boolean**| Specify whether the SAP HANA database is accessible on the Rubrik cluster. | [optional] |
| **sortBy** | **String**| Specifies the SAP HANA Database attribute to use in sorting the summary information. | [optional] [enum: effectiveSlaDomainName, name, sapHanaSystemName] |
| **sortOrder** | **String**| The order to sort the responses by. Valid choices are asc (ascending) and desc (descending). | [optional] [enum: asc, desc] |

### Return type

[**SapHanaDatabaseSummaryListResponse**](SapHanaDatabaseSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the query is successful, returns summary information for SAP HANA databases connected to the cluster. |  -  |

<a id="querySapHanaDbSnapshot"></a>
# **querySapHanaDbSnapshot**
> SapHanaDatabaseSnapshotSummaryListResponse querySapHanaDbSnapshot(id, backupType, afterTime, beforeTime)

Get a summary list of snapshots for a SAP HANA database

Retrieve summary information about the full and incremental snapshots of a specified SAP HANA database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a SAP HANA database object.
    String backupType = "FULL"; // String | Filter snapshots to those of a particular backup type.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \"2016-01-01T01:23:45.678\".
    try {
      SapHanaDatabaseSnapshotSummaryListResponse result = apiInstance.querySapHanaDbSnapshot(id, backupType, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#querySapHanaDbSnapshot");
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
| **id** | **String**| ID assigned to a SAP HANA database object. | |
| **backupType** | **String**| Filter snapshots to those of a particular backup type. | [optional] [enum: FULL, INCREMENTAL] |
| **afterTime** | **OffsetDateTime**| Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |

### Return type

[**SapHanaDatabaseSnapshotSummaryListResponse**](SapHanaDatabaseSnapshotSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns summary information for all snapshots. |  -  |

<a id="querySapHanaSystems"></a>
# **querySapHanaSystems**
> SapHanaSystemSummaryListResponse querySapHanaSystems(primaryClusterId, sid, limit, offset, sortBy, sortOrder)

Get summary information for added SAP HANA systems

Returns summary information for SAP HANA systems.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String primaryClusterId = "primaryClusterId_example"; // String | The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases.
    String sid = "sid_example"; // String | The SAP System Identification (SID) code for the SAP HANA system.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | An integer that specifies a number of initial matches to ignore.
    String sortBy = "sid"; // String | The SAP HANA system attribute to use in sorting the responses.
    String sortOrder = "asc"; // String | The order to sort the responses by. Valid choices are asc (ascending) and desc (descending).
    try {
      SapHanaSystemSummaryListResponse result = apiInstance.querySapHanaSystems(primaryClusterId, sid, limit, offset, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#querySapHanaSystems");
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
| **primaryClusterId** | **String**| The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases. | [optional] |
| **sid** | **String**| The SAP System Identification (SID) code for the SAP HANA system. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| An integer that specifies a number of initial matches to ignore. | [optional] |
| **sortBy** | **String**| The SAP HANA system attribute to use in sorting the responses. | [optional] [enum: sid] |
| **sortOrder** | **String**| The order to sort the responses by. Valid choices are asc (ascending) and desc (descending). | [optional] [enum: asc, desc] |

### Return type

[**SapHanaSystemSummaryListResponse**](SapHanaSystemSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If query is successful, returns summary information for SAP HANA systems. |  -  |

<a id="unconfigureSapHanaRestore"></a>
# **unconfigureSapHanaRestore**
> AsyncRequestStatus unconfigureSapHanaRestore(id)

Reset the configuration for system copy restore on target database

Initiates a job to reset the configuration for the system copy restore on the specified target database. System copy restore in SAP HANA is done across different databases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SapHanaApi;

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

    SapHanaApi apiInstance = new SapHanaApi(defaultClient);
    String id = "id_example"; // String | ID assigned to target SAP HANA database object.
    try {
      AsyncRequestStatus result = apiInstance.unconfigureSapHanaRestore(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SapHanaApi#unconfigureSapHanaRestore");
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
| **id** | **String**| ID assigned to target SAP HANA database object. | |

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
| **202** | Status of the request. |  -  |

