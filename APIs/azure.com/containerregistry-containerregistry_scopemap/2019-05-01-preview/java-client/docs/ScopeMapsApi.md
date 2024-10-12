# ScopeMapsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scopeMapsCreate**](ScopeMapsApi.md#scopeMapsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/scopeMaps/{scopeMapName} |  |
| [**scopeMapsDelete**](ScopeMapsApi.md#scopeMapsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/scopeMaps/{scopeMapName} |  |
| [**scopeMapsGet**](ScopeMapsApi.md#scopeMapsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/scopeMaps/{scopeMapName} |  |
| [**scopeMapsList**](ScopeMapsApi.md#scopeMapsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/scopeMaps |  |
| [**scopeMapsUpdate**](ScopeMapsApi.md#scopeMapsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/scopeMaps/{scopeMapName} |  |


<a id="scopeMapsCreate"></a>
# **scopeMapsCreate**
> ScopeMap scopeMapsCreate(apiVersion, subscriptionId, resourceGroupName, registryName, scopeMapName, scopeMapCreateParameters)



Creates a scope map for a container registry with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScopeMapsApi apiInstance = new ScopeMapsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String scopeMapName = "scopeMapName_example"; // String | The name of the scope map.
    ScopeMap scopeMapCreateParameters = new ScopeMap(); // ScopeMap | The parameters for creating a scope map.
    try {
      ScopeMap result = apiInstance.scopeMapsCreate(apiVersion, subscriptionId, resourceGroupName, registryName, scopeMapName, scopeMapCreateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMapsApi#scopeMapsCreate");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **scopeMapName** | **String**| The name of the scope map. | |
| **scopeMapCreateParameters** | [**ScopeMap**](ScopeMap.md)| The parameters for creating a scope map. | |

### Return type

[**ScopeMap**](ScopeMap.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **201** | The request was successful; the operation will complete asynchronously. |  -  |

<a id="scopeMapsDelete"></a>
# **scopeMapsDelete**
> scopeMapsDelete(apiVersion, subscriptionId, resourceGroupName, registryName, scopeMapName)



Deletes a scope map from a container registry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScopeMapsApi apiInstance = new ScopeMapsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String scopeMapName = "scopeMapName_example"; // String | The name of the scope map.
    try {
      apiInstance.scopeMapsDelete(apiVersion, subscriptionId, resourceGroupName, registryName, scopeMapName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMapsApi#scopeMapsDelete");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **scopeMapName** | **String**| The name of the scope map. | |

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
| **202** | The request was successful; the operation will complete asynchronously. |  -  |
| **204** | The scopemap does not exist in the subscription. |  -  |

<a id="scopeMapsGet"></a>
# **scopeMapsGet**
> ScopeMap scopeMapsGet(apiVersion, subscriptionId, resourceGroupName, registryName, scopeMapName)



Gets the properties of the specified scope map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScopeMapsApi apiInstance = new ScopeMapsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String scopeMapName = "scopeMapName_example"; // String | The name of the scope map.
    try {
      ScopeMap result = apiInstance.scopeMapsGet(apiVersion, subscriptionId, resourceGroupName, registryName, scopeMapName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMapsApi#scopeMapsGet");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **scopeMapName** | **String**| The name of the scope map. | |

### Return type

[**ScopeMap**](ScopeMap.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |

<a id="scopeMapsList"></a>
# **scopeMapsList**
> ScopeMapListResult scopeMapsList(apiVersion, subscriptionId, resourceGroupName, registryName)



Lists all the scope maps for the specified container registry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScopeMapsApi apiInstance = new ScopeMapsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    try {
      ScopeMapListResult result = apiInstance.scopeMapsList(apiVersion, subscriptionId, resourceGroupName, registryName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMapsApi#scopeMapsList");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |

### Return type

[**ScopeMapListResult**](ScopeMapListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |

<a id="scopeMapsUpdate"></a>
# **scopeMapsUpdate**
> ScopeMap scopeMapsUpdate(apiVersion, subscriptionId, resourceGroupName, registryName, scopeMapName, scopeMapUpdateParameters)



Updates a scope map with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScopeMapsApi apiInstance = new ScopeMapsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String registryName = "registryName_example"; // String | The name of the container registry.
    String scopeMapName = "scopeMapName_example"; // String | The name of the scope map.
    ScopeMapUpdateParameters scopeMapUpdateParameters = new ScopeMapUpdateParameters(); // ScopeMapUpdateParameters | The parameters for updating a scope map.
    try {
      ScopeMap result = apiInstance.scopeMapsUpdate(apiVersion, subscriptionId, resourceGroupName, registryName, scopeMapName, scopeMapUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMapsApi#scopeMapsUpdate");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **registryName** | **String**| The name of the container registry. | |
| **scopeMapName** | **String**| The name of the scope map. | |
| **scopeMapUpdateParameters** | [**ScopeMapUpdateParameters**](ScopeMapUpdateParameters.md)| The parameters for updating a scope map. | |

### Return type

[**ScopeMap**](ScopeMap.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **201** | The request was successful; the operation will complete asynchronously. |  -  |

