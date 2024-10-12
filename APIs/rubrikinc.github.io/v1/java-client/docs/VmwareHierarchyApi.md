# VmwareHierarchyApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVmwareHierarchyExport**](VmwareHierarchyApi.md#getVmwareHierarchyExport) | **GET** /vmware/hierarchy/export | Get Available VMware Hierarchy Objects for Export Operations |
| [**getVmwareHierarchyObject**](VmwareHierarchyApi.md#getVmwareHierarchyObject) | **GET** /vmware/hierarchy/{id}/export | Get VMware Hierarchy Object Information |


<a id="getVmwareHierarchyExport"></a>
# **getVmwareHierarchyExport**
> VmwareHierarchyInfoListResponse getVmwareHierarchyExport(rootId)

Get Available VMware Hierarchy Objects for Export Operations

Get VMware Clusters, Hosts, and Resource Pool hierarchy objects that are available as the target for Virtual Machine Export operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareHierarchyApi;

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

    VmwareHierarchyApi apiInstance = new VmwareHierarchyApi(defaultClient);
    String rootId = "rootId_example"; // String | Get child objects of given root ID.
    try {
      VmwareHierarchyInfoListResponse result = apiInstance.getVmwareHierarchyExport(rootId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareHierarchyApi#getVmwareHierarchyExport");
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
| **rootId** | **String**| Get child objects of given root ID. | [optional] |

### Return type

[**VmwareHierarchyInfoListResponse**](VmwareHierarchyInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about Child Hierarchy Objects of Root. |  -  |

<a id="getVmwareHierarchyObject"></a>
# **getVmwareHierarchyObject**
> VmwareHierarchyInfo getVmwareHierarchyObject(id)

Get VMware Hierarchy Object Information

Get VMware Clusters, Hosts, and Resource Pool hierarchy object detail information by object ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareHierarchyApi;

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

    VmwareHierarchyApi apiInstance = new VmwareHierarchyApi(defaultClient);
    String id = "id_example"; // String | Get VMware hierarchy objects of given ID.
    try {
      VmwareHierarchyInfo result = apiInstance.getVmwareHierarchyObject(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareHierarchyApi#getVmwareHierarchyObject");
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
| **id** | **String**| Get VMware hierarchy objects of given ID. | |

### Return type

[**VmwareHierarchyInfo**](VmwareHierarchyInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | VMware hierarchy object details. |  -  |

