# ExpressRouteCircuitStatsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRouteCircuitsGetPeeringStats**](ExpressRouteCircuitStatsApi.md#expressRouteCircuitsGetPeeringStats) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/stats |  |
| [**expressRouteCircuitsGetStats**](ExpressRouteCircuitStatsApi.md#expressRouteCircuitsGetStats) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/stats |  |


<a id="expressRouteCircuitsGetPeeringStats"></a>
# **expressRouteCircuitsGetPeeringStats**
> ExpressRouteCircuitStats expressRouteCircuitsGetPeeringStats(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId)



Gets all stats from an express route circuit in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitStatsApi apiInstance = new ExpressRouteCircuitStatsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCircuitStats result = apiInstance.expressRouteCircuitsGetPeeringStats(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitStatsApi#expressRouteCircuitsGetPeeringStats");
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
| **circuitName** | **String**| The name of the express route circuit. | |
| **peeringName** | **String**| The name of the peering. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteCircuitStats**](ExpressRouteCircuitStats.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting ExpressRouteCircuitStats resource. |  -  |

<a id="expressRouteCircuitsGetStats"></a>
# **expressRouteCircuitsGetStats**
> ExpressRouteCircuitStats expressRouteCircuitsGetStats(resourceGroupName, circuitName, apiVersion, subscriptionId)



Gets all the stats from an express route circuit in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitStatsApi apiInstance = new ExpressRouteCircuitStatsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCircuitStats result = apiInstance.expressRouteCircuitsGetStats(resourceGroupName, circuitName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitStatsApi#expressRouteCircuitsGetStats");
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
| **circuitName** | **String**| The name of the express route circuit. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteCircuitStats**](ExpressRouteCircuitStats.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting ExpressRouteCircuitStats resource. |  -  |

