# VcdClusterApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVcdClusterV1**](VcdClusterApi.md#createVcdClusterV1) | **POST** /vcd/cluster | Add a vCD Cluster |
| [**deleteVcdClusterV1**](VcdClusterApi.md#deleteVcdClusterV1) | **DELETE** /vcd/cluster/{id} | Remove vCD Cluster |
| [**getVcdClusterAsyncRequestStatusV1**](VcdClusterApi.md#getVcdClusterAsyncRequestStatusV1) | **GET** /vcd/cluster/request/{id} | Get vCD Cluster job status |
| [**getVcdClusterV1**](VcdClusterApi.md#getVcdClusterV1) | **GET** /vcd/cluster/{id} | Get vCD Cluster details |
| [**queryVcdClusterV1**](VcdClusterApi.md#queryVcdClusterV1) | **GET** /vcd/cluster | Get summary for all vCD Clusters |
| [**queryVcdVimServerV1**](VcdClusterApi.md#queryVcdVimServerV1) | **GET** /vcd/cluster/{id}/vimserver | Get VimServers of a vCD Cluster |
| [**refreshVcdClusterV1**](VcdClusterApi.md#refreshVcdClusterV1) | **POST** /vcd/cluster/{id}/refresh | Refresh a vCD Cluster |
| [**updateVcdClusterV1**](VcdClusterApi.md#updateVcdClusterV1) | **PATCH** /vcd/cluster/{id} | Change vCD Cluster object |


<a id="createVcdClusterV1"></a>
# **createVcdClusterV1**
> AsyncRequestStatus createVcdClusterV1(vcdClusterConfig)

Add a vCD Cluster

Create a vCD Cluster object by providing the address of the vCD Cluster and the credentials for an account on the vCD Cluster that has administrator privileges. This request initiates an asynchronous job to connect with the vCD Cluster and retrieve the required metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdClusterApi;

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

    VcdClusterApi apiInstance = new VcdClusterApi(defaultClient);
    VcdClusterConfig vcdClusterConfig = new VcdClusterConfig(); // VcdClusterConfig | IP address and account credentials of the vCD Cluster, and ID of the managing Rubrik cluster.
    try {
      AsyncRequestStatus result = apiInstance.createVcdClusterV1(vcdClusterConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdClusterApi#createVcdClusterV1");
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
| **vcdClusterConfig** | [**VcdClusterConfig**](VcdClusterConfig.md)| IP address and account credentials of the vCD Cluster, and ID of the managing Rubrik cluster. | |

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
| **202** | Status of an async request to add a vCD Cluster. |  -  |

<a id="deleteVcdClusterV1"></a>
# **deleteVcdClusterV1**
> AsyncRequestStatus deleteVcdClusterV1(id)

Remove vCD Cluster

Start an asynchronous job to remove a vCD Cluster object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdClusterApi;

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

    VcdClusterApi apiInstance = new VcdClusterApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vCD Cluster object.
    try {
      AsyncRequestStatus result = apiInstance.deleteVcdClusterV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdClusterApi#deleteVcdClusterV1");
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
| **id** | **String**| ID assigned to a vCD Cluster object. | |

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
| **202** | Status of a job to delete a vCD Cluster. |  -  |

<a id="getVcdClusterAsyncRequestStatusV1"></a>
# **getVcdClusterAsyncRequestStatusV1**
> AsyncRequestStatus getVcdClusterAsyncRequestStatusV1(id)

Get vCD Cluster job status

Retrieve the details of a specified asynchronous job for a vCD Cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdClusterApi;

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

    VcdClusterApi apiInstance = new VcdClusterApi(defaultClient);
    String id = "id_example"; // String | ID assigned to an asynchronous job.
    try {
      AsyncRequestStatus result = apiInstance.getVcdClusterAsyncRequestStatusV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdClusterApi#getVcdClusterAsyncRequestStatusV1");
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
| **id** | **String**| ID assigned to an asynchronous job. | |

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
| **202** | Status of a vCD Cluster asynchronous job. |  -  |

<a id="getVcdClusterV1"></a>
# **getVcdClusterV1**
> VcdClusterDetail getVcdClusterV1(id)

Get vCD Cluster details

Retrieve detailed information for a vCD Cluster object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdClusterApi;

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

    VcdClusterApi apiInstance = new VcdClusterApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vCD Cluster object.
    try {
      VcdClusterDetail result = apiInstance.getVcdClusterV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdClusterApi#getVcdClusterV1");
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
| **id** | **String**| ID assigned to a vCD Cluster object. | |

### Return type

[**VcdClusterDetail**](VcdClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details for a vCD Cluster object. |  -  |

<a id="queryVcdClusterV1"></a>
# **queryVcdClusterV1**
> VcdClusterSummaryListResponse queryVcdClusterV1(name, status, sortBy, sortOrder)

Get summary for all vCD Clusters

Retrieve summary information for all vCD cluster objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdClusterApi;

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

    VcdClusterApi apiInstance = new VcdClusterApi(defaultClient);
    String name = "name_example"; // String | Search for a vCD Cluster object by name.
    String status = "Disconnected"; // String | Filter the results using the status value of the vCD Cluster objects.
    String sortBy = "Name"; // String | Attribute to sort the results on.
    String sortOrder = "asc"; // String | Order for sorting the results, either ascending or descending.
    try {
      VcdClusterSummaryListResponse result = apiInstance.queryVcdClusterV1(name, status, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdClusterApi#queryVcdClusterV1");
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
| **name** | **String**| Search for a vCD Cluster object by name. | [optional] |
| **status** | **String**| Filter the results using the status value of the vCD Cluster objects. | [optional] [enum: Disconnected, Refreshing, Connected, BadlyConfigured, Deleting, Remote] |
| **sortBy** | **String**| Attribute to sort the results on. | [optional] [enum: Name, Status] |
| **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**VcdClusterSummaryListResponse**](VcdClusterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for vCD clusters. |  -  |

<a id="queryVcdVimServerV1"></a>
# **queryVcdVimServerV1**
> VimserverSummaryListResponse queryVcdVimServerV1(id, sortBy, sortOrder)

Get VimServers of a vCD Cluster

Retrieves the VimServer representation of the vCenter Servers that are attached to a specified vCD Cluster object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdClusterApi;

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

    VcdClusterApi apiInstance = new VcdClusterApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vCD Cluster object.
    String sortBy = "Name"; // String | Attribute to sort the results on.
    String sortOrder = "asc"; // String | Order for sorting the results, either ascending or descending.
    try {
      VimserverSummaryListResponse result = apiInstance.queryVcdVimServerV1(id, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdClusterApi#queryVcdVimServerV1");
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
| **id** | **String**| ID assigned to a vCD Cluster object. | |
| **sortBy** | **String**| Attribute to sort the results on. | [optional] [enum: Name, Status] |
| **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**VimserverSummaryListResponse**](VimserverSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for VimServer objects. |  -  |

<a id="refreshVcdClusterV1"></a>
# **refreshVcdClusterV1**
> AsyncRequestStatus refreshVcdClusterV1(id)

Refresh a vCD Cluster

Start an asynchronous job to refresh the metadata for a specified vCD Cluster object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdClusterApi;

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

    VcdClusterApi apiInstance = new VcdClusterApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vCD Cluster object.
    try {
      AsyncRequestStatus result = apiInstance.refreshVcdClusterV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdClusterApi#refreshVcdClusterV1");
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
| **id** | **String**| ID assigned to a vCD Cluster object. | |

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
| **202** | Status of a vCD Cluster metadata refresh job. |  -  |

<a id="updateVcdClusterV1"></a>
# **updateVcdClusterV1**
> VcdClusterDetail updateVcdClusterV1(id, vcdClusterPatch)

Change vCD Cluster object

Modify the hostname and credentials of a specified vCD Cluster object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdClusterApi;

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

    VcdClusterApi apiInstance = new VcdClusterApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a vCD Cluster object.
    VcdClusterPatch vcdClusterPatch = new VcdClusterPatch(); // VcdClusterPatch | Updated hostname and credentials for a specified vCD Cluster object.
    try {
      VcdClusterDetail result = apiInstance.updateVcdClusterV1(id, vcdClusterPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdClusterApi#updateVcdClusterV1");
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
| **id** | **String**| ID assigned to a vCD Cluster object. | |
| **vcdClusterPatch** | [**VcdClusterPatch**](VcdClusterPatch.md)| Updated hostname and credentials for a specified vCD Cluster object. | |

### Return type

[**VcdClusterDetail**](VcdClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of an updated vCD Cluster object. |  -  |

