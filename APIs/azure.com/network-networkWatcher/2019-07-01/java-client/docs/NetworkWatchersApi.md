# NetworkWatchersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkWatchersCheckConnectivity**](NetworkWatchersApi.md#networkWatchersCheckConnectivity) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectivityCheck |  |
| [**networkWatchersCreateOrUpdate**](NetworkWatchersApi.md#networkWatchersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName} |  |
| [**networkWatchersDelete**](NetworkWatchersApi.md#networkWatchersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName} |  |
| [**networkWatchersGet**](NetworkWatchersApi.md#networkWatchersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName} |  |
| [**networkWatchersGetAzureReachabilityReport**](NetworkWatchersApi.md#networkWatchersGetAzureReachabilityReport) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/azureReachabilityReport |  |
| [**networkWatchersGetFlowLogStatus**](NetworkWatchersApi.md#networkWatchersGetFlowLogStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/queryFlowLogStatus |  |
| [**networkWatchersGetNetworkConfigurationDiagnostic**](NetworkWatchersApi.md#networkWatchersGetNetworkConfigurationDiagnostic) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/networkConfigurationDiagnostic |  |
| [**networkWatchersGetNextHop**](NetworkWatchersApi.md#networkWatchersGetNextHop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/nextHop |  |
| [**networkWatchersGetTopology**](NetworkWatchersApi.md#networkWatchersGetTopology) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/topology |  |
| [**networkWatchersGetTroubleshooting**](NetworkWatchersApi.md#networkWatchersGetTroubleshooting) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/troubleshoot |  |
| [**networkWatchersGetTroubleshootingResult**](NetworkWatchersApi.md#networkWatchersGetTroubleshootingResult) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/queryTroubleshootResult |  |
| [**networkWatchersGetVMSecurityRules**](NetworkWatchersApi.md#networkWatchersGetVMSecurityRules) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/securityGroupView |  |
| [**networkWatchersList**](NetworkWatchersApi.md#networkWatchersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers |  |
| [**networkWatchersListAll**](NetworkWatchersApi.md#networkWatchersListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/networkWatchers |  |
| [**networkWatchersListAvailableProviders**](NetworkWatchersApi.md#networkWatchersListAvailableProviders) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/availableProvidersList |  |
| [**networkWatchersSetFlowLogConfiguration**](NetworkWatchersApi.md#networkWatchersSetFlowLogConfiguration) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/configureFlowLog |  |
| [**networkWatchersUpdateTags**](NetworkWatchersApi.md#networkWatchersUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName} |  |
| [**networkWatchersVerifyIPFlow**](NetworkWatchersApi.md#networkWatchersVerifyIPFlow) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/ipFlowVerify |  |


<a id="networkWatchersCheckConnectivity"></a>
# **networkWatchersCheckConnectivity**
> ConnectivityInformation networkWatchersCheckConnectivity(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Verifies the possibility of establishing a direct TCP connection from a virtual machine to a given endpoint including another VM or an arbitrary remote server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ConnectivityParameters parameters = new ConnectivityParameters(); // ConnectivityParameters | Parameters that determine how the connectivity check will be performed.
    try {
      ConnectivityInformation result = apiInstance.networkWatchersCheckConnectivity(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersCheckConnectivity");
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
| **resourceGroupName** | **String**| The name of the network watcher resource group. | |
| **networkWatcherName** | **String**| The name of the network watcher resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ConnectivityParameters**](ConnectivityParameters.md)| Parameters that determine how the connectivity check will be performed. | |

### Return type

[**ConnectivityInformation**](ConnectivityInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for checking connectivity. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersCreateOrUpdate"></a>
# **networkWatchersCreateOrUpdate**
> NetworkWatcher networkWatchersCreateOrUpdate(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Creates or updates a network watcher in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    NetworkWatcher parameters = new NetworkWatcher(); // NetworkWatcher | Parameters that define the network watcher resource.
    try {
      NetworkWatcher result = apiInstance.networkWatchersCreateOrUpdate(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersCreateOrUpdate");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**NetworkWatcher**](NetworkWatcher.md)| Parameters that define the network watcher resource. | |

### Return type

[**NetworkWatcher**](NetworkWatcher.md)

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

<a id="networkWatchersDelete"></a>
# **networkWatchersDelete**
> networkWatchersDelete(resourceGroupName, networkWatcherName, apiVersion, subscriptionId)



Deletes the specified network watcher resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.networkWatchersDelete(resourceGroupName, networkWatcherName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersDelete");
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

<a id="networkWatchersGet"></a>
# **networkWatchersGet**
> NetworkWatcher networkWatchersGet(resourceGroupName, networkWatcherName, apiVersion, subscriptionId)



Gets the specified network watcher by resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      NetworkWatcher result = apiInstance.networkWatchersGet(resourceGroupName, networkWatcherName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersGet");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**NetworkWatcher**](NetworkWatcher.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a network watcher resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersGetAzureReachabilityReport"></a>
# **networkWatchersGetAzureReachabilityReport**
> AzureReachabilityReport networkWatchersGetAzureReachabilityReport(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Gets the relative latency score for internet service providers from a specified location to Azure regions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    AzureReachabilityReportParameters parameters = new AzureReachabilityReportParameters(); // AzureReachabilityReportParameters | Parameters that determine Azure reachability report configuration.
    try {
      AzureReachabilityReport result = apiInstance.networkWatchersGetAzureReachabilityReport(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersGetAzureReachabilityReport");
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
| **resourceGroupName** | **String**| The name of the network watcher resource group. | |
| **networkWatcherName** | **String**| The name of the network watcher resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**AzureReachabilityReportParameters**](AzureReachabilityReportParameters.md)| Parameters that determine Azure reachability report configuration. | |

### Return type

[**AzureReachabilityReport**](AzureReachabilityReport.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for Azure reachability report. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersGetFlowLogStatus"></a>
# **networkWatchersGetFlowLogStatus**
> FlowLogInformation networkWatchersGetFlowLogStatus(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Queries status of flow log and traffic analytics (optional) on a specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    FlowLogStatusParameters parameters = new FlowLogStatusParameters(); // FlowLogStatusParameters | Parameters that define a resource to query flow log and traffic analytics (optional) status.
    try {
      FlowLogInformation result = apiInstance.networkWatchersGetFlowLogStatus(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersGetFlowLogStatus");
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
| **resourceGroupName** | **String**| The name of the network watcher resource group. | |
| **networkWatcherName** | **String**| The name of the network watcher resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**FlowLogStatusParameters**](FlowLogStatusParameters.md)| Parameters that define a resource to query flow log and traffic analytics (optional) status. | |

### Return type

[**FlowLogInformation**](FlowLogInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for query flow log and traffic analytics (optional) status. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersGetNetworkConfigurationDiagnostic"></a>
# **networkWatchersGetNetworkConfigurationDiagnostic**
> NetworkConfigurationDiagnosticResponse networkWatchersGetNetworkConfigurationDiagnostic(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Gets Network Configuration Diagnostic data to help customers understand and debug network behavior. It provides detailed information on what security rules were applied to a specified traffic flow and the result of evaluating these rules. Customers must provide details of a flow like source, destination, protocol, etc. The API returns whether traffic was allowed or denied, the rules evaluated for the specified flow and the evaluation results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    NetworkConfigurationDiagnosticParameters parameters = new NetworkConfigurationDiagnosticParameters(); // NetworkConfigurationDiagnosticParameters | Parameters to get network configuration diagnostic.
    try {
      NetworkConfigurationDiagnosticResponse result = apiInstance.networkWatchersGetNetworkConfigurationDiagnostic(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersGetNetworkConfigurationDiagnostic");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**NetworkConfigurationDiagnosticParameters**](NetworkConfigurationDiagnosticParameters.md)| Parameters to get network configuration diagnostic. | |

### Return type

[**NetworkConfigurationDiagnosticResponse**](NetworkConfigurationDiagnosticResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the result of network configuration diagnostic. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersGetNextHop"></a>
# **networkWatchersGetNextHop**
> NextHopResult networkWatchersGetNextHop(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Gets the next hop from the specified VM.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    NextHopParameters parameters = new NextHopParameters(); // NextHopParameters | Parameters that define the source and destination endpoint.
    try {
      NextHopResult result = apiInstance.networkWatchersGetNextHop(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersGetNextHop");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**NextHopParameters**](NextHopParameters.md)| Parameters that define the source and destination endpoint. | |

### Return type

[**NextHopResult**](NextHopResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the next hop from the VM. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersGetTopology"></a>
# **networkWatchersGetTopology**
> Topology networkWatchersGetTopology(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Gets the current network topology by resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    TopologyParameters parameters = new TopologyParameters(); // TopologyParameters | Parameters that define the representation of topology.
    try {
      Topology result = apiInstance.networkWatchersGetTopology(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersGetTopology");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**TopologyParameters**](TopologyParameters.md)| Parameters that define the representation of topology. | |

### Return type

[**Topology**](Topology.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the topology of resource group. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersGetTroubleshooting"></a>
# **networkWatchersGetTroubleshooting**
> TroubleshootingResult networkWatchersGetTroubleshooting(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Initiate troubleshooting on a specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    TroubleshootingParameters parameters = new TroubleshootingParameters(); // TroubleshootingParameters | Parameters that define the resource to troubleshoot.
    try {
      TroubleshootingResult result = apiInstance.networkWatchersGetTroubleshooting(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersGetTroubleshooting");
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
| **networkWatcherName** | **String**| The name of the network watcher resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**TroubleshootingParameters**](TroubleshootingParameters.md)| Parameters that define the resource to troubleshoot. | |

### Return type

[**TroubleshootingResult**](TroubleshootingResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful troubleshooting request. |  -  |
| **202** | Accepted get troubleshooting request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersGetTroubleshootingResult"></a>
# **networkWatchersGetTroubleshootingResult**
> TroubleshootingResult networkWatchersGetTroubleshootingResult(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Get the last completed troubleshooting result on a specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    QueryTroubleshootingParameters parameters = new QueryTroubleshootingParameters(); // QueryTroubleshootingParameters | Parameters that define the resource to query the troubleshooting result.
    try {
      TroubleshootingResult result = apiInstance.networkWatchersGetTroubleshootingResult(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersGetTroubleshootingResult");
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
| **networkWatcherName** | **String**| The name of the network watcher resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**QueryTroubleshootingParameters**](QueryTroubleshootingParameters.md)| Parameters that define the resource to query the troubleshooting result. | |

### Return type

[**TroubleshootingResult**](TroubleshootingResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful get troubleshooting result request. |  -  |
| **202** | Accepted get troubleshooting result request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersGetVMSecurityRules"></a>
# **networkWatchersGetVMSecurityRules**
> SecurityGroupViewResult networkWatchersGetVMSecurityRules(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Gets the configured and effective security group rules on the specified VM.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SecurityGroupViewParameters parameters = new SecurityGroupViewParameters(); // SecurityGroupViewParameters | Parameters that define the VM to check security groups for.
    try {
      SecurityGroupViewResult result = apiInstance.networkWatchersGetVMSecurityRules(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersGetVMSecurityRules");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SecurityGroupViewParameters**](SecurityGroupViewParameters.md)| Parameters that define the VM to check security groups for. | |

### Return type

[**SecurityGroupViewResult**](SecurityGroupViewResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns security group rules on the VM. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersList"></a>
# **networkWatchersList**
> NetworkWatcherListResult networkWatchersList(resourceGroupName, apiVersion, subscriptionId)



Gets all network watchers by resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      NetworkWatcherListResult result = apiInstance.networkWatchersList(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersList");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**NetworkWatcherListResult**](NetworkWatcherListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of network watcher resources. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersListAll"></a>
# **networkWatchersListAll**
> NetworkWatcherListResult networkWatchersListAll(apiVersion, subscriptionId)



Gets all network watchers by subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      NetworkWatcherListResult result = apiInstance.networkWatchersListAll(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersListAll");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**NetworkWatcherListResult**](NetworkWatcherListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of network watcher resources. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersListAvailableProviders"></a>
# **networkWatchersListAvailableProviders**
> AvailableProvidersList networkWatchersListAvailableProviders(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Lists all available internet service providers for a specified Azure region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    AvailableProvidersListParameters parameters = new AvailableProvidersListParameters(); // AvailableProvidersListParameters | Parameters that scope the list of available providers.
    try {
      AvailableProvidersList result = apiInstance.networkWatchersListAvailableProviders(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersListAvailableProviders");
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
| **resourceGroupName** | **String**| The name of the network watcher resource group. | |
| **networkWatcherName** | **String**| The name of the network watcher resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**AvailableProvidersListParameters**](AvailableProvidersListParameters.md)| Parameters that scope the list of available providers. | |

### Return type

[**AvailableProvidersList**](AvailableProvidersList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for list of available providers. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersSetFlowLogConfiguration"></a>
# **networkWatchersSetFlowLogConfiguration**
> FlowLogInformation networkWatchersSetFlowLogConfiguration(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Configures flow log and traffic analytics (optional) on a specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    FlowLogInformation parameters = new FlowLogInformation(); // FlowLogInformation | Parameters that define the configuration of flow log.
    try {
      FlowLogInformation result = apiInstance.networkWatchersSetFlowLogConfiguration(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersSetFlowLogConfiguration");
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
| **resourceGroupName** | **String**| The name of the network watcher resource group. | |
| **networkWatcherName** | **String**| The name of the network watcher resource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**FlowLogInformation**](FlowLogInformation.md)| Parameters that define the configuration of flow log. | |

### Return type

[**FlowLogInformation**](FlowLogInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for setting flow log and traffic analytics (optional) configuration. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersUpdateTags"></a>
# **networkWatchersUpdateTags**
> NetworkWatcher networkWatchersUpdateTags(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Updates a network watcher tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    NetworkWatchersUpdateTagsRequest parameters = new NetworkWatchersUpdateTagsRequest(); // NetworkWatchersUpdateTagsRequest | Parameters supplied to update network watcher tags.
    try {
      NetworkWatcher result = apiInstance.networkWatchersUpdateTags(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersUpdateTags");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**NetworkWatchersUpdateTagsRequest**](NetworkWatchersUpdateTagsRequest.md)| Parameters supplied to update network watcher tags. | |

### Return type

[**NetworkWatcher**](NetworkWatcher.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting network watcher resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="networkWatchersVerifyIPFlow"></a>
# **networkWatchersVerifyIPFlow**
> VerificationIPFlowResult networkWatchersVerifyIPFlow(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Verify IP flow from the specified VM to a location given the currently configured NSG rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkWatchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkWatchersApi apiInstance = new NetworkWatchersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VerificationIPFlowParameters parameters = new VerificationIPFlowParameters(); // VerificationIPFlowParameters | Parameters that define the IP flow to be verified.
    try {
      VerificationIPFlowResult result = apiInstance.networkWatchersVerifyIPFlow(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkWatchersApi#networkWatchersVerifyIPFlow");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VerificationIPFlowParameters**](VerificationIPFlowParameters.md)| Parameters that define the IP flow to be verified. | |

### Return type

[**VerificationIPFlowResult**](VerificationIPFlowResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the result of IP flow verification. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

