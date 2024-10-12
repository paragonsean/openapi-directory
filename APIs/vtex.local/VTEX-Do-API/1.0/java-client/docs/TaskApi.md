# TaskApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addComment**](TaskApi.md#addComment) | **POST** /tasks/{taskId}/comments | Add Comment on a Task |
| [**editTask**](TaskApi.md#editTask) | **PUT** /tasks/{taskId} | Update Task |
| [**getTask**](TaskApi.md#getTask) | **GET** /tasks/{taskId} | Retrieve Task |
| [**listtasksbyassignee**](TaskApi.md#listtasksbyassignee) | **GET** /tasks | List tasks |
| [**newTask**](TaskApi.md#newTask) | **POST** /tasks | Create Task |


<a id="addComment"></a>
# **addComment**
> Object addComment(accept, contentType, taskId, addCommentRequest)

Add Comment on a Task

Adds a comment to a given task, filtering by &#x60;taskId&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    String taskId = "123456abc"; // String | Task ID.
    AddCommentRequest addCommentRequest = new AddCommentRequest(); // AddCommentRequest | 
    try {
      Object result = apiInstance.addComment(accept, contentType, taskId, addCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#addComment");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Type of the content being sent. | |
| **taskId** | **String**| Task ID. | |
| **addCommentRequest** | [**AddCommentRequest**](AddCommentRequest.md)|  | |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="editTask"></a>
# **editTask**
> Object editTask(accept, contentType, taskId, editTaskRequest)

Update Task

Updates a given task&#39;s status, for example, filtering by &#x60;taskId&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    String taskId = "123456abc"; // String | Task ID.
    EditTaskRequest editTaskRequest = new EditTaskRequest(); // EditTaskRequest | 
    try {
      Object result = apiInstance.editTask(accept, contentType, taskId, editTaskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#editTask");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Type of the content being sent. | |
| **taskId** | **String**| Task ID. | |
| **editTaskRequest** | [**EditTaskRequest**](EditTaskRequest.md)|  | |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getTask"></a>
# **getTask**
> Object getTask(accept, contentType, taskId)

Retrieve Task

Retrieves a given task, filtering by &#x60;taskId&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    String taskId = "123456abc"; // String | Task ID.
    try {
      Object result = apiInstance.getTask(accept, contentType, taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#getTask");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Type of the content being sent. | |
| **taskId** | **String**| Task ID. | |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listtasksbyassignee"></a>
# **listtasksbyassignee**
> Object listtasksbyassignee(accept, contentType, assigneeEmail, targetId, context, page, perPage, status)

List tasks

This endpoint allows you to filter tasks. You can choose between the following filtering options:     - **Assignees:** using &#x60;assignee.email&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?assignee.email&#x3D;{{person@email.com}}&amp;status&#x3D;{{open}}&#x60;.     - **Targets:** using &#x60;targetId&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?target.id&#x3D;{{name}}&amp;status&#x3D;{{open}}&#x60;.     - **Paged tasks:** using &#x60;page&#x60;, &#x60;perPage&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?page&#x3D;{{1}}&amp;perPage&#x3D;{{10}}&amp;status&#x3D;;{{-Closed}}&#x60;.     - **Context:** using &#x60;context&#x60;, &#x60;page&#x60;, &#x60;perPage&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?context&#x3D;{{context}}&amp;page&#x3D;{{1}}&amp;perPage&#x3D;{{10}}&amp;status&#x3D;{{-Closed}}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    String assigneeEmail = "{{assigneeEmail}}"; // String | If you wish to list tasks by assignee, insert the desired assignee's email and status.
    String targetId = "{{targetId}}"; // String | If you wish to list tasks by target, insert the desired `targetId` and `status`.
    String context = "{{context}}"; // String | If you wish to list tasks by context, insert the desired context, `page`, `perPage` and `status`.
    String page = "{{page}}"; // String | If you wish to list tasks by context, also insert the desired `page`.
    String perPage = "{{desired number per page}}"; // String | If you wish to list tasks by context, also insert the desired `perPage` value.
    String status = "open"; // String | If you wish to list tasks by context, also insert the desired `status`.
    try {
      Object result = apiInstance.listtasksbyassignee(accept, contentType, assigneeEmail, targetId, context, page, perPage, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#listtasksbyassignee");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Type of the content being sent. | |
| **assigneeEmail** | **String**| If you wish to list tasks by assignee, insert the desired assignee&#39;s email and status. | [optional] |
| **targetId** | **String**| If you wish to list tasks by target, insert the desired &#x60;targetId&#x60; and &#x60;status&#x60;. | [optional] |
| **context** | **String**| If you wish to list tasks by context, insert the desired context, &#x60;page&#x60;, &#x60;perPage&#x60; and &#x60;status&#x60;. | [optional] |
| **page** | **String**| If you wish to list tasks by context, also insert the desired &#x60;page&#x60;. | [optional] |
| **perPage** | **String**| If you wish to list tasks by context, also insert the desired &#x60;perPage&#x60; value. | [optional] |
| **status** | **String**| If you wish to list tasks by context, also insert the desired &#x60;status&#x60;. | [optional] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="newTask"></a>
# **newTask**
> Object newTask(contentType, accept, newTaskRequest)

Create Task

Creates a new task in VTEX DO.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    NewTaskRequest newTaskRequest = new NewTaskRequest(); // NewTaskRequest | 
    try {
      Object result = apiInstance.newTask(contentType, accept, newTaskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#newTask");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **newTaskRequest** | [**NewTaskRequest**](NewTaskRequest.md)|  | |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

