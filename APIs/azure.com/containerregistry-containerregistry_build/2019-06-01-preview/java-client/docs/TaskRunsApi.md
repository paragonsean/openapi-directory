# TaskRunsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taskRunsCreate**](TaskRunsApi.md#taskRunsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName} |  |
| [**taskRunsDelete**](TaskRunsApi.md#taskRunsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName} |  |
| [**taskRunsGet**](TaskRunsApi.md#taskRunsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName} |  |
| [**taskRunsList**](TaskRunsApi.md#taskRunsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns |  |
| [**taskRunsUpdate**](TaskRunsApi.md#taskRunsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/taskRuns/{taskRunName} |  |


<a id="taskRunsCreate"></a>
# **taskRunsCreate**
> TaskRun taskRunsCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, taskRun)



Creates a task run for a container registry with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TaskRunsApi apiInstance = new TaskRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String taskRunName = "taskRunName_example"; // String | The name of task run.
    TaskRun taskRun = new TaskRun(); // TaskRun | The parameters of a run that needs to scheduled.
    try {
      TaskRun result = apiInstance.taskRunsCreate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, taskRun);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskRunsApi#taskRunsCreate");
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
| **taskRunName** | **String**| The name of task run. | |
| **taskRun** | [**TaskRun**](TaskRun.md)| The parameters of a run that needs to scheduled. | |

### Return type

[**TaskRun**](TaskRun.md)

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

<a id="taskRunsDelete"></a>
# **taskRunsDelete**
> taskRunsDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName)



Deletes a specified task run resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TaskRunsApi apiInstance = new TaskRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String taskRunName = "taskRunName_example"; // String | The task run name.
    try {
      apiInstance.taskRunsDelete(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskRunsApi#taskRunsDelete");
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
| **taskRunName** | **String**| The task run name. | |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **202** | The request was successfully accepted; the operation will complete asynchronously. |  -  |
| **204** | No Content - the specified resource was not found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="taskRunsGet"></a>
# **taskRunsGet**
> TaskRun taskRunsGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName)



Gets the detailed information for a given task run.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TaskRunsApi apiInstance = new TaskRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String taskRunName = "taskRunName_example"; // String | The run request name.
    try {
      TaskRun result = apiInstance.taskRunsGet(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskRunsApi#taskRunsGet");
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
| **taskRunName** | **String**| The run request name. | |

### Return type

[**TaskRun**](TaskRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed. If the registry/run doesn&#39;t exist, 404 (Not found) is returned. |  -  |

<a id="taskRunsList"></a>
# **taskRunsList**
> TaskRunListResult taskRunsList(subscriptionId, resourceGroupName, registryName, apiVersion)



Lists all the task runs for a specified container registry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TaskRunsApi apiInstance = new TaskRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      TaskRunListResult result = apiInstance.taskRunsList(subscriptionId, resourceGroupName, registryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskRunsApi#taskRunsList");
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

[**TaskRunListResult**](TaskRunListResult.md)

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

<a id="taskRunsUpdate"></a>
# **taskRunsUpdate**
> TaskRun taskRunsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, updateParameters)



Updates a task run with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TaskRunsApi apiInstance = new TaskRunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String taskRunName = "taskRunName_example"; // String | The task run name.
    TaskRunUpdateParameters updateParameters = new TaskRunUpdateParameters(); // TaskRunUpdateParameters | The parameters for updating a task run.
    try {
      TaskRun result = apiInstance.taskRunsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, taskRunName, updateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskRunsApi#taskRunsUpdate");
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
| **taskRunName** | **String**| The task run name. | |
| **updateParameters** | [**TaskRunUpdateParameters**](TaskRunUpdateParameters.md)| The parameters for updating a task run. | |

### Return type

[**TaskRun**](TaskRun.md)

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

