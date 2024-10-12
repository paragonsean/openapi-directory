# ProjectsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectsCreateOrUpdate**](ProjectsApi.md#projectsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName}/projects/{projectName} |  |
| [**projectsDelete**](ProjectsApi.md#projectsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName}/projects/{projectName} |  |
| [**projectsGet**](ProjectsApi.md#projectsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName}/projects/{projectName} |  |
| [**projectsListByWorkspace**](ProjectsApi.md#projectsListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces{workspaceName}/projects |  |
| [**projectsUpdate**](ProjectsApi.md#projectsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName}/workspaces/{workspaceName}/projects/{projectName} |  |


<a id="projectsCreateOrUpdate"></a>
# **projectsCreateOrUpdate**
> Project projectsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, parameters)



Creates or updates a project with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
    String projectName = "projectName_example"; // String | The name of the machine learning project under a team account workspace.
    Project parameters = new Project(); // Project | The parameters for creating or updating a project.
    try {
      Project result = apiInstance.projectsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsCreateOrUpdate");
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
| **projectName** | **String**| The name of the machine learning project under a team account workspace. | |
| **parameters** | [**Project**](Project.md)| The parameters for creating or updating a project. | |

### Return type

[**Project**](Project.md)

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

<a id="projectsDelete"></a>
# **projectsDelete**
> projectsDelete(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName)



Deletes a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
    String projectName = "projectName_example"; // String | The name of the machine learning project under a team account workspace.
    try {
      apiInstance.projectsDelete(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsDelete");
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
| **projectName** | **String**| The name of the machine learning project under a team account workspace. | |

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
| **204** | The machine learning team account does not exist in the subscription. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="projectsGet"></a>
# **projectsGet**
> Project projectsGet(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName)



Gets the properties of the specified machine learning project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
    String projectName = "projectName_example"; // String | The name of the machine learning project under a team account workspace.
    try {
      Project result = apiInstance.projectsGet(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsGet");
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
| **projectName** | **String**| The name of the machine learning project under a team account workspace. | |

### Return type

[**Project**](Project.md)

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

<a id="projectsListByWorkspace"></a>
# **projectsListByWorkspace**
> ProjectListResult projectsListByWorkspace(apiVersion, subscriptionId, accountName, workspaceName, resourceGroupName)



Lists all the available machine learning projects under the specified workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    try {
      ProjectListResult result = apiInstance.projectsListByWorkspace(apiVersion, subscriptionId, accountName, workspaceName, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsListByWorkspace");
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
| **workspaceName** | **String**| The name of the machine learning team account workspace. | |
| **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | |

### Return type

[**ProjectListResult**](ProjectListResult.md)

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

<a id="projectsUpdate"></a>
# **projectsUpdate**
> Project projectsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, parameters)



Updates a project with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
    String accountName = "accountName_example"; // String | The name of the machine learning team account.
    String workspaceName = "workspaceName_example"; // String | The name of the machine learning team account workspace.
    String projectName = "projectName_example"; // String | The name of the machine learning project under a team account workspace.
    ProjectUpdateParameters parameters = new ProjectUpdateParameters(); // ProjectUpdateParameters | The parameters for updating a machine learning team account.
    try {
      Project result = apiInstance.projectsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, workspaceName, projectName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsUpdate");
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
| **projectName** | **String**| The name of the machine learning project under a team account workspace. | |
| **parameters** | [**ProjectUpdateParameters**](ProjectUpdateParameters.md)| The parameters for updating a machine learning team account. | |

### Return type

[**Project**](Project.md)

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

