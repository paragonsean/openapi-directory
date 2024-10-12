# WorkspacesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceFeaturesList**](WorkspacesApi.md#workspaceFeaturesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/features |  |
| [**workspacesCreateOrUpdate**](WorkspacesApi.md#workspacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName} |  |
| [**workspacesDelete**](WorkspacesApi.md#workspacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName} |  |
| [**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName} |  |
| [**workspacesListByResourceGroup**](WorkspacesApi.md#workspacesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces |  |
| [**workspacesListBySubscription**](WorkspacesApi.md#workspacesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/workspaces |  |
| [**workspacesListKeys**](WorkspacesApi.md#workspacesListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/listKeys |  |
| [**workspacesResyncKeys**](WorkspacesApi.md#workspacesResyncKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/resyncKeys |  |
| [**workspacesUpdate**](WorkspacesApi.md#workspacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName} |  |


<a id="workspaceFeaturesList"></a>
# **workspaceFeaturesList**
> ListAmlUserFeatureResult workspaceFeaturesList(apiVersion, subscriptionId, resourceGroupName, workspaceName)



Lists all enabled features for a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    try {
      ListAmlUserFeatureResult result = apiInstance.workspaceFeaturesList(apiVersion, subscriptionId, resourceGroupName, workspaceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspaceFeaturesList");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |

### Return type

[**ListAmlUserFeatureResult**](ListAmlUserFeatureResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="workspacesCreateOrUpdate"></a>
# **workspacesCreateOrUpdate**
> Workspace workspacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, workspaceName, parameters)



Creates or updates a workspace with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    Workspace parameters = new Workspace(); // Workspace | The parameters for creating or updating a machine learning workspace.
    try {
      Workspace result = apiInstance.workspacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, workspaceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesCreateOrUpdate");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **parameters** | [**Workspace**](Workspace.md)| The parameters for creating or updating a machine learning workspace. | |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **201** | The request was successful; the request was well-formed and received properly. |  -  |
| **202** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="workspacesDelete"></a>
# **workspacesDelete**
> workspacesDelete(apiVersion, subscriptionId, resourceGroupName, workspaceName)



Deletes a machine learning workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    try {
      apiInstance.workspacesDelete(apiVersion, subscriptionId, resourceGroupName, workspaceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesDelete");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **204** | The machine learning workspace does not exist in the subscription. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="workspacesGet"></a>
# **workspacesGet**
> Workspace workspacesGet(apiVersion, subscriptionId, resourceGroupName, workspaceName)



Gets the properties of the specified machine learning workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    try {
      Workspace result = apiInstance.workspacesGet(apiVersion, subscriptionId, resourceGroupName, workspaceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesGet");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="workspacesListByResourceGroup"></a>
# **workspacesListByResourceGroup**
> WorkspaceListResult workspacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, $skiptoken)



Lists all the available machine learning workspaces under the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String $skiptoken = "$skiptoken_example"; // String | Continuation token for pagination.
    try {
      WorkspaceListResult result = apiInstance.workspacesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListByResourceGroup");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **$skiptoken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="workspacesListBySubscription"></a>
# **workspacesListBySubscription**
> WorkspaceListResult workspacesListBySubscription(apiVersion, subscriptionId, $skiptoken)



Lists all the available machine learning workspaces under the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String $skiptoken = "$skiptoken_example"; // String | Continuation token for pagination.
    try {
      WorkspaceListResult result = apiInstance.workspacesListBySubscription(apiVersion, subscriptionId, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListBySubscription");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **$skiptoken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="workspacesListKeys"></a>
# **workspacesListKeys**
> ListWorkspaceKeysResult workspacesListKeys(apiVersion, subscriptionId, resourceGroupName, workspaceName)



Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    try {
      ListWorkspaceKeysResult result = apiInstance.workspacesListKeys(apiVersion, subscriptionId, resourceGroupName, workspaceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListKeys");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |

### Return type

[**ListWorkspaceKeysResult**](ListWorkspaceKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="workspacesResyncKeys"></a>
# **workspacesResyncKeys**
> workspacesResyncKeys(apiVersion, subscriptionId, resourceGroupName, workspaceName)



Resync all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    try {
      apiInstance.workspacesResyncKeys(apiVersion, subscriptionId, resourceGroupName, workspaceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesResyncKeys");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="workspacesUpdate"></a>
# **workspacesUpdate**
> Workspace workspacesUpdate(apiVersion, subscriptionId, resourceGroupName, workspaceName, parameters)



Updates a machine learning workspace with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    WorkspaceUpdateParameters parameters = new WorkspaceUpdateParameters(); // WorkspaceUpdateParameters | The parameters for updating a machine learning workspace.
    try {
      Workspace result = apiInstance.workspacesUpdate(apiVersion, subscriptionId, resourceGroupName, workspaceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesUpdate");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **parameters** | [**WorkspaceUpdateParameters**](WorkspaceUpdateParameters.md)| The parameters for updating a machine learning workspace. | |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

