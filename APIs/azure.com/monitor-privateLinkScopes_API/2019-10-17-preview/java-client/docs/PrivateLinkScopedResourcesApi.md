# PrivateLinkScopedResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateLinkScopedResourcesCreateOrUpdate**](PrivateLinkScopedResourcesApi.md#privateLinkScopedResourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/scopedResources/{name} |  |
| [**privateLinkScopedResourcesDelete**](PrivateLinkScopedResourcesApi.md#privateLinkScopedResourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/scopedResources/{name} |  |
| [**privateLinkScopedResourcesGet**](PrivateLinkScopedResourcesApi.md#privateLinkScopedResourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/scopedResources/{name} |  |
| [**privateLinkScopedResourcesListByPrivateLinkScope**](PrivateLinkScopedResourcesApi.md#privateLinkScopedResourcesListByPrivateLinkScope) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/scopedResources |  |


<a id="privateLinkScopedResourcesCreateOrUpdate"></a>
# **privateLinkScopedResourcesCreateOrUpdate**
> ScopedResource privateLinkScopedResourcesCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, scopeName, name, parameters)



Approve or reject a private endpoint connection with a given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkScopedResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkScopedResourcesApi apiInstance = new PrivateLinkScopedResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    String name = "name_example"; // String | The name of the scoped resource object.
    ScopedResource parameters = new ScopedResource(); // ScopedResource | 
    try {
      ScopedResource result = apiInstance.privateLinkScopedResourcesCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, scopeName, name, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkScopedResourcesApi#privateLinkScopedResourcesCreateOrUpdate");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |
| **name** | **String**| The name of the scoped resource object. | |
| **parameters** | [**ScopedResource**](ScopedResource.md)|  | |

### Return type

[**ScopedResource**](ScopedResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully scoped azure monitor resource in a private link scope. |  -  |
| **202** | Accepted |  -  |

<a id="privateLinkScopedResourcesDelete"></a>
# **privateLinkScopedResourcesDelete**
> privateLinkScopedResourcesDelete(subscriptionId, resourceGroupName, apiVersion, scopeName, name)



Deletes a private endpoint connection with a given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkScopedResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkScopedResourcesApi apiInstance = new PrivateLinkScopedResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    String name = "name_example"; // String | The name of the scoped resource object.
    try {
      apiInstance.privateLinkScopedResourcesDelete(subscriptionId, resourceGroupName, apiVersion, scopeName, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkScopedResourcesApi#privateLinkScopedResourcesDelete");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |
| **name** | **String**| The name of the scoped resource object. | |

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
| **200** | Successfully deleted scoped resource. |  -  |
| **202** | Accepted |  -  |
| **204** | Scoped resource does not exist. |  -  |

<a id="privateLinkScopedResourcesGet"></a>
# **privateLinkScopedResourcesGet**
> ScopedResource privateLinkScopedResourcesGet(subscriptionId, resourceGroupName, apiVersion, scopeName, name)



Gets a scoped resource in a private link scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkScopedResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkScopedResourcesApi apiInstance = new PrivateLinkScopedResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    String name = "name_example"; // String | The name of the scoped resource object.
    try {
      ScopedResource result = apiInstance.privateLinkScopedResourcesGet(subscriptionId, resourceGroupName, apiVersion, scopeName, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkScopedResourcesApi#privateLinkScopedResourcesGet");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |
| **name** | **String**| The name of the scoped resource object. | |

### Return type

[**ScopedResource**](ScopedResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved a scoped resource in a private link scope. |  -  |

<a id="privateLinkScopedResourcesListByPrivateLinkScope"></a>
# **privateLinkScopedResourcesListByPrivateLinkScope**
> ScopedResourceListResult privateLinkScopedResourcesListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName)



Gets all private endpoint connections on a private link scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkScopedResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkScopedResourcesApi apiInstance = new PrivateLinkScopedResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    try {
      ScopedResourceListResult result = apiInstance.privateLinkScopedResourcesListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkScopedResourcesApi#privateLinkScopedResourcesListByPrivateLinkScope");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |

### Return type

[**ScopedResourceListResult**](ScopedResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved scoped resources in a private link scope. |  -  |

