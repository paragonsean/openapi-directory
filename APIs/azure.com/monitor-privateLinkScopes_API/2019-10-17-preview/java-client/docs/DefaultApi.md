# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateLinkScopesCreateOrUpdate**](DefaultApi.md#privateLinkScopesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes/{scopeName} |  |
| [**privateLinkScopesDelete**](DefaultApi.md#privateLinkScopesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes/{scopeName} |  |
| [**privateLinkScopesGet**](DefaultApi.md#privateLinkScopesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes/{scopeName} |  |
| [**privateLinkScopesList**](DefaultApi.md#privateLinkScopesList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/privateLinkScopes |  |
| [**privateLinkScopesListByResourceGroup**](DefaultApi.md#privateLinkScopesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes |  |
| [**privateLinkScopesUpdateTags**](DefaultApi.md#privateLinkScopesUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes/{scopeName} |  |


<a id="privateLinkScopesCreateOrUpdate"></a>
# **privateLinkScopesCreateOrUpdate**
> AzureMonitorPrivateLinkScope privateLinkScopesCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, scopeName, azureMonitorPrivateLinkScopePayload)



Creates (or updates) a Azure Monitor PrivateLinkScope. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String scopeName = "scopeName_example"; // String | The name of the Azure Monitor PrivateLinkScope resource.
    AzureMonitorPrivateLinkScope azureMonitorPrivateLinkScopePayload = new AzureMonitorPrivateLinkScope(); // AzureMonitorPrivateLinkScope | Properties that need to be specified to create or update a Azure Monitor PrivateLinkScope.
    try {
      AzureMonitorPrivateLinkScope result = apiInstance.privateLinkScopesCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, scopeName, azureMonitorPrivateLinkScopePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#privateLinkScopesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **scopeName** | **String**| The name of the Azure Monitor PrivateLinkScope resource. | |
| **azureMonitorPrivateLinkScopePayload** | [**AzureMonitorPrivateLinkScope**](AzureMonitorPrivateLinkScope.md)| Properties that need to be specified to create or update a Azure Monitor PrivateLinkScope. | |

### Return type

[**AzureMonitorPrivateLinkScope**](AzureMonitorPrivateLinkScope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request when creating or updating a Azure Monitor PrivateLinkScope. The updated PrivateLinkScope is returned. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="privateLinkScopesDelete"></a>
# **privateLinkScopesDelete**
> privateLinkScopesDelete(resourceGroupName, apiVersion, subscriptionId, scopeName)



Deletes a Azure Monitor PrivateLinkScope.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String scopeName = "scopeName_example"; // String | The name of the Azure Monitor PrivateLinkScope resource.
    try {
      apiInstance.privateLinkScopesDelete(resourceGroupName, apiVersion, subscriptionId, scopeName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#privateLinkScopesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **scopeName** | **String**| The name of the Azure Monitor PrivateLinkScope resource. | |

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
| **200** | Successful request when deleting a Azure Monitor PrivateLinkScope. |  -  |
| **202** | Accepted. |  -  |
| **204** | The specified PrivateLinkScope does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="privateLinkScopesGet"></a>
# **privateLinkScopesGet**
> AzureMonitorPrivateLinkScope privateLinkScopesGet(resourceGroupName, apiVersion, subscriptionId, scopeName)



Returns a Azure Monitor PrivateLinkScope.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String scopeName = "scopeName_example"; // String | The name of the Azure Monitor PrivateLinkScope resource.
    try {
      AzureMonitorPrivateLinkScope result = apiInstance.privateLinkScopesGet(resourceGroupName, apiVersion, subscriptionId, scopeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#privateLinkScopesGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **scopeName** | **String**| The name of the Azure Monitor PrivateLinkScope resource. | |

### Return type

[**AzureMonitorPrivateLinkScope**](AzureMonitorPrivateLinkScope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Azure Monitor PrivateLinkScope definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="privateLinkScopesList"></a>
# **privateLinkScopesList**
> AzureMonitorPrivateLinkScopeListResult privateLinkScopesList(apiVersion, subscriptionId)



Gets a list of all Azure Monitor PrivateLinkScopes within a subscription.

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
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      AzureMonitorPrivateLinkScopeListResult result = apiInstance.privateLinkScopesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#privateLinkScopesList");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**AzureMonitorPrivateLinkScopeListResult**](AzureMonitorPrivateLinkScopeListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more Azure Monitor PrivateLinkScope definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="privateLinkScopesListByResourceGroup"></a>
# **privateLinkScopesListByResourceGroup**
> AzureMonitorPrivateLinkScopeListResult privateLinkScopesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets a list of Azure Monitor PrivateLinkScopes within a resource group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      AzureMonitorPrivateLinkScopeListResult result = apiInstance.privateLinkScopesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#privateLinkScopesListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**AzureMonitorPrivateLinkScopeListResult**](AzureMonitorPrivateLinkScopeListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more Azure Monitor PrivateLinkScope definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="privateLinkScopesUpdateTags"></a>
# **privateLinkScopesUpdateTags**
> AzureMonitorPrivateLinkScope privateLinkScopesUpdateTags(resourceGroupName, apiVersion, subscriptionId, scopeName, privateLinkScopeTags)



Updates an existing PrivateLinkScope&#39;s tags. To update other fields use the CreateOrUpdate method.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String scopeName = "scopeName_example"; // String | The name of the Azure Monitor PrivateLinkScope resource.
    TagsResource privateLinkScopeTags = new TagsResource(); // TagsResource | Updated tag information to set into the PrivateLinkScope instance.
    try {
      AzureMonitorPrivateLinkScope result = apiInstance.privateLinkScopesUpdateTags(resourceGroupName, apiVersion, subscriptionId, scopeName, privateLinkScopeTags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#privateLinkScopesUpdateTags");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **scopeName** | **String**| The name of the Azure Monitor PrivateLinkScope resource. | |
| **privateLinkScopeTags** | [**TagsResource**](TagsResource.md)| Updated tag information to set into the PrivateLinkScope instance. | |

### Return type

[**AzureMonitorPrivateLinkScope**](AzureMonitorPrivateLinkScope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updating the Azure Monitor PrivateLinkScope&#39;s tags was successful. PrivateLinkScope tags are updated and returned with the rest of the PrivateLinkScope&#39;s object properties. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

