# TasksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tasksGetResourceGroupLevelTask**](TasksApi.md#tasksGetResourceGroupLevelTask) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName} |  |
| [**tasksGetSubscriptionLevelTask**](TasksApi.md#tasksGetSubscriptionLevelTask) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName} |  |
| [**tasksList**](TasksApi.md#tasksList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/tasks |  |
| [**tasksListByHomeRegion**](TasksApi.md#tasksListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks |  |
| [**tasksListByResourceGroup**](TasksApi.md#tasksListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks |  |
| [**tasksUpdateResourceGroupLevelTaskState**](TasksApi.md#tasksUpdateResourceGroupLevelTaskState) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}/{taskUpdateActionType} |  |
| [**tasksUpdateSubscriptionLevelTaskState**](TasksApi.md#tasksUpdateSubscriptionLevelTaskState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}/{taskUpdateActionType} |  |


<a id="tasksGetResourceGroupLevelTask"></a>
# **tasksGetResourceGroupLevelTask**
> SecurityTask tasksGetResourceGroupLevelTask(apiVersion, subscriptionId, resourceGroupName, ascLocation, taskName)



Recommended tasks that will help improve the security of the subscription proactively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String taskName = "taskName_example"; // String | Name of the task object, will be a GUID
    try {
      SecurityTask result = apiInstance.tasksGetResourceGroupLevelTask(apiVersion, subscriptionId, resourceGroupName, ascLocation, taskName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksGetResourceGroupLevelTask");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **taskName** | **String**| Name of the task object, will be a GUID | |

### Return type

[**SecurityTask**](SecurityTask.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tasksGetSubscriptionLevelTask"></a>
# **tasksGetSubscriptionLevelTask**
> SecurityTask tasksGetSubscriptionLevelTask(apiVersion, subscriptionId, ascLocation, taskName)



Recommended tasks that will help improve the security of the subscription proactively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String taskName = "taskName_example"; // String | Name of the task object, will be a GUID
    try {
      SecurityTask result = apiInstance.tasksGetSubscriptionLevelTask(apiVersion, subscriptionId, ascLocation, taskName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksGetSubscriptionLevelTask");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **taskName** | **String**| Name of the task object, will be a GUID | |

### Return type

[**SecurityTask**](SecurityTask.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tasksList"></a>
# **tasksList**
> SecurityTaskList tasksList(apiVersion, subscriptionId, $filter)



Recommended tasks that will help improve the security of the subscription proactively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String $filter = "$filter_example"; // String | OData filter. Optional.
    try {
      SecurityTaskList result = apiInstance.tasksList(apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksList");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **$filter** | **String**| OData filter. Optional. | [optional] |

### Return type

[**SecurityTaskList**](SecurityTaskList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tasksListByHomeRegion"></a>
# **tasksListByHomeRegion**
> SecurityTaskList tasksListByHomeRegion(apiVersion, subscriptionId, ascLocation, $filter)



Recommended tasks that will help improve the security of the subscription proactively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String $filter = "$filter_example"; // String | OData filter. Optional.
    try {
      SecurityTaskList result = apiInstance.tasksListByHomeRegion(apiVersion, subscriptionId, ascLocation, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksListByHomeRegion");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **$filter** | **String**| OData filter. Optional. | [optional] |

### Return type

[**SecurityTaskList**](SecurityTaskList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tasksListByResourceGroup"></a>
# **tasksListByResourceGroup**
> SecurityTaskList tasksListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, ascLocation, $filter)



Recommended tasks that will help improve the security of the subscription proactively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String $filter = "$filter_example"; // String | OData filter. Optional.
    try {
      SecurityTaskList result = apiInstance.tasksListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, ascLocation, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksListByResourceGroup");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **$filter** | **String**| OData filter. Optional. | [optional] |

### Return type

[**SecurityTaskList**](SecurityTaskList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tasksUpdateResourceGroupLevelTaskState"></a>
# **tasksUpdateResourceGroupLevelTaskState**
> tasksUpdateResourceGroupLevelTaskState(apiVersion, subscriptionId, resourceGroupName, ascLocation, taskName, taskUpdateActionType)



Recommended tasks that will help improve the security of the subscription proactively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String taskName = "taskName_example"; // String | Name of the task object, will be a GUID
    String taskUpdateActionType = "Activate"; // String | Type of the action to do on the task
    try {
      apiInstance.tasksUpdateResourceGroupLevelTaskState(apiVersion, subscriptionId, resourceGroupName, ascLocation, taskName, taskUpdateActionType);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksUpdateResourceGroupLevelTaskState");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **taskName** | **String**| Name of the task object, will be a GUID | |
| **taskUpdateActionType** | **String**| Type of the action to do on the task | [enum: Activate, Dismiss, Start, Resolve, Close] |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tasksUpdateSubscriptionLevelTaskState"></a>
# **tasksUpdateSubscriptionLevelTaskState**
> tasksUpdateSubscriptionLevelTaskState(apiVersion, subscriptionId, ascLocation, taskName, taskUpdateActionType)



Recommended tasks that will help improve the security of the subscription proactively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String taskName = "taskName_example"; // String | Name of the task object, will be a GUID
    String taskUpdateActionType = "Activate"; // String | Type of the action to do on the task
    try {
      apiInstance.tasksUpdateSubscriptionLevelTaskState(apiVersion, subscriptionId, ascLocation, taskName, taskUpdateActionType);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksUpdateSubscriptionLevelTaskState");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **taskName** | **String**| Name of the task object, will be a GUID | |
| **taskUpdateActionType** | **String**| Type of the action to do on the task | [enum: Activate, Dismiss, Start, Resolve, Close] |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

