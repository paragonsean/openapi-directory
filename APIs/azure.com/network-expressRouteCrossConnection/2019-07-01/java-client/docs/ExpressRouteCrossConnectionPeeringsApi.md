# ExpressRouteCrossConnectionPeeringsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRouteCrossConnectionPeeringsCreateOrUpdate**](ExpressRouteCrossConnectionPeeringsApi.md#expressRouteCrossConnectionPeeringsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName} |  |
| [**expressRouteCrossConnectionPeeringsDelete**](ExpressRouteCrossConnectionPeeringsApi.md#expressRouteCrossConnectionPeeringsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName} |  |
| [**expressRouteCrossConnectionPeeringsGet**](ExpressRouteCrossConnectionPeeringsApi.md#expressRouteCrossConnectionPeeringsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName} |  |
| [**expressRouteCrossConnectionPeeringsList**](ExpressRouteCrossConnectionPeeringsApi.md#expressRouteCrossConnectionPeeringsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings |  |


<a id="expressRouteCrossConnectionPeeringsCreateOrUpdate"></a>
# **expressRouteCrossConnectionPeeringsCreateOrUpdate**
> ExpressRouteCrossConnectionPeering expressRouteCrossConnectionPeeringsCreateOrUpdate(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId, peeringParameters)



Creates or updates a peering in the specified ExpressRouteCrossConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCrossConnectionPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCrossConnectionPeeringsApi apiInstance = new ExpressRouteCrossConnectionPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ExpressRouteCrossConnectionPeering peeringParameters = new ExpressRouteCrossConnectionPeering(); // ExpressRouteCrossConnectionPeering | Parameters supplied to the create or update ExpressRouteCrossConnection peering operation.
    try {
      ExpressRouteCrossConnectionPeering result = apiInstance.expressRouteCrossConnectionPeeringsCreateOrUpdate(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId, peeringParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCrossConnectionPeeringsApi#expressRouteCrossConnectionPeeringsCreateOrUpdate");
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
| **crossConnectionName** | **String**| The name of the ExpressRouteCrossConnection. | |
| **peeringName** | **String**| The name of the peering. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **peeringParameters** | [**ExpressRouteCrossConnectionPeering**](ExpressRouteCrossConnectionPeering.md)| Parameters supplied to the create or update ExpressRouteCrossConnection peering operation. | |

### Return type

[**ExpressRouteCrossConnectionPeering**](ExpressRouteCrossConnectionPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ExpressRouteCrossConnectionPeering resource. |  -  |
| **201** | Create successful. The operation returns the resulting ExpressRouteCrossConnectionPeering resource. |  -  |

<a id="expressRouteCrossConnectionPeeringsDelete"></a>
# **expressRouteCrossConnectionPeeringsDelete**
> expressRouteCrossConnectionPeeringsDelete(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId)



Deletes the specified peering from the ExpressRouteCrossConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCrossConnectionPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCrossConnectionPeeringsApi apiInstance = new ExpressRouteCrossConnectionPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.expressRouteCrossConnectionPeeringsDelete(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCrossConnectionPeeringsApi#expressRouteCrossConnectionPeeringsDelete");
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
| **crossConnectionName** | **String**| The name of the ExpressRouteCrossConnection. | |
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

<a id="expressRouteCrossConnectionPeeringsGet"></a>
# **expressRouteCrossConnectionPeeringsGet**
> ExpressRouteCrossConnectionPeering expressRouteCrossConnectionPeeringsGet(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId)



Gets the specified peering for the ExpressRouteCrossConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCrossConnectionPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCrossConnectionPeeringsApi apiInstance = new ExpressRouteCrossConnectionPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCrossConnectionPeering result = apiInstance.expressRouteCrossConnectionPeeringsGet(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCrossConnectionPeeringsApi#expressRouteCrossConnectionPeeringsGet");
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
| **crossConnectionName** | **String**| The name of the ExpressRouteCrossConnection. | |
| **peeringName** | **String**| The name of the peering. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteCrossConnectionPeering**](ExpressRouteCrossConnectionPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting ExpressRouteCrossConnectionPeering resource. |  -  |

<a id="expressRouteCrossConnectionPeeringsList"></a>
# **expressRouteCrossConnectionPeeringsList**
> ExpressRouteCrossConnectionPeeringList expressRouteCrossConnectionPeeringsList(resourceGroupName, crossConnectionName, apiVersion, subscriptionId)



Gets all peerings in a specified ExpressRouteCrossConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCrossConnectionPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCrossConnectionPeeringsApi apiInstance = new ExpressRouteCrossConnectionPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCrossConnectionPeeringList result = apiInstance.expressRouteCrossConnectionPeeringsList(resourceGroupName, crossConnectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCrossConnectionPeeringsApi#expressRouteCrossConnectionPeeringsList");
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
| **crossConnectionName** | **String**| The name of the ExpressRouteCrossConnection. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteCrossConnectionPeeringList**](ExpressRouteCrossConnectionPeeringList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ExpressRouteCrossConnectionPeering resources. |  -  |

