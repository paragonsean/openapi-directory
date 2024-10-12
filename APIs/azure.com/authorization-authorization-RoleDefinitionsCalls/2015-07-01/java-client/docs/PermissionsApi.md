# PermissionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**permissionsListForResource**](PermissionsApi.md#permissionsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/permissions |  |
| [**permissionsListForResourceGroup**](PermissionsApi.md#permissionsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Authorization/permissions |  |


<a id="permissionsListForResource"></a>
# **permissionsListForResource**
> PermissionGetResult permissionsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Gets all permissions the caller has for a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource. The name is case insensitive.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type of the resource.
    String resourceName = "resourceName_example"; // String | The name of the resource to get the permissions for.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      PermissionGetResult result = apiInstance.permissionsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#permissionsListForResource");
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
| **resourceGroupName** | **String**| The name of the resource group containing the resource. The name is case insensitive. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type of the resource. | |
| **resourceName** | **String**| The name of the resource to get the permissions for. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**PermissionGetResult**](PermissionGetResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of permissions. |  -  |

<a id="permissionsListForResourceGroup"></a>
# **permissionsListForResourceGroup**
> PermissionGetResult permissionsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all permissions the caller has for a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get the permissions for. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      PermissionGetResult result = apiInstance.permissionsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#permissionsListForResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group to get the permissions for. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**PermissionGetResult**](PermissionGetResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of permissions. |  -  |

