# FailoverClusterFailoverClusterAppApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkDeleteFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#bulkDeleteFailoverClusterApp) | **DELETE** /failover_cluster/failover_cluster_app/bulk | Delete failover cluster applications |
| [**createFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#createFailoverClusterApp) | **POST** /failover_cluster/failover_cluster_app | Create a failover cluster app |
| [**deleteFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#deleteFailoverClusterApp) | **DELETE** /failover_cluster/failover_cluster_app/{id} | Delete a failover cluster app |
| [**getFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#getFailoverClusterApp) | **GET** /failover_cluster/failover_cluster_app/{id} | Get details of a failover cluster app |
| [**queryFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#queryFailoverClusterApp) | **GET** /failover_cluster/failover_cluster_app | Get a summary of all failover cluster apps |
| [**updateFailoverClusterApp**](FailoverClusterFailoverClusterAppApi.md#updateFailoverClusterApp) | **PATCH** /failover_cluster/failover_cluster_app/{id} | Update a failover cluster app |


<a id="bulkDeleteFailoverClusterApp"></a>
# **bulkDeleteFailoverClusterApp**
> bulkDeleteFailoverClusterApp(ids, preserveSnapshots)

Delete failover cluster applications

Delete failover cluster applications from Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterFailoverClusterAppApi;

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

    FailoverClusterFailoverClusterAppApi apiInstance = new FailoverClusterFailoverClusterAppApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | The ID of each failover cluster application to delete.
    Boolean preserveSnapshots = true; // Boolean | Specifies whether to preserve the snapshots of the fileset that belongs to a failover cluster application. When this value is 'true,' the snapshots are preserved. The default value is 'true'.
    try {
      apiInstance.bulkDeleteFailoverClusterApp(ids, preserveSnapshots);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterFailoverClusterAppApi#bulkDeleteFailoverClusterApp");
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
| **ids** | [**List&lt;String&gt;**](String.md)| The ID of each failover cluster application to delete. | |
| **preserveSnapshots** | **Boolean**| Specifies whether to preserve the snapshots of the fileset that belongs to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;. | [optional] |

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
| **204** | Successfully deleted all the specified failover cluster applications. |  -  |
| **404** | The failover cluster application deletion failed for at least one failover cluster application. |  -  |

<a id="createFailoverClusterApp"></a>
# **createFailoverClusterApp**
> FailoverClusterAppSummary createFailoverClusterApp(failoverClusterAppConfig)

Create a failover cluster app

Create a failover cluster app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterFailoverClusterAppApi;

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

    FailoverClusterFailoverClusterAppApi apiInstance = new FailoverClusterFailoverClusterAppApi(defaultClient);
    FailoverClusterAppConfig failoverClusterAppConfig = new FailoverClusterAppConfig(); // FailoverClusterAppConfig | Create configuration parameters for a failover cluster app.
    try {
      FailoverClusterAppSummary result = apiInstance.createFailoverClusterApp(failoverClusterAppConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterFailoverClusterAppApi#createFailoverClusterApp");
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
| **failoverClusterAppConfig** | [**FailoverClusterAppConfig**](FailoverClusterAppConfig.md)| Create configuration parameters for a failover cluster app. | |

### Return type

[**FailoverClusterAppSummary**](FailoverClusterAppSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Details of the new failover cluster app. |  -  |

<a id="deleteFailoverClusterApp"></a>
# **deleteFailoverClusterApp**
> deleteFailoverClusterApp(id, preserveSnapshots)

Delete a failover cluster app

Delete a failover cluster app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterFailoverClusterAppApi;

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

    FailoverClusterFailoverClusterAppApi apiInstance = new FailoverClusterFailoverClusterAppApi(defaultClient);
    String id = "id_example"; // String | ID of the failover cluster app.
    Boolean preserveSnapshots = true; // Boolean | A Boolean that specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is 'true,' the snapshots are preserved. The default value is 'true'.
    try {
      apiInstance.deleteFailoverClusterApp(id, preserveSnapshots);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterFailoverClusterAppApi#deleteFailoverClusterApp");
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
| **id** | **String**| ID of the failover cluster app. | |
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
| **204** | Successfully deleted the specified failover cluster app. |  -  |

<a id="getFailoverClusterApp"></a>
# **getFailoverClusterApp**
> FailoverClusterAppDetail getFailoverClusterApp(id)

Get details of a failover cluster app

Get details of a failover cluster app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterFailoverClusterAppApi;

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

    FailoverClusterFailoverClusterAppApi apiInstance = new FailoverClusterFailoverClusterAppApi(defaultClient);
    String id = "id_example"; // String | ID of the failover cluster app.
    try {
      FailoverClusterAppDetail result = apiInstance.getFailoverClusterApp(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterFailoverClusterAppApi#getFailoverClusterApp");
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
| **id** | **String**| ID of the failover cluster app. | |

### Return type

[**FailoverClusterAppDetail**](FailoverClusterAppDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about the failover cluster app. |  -  |

<a id="queryFailoverClusterApp"></a>
# **queryFailoverClusterApp**
> FailoverClusterAppSummaryListResponse queryFailoverClusterApp(name, slaAssignment, primaryClusterId, operatingSystemType, limit, offset, sortBy, sortOrder)

Get a summary of all failover cluster apps

Get a summary of all failover cluster apps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterFailoverClusterAppApi;

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

    FailoverClusterFailoverClusterAppApi apiInstance = new FailoverClusterFailoverClusterAppApi(defaultClient);
    String name = "name_example"; // String | Filter the response by comparing the failover cluster app name with the specified value.
    String slaAssignment = "Derived"; // String | Limit a response to the results that have the specified SLA Domain assignment type.
    String primaryClusterId = "primaryClusterId_example"; // String | Limit a response to the results that have the specified primary cluster value.
    String operatingSystemType = "ANY"; // String | Filter a response based on the failover cluster operating system type.
    Integer limit = 56; // Integer | Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort.
    Integer offset = 56; // Integer | Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results.
    String sortBy = "name"; // String | Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      FailoverClusterAppSummaryListResponse result = apiInstance.queryFailoverClusterApp(name, slaAssignment, primaryClusterId, operatingSystemType, limit, offset, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterFailoverClusterAppApi#queryFailoverClusterApp");
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
| **name** | **String**| Filter the response by comparing the failover cluster app name with the specified value. | [optional] |
| **slaAssignment** | **String**| Limit a response to the results that have the specified SLA Domain assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **primaryClusterId** | **String**| Limit a response to the results that have the specified primary cluster value. | [optional] |
| **operatingSystemType** | **String**| Filter a response based on the failover cluster operating system type. | [optional] [enum: ANY, AIX, HPUX, Linux, SunOS, UnixLike, Windows] |
| **limit** | **Integer**| Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort. | [optional] |
| **offset** | **Integer**| Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results. | [optional] |
| **sortBy** | **String**| Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified. | [optional] [enum: name] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**FailoverClusterAppSummaryListResponse**](FailoverClusterAppSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful query results for failover cluster app. |  -  |

<a id="updateFailoverClusterApp"></a>
# **updateFailoverClusterApp**
> FailoverClusterAppSummary updateFailoverClusterApp(id, failoverClusterAppConfig)

Update a failover cluster app

Update the failover cluster app with specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterFailoverClusterAppApi;

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

    FailoverClusterFailoverClusterAppApi apiInstance = new FailoverClusterFailoverClusterAppApi(defaultClient);
    String id = "id_example"; // String | ID of failover cluster app.
    FailoverClusterAppConfig failoverClusterAppConfig = new FailoverClusterAppConfig(); // FailoverClusterAppConfig | Properties to update.
    try {
      FailoverClusterAppSummary result = apiInstance.updateFailoverClusterApp(id, failoverClusterAppConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterFailoverClusterAppApi#updateFailoverClusterApp");
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
| **id** | **String**| ID of failover cluster app. | |
| **failoverClusterAppConfig** | [**FailoverClusterAppConfig**](FailoverClusterAppConfig.md)| Properties to update. | |

### Return type

[**FailoverClusterAppSummary**](FailoverClusterAppSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return details about the failover cluster app. |  -  |

