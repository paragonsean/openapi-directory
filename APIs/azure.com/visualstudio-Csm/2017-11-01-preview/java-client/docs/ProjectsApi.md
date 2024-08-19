# ProjectsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectListByAccountResource**](ProjectsApi.md#projectListByAccountResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{rootResourceName}/project | Projects_ListByAccountResource |
| [**projectsCreate**](ProjectsApi.md#projectsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{rootResourceName}/project/{resourceName} | Projects_Create |
| [**projectsGet**](ProjectsApi.md#projectsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{rootResourceName}/project/{resourceName} | Projects_Get |
| [**projectsUpdate**](ProjectsApi.md#projectsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{rootResourceName}/project/{resourceName} | Projects_Update |


<a id="projectListByAccountResource"></a>
# **projectListByAccountResource**
> ProjectResourceListResult projectListByAccountResource(resourceGroupName, subscriptionId, apiVersion, rootResourceName)

Projects_ListByAccountResource

Gets all Visual Studio Team Services project resources created in the specified Team Services account.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String rootResourceName = "rootResourceName_example"; // String | Name of the Team Services account.
    try {
      ProjectResourceListResult result = apiInstance.projectListByAccountResource(resourceGroupName, subscriptionId, apiVersion, rootResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectListByAccountResource");
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **rootResourceName** | **String**| Name of the Team Services account. | |

### Return type

[**ProjectResourceListResult**](ProjectResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response contains the details of the Visual Studio Team Services project resources created in the specified Team Services account. |  -  |

<a id="projectsCreate"></a>
# **projectsCreate**
> ProjectResource projectsCreate(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, body, validating)

Projects_Create

Creates a Team Services project in the collection with the specified name. &#39;VersionControlOption&#39; and &#39;ProcessTemplateId&#39; must be specified in the resource properties. Valid values for VersionControlOption: Git, Tfvc. Valid values for ProcessTemplateId: 6B724908-EF14-45CF-84F8-768B5384DA45, ADCC42AB-9882-485E-A3ED-7678F01F66BC, 27450541-8E31-4150-9947-DC59F998FC01 (these IDs correspond to Scrum, Agile, and CMMI process templates).

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String rootResourceName = "rootResourceName_example"; // String | Name of the Team Services account.
    String resourceName = "resourceName_example"; // String | Name of the Team Services project.
    ProjectResource body = new ProjectResource(); // ProjectResource | The request data.
    String validating = "validating_example"; // String | This parameter is ignored and should be set to an empty string.
    try {
      ProjectResource result = apiInstance.projectsCreate(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, body, validating);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsCreate");
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **rootResourceName** | **String**| Name of the Team Services account. | |
| **resourceName** | **String**| Name of the Team Services project. | |
| **body** | [**ProjectResource**](ProjectResource.md)| The request data. | |
| **validating** | **String**| This parameter is ignored and should be set to an empty string. | [optional] |

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response contains the details of the created or updated team project resource. |  -  |
| **202** | The operation succeeded. A job to create the team project resource has been queued. The URI to monitor the status of the job is provided in the &#39;location&#39; header. |  -  |

<a id="projectsGet"></a>
# **projectsGet**
> ProjectResource projectsGet(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName)

Projects_Get

Gets the details of a Team Services project resource.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String rootResourceName = "rootResourceName_example"; // String | Name of the Team Services account.
    String resourceName = "resourceName_example"; // String | Name of the Team Services project.
    try {
      ProjectResource result = apiInstance.projectsGet(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName);
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **rootResourceName** | **String**| Name of the Team Services account. | |
| **resourceName** | **String**| Name of the Team Services project. | |

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response contains the details of the updated team project resource. |  -  |
| **404** | The project or Azure subscription was not found. |  -  |

<a id="projectsUpdate"></a>
# **projectsUpdate**
> ProjectResource projectsUpdate(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, body)

Projects_Update

Updates the tags of the specified Team Services project.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String rootResourceName = "rootResourceName_example"; // String | Name of the Team Services account.
    String resourceName = "resourceName_example"; // String | Name of the Team Services project.
    ProjectResourceUpdateParameters body = new ProjectResourceUpdateParameters(); // ProjectResourceUpdateParameters | The request data.
    try {
      ProjectResource result = apiInstance.projectsUpdate(resourceGroupName, subscriptionId, apiVersion, rootResourceName, resourceName, body);
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **rootResourceName** | **String**| Name of the Team Services account. | |
| **resourceName** | **String**| Name of the Team Services project. | |
| **body** | [**ProjectResourceUpdateParameters**](ProjectResourceUpdateParameters.md)| The request data. | |

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response contains the details of the updated team project resource. |  -  |

