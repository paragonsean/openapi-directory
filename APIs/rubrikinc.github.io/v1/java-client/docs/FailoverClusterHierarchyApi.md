# FailoverClusterHierarchyApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFailoverClusterHierarchyChildren**](FailoverClusterHierarchyApi.md#getFailoverClusterHierarchyChildren) | **GET** /failover_cluster/hierarchy/{id}/children | Get list of immediate descendant objects |
| [**getFailoverClusterHierarchyDescendants**](FailoverClusterHierarchyApi.md#getFailoverClusterHierarchyDescendants) | **GET** /failover_cluster/hierarchy/{id}/descendants | Get list of descendant objects |
| [**getFailoverClusterHierarchyObject**](FailoverClusterHierarchyApi.md#getFailoverClusterHierarchyObject) | **GET** /failover_cluster/hierarchy/{id} | Get summary of a hierarchy object |


<a id="getFailoverClusterHierarchyChildren"></a>
# **getFailoverClusterHierarchyChildren**
> FailoverClusterHierarchyObjectSummaryListResponse getFailoverClusterHierarchyChildren(id, name, operatingSystemType, objectType, primaryClusterId, limit, offset, configuredSlaDomainId, slaAssignment, sortBy, sortOrder)

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
import org.openapitools.client.api.FailoverClusterHierarchyApi;

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

    FailoverClusterHierarchyApi apiInstance = new FailoverClusterHierarchyApi(defaultClient);
    String id = "id_example"; // String | ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID.
    String name = "name_example"; // String | Filter a response by making an infix comparison of the failover cluster name or failover cluster app name.
    String operatingSystemType = "ANY"; // String | Filter a response based on the failover cluster operating system type.
    String objectType = "FailoverClusterApp"; // String | Filter by node object type.
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster ID, or **local**.
    Integer limit = 56; // Integer | An integer that specifies the maximum number of matches to return.
    Integer offset = 56; // Integer | An integer that specifies a number of initial matches to ignore.
    String configuredSlaDomainId = "configuredSlaDomainId_example"; // String | Filter by configured SLA domain.
    String slaAssignment = "Derived"; // String | Filter by SLA assignment type.
    String sortBy = "name"; // String | Attribute to sort the results on.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      FailoverClusterHierarchyObjectSummaryListResponse result = apiInstance.getFailoverClusterHierarchyChildren(id, name, operatingSystemType, objectType, primaryClusterId, limit, offset, configuredSlaDomainId, slaAssignment, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterHierarchyApi#getFailoverClusterHierarchyChildren");
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
| **id** | **String**| ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID. | |
| **name** | **String**| Filter a response by making an infix comparison of the failover cluster name or failover cluster app name. | [optional] |
| **operatingSystemType** | **String**| Filter a response based on the failover cluster operating system type. | [optional] [enum: ANY, AIX, HPUX, Linux, SunOS, UnixLike, Windows] |
| **objectType** | **String**| Filter by node object type. | [optional] [enum: FailoverClusterApp, Fileset, HostFailoverCluster, WindowsCluster] |
| **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] |
| **limit** | **Integer**| An integer that specifies the maximum number of matches to return. | [optional] |
| **offset** | **Integer**| An integer that specifies a number of initial matches to ignore. | [optional] |
| **configuredSlaDomainId** | **String**| Filter by configured SLA domain. | [optional] |
| **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **sortBy** | **String**| Attribute to sort the results on. | [optional] [enum: name, effectiveSlaDomainName] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |

### Return type

[**FailoverClusterHierarchyObjectSummaryListResponse**](FailoverClusterHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary list of descendant objects. |  -  |

<a id="getFailoverClusterHierarchyDescendants"></a>
# **getFailoverClusterHierarchyDescendants**
> FailoverClusterHierarchyObjectSummaryListResponse getFailoverClusterHierarchyDescendants(id, name, operatingSystemType, objectType, primaryClusterId, limit, offset, configuredSlaDomainId, slaAssignment, sortBy, sortOrder)

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
import org.openapitools.client.api.FailoverClusterHierarchyApi;

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

    FailoverClusterHierarchyApi apiInstance = new FailoverClusterHierarchyApi(defaultClient);
    String id = "id_example"; // String | ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID.
    String name = "name_example"; // String | Filter a response by making an infix comparison of the failover cluster name or failover cluster app name.
    String operatingSystemType = "ANY"; // String | Filter a response based on the failover cluster operating system type.
    String objectType = "FailoverClusterApp"; // String | Filter by node object type.
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster ID, or **local**.
    Integer limit = 56; // Integer | An integer that specifies the maximum number of matches to return.
    Integer offset = 56; // Integer | An integer that specifies a number of initial matches to ignore.
    String configuredSlaDomainId = "configuredSlaDomainId_example"; // String | Filter by configured SLA domain.
    String slaAssignment = "Derived"; // String | Filter by SLA assignment type.
    String sortBy = "name"; // String | Attribute to sort the results on.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      FailoverClusterHierarchyObjectSummaryListResponse result = apiInstance.getFailoverClusterHierarchyDescendants(id, name, operatingSystemType, objectType, primaryClusterId, limit, offset, configuredSlaDomainId, slaAssignment, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterHierarchyApi#getFailoverClusterHierarchyDescendants");
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
| **id** | **String**| ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID. | |
| **name** | **String**| Filter a response by making an infix comparison of the failover cluster name or failover cluster app name. | [optional] |
| **operatingSystemType** | **String**| Filter a response based on the failover cluster operating system type. | [optional] [enum: ANY, AIX, HPUX, Linux, SunOS, UnixLike, Windows] |
| **objectType** | **String**| Filter by node object type. | [optional] [enum: FailoverClusterApp, Fileset, HostFailoverCluster, WindowsCluster] |
| **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] |
| **limit** | **Integer**| An integer that specifies the maximum number of matches to return. | [optional] |
| **offset** | **Integer**| An integer that specifies a number of initial matches to ignore. | [optional] |
| **configuredSlaDomainId** | **String**| Filter by configured SLA domain. | [optional] |
| **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **sortBy** | **String**| Attribute to sort the results on. | [optional] [enum: name, effectiveSlaDomainName] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |

### Return type

[**FailoverClusterHierarchyObjectSummaryListResponse**](FailoverClusterHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary list of descendant objects. |  -  |

<a id="getFailoverClusterHierarchyObject"></a>
# **getFailoverClusterHierarchyObject**
> FailoverClusterHierarchyObjectSummary getFailoverClusterHierarchyObject(id)

Get summary of a hierarchy object

Retrieve details for the specified hierarchy object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverClusterHierarchyApi;

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

    FailoverClusterHierarchyApi apiInstance = new FailoverClusterHierarchyApi(defaultClient);
    String id = "id_example"; // String | ID of the hierarchy object.
    try {
      FailoverClusterHierarchyObjectSummary result = apiInstance.getFailoverClusterHierarchyObject(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverClusterHierarchyApi#getFailoverClusterHierarchyObject");
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
| **id** | **String**| ID of the hierarchy object. | |

### Return type

[**FailoverClusterHierarchyObjectSummary**](FailoverClusterHierarchyObjectSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the hierarchy object. |  -  |

