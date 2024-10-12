# WorkspacePrivateEndpointConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateEndpointConnectionsDelete**](WorkspacePrivateEndpointConnectionsApi.md#privateEndpointConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsGet**](WorkspacePrivateEndpointConnectionsApi.md#privateEndpointConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsPut**](WorkspacePrivateEndpointConnectionsApi.md#privateEndpointConnectionsPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/privateEndpointConnections/{privateEndpointConnectionName} |  |


<a id="privateEndpointConnectionsDelete"></a>
# **privateEndpointConnectionsDelete**
> privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion)



Deletes the specified private endpoint connection associated with the workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacePrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacePrivateEndpointConnectionsApi apiInstance = new WorkspacePrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection associated with the workspace
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    try {
      apiInstance.privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacePrivateEndpointConnectionsApi#privateEndpointConnectionsDelete");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **privateEndpointConnectionName** | **String**| The name of the private endpoint connection associated with the workspace | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |

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
| **200** | OK -- Delete the private endpoint connection successfully. |  -  |
| **204** | No Content -- The private endpoint connection does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="privateEndpointConnectionsGet"></a>
# **privateEndpointConnectionsGet**
> PrivateEndpointConnection privateEndpointConnectionsGet(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion)



Gets the specified private endpoint connection associated with the workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacePrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacePrivateEndpointConnectionsApi apiInstance = new WorkspacePrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection associated with the workspace
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    try {
      PrivateEndpointConnection result = apiInstance.privateEndpointConnectionsGet(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacePrivateEndpointConnectionsApi#privateEndpointConnectionsGet");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **privateEndpointConnectionName** | **String**| The name of the private endpoint connection associated with the workspace | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Get the private endpoint connection properties successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="privateEndpointConnectionsPut"></a>
# **privateEndpointConnectionsPut**
> PrivateEndpointConnection privateEndpointConnectionsPut(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion, properties)



Update the state of specified private endpoint connection associated with the workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacePrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacePrivateEndpointConnectionsApi apiInstance = new WorkspacePrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection associated with the workspace
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    PrivateEndpointConnection properties = new PrivateEndpointConnection(); // PrivateEndpointConnection | The private endpoint connection properties.
    try {
      PrivateEndpointConnection result = apiInstance.privateEndpointConnectionsPut(subscriptionId, resourceGroupName, workspaceName, privateEndpointConnectionName, apiVersion, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacePrivateEndpointConnectionsApi#privateEndpointConnectionsPut");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **privateEndpointConnectionName** | **String**| The name of the private endpoint connection associated with the workspace | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **properties** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)| The private endpoint connection properties. | |

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Update the private endpoint connection properties successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

