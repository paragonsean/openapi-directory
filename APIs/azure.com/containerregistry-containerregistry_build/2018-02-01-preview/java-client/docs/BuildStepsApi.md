# BuildStepsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**buildStepsCreate**](BuildStepsApi.md#buildStepsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName} |  |
| [**buildStepsDelete**](BuildStepsApi.md#buildStepsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName} |  |
| [**buildStepsGet**](BuildStepsApi.md#buildStepsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName} |  |
| [**buildStepsList**](BuildStepsApi.md#buildStepsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps |  |
| [**buildStepsListBuildArguments**](BuildStepsApi.md#buildStepsListBuildArguments) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName}/listBuildArguments |  |
| [**buildStepsUpdate**](BuildStepsApi.md#buildStepsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/buildTasks/{buildTaskName}/steps/{stepName} |  |


<a id="buildStepsCreate"></a>
# **buildStepsCreate**
> BuildStep buildStepsCreate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, buildStepCreateParameters)



Creates a build step for a build task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildStepsApi apiInstance = new BuildStepsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
    String stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
    BuildStep buildStepCreateParameters = new BuildStep(); // BuildStep | The parameters for creating a build step.
    try {
      BuildStep result = apiInstance.buildStepsCreate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, buildStepCreateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildStepsApi#buildStepsCreate");
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
| **buildTaskName** | **String**| The name of the container registry build task. | |
| **stepName** | **String**| The name of a build step for a container registry build task. | |
| **buildStepCreateParameters** | [**BuildStep**](BuildStep.md)| The parameters for creating a build step. | |

### Return type

[**BuildStep**](BuildStep.md)

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
| **0** | Error response describing why the operation failed. If the registry doesn&#39;t exist, 404 (Not found) is returned.If any of the input parameters is wrong, 400(Bad Request) is returned. |  -  |

<a id="buildStepsDelete"></a>
# **buildStepsDelete**
> buildStepsDelete(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName)



Deletes a build step from the build task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildStepsApi apiInstance = new BuildStepsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
    String stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
    try {
      apiInstance.buildStepsDelete(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildStepsApi#buildStepsDelete");
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
| **buildTaskName** | **String**| The name of the container registry build task. | |
| **stepName** | **String**| The name of a build step for a container registry build task. | |

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
| **0** | Error response describing why the operation failed. |  -  |

<a id="buildStepsGet"></a>
# **buildStepsGet**
> BuildStep buildStepsGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName)



Gets the build step for a build task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildStepsApi apiInstance = new BuildStepsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
    String stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
    try {
      BuildStep result = apiInstance.buildStepsGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildStepsApi#buildStepsGet");
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
| **buildTaskName** | **String**| The name of the container registry build task. | |
| **stepName** | **String**| The name of a build step for a container registry build task. | |

### Return type

[**BuildStep**](BuildStep.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed. If the registry/step doesn&#39;t exist, 404 (Not found) is returned. |  -  |

<a id="buildStepsList"></a>
# **buildStepsList**
> BuildStepList buildStepsList(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName)



List all the build steps for a given build task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildStepsApi apiInstance = new BuildStepsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
    try {
      BuildStepList result = apiInstance.buildStepsList(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildStepsApi#buildStepsList");
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
| **buildTaskName** | **String**| The name of the container registry build task. | |

### Return type

[**BuildStepList**](BuildStepList.md)

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

<a id="buildStepsListBuildArguments"></a>
# **buildStepsListBuildArguments**
> BuildArgumentList buildStepsListBuildArguments(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName)



List the build arguments for a step including the secret arguments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildStepsApi apiInstance = new BuildStepsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
    String stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
    try {
      BuildArgumentList result = apiInstance.buildStepsListBuildArguments(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildStepsApi#buildStepsListBuildArguments");
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
| **buildTaskName** | **String**| The name of the container registry build task. | |
| **stepName** | **String**| The name of a build step for a container registry build task. | |

### Return type

[**BuildArgumentList**](BuildArgumentList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed. If the registry/step doesn&#39;t exist, 404 (Not found) is returned. |  -  |

<a id="buildStepsUpdate"></a>
# **buildStepsUpdate**
> BuildStep buildStepsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, buildStepUpdateParameters)



Updates a build step in a build task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildStepsApi apiInstance = new BuildStepsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildTaskName = "buildTaskName_example"; // String | The name of the container registry build task.
    String stepName = "stepName_example"; // String | The name of a build step for a container registry build task.
    BuildStepUpdateParameters buildStepUpdateParameters = new BuildStepUpdateParameters(); // BuildStepUpdateParameters | The parameters for updating a build step.
    try {
      BuildStep result = apiInstance.buildStepsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildTaskName, stepName, buildStepUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildStepsApi#buildStepsUpdate");
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
| **buildTaskName** | **String**| The name of the container registry build task. | |
| **stepName** | **String**| The name of a build step for a container registry build task. | |
| **buildStepUpdateParameters** | [**BuildStepUpdateParameters**](BuildStepUpdateParameters.md)| The parameters for updating a build step. | |

### Return type

[**BuildStep**](BuildStep.md)

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
| **0** | Error response describing why the operation failed. If the registry/step doesn&#39;t exist, 404 (Not found) is returned.If any of the input parameters is wrong, 400(Bad Request) is returned. |  -  |

