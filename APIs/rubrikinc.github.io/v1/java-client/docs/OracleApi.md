# OracleApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkUpdateOracleDb**](OracleApi.md#bulkUpdateOracleDb) | **PATCH** /oracle/db/bulk | Update Oracle Databases |
| [**bulkUpdateOracleHost**](OracleApi.md#bulkUpdateOracleHost) | **PATCH** /oracle/host/bulk | Update Oracle Hosts |
| [**bulkUpdateOracleRac**](OracleApi.md#bulkUpdateOracleRac) | **PATCH** /oracle/rac/bulk | Update Oracle RACs |
| [**createOracleValidateBackupJob**](OracleApi.md#createOracleValidateBackupJob) | **POST** /oracle/db/{id}/validate | Validate Oracle database backups |
| [**deleteDownloadedSnapshots**](OracleApi.md#deleteDownloadedSnapshots) | **DELETE** /oracle/db/{id}/downloaded_snapshots | Delete downloaded Oracle database snapshots and log snapshots |
| [**getAcoParameterList**](OracleApi.md#getAcoParameterList) | **GET** /oracle/aco_parameter_list | List of supported Advanced Cloning Options |
| [**getExampleAcoDownloadLink**](OracleApi.md#getExampleAcoDownloadLink) | **GET** /oracle/aco_example_download_link | Link to download the Advanced Recovery Options example file |
| [**getOracleDbV1**](OracleApi.md#getOracleDbV1) | **GET** /oracle/db/{id} | Get Oracle database information |
| [**oracleRestoreEstimate**](OracleApi.md#oracleRestoreEstimate) | **GET** /oracle/db/{id}/restore_estimate | Get a size estimate for a restore or export |
| [**queryOracleDbV1**](OracleApi.md#queryOracleDbV1) | **GET** /oracle/db | Get summary information for Oracle databases |
| [**updateOracleDataGuardGroup**](OracleApi.md#updateOracleDataGuardGroup) | **PATCH** /oracle/data_guard_group/{id} | Update an Oracle Data Guard group |
| [**updateOracleDbV1**](OracleApi.md#updateOracleDbV1) | **PATCH** /oracle/db/{id} | Update an Oracle database |
| [**validateOracleAcoFile**](OracleApi.md#validateOracleAcoFile) | **POST** /oracle/validate_aco_file | Validate Oracle ACO file |


<a id="bulkUpdateOracleDb"></a>
# **bulkUpdateOracleDb**
> BulkOracleDbDetails bulkUpdateOracleDb(oracleBulkUpdate)

Update Oracle Databases

Update the properties of the objects that represent the specified Oracle Databases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    OracleBulkUpdate oracleBulkUpdate = new OracleBulkUpdate(); // OracleBulkUpdate | Properties to use for the update of Oracle Database objects.
    try {
      BulkOracleDbDetails result = apiInstance.bulkUpdateOracleDb(oracleBulkUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#bulkUpdateOracleDb");
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
| **oracleBulkUpdate** | [**OracleBulkUpdate**](OracleBulkUpdate.md)| Properties to use for the update of Oracle Database objects. | |

### Return type

[**BulkOracleDbDetails**](BulkOracleDbDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated Oracle Database objects. |  -  |

<a id="bulkUpdateOracleHost"></a>
# **bulkUpdateOracleHost**
> BulkOracleHostDetails bulkUpdateOracleHost(oracleBulkUpdate)

Update Oracle Hosts

Update properties to Oracle Host objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    OracleBulkUpdate oracleBulkUpdate = new OracleBulkUpdate(); // OracleBulkUpdate | Properties to use for the update of Oracle Host objects.
    try {
      BulkOracleHostDetails result = apiInstance.bulkUpdateOracleHost(oracleBulkUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#bulkUpdateOracleHost");
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
| **oracleBulkUpdate** | [**OracleBulkUpdate**](OracleBulkUpdate.md)| Properties to use for the update of Oracle Host objects. | |

### Return type

[**BulkOracleHostDetails**](BulkOracleHostDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated Oracle Host objects. |  -  |

<a id="bulkUpdateOracleRac"></a>
# **bulkUpdateOracleRac**
> BulkOracleRacDetails bulkUpdateOracleRac(oracleBulkUpdate)

Update Oracle RACs

Update the properties of the objects that represent the specified Oracle RAC.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    OracleBulkUpdate oracleBulkUpdate = new OracleBulkUpdate(); // OracleBulkUpdate | Properties to use for the update of Oracle RAC objects.
    try {
      BulkOracleRacDetails result = apiInstance.bulkUpdateOracleRac(oracleBulkUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#bulkUpdateOracleRac");
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
| **oracleBulkUpdate** | [**OracleBulkUpdate**](OracleBulkUpdate.md)| Properties to use for the update of Oracle RAC objects. | |

### Return type

[**BulkOracleRacDetails**](BulkOracleRacDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated Oracle RAC objects. |  -  |

<a id="createOracleValidateBackupJob"></a>
# **createOracleValidateBackupJob**
> AsyncRequestStatus createOracleValidateBackupJob(id, oracleValidateConfig)

Validate Oracle database backups

Queue a job to validate Oracle backups for a database snapshot or a specified timestamp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    String id = "id_example"; // String | ID of the database to be validated.
    OracleValidateConfig oracleValidateConfig = new OracleValidateConfig(); // OracleValidateConfig | Configuration parameters for a job to validate an Oracle backups.
    try {
      AsyncRequestStatus result = apiInstance.createOracleValidateBackupJob(id, oracleValidateConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#createOracleValidateBackupJob");
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
| **id** | **String**| ID of the database to be validated. | |
| **oracleValidateConfig** | [**OracleValidateConfig**](OracleValidateConfig.md)| Configuration parameters for a job to validate an Oracle backups. | |

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
| **202** | Request status for the queued job to validate Oracle backups for a specified timestamp. |  -  |

<a id="deleteDownloadedSnapshots"></a>
# **deleteDownloadedSnapshots**
> AsyncRequestStatus deleteDownloadedSnapshots(id, afterTime, beforeTime)

Delete downloaded Oracle database snapshots and log snapshots

Requests an asynchronous job to expire downloaded database snapshots taken during a specified time period as well as log snapshots that contain any logs with timestamps within that time period.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    String id = "id_example"; // String | ID of the Oracle database.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Uses the ISO 8601 format to specify the start of the time period used by the asynchronous snapshot expiration job, as in the example \"2016-01-01T01:23:45.678\".
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Uses the ISO 8601 format to specify the end of the time period used by the asynchronous snapshot expiration job, as in the example \"2016-01-01T01:23:45.678\".
    try {
      AsyncRequestStatus result = apiInstance.deleteDownloadedSnapshots(id, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#deleteDownloadedSnapshots");
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
| **id** | **String**| ID of the Oracle database. | |
| **afterTime** | **OffsetDateTime**| Uses the ISO 8601 format to specify the start of the time period used by the asynchronous snapshot expiration job, as in the example \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |
| **beforeTime** | **OffsetDateTime**| Uses the ISO 8601 format to specify the end of the time period used by the asynchronous snapshot expiration job, as in the example \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |

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
| **202** | The request status of the asynchronous job that deletes downloaded Oracle database snapshots and log snapshots. |  -  |

<a id="getAcoParameterList"></a>
# **getAcoParameterList**
> OracleAcoParameterList getAcoParameterList()

List of supported Advanced Cloning Options

Get the list of supported Advanced Cloning Options (ACO) parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    try {
      OracleAcoParameterList result = apiInstance.getAcoParameterList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#getAcoParameterList");
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

[**OracleAcoParameterList**](OracleAcoParameterList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of supported Advanced Cloning Options (ACO) parameters. |  -  |

<a id="getExampleAcoDownloadLink"></a>
# **getExampleAcoDownloadLink**
> OracleFileDownloadLink getExampleAcoDownloadLink()

Link to download the Advanced Recovery Options example file

Link to download the Advanced Recovery Options example file which can be used to customize Oracle recoveries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    try {
      OracleFileDownloadLink result = apiInstance.getExampleAcoDownloadLink();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#getExampleAcoDownloadLink");
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

[**OracleFileDownloadLink**](OracleFileDownloadLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Link to download the example Advanced Recovery Options file. |  -  |

<a id="getOracleDbV1"></a>
# **getOracleDbV1**
> OracleDbDetail getOracleDbV1(id)

Get Oracle database information

Retrieves detailed information for a specified Oracle database object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    String id = "id_example"; // String | ID of an Oracle database object.
    try {
      OracleDbDetail result = apiInstance.getOracleDbV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#getOracleDbV1");
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
| **id** | **String**| ID of an Oracle database object. | |

### Return type

[**OracleDbDetail**](OracleDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information for the specified Oracle database. |  -  |

<a id="oracleRestoreEstimate"></a>
# **oracleRestoreEstimate**
> OracleRestoreEstimateResult oracleRestoreEstimate(id, snapshotId, recoveryTime)

Get a size estimate for a restore or export

The estimated size of the data to download from an archival location in order to perform a specified restore or export operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    String id = "id_example"; // String | ID of the Oracle database.
    String snapshotId = "snapshotId_example"; // String | ID of the snapshot to recover to.
    OffsetDateTime recoveryTime = OffsetDateTime.now(); // OffsetDateTime | The date and time for the recovery restore point, specified in the ISO 8601 format, as in the example \"2016-01-01T01:23:45.678\".
    try {
      OracleRestoreEstimateResult result = apiInstance.oracleRestoreEstimate(id, snapshotId, recoveryTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#oracleRestoreEstimate");
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
| **id** | **String**| ID of the Oracle database. | |
| **snapshotId** | **String**| ID of the snapshot to recover to. | [optional] |
| **recoveryTime** | **OffsetDateTime**| The date and time for the recovery restore point, specified in the ISO 8601 format, as in the example \&quot;2016-01-01T01:23:45.678\&quot;. | [optional] |

### Return type

[**OracleRestoreEstimateResult**](OracleRestoreEstimateResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the estimate for a restore or export to the specified recovery point. |  -  |

<a id="queryOracleDbV1"></a>
# **queryOracleDbV1**
> OracleDbSummaryListResponse queryOracleDbV1(name, slaAssignment, effectiveSlaDomainId, primaryClusterId, isRelic, isLiveMount, limit, offset, sortBy, sortOrder, includeBackupTaskInfo, isDataGuardGroup)

Get summary information for Oracle databases

Retrieves an array containing summary information about the Oracle database objects in the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    String name = "name_example"; // String | Filters a response by making an infix comparison of the database name, SID, and tablespaces in the response with the specified value.
    String slaAssignment = "Derived"; // String | Limits the response to Oracle databases that are protected by the specified type of SLA Domain assignment.
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filters by effective SLA Domain ID.
    String primaryClusterId = "primaryClusterId_example"; // String | Limits the response to Oracle databases that have the specified primary cluster value.
    Boolean isRelic = true; // Boolean | Limits the response to Oracle databases that have the specified isRelic value.
    Boolean isLiveMount = true; // Boolean | Limits the response to Oracle databases that have the specified isLiveMount value.
    Integer limit = 56; // Integer | Limits the summary information to the specified number of matches. Optionally, it can be used with offset to begin the count of matches at the number specified in the offset parameter, and with sort_by to sort the results by the specified attribute.
    Integer offset = 56; // Integer | Determines the elements to include in the response starting with the element at the index number specified here. Optionally used with limit to enable paging of the results by retrieving a smaller number of elements in the response.
    String sortBy = "effectiveSlaDomainName"; // String | Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
    String sortOrder = "asc"; // String | Specifies the ascending or descending order to sort the elements in the response by the attributes specified in the sort_by parameter.
    Boolean includeBackupTaskInfo = false; // Boolean | Specifies whether to include the backup task information in the response.
    Boolean isDataGuardGroup = true; // Boolean | Limits the response to Oracle databases that have the specified value for the isDataGuardGroup flag.
    try {
      OracleDbSummaryListResponse result = apiInstance.queryOracleDbV1(name, slaAssignment, effectiveSlaDomainId, primaryClusterId, isRelic, isLiveMount, limit, offset, sortBy, sortOrder, includeBackupTaskInfo, isDataGuardGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#queryOracleDbV1");
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
| **name** | **String**| Filters a response by making an infix comparison of the database name, SID, and tablespaces in the response with the specified value. | [optional] |
| **slaAssignment** | **String**| Limits the response to Oracle databases that are protected by the specified type of SLA Domain assignment. | [optional] [enum: Derived, Direct, Unassigned] |
| **effectiveSlaDomainId** | **String**| Filters by effective SLA Domain ID. | [optional] |
| **primaryClusterId** | **String**| Limits the response to Oracle databases that have the specified primary cluster value. | [optional] |
| **isRelic** | **Boolean**| Limits the response to Oracle databases that have the specified isRelic value. | [optional] |
| **isLiveMount** | **Boolean**| Limits the response to Oracle databases that have the specified isLiveMount value. | [optional] |
| **limit** | **Integer**| Limits the summary information to the specified number of matches. Optionally, it can be used with offset to begin the count of matches at the number specified in the offset parameter, and with sort_by to sort the results by the specified attribute. | [optional] |
| **offset** | **Integer**| Determines the elements to include in the response starting with the element at the index number specified here. Optionally used with limit to enable paging of the results by retrieving a smaller number of elements in the response. | [optional] |
| **sortBy** | **String**| Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified. | [optional] [enum: effectiveSlaDomainName, name] |
| **sortOrder** | **String**| Specifies the ascending or descending order to sort the elements in the response by the attributes specified in the sort_by parameter. | [optional] [enum: asc, desc] |
| **includeBackupTaskInfo** | **Boolean**| Specifies whether to include the backup task information in the response. | [optional] [default to false] |
| **isDataGuardGroup** | **Boolean**| Limits the response to Oracle databases that have the specified value for the isDataGuardGroup flag. | [optional] |

### Return type

[**OracleDbSummaryListResponse**](OracleDbSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of Oracle databases. |  -  |

<a id="updateOracleDataGuardGroup"></a>
# **updateOracleDataGuardGroup**
> OracleDbDetail updateOracleDataGuardGroup(id, oracleDataGuardGroupUpdate)

Update an Oracle Data Guard group

Update properties of an Oracle Data Guard group object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    String id = "id_example"; // String | ID assigned to an Oracle Data Guard group object.
    OracleDataGuardGroupUpdate oracleDataGuardGroupUpdate = new OracleDataGuardGroupUpdate(); // OracleDataGuardGroupUpdate | Properties to use for the update of an Oracle Data Guard group object.
    try {
      OracleDbDetail result = apiInstance.updateOracleDataGuardGroup(id, oracleDataGuardGroupUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#updateOracleDataGuardGroup");
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
| **id** | **String**| ID assigned to an Oracle Data Guard group object. | |
| **oracleDataGuardGroupUpdate** | [**OracleDataGuardGroupUpdate**](OracleDataGuardGroupUpdate.md)| Properties to use for the update of an Oracle Data Guard group object. | |

### Return type

[**OracleDbDetail**](OracleDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the Oracle Data Guard group object. |  -  |

<a id="updateOracleDbV1"></a>
# **updateOracleDbV1**
> OracleDbDetail updateOracleDbV1(id, oracleUpdate)

Update an Oracle database

Updates the properties of a specified Oracle database object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    String id = "id_example"; // String | ID of an Oracle database object.
    OracleUpdate oracleUpdate = new OracleUpdate(); // OracleUpdate | Properties of the Oracle database object to be updated. object.
    try {
      OracleDbDetail result = apiInstance.updateOracleDbV1(id, oracleUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#updateOracleDbV1");
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
| **id** | **String**| ID of an Oracle database object. | |
| **oracleUpdate** | [**OracleUpdate**](OracleUpdate.md)| Properties of the Oracle database object to be updated. object. | |

### Return type

[**OracleDbDetail**](OracleDbDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information for the updated Oracle database. |  -  |

<a id="validateOracleAcoFile"></a>
# **validateOracleAcoFile**
> OracleAcoValidationResult validateOracleAcoFile(isLiveMount, body)

Validate Oracle ACO file

Validate the provided Oracle ACO (Advanced Cloning Options) file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OracleApi;

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

    OracleApi apiInstance = new OracleApi(defaultClient);
    Boolean isLiveMount = true; // Boolean | Boolean that determines whether the ACO file is being used for a Live Mount.
    String body = "body_example"; // String | Contents of the Advanced Cloning Options file in base64 encoded format.
    try {
      OracleAcoValidationResult result = apiInstance.validateOracleAcoFile(isLiveMount, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OracleApi#validateOracleAcoFile");
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
| **isLiveMount** | **Boolean**| Boolean that determines whether the ACO file is being used for a Live Mount. | |
| **body** | **String**| Contents of the Advanced Cloning Options file in base64 encoded format. | |

### Return type

[**OracleAcoValidationResult**](OracleAcoValidationResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Validation result of the provided ACO file. |  -  |

