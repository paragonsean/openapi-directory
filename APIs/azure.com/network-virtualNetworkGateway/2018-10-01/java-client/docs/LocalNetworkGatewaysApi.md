# LocalNetworkGatewaysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**localNetworkGatewaysCreateOrUpdate**](LocalNetworkGatewaysApi.md#localNetworkGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} |  |
| [**localNetworkGatewaysDelete**](LocalNetworkGatewaysApi.md#localNetworkGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} |  |
| [**localNetworkGatewaysGet**](LocalNetworkGatewaysApi.md#localNetworkGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} |  |
| [**localNetworkGatewaysList**](LocalNetworkGatewaysApi.md#localNetworkGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways |  |
| [**localNetworkGatewaysUpdateTags**](LocalNetworkGatewaysApi.md#localNetworkGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} |  |


<a id="localNetworkGatewaysCreateOrUpdate"></a>
# **localNetworkGatewaysCreateOrUpdate**
> LocalNetworkGateway localNetworkGatewaysCreateOrUpdate(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters)



Creates or updates a local network gateway in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocalNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocalNetworkGatewaysApi apiInstance = new LocalNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    LocalNetworkGateway parameters = new LocalNetworkGateway(); // LocalNetworkGateway | Parameters supplied to the create or update local network gateway operation.
    try {
      LocalNetworkGateway result = apiInstance.localNetworkGatewaysCreateOrUpdate(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocalNetworkGatewaysApi#localNetworkGatewaysCreateOrUpdate");
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
| **localNetworkGatewayName** | **String**| The name of the local network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**LocalNetworkGateway**](LocalNetworkGateway.md)| Parameters supplied to the create or update local network gateway operation. | |

### Return type

[**LocalNetworkGateway**](LocalNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting LocalNetworkGateway resource. |  -  |
| **201** | Create successful. The operation returns the resulting LocalNetworkGateway resource. |  -  |

<a id="localNetworkGatewaysDelete"></a>
# **localNetworkGatewaysDelete**
> localNetworkGatewaysDelete(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId)



Deletes the specified local network gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocalNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocalNetworkGatewaysApi apiInstance = new LocalNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.localNetworkGatewaysDelete(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocalNetworkGatewaysApi#localNetworkGatewaysDelete");
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
| **localNetworkGatewayName** | **String**| The name of the local network gateway. | |
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

<a id="localNetworkGatewaysGet"></a>
# **localNetworkGatewaysGet**
> LocalNetworkGateway localNetworkGatewaysGet(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId)



Gets the specified local network gateway in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocalNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocalNetworkGatewaysApi apiInstance = new LocalNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      LocalNetworkGateway result = apiInstance.localNetworkGatewaysGet(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocalNetworkGatewaysApi#localNetworkGatewaysGet");
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
| **localNetworkGatewayName** | **String**| The name of the local network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**LocalNetworkGateway**](LocalNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting LocalNetworkGateway resource. |  -  |

<a id="localNetworkGatewaysList"></a>
# **localNetworkGatewaysList**
> LocalNetworkGatewayListResult localNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId)



Gets all the local network gateways in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocalNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocalNetworkGatewaysApi apiInstance = new LocalNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      LocalNetworkGatewayListResult result = apiInstance.localNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocalNetworkGatewaysApi#localNetworkGatewaysList");
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

[**LocalNetworkGatewayListResult**](LocalNetworkGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of LocalNetworkGateway resources. |  -  |

<a id="localNetworkGatewaysUpdateTags"></a>
# **localNetworkGatewaysUpdateTags**
> LocalNetworkGateway localNetworkGatewaysUpdateTags(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters)



Updates a local network gateway tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocalNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocalNetworkGatewaysApi apiInstance = new LocalNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualNetworkGatewayConnectionsUpdateTagsRequest parameters = new VirtualNetworkGatewayConnectionsUpdateTagsRequest(); // VirtualNetworkGatewayConnectionsUpdateTagsRequest | Parameters supplied to update local network gateway tags.
    try {
      LocalNetworkGateway result = apiInstance.localNetworkGatewaysUpdateTags(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocalNetworkGatewaysApi#localNetworkGatewaysUpdateTags");
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
| **localNetworkGatewayName** | **String**| The name of the local network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VirtualNetworkGatewayConnectionsUpdateTagsRequest**](VirtualNetworkGatewayConnectionsUpdateTagsRequest.md)| Parameters supplied to update local network gateway tags. | |

### Return type

[**LocalNetworkGateway**](LocalNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting LocalNetworkGateway resource. |  -  |

