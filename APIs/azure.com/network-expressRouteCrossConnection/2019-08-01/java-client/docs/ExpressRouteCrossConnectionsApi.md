# ExpressRouteCrossConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRouteCrossConnectionsCreateOrUpdate**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName} |  |
| [**expressRouteCrossConnectionsGet**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName} |  |
| [**expressRouteCrossConnectionsList**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/expressRouteCrossConnections |  |
| [**expressRouteCrossConnectionsListByResourceGroup**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections |  |
| [**expressRouteCrossConnectionsUpdateTags**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName} |  |


<a id="expressRouteCrossConnectionsCreateOrUpdate"></a>
# **expressRouteCrossConnectionsCreateOrUpdate**
> ExpressRouteCrossConnection expressRouteCrossConnectionsCreateOrUpdate(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, parameters)



Update the specified ExpressRouteCrossConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCrossConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCrossConnectionsApi apiInstance = new ExpressRouteCrossConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ExpressRouteCrossConnection parameters = new ExpressRouteCrossConnection(); // ExpressRouteCrossConnection | Parameters supplied to the update express route crossConnection operation.
    try {
      ExpressRouteCrossConnection result = apiInstance.expressRouteCrossConnectionsCreateOrUpdate(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCrossConnectionsApi#expressRouteCrossConnectionsCreateOrUpdate");
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
| **parameters** | [**ExpressRouteCrossConnection**](ExpressRouteCrossConnection.md)| Parameters supplied to the update express route crossConnection operation. | |

### Return type

[**ExpressRouteCrossConnection**](ExpressRouteCrossConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ExpressRouteCrossConnection resource. |  -  |

<a id="expressRouteCrossConnectionsGet"></a>
# **expressRouteCrossConnectionsGet**
> ExpressRouteCrossConnection expressRouteCrossConnectionsGet(resourceGroupName, crossConnectionName, apiVersion, subscriptionId)



Gets details about the specified ExpressRouteCrossConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCrossConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCrossConnectionsApi apiInstance = new ExpressRouteCrossConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group (peering location of the circuit).
    String crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection (service key of the circuit).
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCrossConnection result = apiInstance.expressRouteCrossConnectionsGet(resourceGroupName, crossConnectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCrossConnectionsApi#expressRouteCrossConnectionsGet");
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
| **resourceGroupName** | **String**| The name of the resource group (peering location of the circuit). | |
| **crossConnectionName** | **String**| The name of the ExpressRouteCrossConnection (service key of the circuit). | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ExpressRouteCrossConnection**](ExpressRouteCrossConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting ExpressRouteCrossConnection resource. |  -  |

<a id="expressRouteCrossConnectionsList"></a>
# **expressRouteCrossConnectionsList**
> ExpressRouteCrossConnectionListResult expressRouteCrossConnectionsList(apiVersion, subscriptionId)



Retrieves all the ExpressRouteCrossConnections in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCrossConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCrossConnectionsApi apiInstance = new ExpressRouteCrossConnectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCrossConnectionListResult result = apiInstance.expressRouteCrossConnectionsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCrossConnectionsApi#expressRouteCrossConnectionsList");
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

[**ExpressRouteCrossConnectionListResult**](ExpressRouteCrossConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ExpressRouteCrossConnection resources. If there are no cross connection resources an empty list is returned. |  -  |

<a id="expressRouteCrossConnectionsListByResourceGroup"></a>
# **expressRouteCrossConnectionsListByResourceGroup**
> ExpressRouteCrossConnectionListResult expressRouteCrossConnectionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Retrieves all the ExpressRouteCrossConnections in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCrossConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCrossConnectionsApi apiInstance = new ExpressRouteCrossConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ExpressRouteCrossConnectionListResult result = apiInstance.expressRouteCrossConnectionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCrossConnectionsApi#expressRouteCrossConnectionsListByResourceGroup");
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

[**ExpressRouteCrossConnectionListResult**](ExpressRouteCrossConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful.The operation returns a list of ExpressRouteCrossConnection resources. If there are no cross connection resources an empty list is returned. |  -  |

<a id="expressRouteCrossConnectionsUpdateTags"></a>
# **expressRouteCrossConnectionsUpdateTags**
> ExpressRouteCrossConnection expressRouteCrossConnectionsUpdateTags(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, crossConnectionParameters)



Updates an express route cross connection tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteCrossConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteCrossConnectionsApi apiInstance = new ExpressRouteCrossConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String crossConnectionName = "crossConnectionName_example"; // String | The name of the cross connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ExpressRouteCrossConnectionsUpdateTagsRequest crossConnectionParameters = new ExpressRouteCrossConnectionsUpdateTagsRequest(); // ExpressRouteCrossConnectionsUpdateTagsRequest | Parameters supplied to update express route cross connection tags.
    try {
      ExpressRouteCrossConnection result = apiInstance.expressRouteCrossConnectionsUpdateTags(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, crossConnectionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteCrossConnectionsApi#expressRouteCrossConnectionsUpdateTags");
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
| **crossConnectionName** | **String**| The name of the cross connection. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **crossConnectionParameters** | [**ExpressRouteCrossConnectionsUpdateTagsRequest**](ExpressRouteCrossConnectionsUpdateTagsRequest.md)| Parameters supplied to update express route cross connection tags. | |

### Return type

[**ExpressRouteCrossConnection**](ExpressRouteCrossConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ExpressRouteCrossConnection resource. |  -  |

