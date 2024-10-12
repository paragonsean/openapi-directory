# WorkspacesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspacesCreateOrUpdate**](WorkspacesApi.md#workspacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName} |  |
| [**workspacesDelete**](WorkspacesApi.md#workspacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName} |  |
| [**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName} |  |
| [**workspacesListByAccounts**](WorkspacesApi.md#workspacesListByAccounts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces |  |
| [**workspacesUpdate**](WorkspacesApi.md#workspacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName} |  |


<a id="workspacesCreateOrUpdate"></a>
# **workspacesCreateOrUpdate**
> Workspace workspacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, parameters)



Creates or updates a machine learning workspace with the specified parameters.

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
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
    Workspace parameters = new Workspace(); // Workspace | The parameters for creating or updating a machine learning workspace.
    try {
      Workspace result = apiInstance.workspacesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, parameters);
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | |
| **accountName** | **String**| The name of the machine learning team account. | |
| **workspaceName** | **String**| The name of the machine learning team account workspace. | |
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
| **200** | The request was successful; the resource already exists and was updated. |  -  |
| **201** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="workspacesDelete"></a>
# **workspacesDelete**
> workspacesDelete(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName)



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
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
    try {
      apiInstance.workspacesDelete(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName);
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | |
| **accountName** | **String**| The name of the machine learning team account. | |
| **workspaceName** | **String**| The name of the machine learning team account workspace. | |

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
> Workspace workspacesGet(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName)



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
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
    try {
      Workspace result = apiInstance.workspacesGet(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName);
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | |
| **accountName** | **String**| The name of the machine learning team account. | |
| **workspaceName** | **String**| The name of the machine learning team account workspace. | |

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

<a id="workspacesListByAccounts"></a>
# **workspacesListByAccounts**
> WorkspaceListResult workspacesListByAccounts(apiVersion, subscriptionId, accountName, resourceGroupName)



Lists all the available machine learning workspaces under the specified team account.

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
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    try {
      WorkspaceListResult result = apiInstance.workspacesListByAccounts(apiVersion, subscriptionId, accountName, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListByAccounts");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **accountName** | **String**| The name of the machine learning team account. | |
| **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | |

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

<a id="workspacesUpdate"></a>
# **workspacesUpdate**
> Workspace workspacesUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, parameters)



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
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
    WorkspaceUpdateParameters parameters = new WorkspaceUpdateParameters(); // WorkspaceUpdateParameters | The parameters for updating a machine learning workspace.
    try {
      Workspace result = apiInstance.workspacesUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, parameters);
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | |
| **accountName** | **String**| The name of the machine learning team account. | |
| **workspaceName** | **String**| The name of the machine learning team account workspace. | |
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

