# TasksApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2TasksIdJsonGet**](TasksApi.md#v2TasksIdJsonGet) | **GET** /v2/tasks/{id}.json | Fetch a task |
| [**v2TasksIdJsonPut**](TasksApi.md#v2TasksIdJsonPut) | **PUT** /v2/tasks/{id}.json | Update a Task |
| [**v2TasksJsonGet**](TasksApi.md#v2TasksJsonGet) | **GET** /v2/tasks.json | List tasks |
| [**v2TasksJsonPost**](TasksApi.md#v2TasksJsonPost) | **POST** /v2/tasks.json | Create a Task |


<a id="v2TasksIdJsonGet"></a>
# **v2TasksIdJsonGet**
> Step v2TasksIdJsonGet(id)

Fetch a task

Fetches a task, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String id = "id_example"; // String | Task ID
    try {
      Step result = apiInstance.v2TasksIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#v2TasksIdJsonGet");
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
| **id** | **String**| Task ID | |

### Return type

[**Step**](Step.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2TasksIdJsonPut"></a>
# **v2TasksIdJsonPut**
> Task v2TasksIdJsonPut(id, currentState, description, dueDate, isLogged, remindAt, subject)

Update a Task

Updates a task. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String id = "id_example"; // String | Task ID
    String currentState = "currentState_example"; // String | Current state of the task, valid options are: completed
    String description = "description_example"; // String | A description of the task recorded for person at completion time
    String dueDate = "dueDate_example"; // String | Date of when the Task is due, ISO-8601 date format required
    Boolean isLogged = true; // Boolean | A flag to indicate that the task should only be logged
    String remindAt = "remindAt_example"; // String | Datetime of when the user will be reminded of the task, ISO-8601 datetime format required
    String subject = "subject_example"; // String | Subject line of the task
    try {
      Task result = apiInstance.v2TasksIdJsonPut(id, currentState, description, dueDate, isLogged, remindAt, subject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#v2TasksIdJsonPut");
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
| **id** | **String**| Task ID | |
| **currentState** | **String**| Current state of the task, valid options are: completed | [optional] |
| **description** | **String**| A description of the task recorded for person at completion time | [optional] |
| **dueDate** | **String**| Date of when the Task is due, ISO-8601 date format required | [optional] |
| **isLogged** | **Boolean**| A flag to indicate that the task should only be logged | [optional] |
| **remindAt** | **String**| Datetime of when the user will be reminded of the task, ISO-8601 datetime format required | [optional] |
| **subject** | **String**| Subject line of the task | [optional] |

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2TasksJsonGet"></a>
# **v2TasksJsonGet**
> List&lt;Task&gt; v2TasksJsonGet(ids, userId, personId, accountId, currentState, taskType, timeIntervalFilter, idempotencyKey, locale, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List tasks

Fetches multiple task records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of tasks to fetch.
    List<Integer> userId = Arrays.asList(); // List<Integer> | Filters tasks by the user to which they are assigned.
    List<Integer> personId = Arrays.asList(); // List<Integer> | Filters tasks by the person to which they are associated.
    List<Integer> accountId = Arrays.asList(); // List<Integer> | Filters tasks by the account to which they are associated.
    List<String> currentState = Arrays.asList(); // List<String> | Filters tasks by their current state. Valid current_states include: ['scheduled', 'completed'].
    List<String> taskType = Arrays.asList(); // List<String> | Filters tasks by their task type. Valid task_types include: ['call', 'email', 'general'].
    String timeIntervalFilter = "timeIntervalFilter_example"; // String | Filters tasks by time interval. Valid time_intervals include: ['overdue', 'today', 'tomorrow', 'this_week', 'next_week'].
    String idempotencyKey = "idempotencyKey_example"; // String | Filters tasks by idempotency key.
    List<String> locale = Arrays.asList(); // List<String> | Filters tasks by locale of the person to which they are associated.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: due_date, due_at. Defaults to due_date
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to ASC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<Task> result = apiInstance.v2TasksJsonGet(ids, userId, personId, accountId, currentState, taskType, timeIntervalFilter, idempotencyKey, locale, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#v2TasksJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of tasks to fetch. | [optional] |
| **userId** | [**List&lt;Integer&gt;**](Integer.md)| Filters tasks by the user to which they are assigned. | [optional] |
| **personId** | [**List&lt;Integer&gt;**](Integer.md)| Filters tasks by the person to which they are associated. | [optional] |
| **accountId** | [**List&lt;Integer&gt;**](Integer.md)| Filters tasks by the account to which they are associated. | [optional] |
| **currentState** | [**List&lt;String&gt;**](String.md)| Filters tasks by their current state. Valid current_states include: [&#39;scheduled&#39;, &#39;completed&#39;]. | [optional] |
| **taskType** | [**List&lt;String&gt;**](String.md)| Filters tasks by their task type. Valid task_types include: [&#39;call&#39;, &#39;email&#39;, &#39;general&#39;]. | [optional] |
| **timeIntervalFilter** | **String**| Filters tasks by time interval. Valid time_intervals include: [&#39;overdue&#39;, &#39;today&#39;, &#39;tomorrow&#39;, &#39;this_week&#39;, &#39;next_week&#39;]. | [optional] |
| **idempotencyKey** | **String**| Filters tasks by idempotency key. | [optional] |
| **locale** | [**List&lt;String&gt;**](String.md)| Filters tasks by locale of the person to which they are associated. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: due_date, due_at. Defaults to due_date | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to ASC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;Task&gt;**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2TasksJsonPost"></a>
# **v2TasksJsonPost**
> Task v2TasksJsonPost(currentState, dueDate, personId, subject, taskType, userId, description, idempotencyKey, remindAt)

Create a Task

Creates a task. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String currentState = "currentState_example"; // String | Current state of the task, valid options are: scheduled
    String dueDate = "dueDate_example"; // String | Date of when the Task is due, ISO-8601 date format required
    String personId = "personId_example"; // String | ID of the person to be contacted
    String subject = "subject_example"; // String | Subject line of the task.
    String taskType = "taskType_example"; // String | Task type, valid options are: call, email, general
    Integer userId = 56; // Integer | ID of the user linked to the task
    String description = "description_example"; // String | A description of the task recorded for person at completion time
    String idempotencyKey = "idempotencyKey_example"; // String | Establishes a unique identifier to prevent duplicates from being created
    String remindAt = "remindAt_example"; // String | Datetime of when the user will be reminded of the task, ISO-8601 datetime format required
    try {
      Task result = apiInstance.v2TasksJsonPost(currentState, dueDate, personId, subject, taskType, userId, description, idempotencyKey, remindAt);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#v2TasksJsonPost");
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
| **currentState** | **String**| Current state of the task, valid options are: scheduled | |
| **dueDate** | **String**| Date of when the Task is due, ISO-8601 date format required | |
| **personId** | **String**| ID of the person to be contacted | |
| **subject** | **String**| Subject line of the task. | |
| **taskType** | **String**| Task type, valid options are: call, email, general | |
| **userId** | **Integer**| ID of the user linked to the task | |
| **description** | **String**| A description of the task recorded for person at completion time | [optional] |
| **idempotencyKey** | **String**| Establishes a unique identifier to prevent duplicates from being created | [optional] |
| **remindAt** | **String**| Datetime of when the user will be reminded of the task, ISO-8601 datetime format required | [optional] |

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

