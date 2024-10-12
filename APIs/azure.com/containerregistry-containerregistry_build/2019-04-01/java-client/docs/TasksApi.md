# TasksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tasksCreate**](TasksApi.md#tasksCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName} |  |
| [**tasksDelete**](TasksApi.md#tasksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName} |  |
| [**tasksGet**](TasksApi.md#tasksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName} |  |
| [**tasksGetDetails**](TasksApi.md#tasksGetDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}/listDetails |  |
| [**tasksList**](TasksApi.md#tasksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks |  |
| [**tasksUpdate**](TasksApi.md#tasksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName} |  |


<a id="tasksCreate"></a>
# **tasksCreate**
> Task tasksCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskCreateParameters)



Creates a task for a container registry with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String taskName = "taskName_example"; // String | The name of the container registry task.
    Task taskCreateParameters = new Task(); // Task | The parameters for creating a task.
    try {
      Task result = apiInstance.tasksCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskCreateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksCreate");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **apiVersion** | **String**| The client API version. | |
| **taskName** | **String**| The name of the container registry task. | |
| **taskCreateParameters** | [**Task**](Task.md)| The parameters for creating a task. | |

### Return type

[**Task**](Task.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **201** | The request was successfully accepted; the operation will complete asynchronously. The provisioning state of the resource should indicate the current state of the resource. |  -  |
| **0** | Error response describing why the operation failed. If the registry doesn&#39;t exist, 404 (Not found) is returned. If any of the input parameters is wrong, 400(Bad Request) is returned. |  -  |

<a id="tasksDelete"></a>
# **tasksDelete**
> tasksDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskName)



Deletes a specified task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String taskName = "taskName_example"; // String | The name of the container registry task.
    try {
      apiInstance.tasksDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksDelete");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **apiVersion** | **String**| The client API version. | |
| **taskName** | **String**| The name of the container registry task. | |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **202** | The request was successfully accepted; the operation will complete asynchronously. |  -  |
| **204** | No Content - the specified resource was not found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tasksGet"></a>
# **tasksGet**
> Task tasksGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskName)



Get the properties of a specified task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String taskName = "taskName_example"; // String | The name of the container registry task.
    try {
      Task result = apiInstance.tasksGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksGet");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **apiVersion** | **String**| The client API version. | |
| **taskName** | **String**| The name of the container registry task. | |

### Return type

[**Task**](Task.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed. If the registry doesn&#39;t exist, 404 (Not found) is returned. |  -  |

<a id="tasksGetDetails"></a>
# **tasksGetDetails**
> Task tasksGetDetails(subscriptionId, resourceGroupName, registryName, apiVersion, taskName)



Returns a task with extended information that includes all secrets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String taskName = "taskName_example"; // String | The name of the container registry task.
    try {
      Task result = apiInstance.tasksGetDetails(subscriptionId, resourceGroupName, registryName, apiVersion, taskName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksGetDetails");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **apiVersion** | **String**| The client API version. | |
| **taskName** | **String**| The name of the container registry task. | |

### Return type

[**Task**](Task.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed. If the registry doesn&#39;t exist, 404 (Not found) is returned. |  -  |

<a id="tasksList"></a>
# **tasksList**
> TaskListResult tasksList(subscriptionId, resourceGroupName, registryName, apiVersion)



Lists all the tasks for a specified container registry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      TaskListResult result = apiInstance.tasksList(subscriptionId, resourceGroupName, registryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksList");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**TaskListResult**](TaskListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tasksUpdate"></a>
# **tasksUpdate**
> Task tasksUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskUpdateParameters)



Updates a task with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String taskName = "taskName_example"; // String | The name of the container registry task.
    TaskUpdateParameters taskUpdateParameters = new TaskUpdateParameters(); // TaskUpdateParameters | The parameters for updating a task.
    try {
      Task result = apiInstance.tasksUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskName, taskUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksUpdate");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **apiVersion** | **String**| The client API version. | |
| **taskName** | **String**| The name of the container registry task. | |
| **taskUpdateParameters** | [**TaskUpdateParameters**](TaskUpdateParameters.md)| The parameters for updating a task. | |

### Return type

[**Task**](Task.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **201** | The request was successfully accepted; the operation will complete asynchronously. The provisioning state of the resource should indicate the current state of the resource. |  -  |
| **0** | Error response describing why the operation failed. If the registry doesn&#39;t exist, 404 (Not found) is returned. If any of the input parameters is wrong, 400(Bad Request) is returned. |  -  |

