# PolicyAssignmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policyAssignmentsCreate**](PolicyAssignmentsApi.md#policyAssignmentsCreate) | **PUT** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} | Creates a policy assignment. |
| [**policyAssignmentsCreateById**](PolicyAssignmentsApi.md#policyAssignmentsCreateById) | **PUT** /{policyAssignmentId} | Creates a policy assignment by ID. |
| [**policyAssignmentsDelete**](PolicyAssignmentsApi.md#policyAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} |  |
| [**policyAssignmentsDeleteById**](PolicyAssignmentsApi.md#policyAssignmentsDeleteById) | **DELETE** /{policyAssignmentId} | Deletes a policy assignment by ID. |
| [**policyAssignmentsGet**](PolicyAssignmentsApi.md#policyAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName} |  |
| [**policyAssignmentsGetById**](PolicyAssignmentsApi.md#policyAssignmentsGetById) | **GET** /{policyAssignmentId} | Gets a policy assignment by ID. |
| [**policyAssignmentsList**](PolicyAssignmentsApi.md#policyAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments |  |
| [**policyAssignmentsListForResource**](PolicyAssignmentsApi.md#policyAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/policyAssignments |  |
| [**policyAssignmentsListForResourceGroup**](PolicyAssignmentsApi.md#policyAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyAssignments |  |


<a id="policyAssignmentsCreate"></a>
# **policyAssignmentsCreate**
> PolicyAssignment policyAssignmentsCreate(scope, policyAssignmentName, apiVersion, parameters)

Creates a policy assignment.

Policy assignments are inherited by child resources. For example, when you apply a policy to a resource group that policy is assigned to all resources in the group.

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
    String scope = "scope_example"; // String | The scope of the policy assignment.
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
| **scope** | **String**| The scope of the policy assignment. | |
| **policyAssignmentName** | **String**| The name of the policy assignment. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Parameters for the policy assignment. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created - Returns information about the new policy assignment. |  -  |

<a id="policyAssignmentsCreateById"></a>
# **policyAssignmentsCreateById**
> PolicyAssignment policyAssignmentsCreateById(policyAssignmentId, apiVersion, parameters)

Creates a policy assignment by ID.

Policy assignments are inherited by child resources. For example, when you apply a policy to a resource group that policy is assigned to all resources in the group. When providing a scope for the assignment, use &#39;/subscriptions/{subscription-id}/&#39; for subscriptions, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for resource groups, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}&#39; for resources.

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
    String policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to create. Use the format '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
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
| **policyAssignmentId** | **String**| The ID of the policy assignment to create. Use the format &#39;/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}&#39;. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **parameters** | [**PolicyAssignment**](PolicyAssignment.md)| Parameters for policy assignment. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created - Returns information about the policy assignment. |  -  |

<a id="policyAssignmentsDelete"></a>
# **policyAssignmentsDelete**
> PolicyAssignment policyAssignmentsDelete(scope, policyAssignmentName, apiVersion)



Deletes a policy assignment.

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
    String scope = "scope_example"; // String | The scope of the policy assignment.
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
| **scope** | **String**| The scope of the policy assignment. | |
| **policyAssignmentName** | **String**| The name of the policy assignment to delete. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deleted assignment. |  -  |
| **204** | No Content |  -  |

<a id="policyAssignmentsDeleteById"></a>
# **policyAssignmentsDeleteById**
> PolicyAssignment policyAssignmentsDeleteById(policyAssignmentId, apiVersion)

Deletes a policy assignment by ID.

When providing a scope for the assignment, use &#39;/subscriptions/{subscription-id}/&#39; for subscriptions, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for resource groups, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}&#39; for resources.

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
    String policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to delete. Use the format '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
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
| **policyAssignmentId** | **String**| The ID of the policy assignment to delete. Use the format &#39;/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}&#39;. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy assignment. |  -  |

<a id="policyAssignmentsGet"></a>
# **policyAssignmentsGet**
> PolicyAssignment policyAssignmentsGet(scope, policyAssignmentName, apiVersion)



Gets a policy assignment.

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
    String scope = "scope_example"; // String | The scope of the policy assignment.
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
| **scope** | **String**| The scope of the policy assignment. | |
| **policyAssignmentName** | **String**| The name of the policy assignment to get. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy assignment. |  -  |

<a id="policyAssignmentsGetById"></a>
# **policyAssignmentsGetById**
> PolicyAssignment policyAssignmentsGetById(policyAssignmentId, apiVersion)

Gets a policy assignment by ID.

When providing a scope for the assignment, use &#39;/subscriptions/{subscription-id}/&#39; for subscriptions, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for resource groups, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}&#39; for resources.

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
    String policyAssignmentId = "policyAssignmentId_example"; // String | The ID of the policy assignment to get. Use the format '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
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
| **policyAssignmentId** | **String**| The ID of the policy assignment to get. Use the format &#39;/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}&#39;. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the policy assignment. |  -  |

<a id="policyAssignmentsList"></a>
# **policyAssignmentsList**
> PolicyAssignmentListResult policyAssignmentsList(apiVersion, subscriptionId, $filter)



Gets all the policy assignments for a subscription.

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
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
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
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of policy assignments. |  -  |

<a id="policyAssignmentsListForResource"></a>
# **policyAssignmentsListForResource**
> PolicyAssignmentListResult policyAssignmentsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter)



Gets policy assignments for a resource.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource. The name is case insensitive.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource path.
    String resourceType = "resourceType_example"; // String | The resource type.
    String resourceName = "resourceName_example"; // String | The name of the resource with policy assignments.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
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
| **resourceGroupName** | **String**| The name of the resource group containing the resource. The name is case insensitive. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource path. | |
| **resourceType** | **String**| The resource type. | |
| **resourceName** | **String**| The name of the resource with policy assignments. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of policy assignments. |  -  |

<a id="policyAssignmentsListForResourceGroup"></a>
# **policyAssignmentsListForResourceGroup**
> PolicyAssignmentListResult policyAssignmentsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter)



Gets policy assignments for the resource group.

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
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
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
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**PolicyAssignmentListResult**](PolicyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of policy assignments. |  -  |

