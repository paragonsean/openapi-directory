# BuildsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**buildsCancel**](BuildsApi.md#buildsCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds/{buildId}/cancel |  |
| [**buildsGet**](BuildsApi.md#buildsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds/{buildId} |  |
| [**buildsGetLogLink**](BuildsApi.md#buildsGetLogLink) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds/{buildId}/getLogLink |  |
| [**buildsList**](BuildsApi.md#buildsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds |  |
| [**buildsUpdate**](BuildsApi.md#buildsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/builds/{buildId} |  |


<a id="buildsCancel"></a>
# **buildsCancel**
> buildsCancel(subscriptionId, resourceGroupName, registryName, apiVersion, buildId)



Cancel an existing build.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildId = "buildId_example"; // String | The build ID.
    try {
      apiInstance.buildsCancel(subscriptionId, resourceGroupName, registryName, apiVersion, buildId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsCancel");
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
| **buildId** | **String**| The build ID. | |

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
| **0** | Error response describing why the operation failed. If the registry/build doesn&#39;t exist, 404 (Not found) is returned. |  -  |

<a id="buildsGet"></a>
# **buildsGet**
> Build buildsGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildId)



Gets the detailed information for a given build.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildId = "buildId_example"; // String | The build ID.
    try {
      Build result = apiInstance.buildsGet(subscriptionId, resourceGroupName, registryName, apiVersion, buildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsGet");
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
| **buildId** | **String**| The build ID. | |

### Return type

[**Build**](Build.md)

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

<a id="buildsGetLogLink"></a>
# **buildsGetLogLink**
> BuildGetLogResult buildsGetLogLink(subscriptionId, resourceGroupName, registryName, apiVersion, buildId)



Gets a link to download the build logs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildId = "buildId_example"; // String | The build ID.
    try {
      BuildGetLogResult result = apiInstance.buildsGetLogLink(subscriptionId, resourceGroupName, registryName, apiVersion, buildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsGetLogLink");
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
| **buildId** | **String**| The build ID. | |

### Return type

[**BuildGetLogResult**](BuildGetLogResult.md)

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

<a id="buildsList"></a>
# **buildsList**
> BuildListResult buildsList(subscriptionId, resourceGroupName, registryName, apiVersion, $filter, $top, $skipToken)



Gets all the builds for a registry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String $filter = "$filter_example"; // String | The builds filter to apply on the operation.
    Integer $top = 56; // Integer | $top is supported for get list of builds, which limits the maximum number of builds to return.
    String $skipToken = "$skipToken_example"; // String | $skipToken is supported on get list of builds, which provides the next page in the list of builds.
    try {
      BuildListResult result = apiInstance.buildsList(subscriptionId, resourceGroupName, registryName, apiVersion, $filter, $top, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsList");
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
| **$filter** | **String**| The builds filter to apply on the operation. | [optional] |
| **$top** | **Integer**| $top is supported for get list of builds, which limits the maximum number of builds to return. | [optional] |
| **$skipToken** | **String**| $skipToken is supported on get list of builds, which provides the next page in the list of builds. | [optional] |

### Return type

[**BuildListResult**](BuildListResult.md)

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

<a id="buildsUpdate"></a>
# **buildsUpdate**
> Build buildsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildId, buildUpdateParameters)



Patch the build properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String buildId = "buildId_example"; // String | The build ID.
    BuildUpdateParameters buildUpdateParameters = new BuildUpdateParameters(); // BuildUpdateParameters | The build update properties.
    try {
      Build result = apiInstance.buildsUpdate(subscriptionId, resourceGroupName, registryName, apiVersion, buildId, buildUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsUpdate");
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
| **buildId** | **String**| The build ID. | |
| **buildUpdateParameters** | [**BuildUpdateParameters**](BuildUpdateParameters.md)| The build update properties. | |

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
| **201** | The request was successfully accepted; the operation will complete asynchronously. The provisioning state of the resource should indicate the current state of the resource. |  -  |
| **0** | Error response describing why the operation failed. If the registry/build doesn&#39;t exist, 404 (Not found) is returned. If any of the input parameters is wrong, 400(Bad Request) is returned. |  -  |

