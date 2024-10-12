# DenyAssignmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**denyAssignmentsGet**](DenyAssignmentsApi.md#denyAssignmentsGet) | **GET** /{scope}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} |  |
| [**denyAssignmentsGetById**](DenyAssignmentsApi.md#denyAssignmentsGetById) | **GET** /{denyAssignmentId} |  |
| [**denyAssignmentsList**](DenyAssignmentsApi.md#denyAssignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/denyAssignments |  |
| [**denyAssignmentsListForResource**](DenyAssignmentsApi.md#denyAssignmentsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/denyAssignments |  |
| [**denyAssignmentsListForResourceGroup**](DenyAssignmentsApi.md#denyAssignmentsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/denyAssignments |  |
| [**denyAssignmentsListForScope**](DenyAssignmentsApi.md#denyAssignmentsListForScope) | **GET** /{scope}/providers/Microsoft.Authorization/denyAssignments |  |


<a id="denyAssignmentsGet"></a>
# **denyAssignmentsGet**
> DenyAssignment denyAssignmentsGet(scope, denyAssignmentId, apiVersion)



Get the specified deny assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DenyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DenyAssignmentsApi apiInstance = new DenyAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the deny assignment.
    String denyAssignmentId = "denyAssignmentId_example"; // String | The ID of the deny assignment to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DenyAssignment result = apiInstance.denyAssignmentsGet(scope, denyAssignmentId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DenyAssignmentsApi#denyAssignmentsGet");
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
| **scope** | **String**| The scope of the deny assignment. | |
| **denyAssignmentId** | **String**| The ID of the deny assignment to get. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DenyAssignment**](DenyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deny assignment. |  -  |

<a id="denyAssignmentsGetById"></a>
# **denyAssignmentsGetById**
> DenyAssignment denyAssignmentsGetById(denyAssignmentId, apiVersion)



Gets a deny assignment by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DenyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DenyAssignmentsApi apiInstance = new DenyAssignmentsApi(defaultClient);
    String denyAssignmentId = "denyAssignmentId_example"; // String | The fully qualified deny assignment ID. For example, use the format, /subscriptions/{guid}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for subscription level deny assignments, or /providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for tenant level deny assignments.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DenyAssignment result = apiInstance.denyAssignmentsGetById(denyAssignmentId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DenyAssignmentsApi#denyAssignmentsGetById");
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
| **denyAssignmentId** | **String**| The fully qualified deny assignment ID. For example, use the format, /subscriptions/{guid}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for subscription level deny assignments, or /providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for tenant level deny assignments. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DenyAssignment**](DenyAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the deny assignment. |  -  |

<a id="denyAssignmentsList"></a>
# **denyAssignmentsList**
> DenyAssignmentListResult denyAssignmentsList(subscriptionId, apiVersion, $filter)



Gets all deny assignments for the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DenyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DenyAssignmentsApi apiInstance = new DenyAssignmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Use $filter=atScope() to return all deny assignments at or above the scope. Use $filter=denyAssignmentName eq '{name}' to search deny assignments by name at specified scope. Use $filter=principalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. Use $filter=gdprExportPrincipalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
    try {
      DenyAssignmentListResult result = apiInstance.denyAssignmentsList(subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DenyAssignmentsApi#denyAssignmentsList");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned. | [optional] |

### Return type

[**DenyAssignmentListResult**](DenyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of deny assignments. |  -  |

<a id="denyAssignmentsListForResource"></a>
# **denyAssignmentsListForResource**
> DenyAssignmentListResult denyAssignmentsListForResource(subscriptionId, resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, $filter)



Gets deny assignments for a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DenyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DenyAssignmentsApi apiInstance = new DenyAssignmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type of the resource.
    String resourceName = "resourceName_example"; // String | The name of the resource to get deny assignments for.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Use $filter=atScope() to return all deny assignments at or above the scope. Use $filter=denyAssignmentName eq '{name}' to search deny assignments by name at specified scope. Use $filter=principalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. Use $filter=gdprExportPrincipalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
    try {
      DenyAssignmentListResult result = apiInstance.denyAssignmentsListForResource(subscriptionId, resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DenyAssignmentsApi#denyAssignmentsListForResource");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type of the resource. | |
| **resourceName** | **String**| The name of the resource to get deny assignments for. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned. | [optional] |

### Return type

[**DenyAssignmentListResult**](DenyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of deny assignments. |  -  |

<a id="denyAssignmentsListForResourceGroup"></a>
# **denyAssignmentsListForResourceGroup**
> DenyAssignmentListResult denyAssignmentsListForResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter)



Gets deny assignments for a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DenyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DenyAssignmentsApi apiInstance = new DenyAssignmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Use $filter=atScope() to return all deny assignments at or above the scope. Use $filter=denyAssignmentName eq '{name}' to search deny assignments by name at specified scope. Use $filter=principalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. Use $filter=gdprExportPrincipalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
    try {
      DenyAssignmentListResult result = apiInstance.denyAssignmentsListForResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DenyAssignmentsApi#denyAssignmentsListForResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned. | [optional] |

### Return type

[**DenyAssignmentListResult**](DenyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of deny assignments. |  -  |

<a id="denyAssignmentsListForScope"></a>
# **denyAssignmentsListForScope**
> DenyAssignmentListResult denyAssignmentsListForScope(scope, apiVersion, $filter)



Gets deny assignments for a scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DenyAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DenyAssignmentsApi apiInstance = new DenyAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the deny assignments.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Use $filter=atScope() to return all deny assignments at or above the scope. Use $filter=denyAssignmentName eq '{name}' to search deny assignments by name at specified scope. Use $filter=principalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. Use $filter=gdprExportPrincipalId eq '{id}' to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
    try {
      DenyAssignmentListResult result = apiInstance.denyAssignmentsListForScope(scope, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DenyAssignmentsApi#denyAssignmentsListForScope");
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
| **scope** | **String**| The scope of the deny assignments. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$filter** | **String**| The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned. | [optional] |

### Return type

[**DenyAssignmentListResult**](DenyAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of deny assignments. |  -  |

