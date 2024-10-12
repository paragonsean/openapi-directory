# RegistriesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registriesGetBuildSourceUploadUrl**](RegistriesApi.md#registriesGetBuildSourceUploadUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/getBuildSourceUploadUrl |  |
| [**registriesQueueBuild**](RegistriesApi.md#registriesQueueBuild) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/queueBuild |  |


<a id="registriesGetBuildSourceUploadUrl"></a>
# **registriesGetBuildSourceUploadUrl**
> SourceUploadDefinition registriesGetBuildSourceUploadUrl(subscriptionId, resourceGroupName, registryName, apiVersion)



Get the upload location for the user to be able to upload the source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistriesApi apiInstance = new RegistriesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      SourceUploadDefinition result = apiInstance.registriesGetBuildSourceUploadUrl(subscriptionId, resourceGroupName, registryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistriesApi#registriesGetBuildSourceUploadUrl");
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

[**SourceUploadDefinition**](SourceUploadDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed. If the registry/build doesn&#39;t exist, 404 (Not found) is returned. |  -  |

<a id="registriesQueueBuild"></a>
# **registriesQueueBuild**
> Build registriesQueueBuild(subscriptionId, resourceGroupName, registryName, apiVersion, buildRequest)



Creates a new build based on the request parameters and add it to the build queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistriesApi apiInstance = new RegistriesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    QueueBuildRequest buildRequest = new QueueBuildRequest(); // QueueBuildRequest | The parameters of a build that needs to queued.
    try {
      Build result = apiInstance.registriesQueueBuild(subscriptionId, resourceGroupName, registryName, apiVersion, buildRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistriesApi#registriesQueueBuild");
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
| **buildRequest** | [**QueueBuildRequest**](QueueBuildRequest.md)| The parameters of a build that needs to queued. | |

### Return type

[**Build**](Build.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **202** | The request was successfully accepted; the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. If the registry/build doesn&#39;t exist, 404 (Not found) is returned. If any of the input parameters is wrong, 400(Bad Request) is returned. |  -  |

