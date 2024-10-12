# CustomOperationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicesCheckChildrenNameAvailability**](CustomOperationApi.md#servicesCheckChildrenNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/checkNameAvailability | Check nested resource name validity and availability |
| [**servicesCheckStatus_0**](CustomOperationApi.md#servicesCheckStatus_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/checkStatus | Check service health status |
| [**servicesStart_0**](CustomOperationApi.md#servicesStart_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/start | Start service |
| [**servicesStop_0**](CustomOperationApi.md#servicesStop_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/stop | Stop service |
| [**tasksCancel_0**](CustomOperationApi.md#tasksCancel_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}/cancel | Cancel a task |


<a id="servicesCheckChildrenNameAvailability"></a>
# **servicesCheckChildrenNameAvailability**
> ServicesCheckNameAvailability200Response servicesCheckChildrenNameAvailability(subscriptionId, groupName, apiVersion, serviceName, parameters)

Check nested resource name validity and availability

This method checks whether a proposed nested resource name is valid and available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomOperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomOperationApi apiInstance = new CustomOperationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String apiVersion = "apiVersion_example"; // String | Version of the API
    String serviceName = "serviceName_example"; // String | Name of the service
    ServicesCheckNameAvailabilityRequest parameters = new ServicesCheckNameAvailabilityRequest(); // ServicesCheckNameAvailabilityRequest | Requested name to validate
    try {
      ServicesCheckNameAvailability200Response result = apiInstance.servicesCheckChildrenNameAvailability(subscriptionId, groupName, apiVersion, serviceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomOperationApi#servicesCheckChildrenNameAvailability");
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
| **serviceName** | **String**| Name of the service | |
| **parameters** | [**ServicesCheckNameAvailabilityRequest**](ServicesCheckNameAvailabilityRequest.md)| Requested name to validate | |

### Return type

[**ServicesCheckNameAvailability200Response**](ServicesCheckNameAvailability200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Name checked |  -  |
| **0** | Error |  -  |

<a id="servicesCheckStatus_0"></a>
# **servicesCheckStatus_0**
> ServicesCheckStatus200Response servicesCheckStatus_0(subscriptionId, groupName, serviceName, apiVersion)

Check service health status

The services resource is the top-level resource that represents the Data Migration Service. This action performs a health check and returns the status of the service and virtual machine size.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomOperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomOperationApi apiInstance = new CustomOperationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesCheckStatus200Response result = apiInstance.servicesCheckStatus_0(subscriptionId, groupName, serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomOperationApi#servicesCheckStatus_0");
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

[**ServicesCheckStatus200Response**](ServicesCheckStatus200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Health checked |  -  |
| **0** | Error |  -  |

<a id="servicesStart_0"></a>
# **servicesStart_0**
> servicesStart_0(subscriptionId, groupName, serviceName, apiVersion)

Start service

The services resource is the top-level resource that represents the Data Migration Service. This action starts the service and the service can be used for data migration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomOperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomOperationApi apiInstance = new CustomOperationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      apiInstance.servicesStart_0(subscriptionId, groupName, serviceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomOperationApi#servicesStart_0");
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

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service has already been started. |  -  |
| **202** | The request to start service is accepted. |  -  |
| **0** | Error |  -  |

<a id="servicesStop_0"></a>
# **servicesStop_0**
> servicesStop_0(subscriptionId, groupName, serviceName, apiVersion)

Stop service

The services resource is the top-level resource that represents the Data Migration Service. This action stops the service and the service cannot be used for data migration. The service owner won&#39;t be billed when the service is stopped.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomOperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomOperationApi apiInstance = new CustomOperationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      apiInstance.servicesStop_0(subscriptionId, groupName, serviceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomOperationApi#servicesStop_0");
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

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service has already been stopped. |  -  |
| **202** | The request to stop service is accepted. |  -  |
| **0** | Error |  -  |

<a id="tasksCancel_0"></a>
# **tasksCancel_0**
> TasksGet200Response tasksCancel_0(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion)

Cancel a task

The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. This method cancels a task if it&#39;s currently queued or running.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomOperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomOperationApi apiInstance = new CustomOperationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String projectName = "projectName_example"; // String | Name of the project
    String taskName = "taskName_example"; // String | Name of the Task
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      TasksGet200Response result = apiInstance.tasksCancel_0(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomOperationApi#tasksCancel_0");
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
| **200** | Task canceled |  -  |
| **0** | Error |  -  |

