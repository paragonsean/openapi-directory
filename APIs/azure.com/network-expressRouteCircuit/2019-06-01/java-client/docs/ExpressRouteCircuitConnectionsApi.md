# ExpressRouteCircuitConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRouteCircuitConnectionsCreateOrUpdate**](ExpressRouteCircuitConnectionsApi.md#expressRouteCircuitConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections/{connectionName} |  |
| [**expressRouteCircuitConnectionsDelete**](ExpressRouteCircuitConnectionsApi.md#expressRouteCircuitConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections/{connectionName} |  |
| [**expressRouteCircuitConnectionsGet**](ExpressRouteCircuitConnectionsApi.md#expressRouteCircuitConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections/{connectionName} |  |
| [**expressRouteCircuitConnectionsList**](ExpressRouteCircuitConnectionsApi.md#expressRouteCircuitConnectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections |  |


<a id="expressRouteCircuitConnectionsCreateOrUpdate"></a>
# **expressRouteCircuitConnectionsCreateOrUpdate**
> ExpressRouteCircuitConnection expressRouteCircuitConnectionsCreateOrUpdate(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId, expressRouteCircuitConnectionParameters)



Creates or updates a Express Route Circuit Connection in the specified express route circuits.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitConnectionsApi apiInstance = new ExpressRouteCircuitConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String connectionName = "connectionName_example"; // String | The name of the express route circuit connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ExpressRouteCircuitConnection expressRouteCircuitConnectionParameters = new ExpressRouteCircuitConnection(); // ExpressRouteCircuitConnection | Parameters supplied to the create or update express route circuit connection operation.
    try {
      ExpressRouteCircuitConnection result = apiInstance.expressRouteCircuitConnectionsCreateOrUpdate(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId, expressRouteCircuitConnectionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitConnectionsApi#expressRouteCircuitConnectionsCreateOrUpdate");
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
| **connectionName** | **String**| The name of the express route circuit connection. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **expressRouteCircuitConnectionParameters** | [**ExpressRouteCircuitConnection**](ExpressRouteCircuitConnection.md)| Parameters supplied to the create or update express route circuit connection operation. | |

### Return type

[**ExpressRouteCircuitConnection**](ExpressRouteCircuitConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ExpressRouteCircuitPeering resource. |  -  |
| **201** | Create successful. The operation returns the resulting ExpressRouteCircuitPeering resource. |  -  |

<a id="expressRouteCircuitConnectionsDelete"></a>
# **expressRouteCircuitConnectionsDelete**
> expressRouteCircuitConnectionsDelete(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId)



Deletes the specified Express Route Circuit Connection from the specified express route circuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitConnectionsApi apiInstance = new ExpressRouteCircuitConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String connectionName = "connectionName_example"; // String | The name of the express route circuit connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.expressRouteCircuitConnectionsDelete(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitConnectionsApi#expressRouteCircuitConnectionsDelete");
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
| **connectionName** | **String**| The name of the express route circuit connection. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Delete successful. |  -  |

<a id="expressRouteCircuitConnectionsGet"></a>
# **expressRouteCircuitConnectionsGet**
> ExpressRouteCircuitConnection expressRouteCircuitConnectionsGet(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId)



Gets the specified Express Route Circuit Connection from the specified express route circuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitConnectionsApi apiInstance = new ExpressRouteCircuitConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String connectionName = "connectionName_example"; // String | The name of the express route circuit connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCircuitConnection result = apiInstance.expressRouteCircuitConnectionsGet(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitConnectionsApi#expressRouteCircuitConnectionsGet");
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
| **connectionName** | **String**| The name of the express route circuit connection. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteCircuitConnection**](ExpressRouteCircuitConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting Express Route Circuit Connection resource. |  -  |

<a id="expressRouteCircuitConnectionsList"></a>
# **expressRouteCircuitConnectionsList**
> ExpressRouteCircuitConnectionListResult expressRouteCircuitConnectionsList(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId)



Gets all global reach connections associated with a private peering in an express route circuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitConnectionsApi apiInstance = new ExpressRouteCircuitConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the circuit.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCircuitConnectionListResult result = apiInstance.expressRouteCircuitConnectionsList(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitConnectionsApi#expressRouteCircuitConnectionsList");
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
| **circuitName** | **String**| The name of the circuit. | |
| **peeringName** | **String**| The name of the peering. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteCircuitConnectionListResult**](ExpressRouteCircuitConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ExpressRouteCircuitConnections resources. |  -  |

