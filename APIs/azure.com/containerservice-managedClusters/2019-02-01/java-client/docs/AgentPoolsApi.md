# AgentPoolsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**agentPoolsCreateOrUpdate**](AgentPoolsApi.md#agentPoolsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{managedClusterName}/agentPools/{agentPoolName} | Creates or updates an agent pool. |
| [**agentPoolsDelete**](AgentPoolsApi.md#agentPoolsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{managedClusterName}/agentPools/{agentPoolName} | Deletes an agent pool. |
| [**agentPoolsGet**](AgentPoolsApi.md#agentPoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{managedClusterName}/agentPools/{agentPoolName} | Gets the agent pool. |
| [**agentPoolsList**](AgentPoolsApi.md#agentPoolsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{managedClusterName}/agentPools | Gets a list of agent pools in the specified managed cluster. |


<a id="agentPoolsCreateOrUpdate"></a>
# **agentPoolsCreateOrUpdate**
> AgentPool agentPoolsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, managedClusterName, agentPoolName, parameters)

Creates or updates an agent pool.

Creates or updates an agent pool in the specified managed cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AgentPoolsApi apiInstance = new AgentPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String managedClusterName = "managedClusterName_example"; // String | The name of the managed cluster resource.
    String agentPoolName = "agentPoolName_example"; // String | The name of the agent pool.
    AgentPool parameters = new AgentPool(); // AgentPool | Parameters supplied to the Create or Update an agent pool operation.
    try {
      AgentPool result = apiInstance.agentPoolsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, managedClusterName, agentPoolName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentPoolsApi#agentPoolsCreateOrUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **managedClusterName** | **String**| The name of the managed cluster resource. | |
| **agentPoolName** | **String**| The name of the agent pool. | |
| **parameters** | [**AgentPool**](AgentPool.md)| Parameters supplied to the Create or Update an agent pool operation. | |

### Return type

[**AgentPool**](AgentPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="agentPoolsDelete"></a>
# **agentPoolsDelete**
> agentPoolsDelete(apiVersion, subscriptionId, resourceGroupName, managedClusterName, agentPoolName)

Deletes an agent pool.

Deletes the agent pool in the specified managed cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AgentPoolsApi apiInstance = new AgentPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String managedClusterName = "managedClusterName_example"; // String | The name of the managed cluster resource.
    String agentPoolName = "agentPoolName_example"; // String | The name of the agent pool.
    try {
      apiInstance.agentPoolsDelete(apiVersion, subscriptionId, resourceGroupName, managedClusterName, agentPoolName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentPoolsApi#agentPoolsDelete");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **managedClusterName** | **String**| The name of the managed cluster resource. | |
| **agentPoolName** | **String**| The name of the agent pool. | |

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
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="agentPoolsGet"></a>
# **agentPoolsGet**
> AgentPool agentPoolsGet(apiVersion, subscriptionId, resourceGroupName, managedClusterName, agentPoolName)

Gets the agent pool.

Gets the details of the agent pool by managed cluster and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AgentPoolsApi apiInstance = new AgentPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String managedClusterName = "managedClusterName_example"; // String | The name of the managed cluster resource.
    String agentPoolName = "agentPoolName_example"; // String | The name of the agent pool.
    try {
      AgentPool result = apiInstance.agentPoolsGet(apiVersion, subscriptionId, resourceGroupName, managedClusterName, agentPoolName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentPoolsApi#agentPoolsGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **managedClusterName** | **String**| The name of the managed cluster resource. | |
| **agentPoolName** | **String**| The name of the agent pool. | |

### Return type

[**AgentPool**](AgentPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="agentPoolsList"></a>
# **agentPoolsList**
> AgentPoolListResult agentPoolsList(apiVersion, subscriptionId, resourceGroupName, managedClusterName)

Gets a list of agent pools in the specified managed cluster.

Gets a list of agent pools in the specified managed cluster. The operation returns properties of each agent pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AgentPoolsApi apiInstance = new AgentPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String managedClusterName = "managedClusterName_example"; // String | The name of the managed cluster resource.
    try {
      AgentPoolListResult result = apiInstance.agentPoolsList(apiVersion, subscriptionId, resourceGroupName, managedClusterName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentPoolsApi#agentPoolsList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **managedClusterName** | **String**| The name of the managed cluster resource. | |

### Return type

[**AgentPoolListResult**](AgentPoolListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

