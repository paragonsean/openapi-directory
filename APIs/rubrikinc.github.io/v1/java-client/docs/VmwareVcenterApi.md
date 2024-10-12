# VmwareVcenterApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRefresh**](VmwareVcenterApi.md#createRefresh) | **POST** /vmware/vcenter/{id}/refresh | Refresh vCenter Server metadata |
| [**createRefreshVmV1**](VmwareVcenterApi.md#createRefreshVmV1) | **POST** /vmware/vcenter/{id}/refresh_vm | Refresh single virtual machine metadata in a vcenter |
| [**createVcenter**](VmwareVcenterApi.md#createVcenter) | **POST** /vmware/vcenter | Add vCenter Server |
| [**deleteVcenter**](VmwareVcenterApi.md#deleteVcenter) | **DELETE** /vmware/vcenter/{id} | Remove vCenter Server |
| [**getHotAddBandwidth**](VmwareVcenterApi.md#getHotAddBandwidth) | **GET** /vmware/vcenter/{id}/hotadd/bandwidth | Get the ingest and export bandwidth limits for HotAdd with the vCenter |
| [**getHotAddNetwork**](VmwareVcenterApi.md#getHotAddNetwork) | **GET** /vmware/vcenter/{id}/hotadd/network | Retrieve the user-configured network for HotAdd operations |
| [**getNetworks**](VmwareVcenterApi.md#getNetworks) | **GET** /vmware/vcenter/{id}/networks | Get the user-configured networks in the vCenter |
| [**getNumProxiesNeeded**](VmwareVcenterApi.md#getNumProxiesNeeded) | **GET** /vmware/vcenter/{id}/hotadd/needed | Get the number of HotAdd proxies needed for the vCenter |
| [**getVcenter**](VmwareVcenterApi.md#getVcenter) | **GET** /vmware/vcenter/{id} | Get the details of a vCenter Server |
| [**getVcenterAsyncRequestStatus**](VmwareVcenterApi.md#getVcenterAsyncRequestStatus) | **GET** /vmware/vcenter/request/{id} | Get vCenter Server async request |
| [**patchVcenter**](VmwareVcenterApi.md#patchVcenter) | **PATCH** /vmware/vcenter/{id} | Update the SLA Domain for a vCenter Server |
| [**queryHotAddProxyVm**](VmwareVcenterApi.md#queryHotAddProxyVm) | **GET** /vmware/vcenter/hotadd/vm | Get a list of HotAdd proxy virtual machines |
| [**queryVcenter**](VmwareVcenterApi.md#queryVcenter) | **GET** /vmware/vcenter | Get list of vCenters |
| [**setHotAddBandwidth**](VmwareVcenterApi.md#setHotAddBandwidth) | **POST** /vmware/vcenter/{id}/hotadd/bandwidth | Set the ingest and export bandwidth limits for HotAdd with the vCenter |
| [**setHotAddNetwork**](VmwareVcenterApi.md#setHotAddNetwork) | **POST** /vmware/vcenter/{id}/hotadd/network | Set the user-configured network for HotAdd backup and recovery |
| [**updateVcenter**](VmwareVcenterApi.md#updateVcenter) | **PUT** /vmware/vcenter/{id} | Update vCenter Server |


<a id="createRefresh"></a>
# **createRefresh**
> AsyncRequestStatus createRefresh(id)

Refresh vCenter Server metadata

Create a job to refresh the metadata for the specified vCenter Server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | ID of the vCenter Server.
    try {
      AsyncRequestStatus result = apiInstance.createRefresh(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#createRefresh");
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
| **id** | **String**| ID of the vCenter Server. | |

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
| **202** | Job Instance ID of the scheduled vCenter Server refresh job. |  -  |

<a id="createRefreshVmV1"></a>
# **createRefreshVmV1**
> createRefreshVmV1(id, body)

Refresh single virtual machine metadata in a vcenter

Refresh the metadata for a single virtual machine controlled by vCenter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | The ID of the vCenter server that controls the management of the virtual machine whose metadata will be refreshed.
    String body = "body_example"; // String | The vCenter managed object ID (MOID) of the virtual machine whose metadata will be refreshed.
    try {
      apiInstance.createRefreshVmV1(id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#createRefreshVmV1");
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
| **id** | **String**| The ID of the vCenter server that controls the management of the virtual machine whose metadata will be refreshed. | |
| **body** | **String**| The vCenter managed object ID (MOID) of the virtual machine whose metadata will be refreshed. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The virtual machine metadata was refreshed successfully. |  -  |

<a id="createVcenter"></a>
# **createVcenter**
> AsyncRequestStatus createVcenter(vcenterConfig)

Add vCenter Server

(DEPRECATED) Create a vCenter Server object by providing the address and account credentials of the vCenter Server. Initiates an asynchronous job to establish a connection with the vCenter Server and retrieve all metadata. Use GET /vcenter/{id}/status to check status. The recommended endpoint is /v2/vmware/vcenter. This endpoint will remain available in future releases despite deprecation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    VcenterConfig vcenterConfig = new VcenterConfig(); // VcenterConfig | IP address and account credentials of the vCenter Server server, and ID of the managing Rubrik cluster.
    try {
      AsyncRequestStatus result = apiInstance.createVcenter(vcenterConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#createVcenter");
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
| **vcenterConfig** | [**VcenterConfig**](VcenterConfig.md)| IP address and account credentials of the vCenter Server server, and ID of the managing Rubrik cluster. | |

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
| **202** | Status for the add vCenter Server request. |  -  |

<a id="deleteVcenter"></a>
# **deleteVcenter**
> AsyncRequestStatus deleteVcenter(id)

Remove vCenter Server

Initiates an asynchronous job to remove a vCenter Server object. The vCenter Server cannot have VMs mounted through the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | ID of the vCenter Server. to remove.
    try {
      AsyncRequestStatus result = apiInstance.deleteVcenter(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#deleteVcenter");
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
| **id** | **String**| ID of the vCenter Server. to remove. | |

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
| **202** | Status for the async request. |  -  |

<a id="getHotAddBandwidth"></a>
# **getHotAddBandwidth**
> HotAddBandwidthInfo getHotAddBandwidth(id)

Get the ingest and export bandwidth limits for HotAdd with the vCenter

Get the ingest and export bandwidth limits in Mbps when using HotAdd with the vCenter. These limits are shared across all HotAdd proxies for the Center.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | The ID of the vCenter server from which to derive the number of proxies needed.
    try {
      HotAddBandwidthInfo result = apiInstance.getHotAddBandwidth(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#getHotAddBandwidth");
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
| **id** | **String**| The ID of the vCenter server from which to derive the number of proxies needed. | |

### Return type

[**HotAddBandwidthInfo**](HotAddBandwidthInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ingest and export bandwidth limits for the vCenter. |  -  |

<a id="getHotAddNetwork"></a>
# **getHotAddNetwork**
> HotAddNetworkConfigWithName getHotAddNetwork(id)

Retrieve the user-configured network for HotAdd operations

Retrieve the user-configured network for HotAdd backup and recovery operations on VMware on AWS.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | ID of the vCenter server for which the Rubrik cluster is retrieving the configured HotAdd network information.
    try {
      HotAddNetworkConfigWithName result = apiInstance.getHotAddNetwork(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#getHotAddNetwork");
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
| **id** | **String**| ID of the vCenter server for which the Rubrik cluster is retrieving the configured HotAdd network information. | |

### Return type

[**HotAddNetworkConfigWithName**](HotAddNetworkConfigWithName.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Configured network information for the HotAdd proxy virtual machines. |  -  |

<a id="getNetworks"></a>
# **getNetworks**
> NetworkInfoListResponse getNetworks(id)

Get the user-configured networks in the vCenter

Get the names and IDs of the user configured networks in the vCenter. This information enables users to choose a desired network for backups to go through for VMware Cloud on AWS setups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | The ID of the vCenter server for which to retrieve user-configured networks.
    try {
      NetworkInfoListResponse result = apiInstance.getNetworks(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#getNetworks");
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
| **id** | **String**| The ID of the vCenter server for which to retrieve user-configured networks. | |

### Return type

[**NetworkInfoListResponse**](NetworkInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of network IDs and Names. |  -  |

<a id="getNumProxiesNeeded"></a>
# **getNumProxiesNeeded**
> HotAddProxiesNeededInfo getNumProxiesNeeded(id)

Get the number of HotAdd proxies needed for the vCenter

Get the number of HotAdd proxies that need to be deployed to the vCenter to support the maximum number of ingest jobs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | The ID of the vCenter server for which to get the number of proxies needed.
    try {
      HotAddProxiesNeededInfo result = apiInstance.getNumProxiesNeeded(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#getNumProxiesNeeded");
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
| **id** | **String**| The ID of the vCenter server for which to get the number of proxies needed. | |

### Return type

[**HotAddProxiesNeededInfo**](HotAddProxiesNeededInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number of HotAdd proxies needed for the vCenter. |  -  |

<a id="getVcenter"></a>
# **getVcenter**
> VcenterDetail getVcenter(id)

Get the details of a vCenter Server

Retrieve detailed information for a vCenter Server object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | ID of the vCenter Server.
    try {
      VcenterDetail result = apiInstance.getVcenter(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#getVcenter");
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
| **id** | **String**| ID of the vCenter Server. | |

### Return type

[**VcenterDetail**](VcenterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details for a vCenter Server object. |  -  |

<a id="getVcenterAsyncRequestStatus"></a>
# **getVcenterAsyncRequestStatus**
> AsyncRequestStatus getVcenterAsyncRequestStatus(id)

Get vCenter Server async request

Get details about a vcenter related async request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | ID of the request.
    try {
      AsyncRequestStatus result = apiInstance.getVcenterAsyncRequestStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#getVcenterAsyncRequestStatus");
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

<a id="patchVcenter"></a>
# **patchVcenter**
> VcenterSummary patchVcenter(id, vcenterPatch)

Update the SLA Domain for a vCenter Server

Update the SLA Domain that is configured for a vCenter Server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | ID of the vCenter Server.
    VcenterPatch vcenterPatch = new VcenterPatch(); // VcenterPatch | Object containing updated vCenter Server information.
    try {
      VcenterSummary result = apiInstance.patchVcenter(id, vcenterPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#patchVcenter");
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
| **id** | **String**| ID of the vCenter Server. | |
| **vcenterPatch** | [**VcenterPatch**](VcenterPatch.md)| Object containing updated vCenter Server information. | |

### Return type

[**VcenterSummary**](VcenterSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the updated vCenter Server object. |  -  |

<a id="queryHotAddProxyVm"></a>
# **queryHotAddProxyVm**
> HotAddProxyVmInfoListResponse queryHotAddProxyVm(name, sortBy, sortOrder)

Get a list of HotAdd proxy virtual machines

Retrieve summary information for all HotAdd proxy virtual machines.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String name = "name_example"; // String | Limit the list information to HotAdd proxy virtual machines that match the specified HotAdd proxy virtual machine 'name' value.
    String sortBy = "name"; // String | Attribute to use to sort the HotAdd proxy virtual machines summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      HotAddProxyVmInfoListResponse result = apiInstance.queryHotAddProxyVm(name, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#queryHotAddProxyVm");
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
| **name** | **String**| Limit the list information to HotAdd proxy virtual machines that match the specified HotAdd proxy virtual machine &#39;name&#39; value. | [optional] |
| **sortBy** | **String**| Attribute to use to sort the HotAdd proxy virtual machines summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order. | [optional] [enum: name] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |

### Return type

[**HotAddProxyVmInfoListResponse**](HotAddProxyVmInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for HotAdd proxy virtual machines. |  -  |

<a id="queryVcenter"></a>
# **queryVcenter**
> VcenterSummaryListResponse queryVcenter(primaryClusterId, snappableStatus, ignoreConnectionStatus)

Get list of vCenters

Retrieve information for each managed vCenter, including: ID, managed ID, address, username, SLA ID, and primary cluster ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String primaryClusterId = "primaryClusterId_example"; // String | Limits the information to the Rubrik cluster specified by the value of primary_cluster_id. Use 'local' for the Rubrik cluster that is hosting the current REST API session.
    String snappableStatus = "Protectable"; // String | Determines whether to fetch vCenters with additional privilege checks.
    Boolean ignoreConnectionStatus = true; // Boolean | Don't ping vCenters for connection status. The connection_status field in the response is unusable.
    try {
      VcenterSummaryListResponse result = apiInstance.queryVcenter(primaryClusterId, snappableStatus, ignoreConnectionStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#queryVcenter");
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
| **primaryClusterId** | **String**| Limits the information to the Rubrik cluster specified by the value of primary_cluster_id. Use &#39;local&#39; for the Rubrik cluster that is hosting the current REST API session. | [optional] |
| **snappableStatus** | **String**| Determines whether to fetch vCenters with additional privilege checks. | [optional] [enum: Protectable] |
| **ignoreConnectionStatus** | **Boolean**| Don&#39;t ping vCenters for connection status. The connection_status field in the response is unusable. | [optional] |

### Return type

[**VcenterSummaryListResponse**](VcenterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for managed vCenters. |  -  |

<a id="setHotAddBandwidth"></a>
# **setHotAddBandwidth**
> setHotAddBandwidth(id, hotAddBandwidthInfo)

Set the ingest and export bandwidth limits for HotAdd with the vCenter

Set the ingest and export bandwidth limits in Mbps when using HotAdd with the vCenter. These limits are shared across all HotAdd proxies for the Center.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | ID of the vCenter server upon which the Rubrik cluster is setting the HotAdd bandwidth limits.
    HotAddBandwidthInfo hotAddBandwidthInfo = new HotAddBandwidthInfo(); // HotAddBandwidthInfo | The ingest and export bandwidth limits for the vCenter.
    try {
      apiInstance.setHotAddBandwidth(id, hotAddBandwidthInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#setHotAddBandwidth");
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
| **id** | **String**| ID of the vCenter server upon which the Rubrik cluster is setting the HotAdd bandwidth limits. | |
| **hotAddBandwidthInfo** | [**HotAddBandwidthInfo**](HotAddBandwidthInfo.md)| The ingest and export bandwidth limits for the vCenter. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The bandwidth was set correctly. |  -  |

<a id="setHotAddNetwork"></a>
# **setHotAddNetwork**
> setHotAddNetwork(id, hotAddNetworkConfigWithId)

Set the user-configured network for HotAdd backup and recovery

Set the user-configured network for HotAdd backup and recovery operations on VMware on AWS.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | ID of the vCenter server for which the Rubrik cluster is setting the HotAdd network information.
    HotAddNetworkConfigWithId hotAddNetworkConfigWithId = new HotAddNetworkConfigWithId(); // HotAddNetworkConfigWithId | The information about a static IP address and user-configured vCenter network selected for HotAdd backup and recovery.
    try {
      apiInstance.setHotAddNetwork(id, hotAddNetworkConfigWithId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#setHotAddNetwork");
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
| **id** | **String**| ID of the vCenter server for which the Rubrik cluster is setting the HotAdd network information. | |
| **hotAddNetworkConfigWithId** | [**HotAddNetworkConfigWithId**](HotAddNetworkConfigWithId.md)| The information about a static IP address and user-configured vCenter network selected for HotAdd backup and recovery. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The network was set correctly. |  -  |

<a id="updateVcenter"></a>
# **updateVcenter**
> VcenterSummary updateVcenter(id, vcenterConfig)

Update vCenter Server

Update the address, username and password of the specified vCenter Server object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareVcenterApi;

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

    VmwareVcenterApi apiInstance = new VmwareVcenterApi(defaultClient);
    String id = "id_example"; // String | ID of the vCenter Server.
    VcenterConfig vcenterConfig = new VcenterConfig(); // VcenterConfig | Object containing updated vCenter Server information.
    try {
      VcenterSummary result = apiInstance.updateVcenter(id, vcenterConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareVcenterApi#updateVcenter");
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
| **id** | **String**| ID of the vCenter Server. | |
| **vcenterConfig** | [**VcenterConfig**](VcenterConfig.md)| Object containing updated vCenter Server information. | |

### Return type

[**VcenterSummary**](VcenterSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the updated vCenter Server object. |  -  |

