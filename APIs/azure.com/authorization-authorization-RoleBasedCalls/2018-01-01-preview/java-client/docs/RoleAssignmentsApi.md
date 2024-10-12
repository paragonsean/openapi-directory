# RoleAssignmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**roleAssignmentsCreate**](RoleAssignmentsApi.md#roleAssignmentsCreate) | **PUT** /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName} |  |
| [**roleAssignmentsCreateById**](RoleAssignmentsApi.md#roleAssignmentsCreateById) | **PUT** /{roleId} |  |
| [**roleAssignmentsDelete**](RoleAssignmentsApi.md#roleAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName} |  |
| [**roleAssignmentsDeleteById**](RoleAssignmentsApi.md#roleAssignmentsDeleteById) | **DELETE** /{roleId} |  |
| [**roleAssignmentsGet**](RoleAssignmentsApi.md#roleAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName} |  |
| [**roleAssignmentsGetById**](RoleAssignmentsApi.md#roleAssignmentsGetById) | **GET** /{roleId} |  |
| [**roleAssignmentsList**](RoleAssignmentsApi.md#roleAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/roleAssignments |  |
| [**roleAssignmentsListForResource**](RoleAssignmentsApi.md#roleAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/roleAssignments |  |
| [**roleAssignmentsListForResourceGroup**](RoleAssignmentsApi.md#roleAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/roleAssignments |  |
| [**roleAssignmentsListForScope**](RoleAssignmentsApi.md#roleAssignmentsListForScope) | **GET** /{scope}/providers/Microsoft.Authorization/roleAssignments |  |


<a id="roleAssignmentsCreate"></a>
# **roleAssignmentsCreate**
> RoleAssignment roleAssignmentsCreate(scope, roleAssignmentName, apiVersion, parameters)



Creates a role assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the role assignment to create. The scope can be any REST resource instance. For example, use '/subscriptions/{subscription-id}/' for a subscription, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for a resource group, and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}' for a resource.
    String roleAssignmentName = "roleAssignmentName_example"; // String | The name of the role assignment to create. It can be any valid GUID.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    RoleAssignmentCreateParameters parameters = new RoleAssignmentCreateParameters(); // RoleAssignmentCreateParameters | Parameters for the role assignment.
    try {
      RoleAssignment result = apiInstance.roleAssignmentsCreate(scope, roleAssignmentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsCreate");
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
| **scope** | **String**| The scope of the role assignment to create. The scope can be any REST resource instance. For example, use &#39;/subscriptions/{subscription-id}/&#39; for a subscription, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for a resource group, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}&#39; for a resource. | |
| **roleAssignmentName** | **String**| The name of the role assignment to create. It can be any valid GUID. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**RoleAssignmentCreateParameters**](RoleAssignmentCreateParameters.md)| Parameters for the role assignment. | |

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created - Returns information about the role assignment. |  -  |

<a id="roleAssignmentsCreateById"></a>
# **roleAssignmentsCreateById**
> RoleAssignment roleAssignmentsCreateById(roleId, apiVersion, parameters)



Creates a role assignment by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String roleId = "roleId_example"; // String | The ID of the role assignment to create.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    RoleAssignmentCreateParameters parameters = new RoleAssignmentCreateParameters(); // RoleAssignmentCreateParameters | Parameters for the role assignment.
    try {
      RoleAssignment result = apiInstance.roleAssignmentsCreateById(roleId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsCreateById");
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
| **roleId** | **String**| The ID of the role assignment to create. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**RoleAssignmentCreateParameters**](RoleAssignmentCreateParameters.md)| Parameters for the role assignment. | |

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created - Returns the role assignment. |  -  |

<a id="roleAssignmentsDelete"></a>
# **roleAssignmentsDelete**
> RoleAssignment roleAssignmentsDelete(scope, roleAssignmentName, apiVersion)



Deletes a role assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the role assignment to delete.
    String roleAssignmentName = "roleAssignmentName_example"; // String | The name of the role assignment to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      RoleAssignment result = apiInstance.roleAssignmentsDelete(scope, roleAssignmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsDelete");
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
| **scope** | **String**| The scope of the role assignment to delete. | |
| **roleAssignmentName** | **String**| The name of the role assignment to delete. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the role assignment. |  -  |

<a id="roleAssignmentsDeleteById"></a>
# **roleAssignmentsDeleteById**
> RoleAssignment roleAssignmentsDeleteById(roleId, apiVersion)



Deletes a role assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String roleId = "roleId_example"; // String | The ID of the role assignment to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      RoleAssignment result = apiInstance.roleAssignmentsDeleteById(roleId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsDeleteById");
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
| **roleId** | **String**| The ID of the role assignment to delete. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the role assignment. |  -  |

<a id="roleAssignmentsGet"></a>
# **roleAssignmentsGet**
> RoleAssignment roleAssignmentsGet(scope, roleAssignmentName, apiVersion)



Get the specified role assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the role assignment.
    String roleAssignmentName = "roleAssignmentName_example"; // String | The name of the role assignment to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      RoleAssignment result = apiInstance.roleAssignmentsGet(scope, roleAssignmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsGet");
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
| **scope** | **String**| The scope of the role assignment. | |
| **roleAssignmentName** | **String**| The name of the role assignment to get. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the role assignment. |  -  |

<a id="roleAssignmentsGetById"></a>
# **roleAssignmentsGetById**
> RoleAssignment roleAssignmentsGetById(roleId, apiVersion)



Gets a role assignment by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String roleId = "roleId_example"; // String | The ID of the role assignment to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      RoleAssignment result = apiInstance.roleAssignmentsGetById(roleId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsGetById");
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
| **roleId** | **String**| The ID of the role assignment to get. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the role assignment. |  -  |

<a id="roleAssignmentsList"></a>
# **roleAssignmentsList**
> RoleAssignmentListResult roleAssignmentsList(apiVersion, subscriptionId, $filter)



Gets all role assignments for the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
    try {
      RoleAssignmentListResult result = apiInstance.roleAssignmentsList(apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsList");
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
| **$filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal. | [optional] |

### Return type

[**RoleAssignmentListResult**](RoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of role assignments. |  -  |

<a id="roleAssignmentsListForResource"></a>
# **roleAssignmentsListForResource**
> RoleAssignmentListResult roleAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter)



Gets role assignments for a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type of the resource.
    String resourceName = "resourceName_example"; // String | The name of the resource to get role assignments for.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
    try {
      RoleAssignmentListResult result = apiInstance.roleAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsListForResource");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type of the resource. | |
| **resourceName** | **String**| The name of the resource to get role assignments for. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal. | [optional] |

### Return type

[**RoleAssignmentListResult**](RoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of role assignments. |  -  |

<a id="roleAssignmentsListForResourceGroup"></a>
# **roleAssignmentsListForResourceGroup**
> RoleAssignmentListResult roleAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter)



Gets role assignments for a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
    try {
      RoleAssignmentListResult result = apiInstance.roleAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsListForResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal. | [optional] |

### Return type

[**RoleAssignmentListResult**](RoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of role assignments. |  -  |

<a id="roleAssignmentsListForScope"></a>
# **roleAssignmentsListForScope**
> RoleAssignmentListResult roleAssignmentsListForScope(scope, apiVersion, $filter)



Gets role assignments for a scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the role assignments.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Use $filter=atScope() to return all role assignments at or above the scope. Use $filter=principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
    try {
      RoleAssignmentListResult result = apiInstance.roleAssignmentsListForScope(scope, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsListForScope");
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
| **scope** | **String**| The scope of the role assignments. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal. | [optional] |

### Return type

[**RoleAssignmentListResult**](RoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of role assignments. |  -  |

