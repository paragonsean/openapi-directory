# DeploymentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deploymentsCalculateTemplateHash**](DeploymentsApi.md#deploymentsCalculateTemplateHash) | **POST** /providers/Microsoft.Resources/calculateTemplateHash |  |
| [**deploymentsCancel**](DeploymentsApi.md#deploymentsCancel) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/cancel | Cancels a currently running template deployment. |
| [**deploymentsCheckExistence**](DeploymentsApi.md#deploymentsCheckExistence) | **HEAD** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsCreateOrUpdate**](DeploymentsApi.md#deploymentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | Deploys resources to a resource group. |
| [**deploymentsDelete**](DeploymentsApi.md#deploymentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} | Deletes a deployment from the deployment history. |
| [**deploymentsExportTemplate**](DeploymentsApi.md#deploymentsExportTemplate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/exportTemplate |  |
| [**deploymentsGet**](DeploymentsApi.md#deploymentsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName} |  |
| [**deploymentsList**](DeploymentsApi.md#deploymentsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/ |  |
| [**deploymentsValidate**](DeploymentsApi.md#deploymentsValidate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}/validate |  |


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
    String deploymentName = "deploymentName_example"; // String | The name of the deployment to cancel.
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
| **deploymentName** | **String**| The name of the deployment to cancel. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | No Content |  -  |

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
    String deploymentName = "deploymentName_example"; // String | The name of the deployment to check.
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
| **deploymentName** | **String**| The name of the deployment to check. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

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
    String deploymentName = "deploymentName_example"; // String | The name of the deployment to delete.
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
| **deploymentName** | **String**| The name of the deployment to delete. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **202** | Accepted - Returns this status until the asynchronous operation has completed. |  -  |
| **204** | No Content |  -  |

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
    String deploymentName = "deploymentName_example"; // String | The name of the deployment from which to get the template.
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
| **deploymentName** | **String**| The name of the deployment from which to get the template. | |
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
    String deploymentName = "deploymentName_example"; // String | The name of the deployment to get.
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
| **deploymentName** | **String**| The name of the deployment to get. | |
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

<a id="deploymentsList"></a>
# **deploymentsList**
> DeploymentListResult deploymentsList(resourceGroupName, apiVersion, subscriptionId, $filter, $top)



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
      DeploymentListResult result = apiInstance.deploymentsList(resourceGroupName, apiVersion, subscriptionId, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsList");
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

