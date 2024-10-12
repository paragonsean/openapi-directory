# VmwareHostApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVmwareHost**](VmwareHostApi.md#getVmwareHost) | **GET** /vmware/host/{id} | Get details of a ESXi hypervisor |
| [**getVmwareHostDatastore**](VmwareHostApi.md#getVmwareHostDatastore) | **GET** /vmware/host/{id}/datastore | Get details of datastores in a ESXi hypervisor |
| [**queryVmwareHost**](VmwareHostApi.md#queryVmwareHost) | **GET** /vmware/host | Get summary of all the ESXi hypervisor |
| [**updateVmwareHost**](VmwareHostApi.md#updateVmwareHost) | **PATCH** /vmware/host/{id} | Update the SLA Domain for an ESXi hypervisor |


<a id="getVmwareHost"></a>
# **getVmwareHost**
> VmwareHostDetail getVmwareHost(id)

Get details of a ESXi hypervisor

Get details of a ESXi hypervisor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareHostApi;

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

    VmwareHostApi apiInstance = new VmwareHostApi(defaultClient);
    String id = "id_example"; // String | ID of the VMWare host.
    try {
      VmwareHostDetail result = apiInstance.getVmwareHost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareHostApi#getVmwareHost");
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
| **id** | **String**| ID of the VMWare host. | |

### Return type

[**VmwareHostDetail**](VmwareHostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about the vmware host. |  -  |

<a id="getVmwareHostDatastore"></a>
# **getVmwareHostDatastore**
> VmwareHostDatastoreDetail getVmwareHostDatastore(id)

Get details of datastores in a ESXi hypervisor

Get details of datastores in a ESXi hypervisor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareHostApi;

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

    VmwareHostApi apiInstance = new VmwareHostApi(defaultClient);
    String id = "id_example"; // String | ID of the VMWare host.
    try {
      VmwareHostDatastoreDetail result = apiInstance.getVmwareHostDatastore(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareHostApi#getVmwareHostDatastore");
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
| **id** | **String**| ID of the VMWare host. | |

### Return type

[**VmwareHostDatastoreDetail**](VmwareHostDatastoreDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about the vmware host. |  -  |

<a id="queryVmwareHost"></a>
# **queryVmwareHost**
> VmwareHostSummaryListResponse queryVmwareHost(primaryClusterId, computeClusterId, snappableStatus)

Get summary of all the ESXi hypervisor

Get summary of all the ESXi hypervisor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareHostApi;

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

    VmwareHostApi apiInstance = new VmwareHostApi(defaultClient);
    String primaryClusterId = "primaryClusterId_example"; // String | ID of the Primary cluster.
    String computeClusterId = "computeClusterId_example"; // String | Filter by ID of Compute Cluster.
    String snappableStatus = "Protectable"; // String | Requests additional data about VMware Hosts based on the specified query value.
    try {
      VmwareHostSummaryListResponse result = apiInstance.queryVmwareHost(primaryClusterId, computeClusterId, snappableStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareHostApi#queryVmwareHost");
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
| **primaryClusterId** | **String**| ID of the Primary cluster. | [optional] |
| **computeClusterId** | **String**| Filter by ID of Compute Cluster. | [optional] |
| **snappableStatus** | **String**| Requests additional data about VMware Hosts based on the specified query value. | [optional] [enum: Protectable] |

### Return type

[**VmwareHostSummaryListResponse**](VmwareHostSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of VMware host summaries. |  -  |

<a id="updateVmwareHost"></a>
# **updateVmwareHost**
> VmwareHostDetail updateVmwareHost(id, vmwareHostUpdate)

Update the SLA Domain for an ESXi hypervisor

Update the SLA Domain that is configured for an ESXi hypervisor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareHostApi;

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

    VmwareHostApi apiInstance = new VmwareHostApi(defaultClient);
    String id = "id_example"; // String | ID of the ESXi hypervisor.
    VmwareHostUpdate vmwareHostUpdate = new VmwareHostUpdate(); // VmwareHostUpdate | Object with changes for the ESXi hypervisor information.
    try {
      VmwareHostDetail result = apiInstance.updateVmwareHost(id, vmwareHostUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareHostApi#updateVmwareHost");
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
| **id** | **String**| ID of the ESXi hypervisor. | |
| **vmwareHostUpdate** | [**VmwareHostUpdate**](VmwareHostUpdate.md)| Object with changes for the ESXi hypervisor information. | |

### Return type

[**VmwareHostDetail**](VmwareHostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details for the ESXi hypervisor. |  -  |

