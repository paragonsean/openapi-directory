# DeploymentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deploymentsCalculateTemplateHash**](DeploymentsApi.md#deploymentsCalculateTemplateHash) | **POST** /providers/Microsoft.Resources/calculateTemplateHash |  |
| [**deploymentsCancel**](DeploymentsApi.md#deploymentsCancel) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment. |
| [**deploymentsCancelAtManagementGroupScope**](DeploymentsApi.md#deploymentsCancelAtManagementGroupScope) | **POST** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment. |
| [**deploymentsCancelAtScope**](DeploymentsApi.md#deploymentsCancelAtScope) | **POST** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment. |
| [**deploymentsCancelAtSubscriptionScope**](DeploymentsApi.md#deploymentsCancelAtSubscriptionScope) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment. |
| [**deploymentsCancelAtTenantScope**](DeploymentsApi.md#deploymentsCancelAtTenantScope) | **POST** /providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment. |
| [**deploymentsCheckExistence**](DeploymentsApi.md#deploymentsCheckExistence) | **HEAD** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsCheckExistenceAtManagementGroupScope**](DeploymentsApi.md#deploymentsCheckExistenceAtManagementGroupScope) | **HEAD** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsCheckExistenceAtScope**](DeploymentsApi.md#deploymentsCheckExistenceAtScope) | **HEAD** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsCheckExistenceAtSubscriptionScope**](DeploymentsApi.md#deploymentsCheckExistenceAtSubscriptionScope) | **HEAD** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsCheckExistenceAtTenantScope**](DeploymentsApi.md#deploymentsCheckExistenceAtTenantScope) | **HEAD** /providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsCreateOrUpdate**](DeploymentsApi.md#deploymentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources to a resource group. |
| [**deploymentsCreateOrUpdateAtManagementGroupScope**](DeploymentsApi.md#deploymentsCreateOrUpdateAtManagementGroupScope) | **PUT** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources at management group scope. |
| [**deploymentsCreateOrUpdateAtScope**](DeploymentsApi.md#deploymentsCreateOrUpdateAtScope) | **PUT** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources at a given scope. |
| [**deploymentsCreateOrUpdateAtSubscriptionScope**](DeploymentsApi.md#deploymentsCreateOrUpdateAtSubscriptionScope) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources at subscription scope. |
| [**deploymentsCreateOrUpdateAtTenantScope**](DeploymentsApi.md#deploymentsCreateOrUpdateAtTenantScope) | **PUT** /providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources at tenant scope. |
| [**deploymentsDelete**](DeploymentsApi.md#deploymentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history. |
| [**deploymentsDeleteAtManagementGroupScope**](DeploymentsApi.md#deploymentsDeleteAtManagementGroupScope) | **DELETE** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history. |
| [**deploymentsDeleteAtScope**](DeploymentsApi.md#deploymentsDeleteAtScope) | **DELETE** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history. |
| [**deploymentsDeleteAtSubscriptionScope**](DeploymentsApi.md#deploymentsDeleteAtSubscriptionScope) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history. |
| [**deploymentsDeleteAtTenantScope**](DeploymentsApi.md#deploymentsDeleteAtTenantScope) | **DELETE** /providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history. |
| [**deploymentsExportTemplate**](DeploymentsApi.md#deploymentsExportTemplate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate |  |
| [**deploymentsExportTemplateAtManagementGroupScope**](DeploymentsApi.md#deploymentsExportTemplateAtManagementGroupScope) | **POST** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate |  |
| [**deploymentsExportTemplateAtScope**](DeploymentsApi.md#deploymentsExportTemplateAtScope) | **POST** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate |  |
| [**deploymentsExportTemplateAtSubscriptionScope**](DeploymentsApi.md#deploymentsExportTemplateAtSubscriptionScope) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate |  |
| [**deploymentsExportTemplateAtTenantScope**](DeploymentsApi.md#deploymentsExportTemplateAtTenantScope) | **POST** /providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate |  |
| [**deploymentsGet**](DeploymentsApi.md#deploymentsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsGetAtManagementGroupScope**](DeploymentsApi.md#deploymentsGetAtManagementGroupScope) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsGetAtScope**](DeploymentsApi.md#deploymentsGetAtScope) | **GET** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsGetAtSubscriptionScope**](DeploymentsApi.md#deploymentsGetAtSubscriptionScope) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsGetAtTenantScope**](DeploymentsApi.md#deploymentsGetAtTenantScope) | **GET** /providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsListAtManagementGroupScope**](DeploymentsApi.md#deploymentsListAtManagementGroupScope) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/ |  |
| [**deploymentsListAtScope**](DeploymentsApi.md#deploymentsListAtScope) | **GET** /{scope}/providers/Microsoft.Resources/deployments/ |  |
| [**deploymentsListAtSubscriptionScope**](DeploymentsApi.md#deploymentsListAtSubscriptionScope) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/ |  |
| [**deploymentsListAtTenantScope**](DeploymentsApi.md#deploymentsListAtTenantScope) | **GET** /providers/Microsoft.Resources/deployments/ |  |
| [**deploymentsListByResourceGroup**](DeploymentsApi.md#deploymentsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/ |  |
| [**deploymentsValidate**](DeploymentsApi.md#deploymentsValidate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/validate |  |
| [**deploymentsValidateAtManagementGroupScope**](DeploymentsApi.md#deploymentsValidateAtManagementGroupScope) | **POST** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/validate |  |
| [**deploymentsValidateAtScope**](DeploymentsApi.md#deploymentsValidateAtScope) | **POST** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName}/validate |  |
| [**deploymentsValidateAtSubscriptionScope**](DeploymentsApi.md#deploymentsValidateAtSubscriptionScope) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/validate |  |
| [**deploymentsValidateAtTenantScope**](DeploymentsApi.md#deploymentsValidateAtTenantScope) | **POST** /providers/Microsoft.Resources/deployments/{deploymentName}/validate |  |
| [**deploymentsWhatIf**](DeploymentsApi.md#deploymentsWhatIf) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/whatIf |  |
| [**deploymentsWhatIfAtSubscriptionScope**](DeploymentsApi.md#deploymentsWhatIfAtSubscriptionScope) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/whatIf |  |


<a id="deploymentsCalculateTemplateHash"></a>
# **deploymentsCalculateTemplateHash**
> TemplateHashResult deploymentsCalculateTemplateHash(apiVersion, template)



Calculate the hash of the given template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Object template = null; // Object | The template provided to calculate hash.
    try {
      TemplateHashResult result = apiInstance.deploymentsCalculateTemplateHash(apiVersion, template);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCalculateTemplateHash");
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
| **template** | **Object**| The template provided to calculate hash. | |

### Return type

[**TemplateHashResult**](TemplateHashResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the hash. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCancel"></a>
# **deploymentsCancel**
> deploymentsCancel(resourceGroupName, deploymentName, apiVersion, subscriptionId)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resource group partially deployed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.deploymentsCancel(resourceGroupName, deploymentName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCancel");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCancelAtManagementGroupScope"></a>
# **deploymentsCancelAtManagementGroupScope**
> deploymentsCancelAtManagementGroupScope(groupId, deploymentName, apiVersion)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.deploymentsCancelAtManagementGroupScope(groupId, deploymentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCancelAtManagementGroupScope");
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
| **groupId** | **String**| The management group ID. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCancelAtScope"></a>
# **deploymentsCancelAtScope**
> deploymentsCancelAtScope(scope, deploymentName, apiVersion)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of a deployment.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.deploymentsCancelAtScope(scope, deploymentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCancelAtScope");
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
| **scope** | **String**| The scope of a deployment. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCancelAtSubscriptionScope"></a>
# **deploymentsCancelAtSubscriptionScope**
> deploymentsCancelAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.deploymentsCancelAtSubscriptionScope(deploymentName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCancelAtSubscriptionScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCancelAtTenantScope"></a>
# **deploymentsCancelAtTenantScope**
> deploymentsCancelAtTenantScope(deploymentName, apiVersion)

Cancels a currently running template deployment.

You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.deploymentsCancelAtTenantScope(deploymentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCancelAtTenantScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCheckExistence"></a>
# **deploymentsCheckExistence**
> deploymentsCheckExistence(resourceGroupName, deploymentName, apiVersion, subscriptionId)



Checks whether the deployment exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group with the deployment to check. The name is case insensitive.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.deploymentsCheckExistence(resourceGroupName, deploymentName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCheckExistence");
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
| **resourceGroupName** | **String**| The name of the resource group with the deployment to check. The name is case insensitive. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCheckExistenceAtManagementGroupScope"></a>
# **deploymentsCheckExistenceAtManagementGroupScope**
> deploymentsCheckExistenceAtManagementGroupScope(groupId, deploymentName, apiVersion)



Checks whether the deployment exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.deploymentsCheckExistenceAtManagementGroupScope(groupId, deploymentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCheckExistenceAtManagementGroupScope");
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
| **groupId** | **String**| The management group ID. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCheckExistenceAtScope"></a>
# **deploymentsCheckExistenceAtScope**
> deploymentsCheckExistenceAtScope(scope, deploymentName, apiVersion)



Checks whether the deployment exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of a deployment.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.deploymentsCheckExistenceAtScope(scope, deploymentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCheckExistenceAtScope");
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
| **scope** | **String**| The scope of a deployment. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCheckExistenceAtSubscriptionScope"></a>
# **deploymentsCheckExistenceAtSubscriptionScope**
> deploymentsCheckExistenceAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)



Checks whether the deployment exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.deploymentsCheckExistenceAtSubscriptionScope(deploymentName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCheckExistenceAtSubscriptionScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCheckExistenceAtTenantScope"></a>
# **deploymentsCheckExistenceAtTenantScope**
> deploymentsCheckExistenceAtTenantScope(deploymentName, apiVersion)



Checks whether the deployment exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.deploymentsCheckExistenceAtTenantScope(deploymentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCheckExistenceAtTenantScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCreateOrUpdate"></a>
# **deploymentsCreateOrUpdate**
> DeploymentExtended deploymentsCreateOrUpdate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters)

Deploys resources to a resource group.

You can provide the template and parameters directly in the request or link to JSON files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to deploy the resources to. The name is case insensitive. The resource group must already exist.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Deployment parameters = new Deployment(); // Deployment | Additional parameters supplied to the operation.
    try {
      DeploymentExtended result = apiInstance.deploymentsCreateOrUpdate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group to deploy the resources to. The name is case insensitive. The resource group must already exist. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**Deployment**](Deployment.md)| Additional parameters supplied to the operation. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **201** | Created - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCreateOrUpdateAtManagementGroupScope"></a>
# **deploymentsCreateOrUpdateAtManagementGroupScope**
> DeploymentExtended deploymentsCreateOrUpdateAtManagementGroupScope(groupId, deploymentName, apiVersion, parameters)

Deploys resources at management group scope.

You can provide the template and parameters directly in the request or link to JSON files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    ScopedDeployment parameters = new ScopedDeployment(); // ScopedDeployment | Additional parameters supplied to the operation.
    try {
      DeploymentExtended result = apiInstance.deploymentsCreateOrUpdateAtManagementGroupScope(groupId, deploymentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCreateOrUpdateAtManagementGroupScope");
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
| **groupId** | **String**| The management group ID. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**ScopedDeployment**](ScopedDeployment.md)| Additional parameters supplied to the operation. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **201** | Created - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCreateOrUpdateAtScope"></a>
# **deploymentsCreateOrUpdateAtScope**
> DeploymentExtended deploymentsCreateOrUpdateAtScope(scope, deploymentName, apiVersion, parameters)

Deploys resources at a given scope.

You can provide the template and parameters directly in the request or link to JSON files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of a deployment.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Deployment parameters = new Deployment(); // Deployment | Additional parameters supplied to the operation.
    try {
      DeploymentExtended result = apiInstance.deploymentsCreateOrUpdateAtScope(scope, deploymentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCreateOrUpdateAtScope");
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
| **scope** | **String**| The scope of a deployment. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**Deployment**](Deployment.md)| Additional parameters supplied to the operation. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **201** | Created - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCreateOrUpdateAtSubscriptionScope"></a>
# **deploymentsCreateOrUpdateAtSubscriptionScope**
> DeploymentExtended deploymentsCreateOrUpdateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters)

Deploys resources at subscription scope.

You can provide the template and parameters directly in the request or link to JSON files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Deployment parameters = new Deployment(); // Deployment | Additional parameters supplied to the operation.
    try {
      DeploymentExtended result = apiInstance.deploymentsCreateOrUpdateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCreateOrUpdateAtSubscriptionScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**Deployment**](Deployment.md)| Additional parameters supplied to the operation. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **201** | Created - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsCreateOrUpdateAtTenantScope"></a>
# **deploymentsCreateOrUpdateAtTenantScope**
> DeploymentExtended deploymentsCreateOrUpdateAtTenantScope(deploymentName, apiVersion, parameters)

Deploys resources at tenant scope.

You can provide the template and parameters directly in the request or link to JSON files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    ScopedDeployment parameters = new ScopedDeployment(); // ScopedDeployment | Additional parameters supplied to the operation.
    try {
      DeploymentExtended result = apiInstance.deploymentsCreateOrUpdateAtTenantScope(deploymentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCreateOrUpdateAtTenantScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**ScopedDeployment**](ScopedDeployment.md)| Additional parameters supplied to the operation. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **201** | Created - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsDelete"></a>
# **deploymentsDelete**
> deploymentsDelete(resourceGroupName, deploymentName, apiVersion, subscriptionId)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group with the deployment to delete. The name is case insensitive.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.deploymentsDelete(resourceGroupName, deploymentName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group with the deployment to delete. The name is case insensitive. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **202** | Accepted - Returns this status until the asynchronous operation has completed. |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsDeleteAtManagementGroupScope"></a>
# **deploymentsDeleteAtManagementGroupScope**
> deploymentsDeleteAtManagementGroupScope(groupId, deploymentName, apiVersion)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.deploymentsDeleteAtManagementGroupScope(groupId, deploymentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsDeleteAtManagementGroupScope");
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
| **groupId** | **String**| The management group ID. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **202** | Accepted - Returns this status until the asynchronous operation has completed. |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsDeleteAtScope"></a>
# **deploymentsDeleteAtScope**
> deploymentsDeleteAtScope(scope, deploymentName, apiVersion)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of a deployment.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.deploymentsDeleteAtScope(scope, deploymentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsDeleteAtScope");
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
| **scope** | **String**| The scope of a deployment. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **202** | Accepted - Returns this status until the asynchronous operation has completed. |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsDeleteAtSubscriptionScope"></a>
# **deploymentsDeleteAtSubscriptionScope**
> deploymentsDeleteAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.deploymentsDeleteAtSubscriptionScope(deploymentName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsDeleteAtSubscriptionScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **202** | Accepted - Returns this status until the asynchronous operation has completed. |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsDeleteAtTenantScope"></a>
# **deploymentsDeleteAtTenantScope**
> deploymentsDeleteAtTenantScope(deploymentName, apiVersion)

Deletes a deployment from the deployment history.

A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.deploymentsDeleteAtTenantScope(deploymentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsDeleteAtTenantScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **202** | Accepted - Returns this status until the asynchronous operation has completed. |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsExportTemplate"></a>
# **deploymentsExportTemplate**
> DeploymentExportResult deploymentsExportTemplate(resourceGroupName, deploymentName, apiVersion, subscriptionId)



Exports the template used for specified deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      DeploymentExportResult result = apiInstance.deploymentsExportTemplate(resourceGroupName, deploymentName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsExportTemplate");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the template. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsExportTemplateAtManagementGroupScope"></a>
# **deploymentsExportTemplateAtManagementGroupScope**
> DeploymentExportResult deploymentsExportTemplateAtManagementGroupScope(groupId, deploymentName, apiVersion)



Exports the template used for specified deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DeploymentExportResult result = apiInstance.deploymentsExportTemplateAtManagementGroupScope(groupId, deploymentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsExportTemplateAtManagementGroupScope");
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
| **groupId** | **String**| The management group ID. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the template. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsExportTemplateAtScope"></a>
# **deploymentsExportTemplateAtScope**
> DeploymentExportResult deploymentsExportTemplateAtScope(scope, deploymentName, apiVersion)



Exports the template used for specified deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of a deployment.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DeploymentExportResult result = apiInstance.deploymentsExportTemplateAtScope(scope, deploymentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsExportTemplateAtScope");
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
| **scope** | **String**| The scope of a deployment. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the template. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsExportTemplateAtSubscriptionScope"></a>
# **deploymentsExportTemplateAtSubscriptionScope**
> DeploymentExportResult deploymentsExportTemplateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)



Exports the template used for specified deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      DeploymentExportResult result = apiInstance.deploymentsExportTemplateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsExportTemplateAtSubscriptionScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the template. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsExportTemplateAtTenantScope"></a>
# **deploymentsExportTemplateAtTenantScope**
> DeploymentExportResult deploymentsExportTemplateAtTenantScope(deploymentName, apiVersion)



Exports the template used for specified deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DeploymentExportResult result = apiInstance.deploymentsExportTemplateAtTenantScope(deploymentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsExportTemplateAtTenantScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DeploymentExportResult**](DeploymentExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the template. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsGet"></a>
# **deploymentsGet**
> DeploymentExtended deploymentsGet(resourceGroupName, deploymentName, apiVersion, subscriptionId)



Gets a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      DeploymentExtended result = apiInstance.deploymentsGet(resourceGroupName, deploymentName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsGet");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsGetAtManagementGroupScope"></a>
# **deploymentsGetAtManagementGroupScope**
> DeploymentExtended deploymentsGetAtManagementGroupScope(groupId, deploymentName, apiVersion)



Gets a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DeploymentExtended result = apiInstance.deploymentsGetAtManagementGroupScope(groupId, deploymentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsGetAtManagementGroupScope");
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
| **groupId** | **String**| The management group ID. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsGetAtScope"></a>
# **deploymentsGetAtScope**
> DeploymentExtended deploymentsGetAtScope(scope, deploymentName, apiVersion)



Gets a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of a deployment.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DeploymentExtended result = apiInstance.deploymentsGetAtScope(scope, deploymentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsGetAtScope");
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
| **scope** | **String**| The scope of a deployment. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsGetAtSubscriptionScope"></a>
# **deploymentsGetAtSubscriptionScope**
> DeploymentExtended deploymentsGetAtSubscriptionScope(deploymentName, apiVersion, subscriptionId)



Gets a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      DeploymentExtended result = apiInstance.deploymentsGetAtSubscriptionScope(deploymentName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsGetAtSubscriptionScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsGetAtTenantScope"></a>
# **deploymentsGetAtTenantScope**
> DeploymentExtended deploymentsGetAtTenantScope(deploymentName, apiVersion)



Gets a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DeploymentExtended result = apiInstance.deploymentsGetAtTenantScope(deploymentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsGetAtTenantScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DeploymentExtended**](DeploymentExtended.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsListAtManagementGroupScope"></a>
# **deploymentsListAtManagementGroupScope**
> DeploymentListResult deploymentsListAtManagementGroupScope(groupId, apiVersion, $filter, $top)



Get all the deployments for a management group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
    Integer $top = 56; // Integer | The number of results to get. If null is passed, returns all deployments.
    try {
      DeploymentListResult result = apiInstance.deploymentsListAtManagementGroupScope(groupId, apiVersion, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsListAtManagementGroupScope");
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
| **groupId** | **String**| The management group ID. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] |
| **$top** | **Integer**| The number of results to get. If null is passed, returns all deployments. | [optional] |

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of deployments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsListAtScope"></a>
# **deploymentsListAtScope**
> DeploymentListResult deploymentsListAtScope(scope, apiVersion, $filter, $top)



Get all the deployments at the given scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of a deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
    Integer $top = 56; // Integer | The number of results to get. If null is passed, returns all deployments.
    try {
      DeploymentListResult result = apiInstance.deploymentsListAtScope(scope, apiVersion, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsListAtScope");
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
| **scope** | **String**| The scope of a deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] |
| **$top** | **Integer**| The number of results to get. If null is passed, returns all deployments. | [optional] |

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of deployments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsListAtSubscriptionScope"></a>
# **deploymentsListAtSubscriptionScope**
> DeploymentListResult deploymentsListAtSubscriptionScope(apiVersion, subscriptionId, $filter, $top)



Get all the deployments for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
    Integer $top = 56; // Integer | The number of results to get. If null is passed, returns all deployments.
    try {
      DeploymentListResult result = apiInstance.deploymentsListAtSubscriptionScope(apiVersion, subscriptionId, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsListAtSubscriptionScope");
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
| **$filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] |
| **$top** | **Integer**| The number of results to get. If null is passed, returns all deployments. | [optional] |

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of deployments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsListAtTenantScope"></a>
# **deploymentsListAtTenantScope**
> DeploymentListResult deploymentsListAtTenantScope(apiVersion, $filter, $top)



Get all the deployments at the tenant scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
    Integer $top = 56; // Integer | The number of results to get. If null is passed, returns all deployments.
    try {
      DeploymentListResult result = apiInstance.deploymentsListAtTenantScope(apiVersion, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsListAtTenantScope");
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
| **$filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] |
| **$top** | **Integer**| The number of results to get. If null is passed, returns all deployments. | [optional] |

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of deployments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsListByResourceGroup"></a>
# **deploymentsListByResourceGroup**
> DeploymentListResult deploymentsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter, $top)



Get all the deployments for a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group with the deployments to get. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For example, you can use $filter=provisioningState eq '{state}'.
    Integer $top = 56; // Integer | The number of results to get. If null is passed, returns all deployments.
    try {
      DeploymentListResult result = apiInstance.deploymentsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group with the deployments to get. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. For example, you can use $filter&#x3D;provisioningState eq &#39;{state}&#39;. | [optional] |
| **$top** | **Integer**| The number of results to get. If null is passed, returns all deployments. | [optional] |

### Return type

[**DeploymentListResult**](DeploymentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of deployments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsValidate"></a>
# **deploymentsValidate**
> DeploymentValidateResult deploymentsValidate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group the template will be deployed to. The name is case insensitive.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Deployment parameters = new Deployment(); // Deployment | Parameters to validate.
    try {
      DeploymentValidateResult result = apiInstance.deploymentsValidate(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsValidate");
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
| **resourceGroupName** | **String**| The name of the resource group the template will be deployed to. The name is case insensitive. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**Deployment**](Deployment.md)| Parameters to validate. | |

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the validation result. |  -  |
| **400** | Returns the validation result. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsValidateAtManagementGroupScope"></a>
# **deploymentsValidateAtManagementGroupScope**
> DeploymentValidateResult deploymentsValidateAtManagementGroupScope(groupId, deploymentName, apiVersion, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    ScopedDeployment parameters = new ScopedDeployment(); // ScopedDeployment | Parameters to validate.
    try {
      DeploymentValidateResult result = apiInstance.deploymentsValidateAtManagementGroupScope(groupId, deploymentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsValidateAtManagementGroupScope");
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
| **groupId** | **String**| The management group ID. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**ScopedDeployment**](ScopedDeployment.md)| Parameters to validate. | |

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the validation result. |  -  |
| **400** | Returns the validation result. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsValidateAtScope"></a>
# **deploymentsValidateAtScope**
> DeploymentValidateResult deploymentsValidateAtScope(scope, deploymentName, apiVersion, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of a deployment.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Deployment parameters = new Deployment(); // Deployment | Parameters to validate.
    try {
      DeploymentValidateResult result = apiInstance.deploymentsValidateAtScope(scope, deploymentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsValidateAtScope");
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
| **scope** | **String**| The scope of a deployment. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**Deployment**](Deployment.md)| Parameters to validate. | |

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the validation result. |  -  |
| **400** | Returns the validation result. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsValidateAtSubscriptionScope"></a>
# **deploymentsValidateAtSubscriptionScope**
> DeploymentValidateResult deploymentsValidateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Deployment parameters = new Deployment(); // Deployment | Parameters to validate.
    try {
      DeploymentValidateResult result = apiInstance.deploymentsValidateAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsValidateAtSubscriptionScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**Deployment**](Deployment.md)| Parameters to validate. | |

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the validation result. |  -  |
| **400** | Returns the validation result. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsValidateAtTenantScope"></a>
# **deploymentsValidateAtTenantScope**
> DeploymentValidateResult deploymentsValidateAtTenantScope(deploymentName, apiVersion, parameters)



Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager..

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    ScopedDeployment parameters = new ScopedDeployment(); // ScopedDeployment | Parameters to validate.
    try {
      DeploymentValidateResult result = apiInstance.deploymentsValidateAtTenantScope(deploymentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsValidateAtTenantScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**ScopedDeployment**](ScopedDeployment.md)| Parameters to validate. | |

### Return type

[**DeploymentValidateResult**](DeploymentValidateResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the validation result. |  -  |
| **400** | Returns the validation result. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsWhatIf"></a>
# **deploymentsWhatIf**
> WhatIfOperationResult deploymentsWhatIf(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters)



Returns changes that will be made by the deployment if executed at the scope of the resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group the template will be deployed to. The name is case insensitive.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    DeploymentWhatIf parameters = new DeploymentWhatIf(); // DeploymentWhatIf | Parameters to validate.
    try {
      WhatIfOperationResult result = apiInstance.deploymentsWhatIf(resourceGroupName, deploymentName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsWhatIf");
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
| **resourceGroupName** | **String**| The name of the resource group the template will be deployed to. The name is case insensitive. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**DeploymentWhatIf**](DeploymentWhatIf.md)| Parameters to validate. | |

### Return type

[**WhatIfOperationResult**](WhatIfOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns What-If operation status |  -  |
| **202** | Accepted - Returns URL in Location header to query for long-running operation status. |  * Retry-After - Number of seconds to wait before polling for status. <br>  * Location - URL to get status of this long-running operation. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentsWhatIfAtSubscriptionScope"></a>
# **deploymentsWhatIfAtSubscriptionScope**
> WhatIfOperationResult deploymentsWhatIfAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters)



Returns changes that will be made by the deployment if executed at the scope of the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    DeploymentWhatIf parameters = new DeploymentWhatIf(); // DeploymentWhatIf | Parameters to What If.
    try {
      WhatIfOperationResult result = apiInstance.deploymentsWhatIfAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsWhatIfAtSubscriptionScope");
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
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**DeploymentWhatIf**](DeploymentWhatIf.md)| Parameters to What If. | |

### Return type

[**WhatIfOperationResult**](WhatIfOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns What-If operation status |  -  |
| **202** | Accepted - Returns URL in Location header to query for long-running operation status. |  * Retry-After - Number of seconds to wait before polling for status. <br>  * Location - URL to get status of this long-running operation. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

