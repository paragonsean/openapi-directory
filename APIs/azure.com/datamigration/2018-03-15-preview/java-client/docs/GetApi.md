# GetApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsList_0**](GetApi.md#operationsList_0) | **GET** /providers/Microsoft.DataMigration/operations | Get available resource provider actions (operations) |
| [**projectsGet_1**](GetApi.md#projectsGet_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName} | Get project information |
| [**projectsList_1**](GetApi.md#projectsList_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects | Get projects in a service |
| [**resourceSkusListSkus_0**](GetApi.md#resourceSkusListSkus_0) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataMigration/skus | Get supported SKUs |
| [**servicesGet_1**](GetApi.md#servicesGet_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName} | Get DMS Service Instance |
| [**servicesListByResourceGroup_1**](GetApi.md#servicesListByResourceGroup_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services | Get services in resource group |
| [**servicesListSkus_1**](GetApi.md#servicesListSkus_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/skus | Get compatible SKUs |
| [**servicesList_1**](GetApi.md#servicesList_1) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataMigration/services | Get services in subscription |
| [**tasksGet_1**](GetApi.md#tasksGet_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName} | Get task information |
| [**tasksList_1**](GetApi.md#tasksList_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks | Get tasks in a service |
| [**usagesList_0**](GetApi.md#usagesList_0) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataMigration/locations/{location}/usages | Get resource quotas and usage information |


<a id="operationsList_0"></a>
# **operationsList_0**
> OperationsList200Response operationsList_0(apiVersion)

Get available resource provider actions (operations)

Lists all available actions exposed by the Data Migration Service resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      OperationsList200Response result = apiInstance.operationsList_0(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#operationsList_0");
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
| **apiVersion** | **String**| Version of the API | |

### Return type

[**OperationsList200Response**](OperationsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got action list |  -  |
| **0** | Error |  -  |

<a id="projectsGet_1"></a>
# **projectsGet_1**
> ProjectsGet200Response projectsGet_1(subscriptionId, groupName, serviceName, projectName, apiVersion)

Get project information

The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String projectName = "projectName_example"; // String | Name of the project
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ProjectsGet200Response result = apiInstance.projectsGet_1(subscriptionId, groupName, serviceName, projectName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#projectsGet_1");
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

### Return type

[**ProjectsGet200Response**](ProjectsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A project resource |  -  |
| **0** | Error |  -  |

<a id="projectsList_1"></a>
# **projectsList_1**
> ProjectsList200Response projectsList_1(subscriptionId, groupName, serviceName, apiVersion)

Get projects in a service

The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ProjectsList200Response result = apiInstance.projectsList_1(subscriptionId, groupName, serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#projectsList_1");
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

### Return type

[**ProjectsList200Response**](ProjectsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of projects |  -  |
| **0** | Error |  -  |

<a id="resourceSkusListSkus_0"></a>
# **resourceSkusListSkus_0**
> ResourceSkusListSkus200Response resourceSkusListSkus_0(subscriptionId, apiVersion)

Get supported SKUs

The skus action returns the list of SKUs that DMS supports.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ResourceSkusListSkus200Response result = apiInstance.resourceSkusListSkus_0(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#resourceSkusListSkus_0");
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
| **apiVersion** | **String**| Version of the API | |

### Return type

[**ResourceSkusListSkus200Response**](ResourceSkusListSkus200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got SKUs |  -  |
| **0** | Error |  -  |

<a id="servicesGet_1"></a>
# **servicesGet_1**
> ServicesGet200Response servicesGet_1(subscriptionId, groupName, serviceName, apiVersion)

Get DMS Service Instance

The services resource is the top-level resource that represents the Data Migration Service. The GET method retrieves information about a service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesGet200Response result = apiInstance.servicesGet_1(subscriptionId, groupName, serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#servicesGet_1");
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

### Return type

[**ServicesGet200Response**](ServicesGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A service instance resource |  -  |
| **0** | Error |  -  |

<a id="servicesListByResourceGroup_1"></a>
# **servicesListByResourceGroup_1**
> ServicesList200Response servicesListByResourceGroup_1(subscriptionId, groupName, apiVersion)

Get services in resource group

The Services resource is the top-level resource that represents the Data Migration Service. This method returns a list of service resources in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesList200Response result = apiInstance.servicesListByResourceGroup_1(subscriptionId, groupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#servicesListByResourceGroup_1");
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
| **apiVersion** | **String**| Version of the API | |

### Return type

[**ServicesList200Response**](ServicesList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got services |  -  |
| **0** | Error |  -  |

<a id="servicesListSkus_1"></a>
# **servicesListSkus_1**
> ServicesListSkus200Response servicesListSkus_1(subscriptionId, groupName, serviceName, apiVersion)

Get compatible SKUs

The services resource is the top-level resource that represents the Data Migration Service. The skus action returns the list of SKUs that a service resource can be updated to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesListSkus200Response result = apiInstance.servicesListSkus_1(subscriptionId, groupName, serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#servicesListSkus_1");
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

### Return type

[**ServicesListSkus200Response**](ServicesListSkus200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got SKUs |  -  |
| **0** | Error |  -  |

<a id="servicesList_1"></a>
# **servicesList_1**
> ServicesList200Response servicesList_1(subscriptionId, apiVersion)

Get services in subscription

The services resource is the top-level resource that represents the Data Migration Service. This method returns a list of service resources in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesList200Response result = apiInstance.servicesList_1(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#servicesList_1");
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
| **apiVersion** | **String**| Version of the API | |

### Return type

[**ServicesList200Response**](ServicesList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got services |  -  |
| **0** | Error |  -  |

<a id="tasksGet_1"></a>
# **tasksGet_1**
> TasksGet200Response tasksGet_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, $expand)

Get task information

The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The GET method retrieves information about a task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String projectName = "projectName_example"; // String | Name of the project
    String taskName = "taskName_example"; // String | Name of the Task
    String apiVersion = "apiVersion_example"; // String | Version of the API
    String $expand = "$expand_example"; // String | Expand the response
    try {
      TasksGet200Response result = apiInstance.tasksGet_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#tasksGet_1");
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
| **$expand** | **String**| Expand the response | [optional] |

### Return type

[**TasksGet200Response**](TasksGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A task resource |  -  |
| **0** | Error |  -  |

<a id="tasksList_1"></a>
# **tasksList_1**
> TasksList200Response tasksList_1(subscriptionId, groupName, serviceName, projectName, apiVersion, taskType)

Get tasks in a service

The services resource is the top-level resource that represents the Data Migration Service. This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String projectName = "projectName_example"; // String | Name of the project
    String apiVersion = "apiVersion_example"; // String | Version of the API
    String taskType = "taskType_example"; // String | Filter tasks by task type
    try {
      TasksList200Response result = apiInstance.tasksList_1(subscriptionId, groupName, serviceName, projectName, apiVersion, taskType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#tasksList_1");
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
| **taskType** | **String**| Filter tasks by task type | [optional] |

### Return type

[**TasksList200Response**](TasksList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got tasks |  -  |
| **0** | Error |  -  |

<a id="usagesList_0"></a>
# **usagesList_0**
> UsagesList200Response usagesList_0(subscriptionId, location, apiVersion)

Get resource quotas and usage information

This method returns region-specific quotas and resource usage information for the Data Migration Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String location = "location_example"; // String | The Azure region of the operation
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      UsagesList200Response result = apiInstance.usagesList_0(subscriptionId, location, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#usagesList_0");
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
| **location** | **String**| The Azure region of the operation | |
| **apiVersion** | **String**| Version of the API | |

### Return type

[**UsagesList200Response**](UsagesList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Quotas returned |  -  |
| **0** | Error |  -  |

