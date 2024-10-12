# TrafficAnalyticsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkWatchersGetFlowLogStatus_0**](TrafficAnalyticsApi.md#networkWatchersGetFlowLogStatus_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/queryFlowLogStatus |  |
| [**networkWatchersSetFlowLogConfiguration_0**](TrafficAnalyticsApi.md#networkWatchersSetFlowLogConfiguration_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/configureFlowLog |  |


<a id="networkWatchersGetFlowLogStatus_0"></a>
# **networkWatchersGetFlowLogStatus_0**
> FlowLogInformation networkWatchersGetFlowLogStatus_0(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Queries status of flow log and traffic analytics (optional) on a specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TrafficAnalyticsApi apiInstance = new TrafficAnalyticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    FlowLogStatusParameters parameters = new FlowLogStatusParameters(); // FlowLogStatusParameters | Parameters that define a resource to query flow log and traffic analytics (optional)  status.
    try {
      FlowLogInformation result = apiInstance.networkWatchersGetFlowLogStatus_0(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficAnalyticsApi#networkWatchersGetFlowLogStatus_0");
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
| **parameters** | [**FlowLogStatusParameters**](FlowLogStatusParameters.md)| Parameters that define a resource to query flow log and traffic analytics (optional)  status. | |

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

<a id="networkWatchersSetFlowLogConfiguration_0"></a>
# **networkWatchersSetFlowLogConfiguration_0**
> FlowLogInformation networkWatchersSetFlowLogConfiguration_0(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Configures flow log and traffic analytics (optional) on a specified resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TrafficAnalyticsApi apiInstance = new TrafficAnalyticsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
    String networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    FlowLogInformation parameters = new FlowLogInformation(); // FlowLogInformation | Parameters that define the configuration of flow log.
    try {
      FlowLogInformation result = apiInstance.networkWatchersSetFlowLogConfiguration_0(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficAnalyticsApi#networkWatchersSetFlowLogConfiguration_0");
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
| **200** | Successful request for setting flow log  and traffic analytics (optional) configuration. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

