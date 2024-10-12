# SlaDomainApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignSlaToDownloadedSnapshots**](SlaDomainApi.md#assignSlaToDownloadedSnapshots) | **POST** /sla_domain/assign_to_downloaded_snapshots | Assign retention SLA Domain to the downloaded snapshots of a single object |
| [**createSlaDomain**](SlaDomainApi.md#createSlaDomain) | **POST** /sla_domain | Create SLA Domain |
| [**deleteSlaDomain**](SlaDomainApi.md#deleteSlaDomain) | **DELETE** /sla_domain/{id} | Remove SLA Domain |
| [**getSlaDomain**](SlaDomainApi.md#getSlaDomain) | **GET** /sla_domain/{id} | Get SLA Domain details |
| [**patchSlaDomain**](SlaDomainApi.md#patchSlaDomain) | **PATCH** /sla_domain/{id} | Patch SLA Domain |
| [**querySlaDomain**](SlaDomainApi.md#querySlaDomain) | **GET** /sla_domain | Get list of SLA Domains |
| [**updateSlaDomain**](SlaDomainApi.md#updateSlaDomain) | **PUT** /sla_domain/{id} | Update SLA Domain |


<a id="assignSlaToDownloadedSnapshots"></a>
# **assignSlaToDownloadedSnapshots**
> BatchAsyncRequestStatus assignSlaToDownloadedSnapshots(downloadedSnapshotSlaAssignmentInfo)

Assign retention SLA Domain to the downloaded snapshots of a single object

Assigns an SLA Domain to a list of downloaded snapshots. The SLA Domain manages retention for the snapshots in the downloaded location. The assignment does not affect the retention of the snapshots in other locations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlaDomainApi;

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

    SlaDomainApi apiInstance = new SlaDomainApi(defaultClient);
    DownloadedSnapshotSlaAssignmentInfo downloadedSnapshotSlaAssignmentInfo = new DownloadedSnapshotSlaAssignmentInfo(); // DownloadedSnapshotSlaAssignmentInfo | An object ID and a list of IDs for the downloaded snapshots. The specified SLA Domain manages retention for the downloaded copy of snapshots assigned to the specified IDs.
    try {
      BatchAsyncRequestStatus result = apiInstance.assignSlaToDownloadedSnapshots(downloadedSnapshotSlaAssignmentInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlaDomainApi#assignSlaToDownloadedSnapshots");
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
| **downloadedSnapshotSlaAssignmentInfo** | [**DownloadedSnapshotSlaAssignmentInfo**](DownloadedSnapshotSlaAssignmentInfo.md)| An object ID and a list of IDs for the downloaded snapshots. The specified SLA Domain manages retention for the downloaded copy of snapshots assigned to the specified IDs. | |

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
| **202** | Queued asynchronous requests for assigning SLA Domains to downloaded snapshots. |  -  |

<a id="createSlaDomain"></a>
# **createSlaDomain**
> SlaDomainSummary createSlaDomain(slaDomainDefinition)

Create SLA Domain

Create a new SLA Domain on a Rubrik cluster by specifying Domain Rules and policies. Only Managed Volume objects support minute frequency to take transaction log backup. SLA assignment on other objects will be disallowed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlaDomainApi;

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

    SlaDomainApi apiInstance = new SlaDomainApi(defaultClient);
    SlaDomainDefinition slaDomainDefinition = new SlaDomainDefinition(); // SlaDomainDefinition | SLA Domain definition. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using Rubrik cluster timezone.
    try {
      SlaDomainSummary result = apiInstance.createSlaDomain(slaDomainDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlaDomainApi#createSlaDomain");
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
| **slaDomainDefinition** | [**SlaDomainDefinition**](SlaDomainDefinition.md)| SLA Domain definition. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using Rubrik cluster timezone. | |

### Return type

[**SlaDomainSummary**](SlaDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Summary of newly created SLA Domain. |  -  |

<a id="deleteSlaDomain"></a>
# **deleteSlaDomain**
> deleteSlaDomain(id)

Remove SLA Domain

Delete an SLA Domain from a Rubrik cluster. The SLA Domain must not be assigned to any VMs, filesets or databases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlaDomainApi;

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

    SlaDomainApi apiInstance = new SlaDomainApi(defaultClient);
    String id = "id_example"; // String | ID of the SLA Domain.
    try {
      apiInstance.deleteSlaDomain(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlaDomainApi#deleteSlaDomain");
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
| **id** | **String**| ID of the SLA Domain. | |

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
| **204** | Removed the specified SLA Domain. |  -  |

<a id="getSlaDomain"></a>
# **getSlaDomain**
> SlaDomainSummary getSlaDomain(id)

Get SLA Domain details

Retrieve summary information for a specified SLA Domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlaDomainApi;

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

    SlaDomainApi apiInstance = new SlaDomainApi(defaultClient);
    String id = "id_example"; // String | ID of the SLA Domain.
    try {
      SlaDomainSummary result = apiInstance.getSlaDomain(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlaDomainApi#getSlaDomain");
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
| **id** | **String**| ID of the SLA Domain. | |

### Return type

[**SlaDomainSummary**](SlaDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing information about the SLA Domain. |  -  |

<a id="patchSlaDomain"></a>
# **patchSlaDomain**
> SlaDomainSummary patchSlaDomain(id, slaDomainPatchDefinition, shouldApplyToExistingSnapshots)

Patch SLA Domain

(DEPRECATED) Patch the properties of an SLA Domain. The recommended endpoint is v3/sla_domain/{id}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlaDomainApi;

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

    SlaDomainApi apiInstance = new SlaDomainApi(defaultClient);
    String id = "id_example"; // String | ID of the SLA Domain.
    SlaDomainPatchDefinition slaDomainPatchDefinition = new SlaDomainPatchDefinition(); // SlaDomainPatchDefinition | Object containing the fields to be edited for SLA Domain. The SLA Domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using the Rubrik cluster timezone. Remote SLA Domain only supports edit to the archival specification.
    Boolean shouldApplyToExistingSnapshots = true; // Boolean | A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is 'true' by default.
    try {
      SlaDomainSummary result = apiInstance.patchSlaDomain(id, slaDomainPatchDefinition, shouldApplyToExistingSnapshots);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlaDomainApi#patchSlaDomain");
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
| **id** | **String**| ID of the SLA Domain. | |
| **slaDomainPatchDefinition** | [**SlaDomainPatchDefinition**](SlaDomainPatchDefinition.md)| Object containing the fields to be edited for SLA Domain. The SLA Domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using the Rubrik cluster timezone. Remote SLA Domain only supports edit to the archival specification. | |
| **shouldApplyToExistingSnapshots** | **Boolean**| A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is &#39;true&#39; by default. | [optional] |

### Return type

[**SlaDomainSummary**](SlaDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing the patched SLA Domain. |  -  |

<a id="querySlaDomain"></a>
# **querySlaDomain**
> SlaDomainSummaryListResponse querySlaDomain(primaryClusterId, name, sortBy, sortOrder, dataSources, snapshotIds)

Get list of SLA Domains

Retrieve summary information for all SLA Domains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlaDomainApi;

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

    SlaDomainApi apiInstance = new SlaDomainApi(defaultClient);
    String primaryClusterId = "primaryClusterId_example"; // String | Limits the information retrieved to those SLA Domains that are associated with the Rubrik cluster ID that is specified by primary_cluster_id. Use **local** for the Rubrik cluster that is hosting the current REST API session.
    String name = "name_example"; // String | Limit the list information to those SLA Domains which match the specified SLA Domain 'name' value.
    String sortBy = "name"; // String | Attribute to use to sort the SLA Domains summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending. If not specified, SLA Domain summary results will be sorted in ascending order.
    List<String> dataSources = Arrays.asList(); // List<String> | Limit the list information to SLA Domains that can be assigned to specified data sources.
    List<String> snapshotIds = Arrays.asList(); // List<String> | Limit the list information to SLA Domains that can be assigned to specified snapshots.
    try {
      SlaDomainSummaryListResponse result = apiInstance.querySlaDomain(primaryClusterId, name, sortBy, sortOrder, dataSources, snapshotIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlaDomainApi#querySlaDomain");
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
| **primaryClusterId** | **String**| Limits the information retrieved to those SLA Domains that are associated with the Rubrik cluster ID that is specified by primary_cluster_id. Use **local** for the Rubrik cluster that is hosting the current REST API session. | [optional] |
| **name** | **String**| Limit the list information to those SLA Domains which match the specified SLA Domain &#39;name&#39; value. | [optional] |
| **sortBy** | **String**| Attribute to use to sort the SLA Domains summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order. | [optional] [enum: name] |
| **sortOrder** | **String**| Sort order, either ascending or descending. If not specified, SLA Domain summary results will be sorted in ascending order. | [optional] [enum: asc, desc] |
| **dataSources** | [**List&lt;String&gt;**](String.md)| Limit the list information to SLA Domains that can be assigned to specified data sources. | [optional] |
| **snapshotIds** | [**List&lt;String&gt;**](String.md)| Limit the list information to SLA Domains that can be assigned to specified snapshots. | [optional] |

### Return type

[**SlaDomainSummaryListResponse**](SlaDomainSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for SLA Domains. |  -  |

<a id="updateSlaDomain"></a>
# **updateSlaDomain**
> SlaDomainSummary updateSlaDomain(id, slaDomainDefinition, shouldApplyToExistingSnapshots)

Update SLA Domain

Update the properties of an SLA Domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlaDomainApi;

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

    SlaDomainApi apiInstance = new SlaDomainApi(defaultClient);
    String id = "id_example"; // String | ID of the SLA Domain.
    SlaDomainDefinition slaDomainDefinition = new SlaDomainDefinition(); // SlaDomainDefinition | Object containing the updated SLA Domain. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snpashot. Specify times using the Rubrik cluster time zone.
    Boolean shouldApplyToExistingSnapshots = true; // Boolean | A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is 'true' by default.
    try {
      SlaDomainSummary result = apiInstance.updateSlaDomain(id, slaDomainDefinition, shouldApplyToExistingSnapshots);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlaDomainApi#updateSlaDomain");
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
| **id** | **String**| ID of the SLA Domain. | |
| **slaDomainDefinition** | [**SlaDomainDefinition**](SlaDomainDefinition.md)| Object containing the updated SLA Domain. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snpashot. Specify times using the Rubrik cluster time zone. | |
| **shouldApplyToExistingSnapshots** | **Boolean**| A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is &#39;true&#39; by default. | [optional] |

### Return type

[**SlaDomainSummary**](SlaDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing updated SLA Domain. |  -  |

