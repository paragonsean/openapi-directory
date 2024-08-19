# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**containerGroupUsageList**](DefaultApi.md#containerGroupUsageList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerInstance/locations/{location}/usages |  |
| [**containerGroupsCreateOrUpdate**](DefaultApi.md#containerGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName} | Create or update container groups. |
| [**containerGroupsDelete**](DefaultApi.md#containerGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName} | Delete the specified container group. |
| [**containerGroupsGet**](DefaultApi.md#containerGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName} | Get the properties of the specified container group. |
| [**containerGroupsList**](DefaultApi.md#containerGroupsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerInstance/containerGroups | Get a list of container groups in the specified subscription. |
| [**containerGroupsListByResourceGroup**](DefaultApi.md#containerGroupsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups | Get a list of container groups in the specified subscription and resource group. |
| [**containerGroupsUpdate**](DefaultApi.md#containerGroupsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName} | Update container groups. |
| [**containerLogsList**](DefaultApi.md#containerLogsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/logs | Get the logs for a specified container instance. |
| [**startContainerLaunchExec**](DefaultApi.md#startContainerLaunchExec) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/exec | Starts the exec command for a specific container instance. |


<a id="containerGroupUsageList"></a>
# **containerGroupUsageList**
> UsageListResult containerGroupUsageList(subscriptionId, location, apiVersion)



Get the usage for a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | The identifier for the physical azure location.
    String apiVersion = "apiVersion_example"; // String | Client API version
    try {
      UsageListResult result = apiInstance.containerGroupUsageList(subscriptionId, location, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#containerGroupUsageList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| The identifier for the physical azure location. | |
| **apiVersion** | **String**| Client API version | |

### Return type

[**UsageListResult**](UsageListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="containerGroupsCreateOrUpdate"></a>
# **containerGroupsCreateOrUpdate**
> ContainerGroup containerGroupsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, containerGroupName, containerGroup)

Create or update container groups.

Create or update container groups with specified configurations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String containerGroupName = "containerGroupName_example"; // String | The name of the container group.
    ContainerGroup containerGroup = new ContainerGroup(); // ContainerGroup | The properties of the container group to be created or updated.
    try {
      ContainerGroup result = apiInstance.containerGroupsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, containerGroupName, containerGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#containerGroupsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **containerGroupName** | **String**| The name of the container group. | |
| **containerGroup** | [**ContainerGroup**](ContainerGroup.md)| The properties of the container group to be created or updated. | |

### Return type

[**ContainerGroup**](ContainerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created - the container group is created. |  -  |

<a id="containerGroupsDelete"></a>
# **containerGroupsDelete**
> ContainerGroup containerGroupsDelete(subscriptionId, apiVersion, resourceGroupName, containerGroupName)

Delete the specified container group.

Delete the specified container group in the specified subscription and resource group. The operation does not delete other resources provided by the user, such as volumes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String containerGroupName = "containerGroupName_example"; // String | The name of the container group.
    try {
      ContainerGroup result = apiInstance.containerGroupsDelete(subscriptionId, apiVersion, resourceGroupName, containerGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#containerGroupsDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **containerGroupName** | **String**| The name of the container group. | |

### Return type

[**ContainerGroup**](ContainerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content - the specified container group was not found. |  -  |

<a id="containerGroupsGet"></a>
# **containerGroupsGet**
> ContainerGroup containerGroupsGet(subscriptionId, apiVersion, resourceGroupName, containerGroupName)

Get the properties of the specified container group.

Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String containerGroupName = "containerGroupName_example"; // String | The name of the container group.
    try {
      ContainerGroup result = apiInstance.containerGroupsGet(subscriptionId, apiVersion, resourceGroupName, containerGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#containerGroupsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **containerGroupName** | **String**| The name of the container group. | |

### Return type

[**ContainerGroup**](ContainerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="containerGroupsList"></a>
# **containerGroupsList**
> ContainerGroupListResult containerGroupsList(subscriptionId, apiVersion)

Get a list of container groups in the specified subscription.

Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version
    try {
      ContainerGroupListResult result = apiInstance.containerGroupsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#containerGroupsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version | |

### Return type

[**ContainerGroupListResult**](ContainerGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="containerGroupsListByResourceGroup"></a>
# **containerGroupsListByResourceGroup**
> ContainerGroupListResult containerGroupsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)

Get a list of container groups in the specified subscription and resource group.

Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    try {
      ContainerGroupListResult result = apiInstance.containerGroupsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#containerGroupsListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version | |
| **resourceGroupName** | **String**| The name of the resource group. | |

### Return type

[**ContainerGroupListResult**](ContainerGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="containerGroupsUpdate"></a>
# **containerGroupsUpdate**
> ContainerGroup containerGroupsUpdate(subscriptionId, apiVersion, resourceGroupName, containerGroupName, resource)

Update container groups.

Updates container group tags with specified values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String containerGroupName = "containerGroupName_example"; // String | The name of the container group.
    Resource resource = new Resource(); // Resource | The container group resource with just the tags to be updated.
    try {
      ContainerGroup result = apiInstance.containerGroupsUpdate(subscriptionId, apiVersion, resourceGroupName, containerGroupName, resource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#containerGroupsUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **containerGroupName** | **String**| The name of the container group. | |
| **resource** | [**Resource**](Resource.md)| The container group resource with just the tags to be updated. | |

### Return type

[**ContainerGroup**](ContainerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="containerLogsList"></a>
# **containerLogsList**
> Logs containerLogsList(subscriptionId, apiVersion, resourceGroupName, containerGroupName, containerName, tail)

Get the logs for a specified container instance.

Get the logs for a specified container instance in a specified resource group and container group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String containerGroupName = "containerGroupName_example"; // String | The name of the container group.
    String containerName = "containerName_example"; // String | The name of the container instance.
    Integer tail = 56; // Integer | The number of lines to show from the tail of the container instance log. If not provided, all available logs are shown up to 4mb.
    try {
      Logs result = apiInstance.containerLogsList(subscriptionId, apiVersion, resourceGroupName, containerGroupName, containerName, tail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#containerLogsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **containerGroupName** | **String**| The name of the container group. | |
| **containerName** | **String**| The name of the container instance. | |
| **tail** | **Integer**| The number of lines to show from the tail of the container instance log. If not provided, all available logs are shown up to 4mb. | [optional] |

### Return type

[**Logs**](Logs.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="startContainerLaunchExec"></a>
# **startContainerLaunchExec**
> ContainerExecResponse startContainerLaunchExec(subscriptionId, apiVersion, resourceGroupName, containerGroupName, containerName, containerExecRequest)

Starts the exec command for a specific container instance.

Starts the exec command for a specified container instance in a specified resource group and container group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String containerGroupName = "containerGroupName_example"; // String | The name of the container group.
    String containerName = "containerName_example"; // String | The name of the container instance.
    ContainerExecRequest containerExecRequest = new ContainerExecRequest(); // ContainerExecRequest | The request for the exec command.
    try {
      ContainerExecResponse result = apiInstance.startContainerLaunchExec(subscriptionId, apiVersion, resourceGroupName, containerGroupName, containerName, containerExecRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startContainerLaunchExec");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **containerGroupName** | **String**| The name of the container group. | |
| **containerName** | **String**| The name of the container instance. | |
| **containerExecRequest** | [**ContainerExecRequest**](ContainerExecRequest.md)| The request for the exec command. | |

### Return type

[**ContainerExecResponse**](ContainerExecResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

