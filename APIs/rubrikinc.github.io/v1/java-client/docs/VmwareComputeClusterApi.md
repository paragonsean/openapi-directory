# VmwareComputeClusterApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAsyncRequestStatusForComputeCluster**](VmwareComputeClusterApi.md#getAsyncRequestStatusForComputeCluster) | **GET** /vmware/compute_cluster/request/{id} | Get asynchronous request details for VMware cluster |
| [**getComputeCluster**](VmwareComputeClusterApi.md#getComputeCluster) | **GET** /vmware/compute_cluster/{id} | Get details for the compute cluster |
| [**getIoFilters**](VmwareComputeClusterApi.md#getIoFilters) | **GET** /vmware/compute_cluster/{id}/io_filter | Get the ioFilters on the VMware compute cluster with a specific ID |
| [**installIoFilter**](VmwareComputeClusterApi.md#installIoFilter) | **POST** /vmware/compute_cluster/{id}/install_io_filter | Install the Rubrik ioFilter to the VMware cluster with a specific ID |
| [**queryComputeCluster**](VmwareComputeClusterApi.md#queryComputeCluster) | **GET** /vmware/compute_cluster | Get all the clusters belonging to this datacenter |
| [**uninstallIoFilter**](VmwareComputeClusterApi.md#uninstallIoFilter) | **POST** /vmware/compute_cluster/{id}/uninstall_io_filter | Uninstall the Rubrik ioFilter from the VMware cluster with a specific ID |
| [**updateComputeCluster**](VmwareComputeClusterApi.md#updateComputeCluster) | **PATCH** /vmware/compute_cluster/{id} | Modify information for a VMware compute cluster |
| [**upgradeIoFilter**](VmwareComputeClusterApi.md#upgradeIoFilter) | **POST** /vmware/compute_cluster/{id}/upgrade_io_filter | Upgrade the Rubrik ioFilter for the VMware cluster with a specific ID |


<a id="getAsyncRequestStatusForComputeCluster"></a>
# **getAsyncRequestStatusForComputeCluster**
> AsyncRequestStatus getAsyncRequestStatusForComputeCluster(id)

Get asynchronous request details for VMware cluster

Get the details of an asynchronous request that involves a VMware compute cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareComputeClusterApi;

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

    VmwareComputeClusterApi apiInstance = new VmwareComputeClusterApi(defaultClient);
    String id = "id_example"; // String | ID of an asynchronous request.
    try {
      AsyncRequestStatus result = apiInstance.getAsyncRequestStatusForComputeCluster(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareComputeClusterApi#getAsyncRequestStatusForComputeCluster");
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
| **id** | **String**| ID of an asynchronous request. | |

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
| **200** | Status of an asynchronous request. |  -  |

<a id="getComputeCluster"></a>
# **getComputeCluster**
> ComputeClusterDetail getComputeCluster(id)

Get details for the compute cluster

Get details for the compute cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareComputeClusterApi;

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

    VmwareComputeClusterApi apiInstance = new VmwareComputeClusterApi(defaultClient);
    String id = "id_example"; // String | ID of the compute cluster.
    try {
      ComputeClusterDetail result = apiInstance.getComputeCluster(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareComputeClusterApi#getComputeCluster");
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
| **id** | **String**| ID of the compute cluster. | |

### Return type

[**ComputeClusterDetail**](ComputeClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the requested compute cluster. |  -  |

<a id="getIoFilters"></a>
# **getIoFilters**
> IoFilterSummaryListResponse getIoFilters(id)

Get the ioFilters on the VMware compute cluster with a specific ID

Get the summary of the ioFilters on the VMware compute cluster with a specific ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareComputeClusterApi;

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

    VmwareComputeClusterApi apiInstance = new VmwareComputeClusterApi(defaultClient);
    String id = "id_example"; // String | ID of the VMware compute cluster.
    try {
      IoFilterSummaryListResponse result = apiInstance.getIoFilters(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareComputeClusterApi#getIoFilters");
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
| **id** | **String**| ID of the VMware compute cluster. | |

### Return type

[**IoFilterSummaryListResponse**](IoFilterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of the ioFilters on the VMware compute cluster. |  -  |
| **404** | Returned if there is no compute cluster with the given ID. |  -  |

<a id="installIoFilter"></a>
# **installIoFilter**
> AsyncRequestStatus installIoFilter(id, fullyQualifiedDomainNameInfo)

Install the Rubrik ioFilter to the VMware cluster with a specific ID

Install the latest version of Rubrik ioFilter to the VMware cluster with a specific ID. The cluster must be in maintenance mode to install the ioFilter successfully. The vCenter of the VMware compute cluster must be of version 6.7 and above.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareComputeClusterApi;

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

    VmwareComputeClusterApi apiInstance = new VmwareComputeClusterApi(defaultClient);
    String id = "id_example"; // String | ID of the VMware compute cluster.
    FullyQualifiedDomainNameInfo fullyQualifiedDomainNameInfo = new FullyQualifiedDomainNameInfo(); // FullyQualifiedDomainNameInfo | 
    try {
      AsyncRequestStatus result = apiInstance.installIoFilter(id, fullyQualifiedDomainNameInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareComputeClusterApi#installIoFilter");
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
| **id** | **String**| ID of the VMware compute cluster. | |
| **fullyQualifiedDomainNameInfo** | [**FullyQualifiedDomainNameInfo**](FullyQualifiedDomainNameInfo.md)|  | |

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
| **202** | Status of the Rubrik ioFilter installation job. |  -  |
| **404** | Returned if there is no compute cluster with the given ID. |  -  |

<a id="queryComputeCluster"></a>
# **queryComputeCluster**
> ComputeClusterSummaryListResponse queryComputeCluster(datacenterId, primaryClusterId, snappableStatus)

Get all the clusters belonging to this datacenter

Get all the clusters belonging to this datacenter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareComputeClusterApi;

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

    VmwareComputeClusterApi apiInstance = new VmwareComputeClusterApi(defaultClient);
    String datacenterId = "datacenterId_example"; // String | Filter clusters on data center ID.
    String primaryClusterId = "primaryClusterId_example"; // String | Filter on a primary cluster ID. Also accepts value 'local'.
    String snappableStatus = "Protectable"; // String | Determines whether to fetch Compute Clusters with additional privilege checks.
    try {
      ComputeClusterSummaryListResponse result = apiInstance.queryComputeCluster(datacenterId, primaryClusterId, snappableStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareComputeClusterApi#queryComputeCluster");
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
| **datacenterId** | **String**| Filter clusters on data center ID. | [optional] |
| **primaryClusterId** | **String**| Filter on a primary cluster ID. Also accepts value &#39;local&#39;. | [optional] |
| **snappableStatus** | **String**| Determines whether to fetch Compute Clusters with additional privilege checks. | [optional] [enum: Protectable] |

### Return type

[**ComputeClusterSummaryListResponse**](ComputeClusterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns list of compute clusters subject to provided filters. |  -  |

<a id="uninstallIoFilter"></a>
# **uninstallIoFilter**
> AsyncRequestStatus uninstallIoFilter(id)

Uninstall the Rubrik ioFilter from the VMware cluster with a specific ID

Uninstall the Rubrik ioFilter from the VMware cluster with a specific ID. The cluster must be in maintenance mode to uninstall the ioFilter successfully. The vCenter of the VMware compute cluster must be of version 6.7 and above.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareComputeClusterApi;

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

    VmwareComputeClusterApi apiInstance = new VmwareComputeClusterApi(defaultClient);
    String id = "id_example"; // String | ID of the VMware compute cluster.
    try {
      AsyncRequestStatus result = apiInstance.uninstallIoFilter(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareComputeClusterApi#uninstallIoFilter");
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
| **id** | **String**| ID of the VMware compute cluster. | |

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
| **202** | Status of the Rubrik ioFilter uninstallation job. |  -  |
| **404** | Returned if there is no compute cluster with the given id. |  -  |

<a id="updateComputeCluster"></a>
# **updateComputeCluster**
> ComputeClusterDetail updateComputeCluster(id, computeClusterUpdate)

Modify information for a VMware compute cluster

Update the configuredSlaDomainId for a VMware compute cluster with a specific ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareComputeClusterApi;

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

    VmwareComputeClusterApi apiInstance = new VmwareComputeClusterApi(defaultClient);
    String id = "id_example"; // String | ID of the compute cluster.
    ComputeClusterUpdate computeClusterUpdate = new ComputeClusterUpdate(); // ComputeClusterUpdate | Object with changes for the Compute Cluster information.
    try {
      ComputeClusterDetail result = apiInstance.updateComputeCluster(id, computeClusterUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareComputeClusterApi#updateComputeCluster");
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
| **id** | **String**| ID of the compute cluster. | |
| **computeClusterUpdate** | [**ComputeClusterUpdate**](ComputeClusterUpdate.md)| Object with changes for the Compute Cluster information. | |

### Return type

[**ComputeClusterDetail**](ComputeClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the updated compute cluster. |  -  |

<a id="upgradeIoFilter"></a>
# **upgradeIoFilter**
> AsyncRequestStatus upgradeIoFilter(id, fullyQualifiedDomainNameInfo)

Upgrade the Rubrik ioFilter for the VMware cluster with a specific ID

Upgrade the Rubrik ioFilter for a VMware cluster with a specific ID. The cluster must be in maintenance mode to upgrade the ioFilter successfully. The vCenter of the VMware compute cluster must be of version 6.7 and above.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareComputeClusterApi;

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

    VmwareComputeClusterApi apiInstance = new VmwareComputeClusterApi(defaultClient);
    String id = "id_example"; // String | ID of the VMware compute cluster.
    FullyQualifiedDomainNameInfo fullyQualifiedDomainNameInfo = new FullyQualifiedDomainNameInfo(); // FullyQualifiedDomainNameInfo | 
    try {
      AsyncRequestStatus result = apiInstance.upgradeIoFilter(id, fullyQualifiedDomainNameInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareComputeClusterApi#upgradeIoFilter");
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
| **id** | **String**| ID of the VMware compute cluster. | |
| **fullyQualifiedDomainNameInfo** | [**FullyQualifiedDomainNameInfo**](FullyQualifiedDomainNameInfo.md)|  | |

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
| **202** | Status of the Rubrik ioFilter upgrade. |  -  |
| **404** | Returned if there is no compute cluster with the given id. |  -  |

