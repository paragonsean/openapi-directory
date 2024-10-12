# VirtualRouterPeeringsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualRouterPeeringsCreateOrUpdate**](VirtualRouterPeeringsApi.md#virtualRouterPeeringsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName}/peerings/{peeringName} |  |
| [**virtualRouterPeeringsDelete**](VirtualRouterPeeringsApi.md#virtualRouterPeeringsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName}/peerings/{peeringName} |  |
| [**virtualRouterPeeringsGet**](VirtualRouterPeeringsApi.md#virtualRouterPeeringsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName}/peerings/{peeringName} |  |
| [**virtualRouterPeeringsList**](VirtualRouterPeeringsApi.md#virtualRouterPeeringsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName}/peerings |  |
| [**virtualRouterPeeringsUpdate**](VirtualRouterPeeringsApi.md#virtualRouterPeeringsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName}/peerings/{peeringName} |  |


<a id="virtualRouterPeeringsCreateOrUpdate"></a>
# **virtualRouterPeeringsCreateOrUpdate**
> VirtualRouterPeering virtualRouterPeeringsCreateOrUpdate(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId, parameters)



Creates or updates the specified Virtual Router Peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualRouterPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualRouterPeeringsApi apiInstance = new VirtualRouterPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
    String peeringName = "peeringName_example"; // String | The name of the Virtual Router Peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualRouterPeering parameters = new VirtualRouterPeering(); // VirtualRouterPeering | Parameters supplied to the create or update Virtual Router Peering operation.
    try {
      VirtualRouterPeering result = apiInstance.virtualRouterPeeringsCreateOrUpdate(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualRouterPeeringsApi#virtualRouterPeeringsCreateOrUpdate");
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
| **virtualRouterName** | **String**| The name of the Virtual Router. | |
| **peeringName** | **String**| The name of the Virtual Router Peering. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VirtualRouterPeering**](VirtualRouterPeering.md)| Parameters supplied to the create or update Virtual Router Peering operation. | |

### Return type

[**VirtualRouterPeering**](VirtualRouterPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting Virtual Router Peering resource. |  -  |
| **201** | Request received successfully. The operation returns the resulting Virtual Router Peering resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualRouterPeeringsDelete"></a>
# **virtualRouterPeeringsDelete**
> virtualRouterPeeringsDelete(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId)



Deletes the specified peering from a Virtual Router.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualRouterPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualRouterPeeringsApi apiInstance = new VirtualRouterPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.virtualRouterPeeringsDelete(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualRouterPeeringsApi#virtualRouterPeeringsDelete");
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
| **virtualRouterName** | **String**| The name of the Virtual Router. | |
| **peeringName** | **String**| The name of the peering. | |
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
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Request successful. Resource with the specified name does not exist |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualRouterPeeringsGet"></a>
# **virtualRouterPeeringsGet**
> VirtualRouterPeering virtualRouterPeeringsGet(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId)



Gets the specified Virtual Router Peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualRouterPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualRouterPeeringsApi apiInstance = new VirtualRouterPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
    String peeringName = "peeringName_example"; // String | The name of the Virtual Router Peering.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualRouterPeering result = apiInstance.virtualRouterPeeringsGet(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualRouterPeeringsApi#virtualRouterPeeringsGet");
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
| **virtualRouterName** | **String**| The name of the Virtual Router. | |
| **peeringName** | **String**| The name of the Virtual Router Peering. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualRouterPeering**](VirtualRouterPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a Virtual Router Peering resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualRouterPeeringsList"></a>
# **virtualRouterPeeringsList**
> VirtualRouterPeeringListResult virtualRouterPeeringsList(resourceGroupName, virtualRouterName, apiVersion, subscriptionId)



Lists all Virtual Router Peerings in a Virtual Router resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualRouterPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualRouterPeeringsApi apiInstance = new VirtualRouterPeeringsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualRouterPeeringListResult result = apiInstance.virtualRouterPeeringsList(resourceGroupName, virtualRouterName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualRouterPeeringsApi#virtualRouterPeeringsList");
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
| **virtualRouterName** | **String**| The name of the Virtual Router. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualRouterPeeringListResult**](VirtualRouterPeeringListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of Virtual Router Peering resources. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualRouterPeeringsUpdate"></a>
# **virtualRouterPeeringsUpdate**
> VirtualRouterPeering virtualRouterPeeringsUpdate(subscriptionId, resourceGroupName, virtualRouterName, apiVersion, peeringName, parameters)



Updates a Virtual Router Peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualRouterPeeringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualRouterPeeringsApi apiInstance = new VirtualRouterPeeringsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the Virtual Router Peering.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String peeringName = "peeringName_example"; // String | The name of the Virtual Router Peering being updated.
    VirtualRouterPeering parameters = new VirtualRouterPeering(); // VirtualRouterPeering | Parameters supplied to update Virtual Router Peering operation.
    try {
      VirtualRouterPeering result = apiInstance.virtualRouterPeeringsUpdate(subscriptionId, resourceGroupName, virtualRouterName, apiVersion, peeringName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualRouterPeeringsApi#virtualRouterPeeringsUpdate");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group name of the Virtual Router Peering. | |
| **virtualRouterName** | **String**| The name of the Virtual Router. | |
| **apiVersion** | **String**| Client API version. | |
| **peeringName** | **String**| The name of the Virtual Router Peering being updated. | |
| **parameters** | [**VirtualRouterPeering**](VirtualRouterPeering.md)| Parameters supplied to update Virtual Router Peering operation. | |

### Return type

[**VirtualRouterPeering**](VirtualRouterPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the Virtual Router Peering updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

