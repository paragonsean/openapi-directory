# DeploymentOperationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deploymentOperationsGet**](DeploymentOperationsApi.md#deploymentOperationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations/{operationId} |  |
| [**deploymentOperationsList**](DeploymentOperationsApi.md#deploymentOperationsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations |  |


<a id="deploymentOperationsGet"></a>
# **deploymentOperationsGet**
> DeploymentOperation deploymentOperationsGet(resourceGroupName, deploymentName, operationId, apiVersion, subscriptionId)



Get a list of deployments operations.

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
    String operationId = "operationId_example"; // String | Operation Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
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
| **operationId** | **String**| Operation Id. | |
| **apiVersion** | **String**| Client Api Version. | |
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
| **200** |  |  -  |

<a id="deploymentOperationsList"></a>
# **deploymentOperationsList**
> DeploymentOperationsListResult deploymentOperationsList(resourceGroupName, deploymentName, apiVersion, subscriptionId, $top)



Gets a list of deployments operations.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Integer $top = 56; // Integer | Query parameters.
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$top** | **Integer**| Query parameters. | [optional] |

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
| **200** |  |  -  |

