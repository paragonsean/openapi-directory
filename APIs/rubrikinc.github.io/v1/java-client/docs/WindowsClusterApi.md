# WindowsClusterApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWindowsCluster**](WindowsClusterApi.md#getWindowsCluster) | **GET** /windows_cluster/{id} | Get detailed information for a Windows cluster |
| [**queryWindowsCluster**](WindowsClusterApi.md#queryWindowsCluster) | **GET** /windows_cluster | Get summary information for Windows clusters |


<a id="getWindowsCluster"></a>
# **getWindowsCluster**
> WindowsClusterDetail getWindowsCluster(id)

Get detailed information for a Windows cluster

Returns a detailed view of a Windows server failover cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WindowsClusterApi;

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

    WindowsClusterApi apiInstance = new WindowsClusterApi(defaultClient);
    String id = "id_example"; // String | ID of the Windows cluster.
    try {
      WindowsClusterDetail result = apiInstance.getWindowsCluster(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WindowsClusterApi#getWindowsCluster");
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
| **id** | **String**| ID of the Windows cluster. | |

### Return type

[**WindowsClusterDetail**](WindowsClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

<a id="queryWindowsCluster"></a>
# **queryWindowsCluster**
> WindowsClusterSummaryListResponse queryWindowsCluster(primaryClusterId, isAgentless, snappableStatus)

Get summary information for Windows clusters

Returns a list of summary information for Windows server failover clusters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WindowsClusterApi;

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

    WindowsClusterApi apiInstance = new WindowsClusterApi(defaultClient);
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary_cluster_id. Use **local** for the local cluster.
    Boolean isAgentless = true; // Boolean | Filter by is_agentless flag.
    String snappableStatus = "Protectable"; // String | Determines whether Windows clusters are fetched with additional privilege checks.
    try {
      WindowsClusterSummaryListResponse result = apiInstance.queryWindowsCluster(primaryClusterId, isAgentless, snappableStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WindowsClusterApi#queryWindowsCluster");
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
| **primaryClusterId** | **String**| Filter by primary_cluster_id. Use **local** for the local cluster. | [optional] |
| **isAgentless** | **Boolean**| Filter by is_agentless flag. | [optional] |
| **snappableStatus** | **String**| Determines whether Windows clusters are fetched with additional privilege checks. | [optional] [enum: Protectable] |

### Return type

[**WindowsClusterSummaryListResponse**](WindowsClusterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the query was successful. |  -  |

