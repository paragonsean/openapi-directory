# FailoverClusterApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkDeleteFailoverCluster**](FailoverClusterApi.md#bulkDeleteFailoverCluster) | **DELETE** /failover_cluster/bulk | Delete the provided failover clusters |
| [**createFailoverCluster**](FailoverClusterApi.md#createFailoverCluster) | **POST** /failover_cluster | Create a failover cluster |
| [**deleteFailoverCluster**](FailoverClusterApi.md#deleteFailoverCluster) | **DELETE** /failover_cluster/{id} | Delete a failover cluster |
| [**getFailoverCluster**](FailoverClusterApi.md#getFailoverCluster) | **GET** /failover_cluster/{id} | Get details of a failover cluster |
| [**queryFailoverCluster**](FailoverClusterApi.md#queryFailoverCluster) | **GET** /failover_cluster | Get a summary of all failover clusters |
| [**updateFailoverCluster**](FailoverClusterApi.md#updateFailoverCluster) | **PATCH** /failover_cluster/{id} | Update a failover cluster |


<a id="bulkDeleteFailoverCluster"></a>
# **bulkDeleteFailoverCluster**
> bulkDeleteFailoverCluster(ids, preserveSnapshots)

Delete the provided failover clusters

Delete the provided failover clusters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterApi;

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

    FailoverClusterApi apiInstance = new FailoverClusterApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | The ID of each failover cluster to delete.
    Boolean preserveSnapshots = true; // Boolean | Specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is 'true,' the snapshots are preserved. The default value is 'true'.
    try {
      apiInstance.bulkDeleteFailoverCluster(ids, preserveSnapshots);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterApi#bulkDeleteFailoverCluster");
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
| **ids** | [**List&lt;String&gt;**](String.md)| The ID of each failover cluster to delete. | |
| **preserveSnapshots** | **Boolean**| Specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;. | [optional] |

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
| **204** | Successfully deleted all the specified failover clusters. |  -  |
| **404** | The failover cluster deletion failed for at least one failover cluster. |  -  |

<a id="createFailoverCluster"></a>
# **createFailoverCluster**
> FailoverClusterDetail createFailoverCluster(failoverClusterConfig)

Create a failover cluster

Create a failover cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterApi;

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

    FailoverClusterApi apiInstance = new FailoverClusterApi(defaultClient);
    FailoverClusterConfig failoverClusterConfig = new FailoverClusterConfig(); // FailoverClusterConfig | Create configuration parameters for a failover cluster.
    try {
      FailoverClusterDetail result = apiInstance.createFailoverCluster(failoverClusterConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterApi#createFailoverCluster");
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
| **failoverClusterConfig** | [**FailoverClusterConfig**](FailoverClusterConfig.md)| Create configuration parameters for a failover cluster. | |

### Return type

[**FailoverClusterDetail**](FailoverClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Details of the new failover cluster. |  -  |

<a id="deleteFailoverCluster"></a>
# **deleteFailoverCluster**
> deleteFailoverCluster(id, preserveSnapshots)

Delete a failover cluster

Delete a failover cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterApi;

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

    FailoverClusterApi apiInstance = new FailoverClusterApi(defaultClient);
    String id = "id_example"; // String | ID of the failover cluster.
    Boolean preserveSnapshots = true; // Boolean | A Boolean that specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is 'true,' the snapshots are preserved. The default value is 'true'.
    try {
      apiInstance.deleteFailoverCluster(id, preserveSnapshots);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterApi#deleteFailoverCluster");
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
| **id** | **String**| ID of the failover cluster. | |
| **preserveSnapshots** | **Boolean**| A Boolean that specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;. | [optional] |

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
| **204** | Successfully deleted the specified failover cluster. |  -  |

<a id="getFailoverCluster"></a>
# **getFailoverCluster**
> FailoverClusterDetail getFailoverCluster(id)

Get details of a failover cluster

Get details of a failover cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterApi;

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

    FailoverClusterApi apiInstance = new FailoverClusterApi(defaultClient);
    String id = "id_example"; // String | ID of the failover cluster.
    try {
      FailoverClusterDetail result = apiInstance.getFailoverCluster(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterApi#getFailoverCluster");
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
| **id** | **String**| ID of the failover cluster. | |

### Return type

[**FailoverClusterDetail**](FailoverClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about the failover cluster. |  -  |

<a id="queryFailoverCluster"></a>
# **queryFailoverCluster**
> FailoverClusterSummaryListResponse queryFailoverCluster(name, operatingSystemType, slaAssignment, primaryClusterId, limit, offset, sortBy, sortOrder)

Get a summary of all failover clusters

Get a summary of all failover clusters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterApi;

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

    FailoverClusterApi apiInstance = new FailoverClusterApi(defaultClient);
    String name = "name_example"; // String | Filter a response by making an infix comparison of the failover cluster name in the response, with the specified value.
    String operatingSystemType = "ANY"; // String | Filter a response based on the operating system type.
    String slaAssignment = "Derived"; // String | Limit a response to the results that have the specified SLA Domain assignment type.
    String primaryClusterId = "primaryClusterId_example"; // String | Limit a response to the results that have the specified primary cluster value.
    Integer limit = 56; // Integer | Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort.
    Integer offset = 56; // Integer | Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results.
    String sortBy = "name"; // String | Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      FailoverClusterSummaryListResponse result = apiInstance.queryFailoverCluster(name, operatingSystemType, slaAssignment, primaryClusterId, limit, offset, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterApi#queryFailoverCluster");
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
| **name** | **String**| Filter a response by making an infix comparison of the failover cluster name in the response, with the specified value. | [optional] |
| **operatingSystemType** | **String**| Filter a response based on the operating system type. | [optional] [enum: ANY, AIX, HPUX, Linux, SunOS, UnixLike, Windows] |
| **slaAssignment** | **String**| Limit a response to the results that have the specified SLA Domain assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **primaryClusterId** | **String**| Limit a response to the results that have the specified primary cluster value. | [optional] |
| **limit** | **Integer**| Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort. | [optional] |
| **offset** | **Integer**| Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results. | [optional] |
| **sortBy** | **String**| Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified. | [optional] [enum: name] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**FailoverClusterSummaryListResponse**](FailoverClusterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful query results for failover cluster. |  -  |

<a id="updateFailoverCluster"></a>
# **updateFailoverCluster**
> FailoverClusterDetail updateFailoverCluster(id, failoverClusterConfig)

Update a failover cluster

Update failover cluster with specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterApi;

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

    FailoverClusterApi apiInstance = new FailoverClusterApi(defaultClient);
    String id = "id_example"; // String | ID of failover cluster.
    FailoverClusterConfig failoverClusterConfig = new FailoverClusterConfig(); // FailoverClusterConfig | Properties to update.
    try {
      FailoverClusterDetail result = apiInstance.updateFailoverCluster(id, failoverClusterConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterApi#updateFailoverCluster");
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
| **id** | **String**| ID of failover cluster. | |
| **failoverClusterConfig** | [**FailoverClusterConfig**](FailoverClusterConfig.md)| Properties to update. | |

### Return type

[**FailoverClusterDetail**](FailoverClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return details about the failover cluster. |  -  |

