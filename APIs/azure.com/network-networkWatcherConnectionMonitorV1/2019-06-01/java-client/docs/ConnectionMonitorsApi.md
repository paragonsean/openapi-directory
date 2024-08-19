# ConnectionMonitorsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connectionMonitorsCreateOrUpdate**](ConnectionMonitorsApi.md#connectionMonitorsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName} |  |
| [**connectionMonitorsDelete**](ConnectionMonitorsApi.md#connectionMonitorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName} |  |
| [**connectionMonitorsGet**](ConnectionMonitorsApi.md#connectionMonitorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName} |  |
| [**connectionMonitorsList**](ConnectionMonitorsApi.md#connectionMonitorsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors |  |
| [**connectionMonitorsQuery**](ConnectionMonitorsApi.md#connectionMonitorsQuery) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/query |  |
| [**connectionMonitorsStart**](ConnectionMonitorsApi.md#connectionMonitorsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/start |  |
| [**connectionMonitorsStop**](ConnectionMonitorsApi.md#connectionMonitorsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/stop |  |
| [**connectionMonitorsUpdateTags**](ConnectionMonitorsApi.md#connectionMonitorsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName} |  |


<a id="connectionMonitorsCreateOrUpdate"></a>
# **connectionMonitorsCreateOrUpdate**
> ConnectionMonitorResult connectionMonitorsCreateOrUpdate(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, parameters)



Create or update a connection monitor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionMonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionMonitorsApi apiInstance = new ConnectionMonitorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
    String connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ConnectionMonitor parameters = new ConnectionMonitor(); // ConnectionMonitor | Parameters that define the operation to create a connection monitor.
    try {
      ConnectionMonitorResult result = apiInstance.connectionMonitorsCreateOrUpdate(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionMonitorsApi#connectionMonitorsCreateOrUpdate");
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
| **connectionMonitorName** | **String**| The name of the connection monitor. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ConnectionMonitor**](ConnectionMonitor.md)| Parameters that define the operation to create a connection monitor. | |

### Return type

[**ConnectionMonitorResult**](ConnectionMonitorResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting network watcher resource. |  -  |
| **201** | Create successful. The operation returns the resulting network watcher resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="connectionMonitorsDelete"></a>
# **connectionMonitorsDelete**
> connectionMonitorsDelete(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Deletes the specified connection monitor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionMonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionMonitorsApi apiInstance = new ConnectionMonitorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
    String connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.connectionMonitorsDelete(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionMonitorsApi#connectionMonitorsDelete");
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
| **connectionMonitorName** | **String**| The name of the connection monitor. | |
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
| **202** | Accepted. The operation will complete asynchronously. |  -  |
| **204** | Delete successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="connectionMonitorsGet"></a>
# **connectionMonitorsGet**
> ConnectionMonitorResult connectionMonitorsGet(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Gets a connection monitor by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionMonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionMonitorsApi apiInstance = new ConnectionMonitorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
    String connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ConnectionMonitorResult result = apiInstance.connectionMonitorsGet(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionMonitorsApi#connectionMonitorsGet");
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
| **connectionMonitorName** | **String**| The name of the connection monitor. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ConnectionMonitorResult**](ConnectionMonitorResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a connection monitor. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="connectionMonitorsList"></a>
# **connectionMonitorsList**
> ConnectionMonitorListResult connectionMonitorsList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId)



Lists all connection monitors for the specified Network Watcher.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionMonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionMonitorsApi apiInstance = new ConnectionMonitorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ConnectionMonitorListResult result = apiInstance.connectionMonitorsList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionMonitorsApi#connectionMonitorsList");
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

[**ConnectionMonitorListResult**](ConnectionMonitorListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful connection monitor enumeration request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="connectionMonitorsQuery"></a>
# **connectionMonitorsQuery**
> ConnectionMonitorQueryResult connectionMonitorsQuery(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Query a snapshot of the most recent connection states.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionMonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionMonitorsApi apiInstance = new ConnectionMonitorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
    String connectionMonitorName = "connectionMonitorName_example"; // String | The name given to the connection monitor.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ConnectionMonitorQueryResult result = apiInstance.connectionMonitorsQuery(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionMonitorsApi#connectionMonitorsQuery");
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
| **connectionMonitorName** | **String**| The name given to the connection monitor. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ConnectionMonitorQueryResult**](ConnectionMonitorQueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful query of connection states. |  -  |
| **202** | Accepted query of connection states. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="connectionMonitorsStart"></a>
# **connectionMonitorsStart**
> connectionMonitorsStart(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Starts the specified connection monitor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionMonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionMonitorsApi apiInstance = new ConnectionMonitorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
    String connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.connectionMonitorsStart(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionMonitorsApi#connectionMonitorsStart");
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
| **connectionMonitorName** | **String**| The name of the connection monitor. | |
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
| **200** | Request successful. The operation starts the connection monitor. |  -  |
| **202** | Accepted. The operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="connectionMonitorsStop"></a>
# **connectionMonitorsStop**
> connectionMonitorsStop(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Stops the specified connection monitor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionMonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionMonitorsApi apiInstance = new ConnectionMonitorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
    String connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.connectionMonitorsStop(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionMonitorsApi#connectionMonitorsStop");
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
| **connectionMonitorName** | **String**| The name of the connection monitor. | |
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
| **200** | Request successful. The operation stops the connection monitor. |  -  |
| **202** | Accepted. The operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="connectionMonitorsUpdateTags"></a>
# **connectionMonitorsUpdateTags**
> ConnectionMonitorResult connectionMonitorsUpdateTags(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, parameters)



Update tags of the specified connection monitor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionMonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionMonitorsApi apiInstance = new ConnectionMonitorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ConnectionMonitorsUpdateTagsRequest parameters = new ConnectionMonitorsUpdateTagsRequest(); // ConnectionMonitorsUpdateTagsRequest | Parameters supplied to update connection monitor tags.
    try {
      ConnectionMonitorResult result = apiInstance.connectionMonitorsUpdateTags(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionMonitorsApi#connectionMonitorsUpdateTags");
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
| **connectionMonitorName** | **String**| The name of the connection monitor. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ConnectionMonitorsUpdateTagsRequest**](ConnectionMonitorsUpdateTagsRequest.md)| Parameters supplied to update connection monitor tags. | |

### Return type

[**ConnectionMonitorResult**](ConnectionMonitorResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns updated connection monitor. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

