# FlowLogsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**flowLogsCreateOrUpdate**](FlowLogsApi.md#flowLogsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/flowLogs/{flowLogName} |  |
| [**flowLogsDelete**](FlowLogsApi.md#flowLogsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/flowLogs/{flowLogName} |  |
| [**flowLogsGet**](FlowLogsApi.md#flowLogsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/flowLogs/{flowLogName} |  |
| [**flowLogsList**](FlowLogsApi.md#flowLogsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/flowLogs |  |


<a id="flowLogsCreateOrUpdate"></a>
# **flowLogsCreateOrUpdate**
> FlowLog flowLogsCreateOrUpdate(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId, parameters)



Create or update a flow log for the specified network security group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlowLogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FlowLogsApi apiInstance = new FlowLogsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String flowLogName = "flowLogName_example"; // String | The name of the flow log.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    FlowLog parameters = new FlowLog(); // FlowLog | Parameters that define the create or update flow log resource.
    try {
      FlowLog result = apiInstance.flowLogsCreateOrUpdate(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlowLogsApi#flowLogsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **networkWatcherName** | **String**| The name of the network watcher. | |
| **flowLogName** | **String**| The name of the flow log. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**FlowLog**](FlowLog.md)| Parameters that define the create or update flow log resource. | |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting flow log resource. |  -  |
| **201** | Request successful. The operation returns the resulting flow log resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="flowLogsDelete"></a>
# **flowLogsDelete**
> flowLogsDelete(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId)



Deletes the specified flow log resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlowLogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FlowLogsApi apiInstance = new FlowLogsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String flowLogName = "flowLogName_example"; // String | The name of the flow log resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.flowLogsDelete(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlowLogsApi#flowLogsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **networkWatcherName** | **String**| The name of the network watcher. | |
| **flowLogName** | **String**| The name of the flow log resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Delete successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="flowLogsGet"></a>
# **flowLogsGet**
> FlowLog flowLogsGet(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId)



Gets a flow log resource by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlowLogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FlowLogsApi apiInstance = new FlowLogsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String flowLogName = "flowLogName_example"; // String | The name of the flow log resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      FlowLog result = apiInstance.flowLogsGet(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlowLogsApi#flowLogsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **networkWatcherName** | **String**| The name of the network watcher. | |
| **flowLogName** | **String**| The name of the flow log resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a flow log resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="flowLogsList"></a>
# **flowLogsList**
> FlowLogListResult flowLogsList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId)



Lists all flow log resources for the specified Network Watcher.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlowLogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FlowLogsApi apiInstance = new FlowLogsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      FlowLogListResult result = apiInstance.flowLogsList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlowLogsApi#flowLogsList");
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
| **resourceGroupName** | **String**| The name of the resource group containing Network Watcher. | |
| **networkWatcherName** | **String**| The name of the Network Watcher resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**FlowLogListResult**](FlowLogListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful flow log enumeration request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

