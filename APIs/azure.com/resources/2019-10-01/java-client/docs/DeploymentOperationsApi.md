# DeploymentOperationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deploymentOperationsGet**](DeploymentOperationsApi.md#deploymentOperationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations/{operationId} |  |
| [**deploymentOperationsGetAtManagementGroupScope**](DeploymentOperationsApi.md#deploymentOperationsGetAtManagementGroupScope) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId} |  |
| [**deploymentOperationsGetAtScope**](DeploymentOperationsApi.md#deploymentOperationsGetAtScope) | **GET** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId} |  |
| [**deploymentOperationsGetAtSubscriptionScope**](DeploymentOperationsApi.md#deploymentOperationsGetAtSubscriptionScope) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId} |  |
| [**deploymentOperationsGetAtTenantScope**](DeploymentOperationsApi.md#deploymentOperationsGetAtTenantScope) | **GET** /providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId} |  |
| [**deploymentOperationsList**](DeploymentOperationsApi.md#deploymentOperationsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations |  |
| [**deploymentOperationsListAtManagementGroupScope**](DeploymentOperationsApi.md#deploymentOperationsListAtManagementGroupScope) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations |  |
| [**deploymentOperationsListAtScope**](DeploymentOperationsApi.md#deploymentOperationsListAtScope) | **GET** /{scope}/providers/Microsoft.Resources/deployments/{deploymentName}/operations |  |
| [**deploymentOperationsListAtSubscriptionScope**](DeploymentOperationsApi.md#deploymentOperationsListAtSubscriptionScope) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations |  |
| [**deploymentOperationsListAtTenantScope**](DeploymentOperationsApi.md#deploymentOperationsListAtTenantScope) | **GET** /providers/Microsoft.Resources/deployments/{deploymentName}/operations |  |


<a id="deploymentOperationsGet"></a>
# **deploymentOperationsGet**
> DeploymentOperation deploymentOperationsGet(resourceGroupName, deploymentName, operationId, apiVersion, subscriptionId)



Gets a deployments operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String operationId = "operationId_example"; // String | The ID of the operation to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      DeploymentOperation result = apiInstance.deploymentOperationsGet(resourceGroupName, deploymentName, operationId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsGet");
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
| **operationId** | **String**| The ID of the operation to get. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**DeploymentOperation**](DeploymentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment operation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentOperationsGetAtManagementGroupScope"></a>
# **deploymentOperationsGetAtManagementGroupScope**
> DeploymentOperation deploymentOperationsGetAtManagementGroupScope(groupId, deploymentName, operationId, apiVersion)



Gets a deployments operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String operationId = "operationId_example"; // String | The ID of the operation to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DeploymentOperation result = apiInstance.deploymentOperationsGetAtManagementGroupScope(groupId, deploymentName, operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsGetAtManagementGroupScope");
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
| **operationId** | **String**| The ID of the operation to get. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DeploymentOperation**](DeploymentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment operation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentOperationsGetAtScope"></a>
# **deploymentOperationsGetAtScope**
> DeploymentOperation deploymentOperationsGetAtScope(scope, deploymentName, operationId, apiVersion)



Gets a deployments operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String scope = "scope_example"; // String | The resource scope.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String operationId = "operationId_example"; // String | The ID of the operation to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DeploymentOperation result = apiInstance.deploymentOperationsGetAtScope(scope, deploymentName, operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsGetAtScope");
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
| **scope** | **String**| The resource scope. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **operationId** | **String**| The ID of the operation to get. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DeploymentOperation**](DeploymentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment operation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentOperationsGetAtSubscriptionScope"></a>
# **deploymentOperationsGetAtSubscriptionScope**
> DeploymentOperation deploymentOperationsGetAtSubscriptionScope(deploymentName, operationId, apiVersion, subscriptionId)



Gets a deployments operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String operationId = "operationId_example"; // String | The ID of the operation to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      DeploymentOperation result = apiInstance.deploymentOperationsGetAtSubscriptionScope(deploymentName, operationId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsGetAtSubscriptionScope");
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
| **operationId** | **String**| The ID of the operation to get. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**DeploymentOperation**](DeploymentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment operation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentOperationsGetAtTenantScope"></a>
# **deploymentOperationsGetAtTenantScope**
> DeploymentOperation deploymentOperationsGetAtTenantScope(deploymentName, operationId, apiVersion)



Gets a deployments operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String operationId = "operationId_example"; // String | The ID of the operation to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      DeploymentOperation result = apiInstance.deploymentOperationsGetAtTenantScope(deploymentName, operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsGetAtTenantScope");
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
| **operationId** | **String**| The ID of the operation to get. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**DeploymentOperation**](DeploymentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the deployment operation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentOperationsList"></a>
# **deploymentOperationsList**
> DeploymentOperationsListResult deploymentOperationsList(resourceGroupName, deploymentName, apiVersion, subscriptionId, $top)



Gets all deployments operations for a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Integer $top = 56; // Integer | The number of results to return.
    try {
      DeploymentOperationsListResult result = apiInstance.deploymentOperationsList(resourceGroupName, deploymentName, apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsList");
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
| **$top** | **Integer**| The number of results to return. | [optional] |

### Return type

[**DeploymentOperationsListResult**](DeploymentOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Return an array of deployment operations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentOperationsListAtManagementGroupScope"></a>
# **deploymentOperationsListAtManagementGroupScope**
> DeploymentOperationsListResult deploymentOperationsListAtManagementGroupScope(groupId, deploymentName, apiVersion, $top)



Gets all deployments operations for a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String groupId = "groupId_example"; // String | The management group ID.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Integer $top = 56; // Integer | The number of results to return.
    try {
      DeploymentOperationsListResult result = apiInstance.deploymentOperationsListAtManagementGroupScope(groupId, deploymentName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsListAtManagementGroupScope");
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
| **$top** | **Integer**| The number of results to return. | [optional] |

### Return type

[**DeploymentOperationsListResult**](DeploymentOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Return an array of deployment operations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentOperationsListAtScope"></a>
# **deploymentOperationsListAtScope**
> DeploymentOperationsListResult deploymentOperationsListAtScope(scope, deploymentName, apiVersion, $top)



Gets all deployments operations for a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String scope = "scope_example"; // String | The resource scope.
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Integer $top = 56; // Integer | The number of results to return.
    try {
      DeploymentOperationsListResult result = apiInstance.deploymentOperationsListAtScope(scope, deploymentName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsListAtScope");
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
| **scope** | **String**| The resource scope. | |
| **deploymentName** | **String**| The name of the deployment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$top** | **Integer**| The number of results to return. | [optional] |

### Return type

[**DeploymentOperationsListResult**](DeploymentOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Return an array of deployment operations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentOperationsListAtSubscriptionScope"></a>
# **deploymentOperationsListAtSubscriptionScope**
> DeploymentOperationsListResult deploymentOperationsListAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, $top)



Gets all deployments operations for a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Integer $top = 56; // Integer | The number of results to return.
    try {
      DeploymentOperationsListResult result = apiInstance.deploymentOperationsListAtSubscriptionScope(deploymentName, apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsListAtSubscriptionScope");
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
| **$top** | **Integer**| The number of results to return. | [optional] |

### Return type

[**DeploymentOperationsListResult**](DeploymentOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Return an array of deployment operations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentOperationsListAtTenantScope"></a>
# **deploymentOperationsListAtTenantScope**
> DeploymentOperationsListResult deploymentOperationsListAtTenantScope(deploymentName, apiVersion, $top)



Gets all deployments operations for a deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentOperationsApi apiInstance = new DeploymentOperationsApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | The name of the deployment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Integer $top = 56; // Integer | The number of results to return.
    try {
      DeploymentOperationsListResult result = apiInstance.deploymentOperationsListAtTenantScope(deploymentName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentOperationsApi#deploymentOperationsListAtTenantScope");
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
| **$top** | **Integer**| The number of results to return. | [optional] |

### Return type

[**DeploymentOperationsListResult**](DeploymentOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Return an array of deployment operations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

