# ExpressRouteConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRouteConnectionsCreateOrUpdate**](ExpressRouteConnectionsApi.md#expressRouteConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName} |  |
| [**expressRouteConnectionsDelete**](ExpressRouteConnectionsApi.md#expressRouteConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName} |  |
| [**expressRouteConnectionsGet**](ExpressRouteConnectionsApi.md#expressRouteConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName} |  |
| [**expressRouteConnectionsList**](ExpressRouteConnectionsApi.md#expressRouteConnectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections |  |


<a id="expressRouteConnectionsCreateOrUpdate"></a>
# **expressRouteConnectionsCreateOrUpdate**
> ExpressRouteConnection expressRouteConnectionsCreateOrUpdate(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId, putExpressRouteConnectionParameters)



Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteConnectionsApi apiInstance = new ExpressRouteConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRouteGatewayName = "expressRouteGatewayName_example"; // String | The name of the ExpressRoute gateway.
    String connectionName = "connectionName_example"; // String | The name of the connection subresource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ExpressRouteConnection putExpressRouteConnectionParameters = new ExpressRouteConnection(); // ExpressRouteConnection | Parameters required in an ExpressRouteConnection PUT operation.
    try {
      ExpressRouteConnection result = apiInstance.expressRouteConnectionsCreateOrUpdate(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId, putExpressRouteConnectionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteConnectionsApi#expressRouteConnectionsCreateOrUpdate");
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
| **expressRouteGatewayName** | **String**| The name of the ExpressRoute gateway. | |
| **connectionName** | **String**| The name of the connection subresource. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **putExpressRouteConnectionParameters** | [**ExpressRouteConnection**](ExpressRouteConnection.md)| Parameters required in an ExpressRouteConnection PUT operation. | |

### Return type

[**ExpressRouteConnection**](ExpressRouteConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the ExpressRouteConnection. |  -  |
| **201** | Create successful. The operation returns the ExpressRouteConnection. |  -  |

<a id="expressRouteConnectionsDelete"></a>
# **expressRouteConnectionsDelete**
> expressRouteConnectionsDelete(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId)



Deletes a connection to a ExpressRoute circuit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteConnectionsApi apiInstance = new ExpressRouteConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRouteGatewayName = "expressRouteGatewayName_example"; // String | The name of the ExpressRoute gateway.
    String connectionName = "connectionName_example"; // String | The name of the connection subresource.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.expressRouteConnectionsDelete(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteConnectionsApi#expressRouteConnectionsDelete");
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
| **expressRouteGatewayName** | **String**| The name of the ExpressRoute gateway. | |
| **connectionName** | **String**| The name of the connection subresource. | |
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
| **202** | Accepted, and the operation will continue asynchronously. |  -  |
| **204** | Delete successful. |  -  |

<a id="expressRouteConnectionsGet"></a>
# **expressRouteConnectionsGet**
> ExpressRouteConnection expressRouteConnectionsGet(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId)



Gets the specified ExpressRouteConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteConnectionsApi apiInstance = new ExpressRouteConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRouteGatewayName = "expressRouteGatewayName_example"; // String | The name of the ExpressRoute gateway.
    String connectionName = "connectionName_example"; // String | The name of the ExpressRoute connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteConnection result = apiInstance.expressRouteConnectionsGet(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteConnectionsApi#expressRouteConnectionsGet");
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
| **expressRouteGatewayName** | **String**| The name of the ExpressRoute gateway. | |
| **connectionName** | **String**| The name of the ExpressRoute connection. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteConnection**](ExpressRouteConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the ExpressRouteConnection. |  -  |

<a id="expressRouteConnectionsList"></a>
# **expressRouteConnectionsList**
> ExpressRouteConnectionList expressRouteConnectionsList(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId)



Lists ExpressRouteConnections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteConnectionsApi apiInstance = new ExpressRouteConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRouteGatewayName = "expressRouteGatewayName_example"; // String | The name of the ExpressRoute gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteConnectionList result = apiInstance.expressRouteConnectionsList(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteConnectionsApi#expressRouteConnectionsList");
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
| **expressRouteGatewayName** | **String**| The name of the ExpressRoute gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteConnectionList**](ExpressRouteConnectionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. |  -  |

