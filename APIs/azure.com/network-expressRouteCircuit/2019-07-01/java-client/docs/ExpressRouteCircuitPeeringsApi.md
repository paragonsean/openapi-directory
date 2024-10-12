# ExpressRouteCircuitPeeringsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRouteCircuitPeeringsCreateOrUpdate**](ExpressRouteCircuitPeeringsApi.md#expressRouteCircuitPeeringsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName} |  |
| [**expressRouteCircuitPeeringsDelete**](ExpressRouteCircuitPeeringsApi.md#expressRouteCircuitPeeringsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName} |  |
| [**expressRouteCircuitPeeringsGet**](ExpressRouteCircuitPeeringsApi.md#expressRouteCircuitPeeringsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName} |  |
| [**expressRouteCircuitPeeringsList**](ExpressRouteCircuitPeeringsApi.md#expressRouteCircuitPeeringsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings |  |


<a id="expressRouteCircuitPeeringsCreateOrUpdate"></a>
# **expressRouteCircuitPeeringsCreateOrUpdate**
> ExpressRouteCircuitPeering expressRouteCircuitPeeringsCreateOrUpdate(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId, peeringParameters)



Creates or updates a peering in the specified express route circuits.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitPeeringsApi apiInstance = new ExpressRouteCircuitPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ExpressRouteCircuitPeering peeringParameters = new ExpressRouteCircuitPeering(); // ExpressRouteCircuitPeering | Parameters supplied to the create or update express route circuit peering operation.
    try {
      ExpressRouteCircuitPeering result = apiInstance.expressRouteCircuitPeeringsCreateOrUpdate(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId, peeringParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitPeeringsApi#expressRouteCircuitPeeringsCreateOrUpdate");
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
| **peeringParameters** | [**ExpressRouteCircuitPeering**](ExpressRouteCircuitPeering.md)| Parameters supplied to the create or update express route circuit peering operation. | |

### Return type

[**ExpressRouteCircuitPeering**](ExpressRouteCircuitPeering.md)

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

<a id="expressRouteCircuitPeeringsDelete"></a>
# **expressRouteCircuitPeeringsDelete**
> expressRouteCircuitPeeringsDelete(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId)



Deletes the specified peering from the specified express route circuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitPeeringsApi apiInstance = new ExpressRouteCircuitPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.expressRouteCircuitPeeringsDelete(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitPeeringsApi#expressRouteCircuitPeeringsDelete");
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

<a id="expressRouteCircuitPeeringsGet"></a>
# **expressRouteCircuitPeeringsGet**
> ExpressRouteCircuitPeering expressRouteCircuitPeeringsGet(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId)



Gets the specified peering for the express route circuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitPeeringsApi apiInstance = new ExpressRouteCircuitPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCircuitPeering result = apiInstance.expressRouteCircuitPeeringsGet(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitPeeringsApi#expressRouteCircuitPeeringsGet");
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

[**ExpressRouteCircuitPeering**](ExpressRouteCircuitPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting ExpressRouteCircuitPeering resource. |  -  |

<a id="expressRouteCircuitPeeringsList"></a>
# **expressRouteCircuitPeeringsList**
> ExpressRouteCircuitPeeringListResult expressRouteCircuitPeeringsList(resourceGroupName, circuitName, apiVersion, subscriptionId)



Gets all peerings in a specified express route circuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCircuitPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCircuitPeeringsApi apiInstance = new ExpressRouteCircuitPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String circuitName = "circuitName_example"; // String | The name of the express route circuit.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCircuitPeeringListResult result = apiInstance.expressRouteCircuitPeeringsList(resourceGroupName, circuitName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCircuitPeeringsApi#expressRouteCircuitPeeringsList");
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

[**ExpressRouteCircuitPeeringListResult**](ExpressRouteCircuitPeeringListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ExpressRouteCircuitPeering resources. |  -  |

