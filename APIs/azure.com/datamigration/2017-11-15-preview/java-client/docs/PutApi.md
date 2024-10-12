# PutApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectsCreateOrUpdate_1**](PutApi.md#projectsCreateOrUpdate_1) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName} | Create or update project |
| [**servicesCreateOrUpdate_1**](PutApi.md#servicesCreateOrUpdate_1) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName} | Create or update DMS Instance |
| [**tasksCreateOrUpdate_1**](PutApi.md#tasksCreateOrUpdate_1) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName} | Create or update task |


<a id="projectsCreateOrUpdate_1"></a>
# **projectsCreateOrUpdate_1**
> ProjectsGet200Response projectsCreateOrUpdate_1(subscriptionId, groupName, serviceName, projectName, apiVersion, parameters)

Create or update project

The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PutApi apiInstance = new PutApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String projectName = "projectName_example"; // String | Name of the project
    String apiVersion = "apiVersion_example"; // String | Version of the API
    ProjectsGet200Response parameters = new ProjectsGet200Response(); // ProjectsGet200Response | Information about the project
    try {
      ProjectsGet200Response result = apiInstance.projectsCreateOrUpdate_1(subscriptionId, groupName, serviceName, projectName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PutApi#projectsCreateOrUpdate_1");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **projectName** | **String**| Name of the project | |
| **apiVersion** | **String**| Version of the API | |
| **parameters** | [**ProjectsGet200Response**](ProjectsGet200Response.md)| Information about the project | |

### Return type

[**ProjectsGet200Response**](ProjectsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project updated |  -  |
| **201** | Project created |  -  |
| **0** | Error |  -  |

<a id="servicesCreateOrUpdate_1"></a>
# **servicesCreateOrUpdate_1**
> ServicesGet200Response servicesCreateOrUpdate_1(subscriptionId, groupName, serviceName, apiVersion, parameters)

Create or update DMS Instance

The services resource is the top-level resource that represents the Data Migration Service. The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, \&quot;vm\&quot;, which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request (\&quot;ServiceIsBusy\&quot;). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PutApi apiInstance = new PutApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    ServicesGet200Response parameters = new ServicesGet200Response(); // ServicesGet200Response | Information about the service
    try {
      ServicesGet200Response result = apiInstance.servicesCreateOrUpdate_1(subscriptionId, groupName, serviceName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PutApi#servicesCreateOrUpdate_1");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **apiVersion** | **String**| Version of the API | |
| **parameters** | [**ServicesGet200Response**](ServicesGet200Response.md)| Information about the service | |

### Return type

[**ServicesGet200Response**](ServicesGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service updated |  -  |
| **201** | Service created (use provisioningState) |  -  |
| **202** | Update accepted |  -  |
| **0** | Error |  -  |

<a id="tasksCreateOrUpdate_1"></a>
# **tasksCreateOrUpdate_1**
> TasksGet200Response tasksCreateOrUpdate_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, parameters)

Create or update task

The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an exising one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PutApi apiInstance = new PutApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String projectName = "projectName_example"; // String | Name of the project
    String taskName = "taskName_example"; // String | Name of the Task
    String apiVersion = "apiVersion_example"; // String | Version of the API
    TasksGet200Response parameters = new TasksGet200Response(); // TasksGet200Response | Information about the task
    try {
      TasksGet200Response result = apiInstance.tasksCreateOrUpdate_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PutApi#tasksCreateOrUpdate_1");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **projectName** | **String**| Name of the project | |
| **taskName** | **String**| Name of the Task | |
| **apiVersion** | **String**| Version of the API | |
| **parameters** | [**TasksGet200Response**](TasksGet200Response.md)| Information about the task | |

### Return type

[**TasksGet200Response**](TasksGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Task updated |  -  |
| **201** | Task created |  -  |
| **0** | Error |  -  |

