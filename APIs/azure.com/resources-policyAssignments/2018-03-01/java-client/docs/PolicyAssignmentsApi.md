# PolicyAssignmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policyAssignmentsCreate**](PolicyAssignmentsApi.md#policyAssignmentsCreate) | **PUT** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | Creates or updates a policy assignment. |
| [**policyAssignmentsCreateById**](PolicyAssignmentsApi.md#policyAssignmentsCreateById) | **PUT** /{policyAssignmentId} | Creates or updates a policy assignment. |
| [**policyAssignmentsDelete**](PolicyAssignmentsApi.md#policyAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | Deletes a policy assignment. |
| [**policyAssignmentsDeleteById**](PolicyAssignmentsApi.md#policyAssignmentsDeleteById) | **DELETE** /{policyAssignmentId} | Deletes a policy assignment. |
| [**policyAssignmentsGet**](PolicyAssignmentsApi.md#policyAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | Retrieves a policy assignment. |
| [**policyAssignmentsGetById**](PolicyAssignmentsApi.md#policyAssignmentsGetById) | **GET** /{policyAssignmentId} | Retrieves the policy assignment with the given ID. |
| [**policyAssignmentsList**](PolicyAssignmentsApi.md#policyAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments | Retrieves all policy assignments that apply to a subscription. |
| [**policyAssignmentsListForResource**](PolicyAssignmentsApi.md#policyAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/policyAssignments | Retrieves all policy assignments that apply to a resource. |
| [**policyAssignmentsListForResourceGroup**](PolicyAssignmentsApi.md#policyAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyAssignments | Retrieves all policy assignments that apply to a resource group. |


<a id="policyAssignmentsCreate"></a>
# **policyAssignmentsCreate**
> PolicyAssignment policyAssignmentsCreate(scope, policyAssignmentName, apiVersion, parameters)

Creates or updates a policy assignment.

 This operation creates or updates a policy assignment with the given scope and name. Policy assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the policy assignment. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
    String policyAssignmentName = "policyAssignmentName_example"; // String | The name of the policy assignment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    PolicyAssignment parameters = new PolicyAssignment(); // PolicyAssignment | Parameters for the policy assignment.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsCreate(scope, policyAssignmentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsCreate");
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
| **scope** | **String**| The scope of the policy assignment. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39; | |
| **policyAssignmentName** | **String**| The name of the policy assignment. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Parameters for the policy assignment. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created - Returns information about the new policy assignment. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyAssignmentsCreateById"></a>
# **policyAssignmentsCreateById**
> PolicyAssignment policyAssignmentsCreateById(policyAssignmentId, apiVersion, parameters)

Creates or updates a policy assignment.

This operation creates or updates the policy assignment with the given ID. Policy assignments made on a scope apply to all resources contained in that scope. For example, when you assign a policy to a resource group that policy applies to all resources in the group. Policy assignment IDs have this format: &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to create. Use the format '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    PolicyAssignment parameters = new PolicyAssignment(); // PolicyAssignment | Parameters for policy assignment.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsCreateById(policyAssignmentId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsCreateById");
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
| **policyAssignmentId** | **String**| The ID of the policy assignment to create. Use the format &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Parameters for policy assignment. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created - Returns information about the policy assignment. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyAssignmentsDelete"></a>
# **policyAssignmentsDelete**
> PolicyAssignment policyAssignmentsDelete(scope, policyAssignmentName, apiVersion)

Deletes a policy assignment.

This operation deletes a policy assignment, given its name and the scope it was created in. The scope of a policy assignment is the part of its ID preceding &#39;/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the policy assignment. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
    String policyAssignmentName = "policyAssignmentName_example"; // String | The name of the policy assignment to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsDelete(scope, policyAssignmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsDelete");
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
| **scope** | **String**| The scope of the policy assignment. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39; | |
| **policyAssignmentName** | **String**| The name of the policy assignment to delete. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deleted assignment. |  -  |
| **204** | No Content - the policy assignment doesn&#39;t exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyAssignmentsDeleteById"></a>
# **policyAssignmentsDeleteById**
> PolicyAssignment policyAssignmentsDeleteById(policyAssignmentId, apiVersion)

Deletes a policy assignment.

This operation deletes the policy with the given ID. Policy assignment IDs have this format: &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. Valid formats for {scope} are: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39; (management group), &#39;/subscriptions/{subscriptionId}&#39; (subscription), &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; (resource group), or &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39; (resource).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to delete. Use the format '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsDeleteById(policyAssignmentId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsDeleteById");
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
| **policyAssignmentId** | **String**| The ID of the policy assignment to delete. Use the format &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy assignment. |  -  |
| **204** | No Content - the policy assignment doesn&#39;t exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyAssignmentsGet"></a>
# **policyAssignmentsGet**
> PolicyAssignment policyAssignmentsGet(scope, policyAssignmentName, apiVersion)

Retrieves a policy assignment.

This operation retrieves a single policy assignment, given its name and the scope it was created at.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the policy assignment. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
    String policyAssignmentName = "policyAssignmentName_example"; // String | The name of the policy assignment to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsGet(scope, policyAssignmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsGet");
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
| **scope** | **String**| The scope of the policy assignment. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39; | |
| **policyAssignmentName** | **String**| The name of the policy assignment to get. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy assignment. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyAssignmentsGetById"></a>
# **policyAssignmentsGetById**
> PolicyAssignment policyAssignmentsGetById(policyAssignmentId, apiVersion)

Retrieves the policy assignment with the given ID.

The operation retrieves the policy assignment with the given ID. Policy assignment IDs have this format: &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to get. Use the format '{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}'.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      PolicyAssignment result = apiInstance.policyAssignmentsGetById(policyAssignmentId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsGetById");
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
| **policyAssignmentId** | **String**| The ID of the policy assignment to get. Use the format &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy assignment. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyAssignmentsList"></a>
# **policyAssignmentsList**
> PolicyAssignmentListResult policyAssignmentsList(apiVersion, subscriptionId, $filter)

Retrieves all policy assignments that apply to a subscription.

This operation retrieves the list of all policy assignments associated with the given subscription that match the optional given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, the unfiltered list includes all policy assignments associated with the subscription, including those that apply directly or from management groups that contain the given subscription, as well as any applied to objects contained within the subscription. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that apply to the subscription, which is everything in the unfiltered list except those applied to objects contained within the subscription. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Valid values for $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If $filter is not provided, no filtering is performed.
    try {
      PolicyAssignmentListResult result = apiInstance.policyAssignmentsList(apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsList");
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
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, no filtering is performed. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of policy assignments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyAssignmentsListForResource"></a>
# **policyAssignmentsListForResource**
> PolicyAssignmentListResult policyAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter)

Retrieves all policy assignments that apply to a resource.

This operation retrieves the list of all policy assignments associated with the specified resource in the given resource group and subscription that match the optional given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource, including those that apply directly or from all containing scopes, as well as any applied to resources contained within the resource. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that apply to the resource, which is everything in the unfiltered list except those applied to resources contained within the resource. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value} that apply to the resource. Three parameters plus the resource name are used to identify a specific resource. If the resource is not part of a parent resource (the more common case), the parent resource path should not be provided (or provided as &#39;&#39;). For example a web app could be specified as ({resourceProviderNamespace} &#x3D;&#x3D; &#39;Microsoft.Web&#39;, {parentResourcePath} &#x3D;&#x3D; &#39;&#39;, {resourceType} &#x3D;&#x3D; &#39;sites&#39;, {resourceName} &#x3D;&#x3D; &#39;MyWebApp&#39;). If the resource is part of a parent resource, then all parameters should be provided. For example a virtual machine DNS name could be specified as ({resourceProviderNamespace} &#x3D;&#x3D; &#39;Microsoft.Compute&#39;, {parentResourcePath} &#x3D;&#x3D; &#39;virtualMachines/MyVirtualMachine&#39;, {resourceType} &#x3D;&#x3D; &#39;domainNames&#39;, {resourceName} &#x3D;&#x3D; &#39;MyComputerName&#39;). A convenient alternative to providing the namespace and type name separately is to provide both in the {resourceType} parameter, format: ({resourceProviderNamespace} &#x3D;&#x3D; &#39;&#39;, {parentResourcePath} &#x3D;&#x3D; &#39;&#39;, {resourceType} &#x3D;&#x3D; &#39;Microsoft.Web/sites&#39;, {resourceName} &#x3D;&#x3D; &#39;MyWebApp&#39;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider. For example, the namespace of a virtual machine is Microsoft.Compute (from Microsoft.Compute/virtualMachines)
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource path. Use empty string if there is none.
    String resourceType = "resourceType_example"; // String | The resource type name. For example the type name of a web app is 'sites' (from Microsoft.Web/sites).
    String resourceName = "resourceName_example"; // String | The name of the resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Valid values for $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If $filter is not provided, no filtering is performed.
    try {
      PolicyAssignmentListResult result = apiInstance.policyAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsListForResource");
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
| **resourceGroupName** | **String**| The name of the resource group containing the resource. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. For example, the namespace of a virtual machine is Microsoft.Compute (from Microsoft.Compute/virtualMachines) | |
| **parentResourcePath** | **String**| The parent resource path. Use empty string if there is none. | |
| **resourceType** | **String**| The resource type name. For example the type name of a web app is &#39;sites&#39; (from Microsoft.Web/sites). | |
| **resourceName** | **String**| The name of the resource. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, no filtering is performed. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of policy assignments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyAssignmentsListForResourceGroup"></a>
# **policyAssignmentsListForResourceGroup**
> PolicyAssignmentListResult policyAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter)

Retrieves all policy assignments that apply to a resource group.

This operation retrieves the list of all policy assignments associated with the given resource group in the given subscription that match the optional given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource group, including those that apply directly or apply from containing scopes, as well as any applied to resources contained within the resource group. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that apply to the resource group, which is everything in the unfiltered list except those applied to resources contained within the resource group. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value} that apply to the resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicyAssignmentsApi apiInstance = new PolicyAssignmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains policy assignments.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Valid values for $filter are: 'atScope()' or 'policyDefinitionId eq '{value}''. If $filter is not provided, no filtering is performed.
    try {
      PolicyAssignmentListResult result = apiInstance.policyAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyAssignmentsApi#policyAssignmentsListForResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group that contains policy assignments. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, no filtering is performed. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of policy assignments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

