# TasksApi

All URIs are relative to *https://api.exhibitday.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tasks0Get**](TasksApi.md#tasks0Get) | **GET** /v1/tasks/ |  |
| [**tasks1Post**](TasksApi.md#tasks1Post) | **POST** /v1/tasks/ |  |
| [**tasks2Patch**](TasksApi.md#tasks2Patch) | **PATCH** /v1/tasks/ |  |
| [**tasks3Delete**](TasksApi.md#tasks3Delete) | **DELETE** /v1/tasks/ |  |
| [**tasksComment0Get**](TasksApi.md#tasksComment0Get) | **GET** /v1/tasks/comment |  |
| [**tasksComment1Post**](TasksApi.md#tasksComment1Post) | **POST** /v1/tasks/comment |  |
| [**tasksComment2Patch**](TasksApi.md#tasksComment2Patch) | **PATCH** /v1/tasks/comment |  |
| [**tasksComment3Delete**](TasksApi.md#tasksComment3Delete) | **DELETE** /v1/tasks/comment |  |
| [**tasksComments0Get**](TasksApi.md#tasksComments0Get) | **GET** /v1/tasks/comments |  |
| [**tasksInfo0Get**](TasksApi.md#tasksInfo0Get) | **GET** /v1/tasks/info |  |


<a id="tasks0Get"></a>
# **tasks0Get**
> String tasks0Get(apiKey, filterByEventId, filterByGeneralTasksOnly, filterByIncompleteOnly, filterByCompletedOnly, filterByNoDueDate, filterByDueDateGreaterThanOrEqualTo, filterByDueDateSmallerThanOrEqualTo, filterByHasAssignee, filterByAssigneeUserId, filterByTaskNameContainsText, filterByIntegrationMetadataField1, filterByIntegrationMetadataField2, filterByIntegrationMetadataField3, filterByIntegrationMetadataField4, filterByIntegrationMetadataField5, hydrateTaskComments)



Retrieve Tasks

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal filterByEventId = new BigDecimal(78); // BigDecimal | Only include tasks from this given event.
    BigDecimal filterByGeneralTasksOnly = new BigDecimal(78); // BigDecimal | Only include general tasks (tasks on the main task board that do not belong to a particular event). Note: this filter cannot be used in conjunction with the filter_by_event_id filter.
    String filterByIncompleteOnly = "false"; // String | If you pass in the value \"true\" for this parameter, the result will only include tasks that are NOT marked as Completed.
    String filterByCompletedOnly = "false"; // String | If you pass in the value \"true\" for this parameter, the result will only include tasks that are marked as Completed.
    String filterByNoDueDate = "false"; // String | If you pass in the value \"true\" for this parameter, the result will only include tasks that do not have a due date set.
    LocalDate filterByDueDateGreaterThanOrEqualTo = LocalDate.now(); // LocalDate | Only include tasks that have a due date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter.
    LocalDate filterByDueDateSmallerThanOrEqualTo = LocalDate.now(); // LocalDate | Only include tasks that have a due date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter.
    String filterByHasAssignee = "false"; // String | Only include tasks that have an assignee. Unassigned tasks will get excluded.
    String filterByAssigneeUserId = "filterByAssigneeUserId_example"; // String | Only include tasks that are assigned to this user. You can get a list of UserId's in your workspace from the /v1/references/users_and_resources endpoint. Note: If you want to retrieve the tasks that are unassigned, include this parameter and pass in the word \"null\" as the value for it.
    String filterByTaskNameContainsText = "filterByTaskNameContainsText_example"; // String | Only include tasks that have the given text in the task Name. For example: If you want to retrieve all the tasks that have the word “order” in the task Name field, pass in the value “order” for the filter_by_task_name_contains_text parameter. Note: this text search is not case-sensitive.
    String filterByIntegrationMetadataField1 = "filterByIntegrationMetadataField1_example"; // String | Only include tasks that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
    String filterByIntegrationMetadataField2 = "filterByIntegrationMetadataField2_example"; // String | Only include tasks that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
    String filterByIntegrationMetadataField3 = "filterByIntegrationMetadataField3_example"; // String | Only include tasks that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
    String filterByIntegrationMetadataField4 = "filterByIntegrationMetadataField4_example"; // String | Only include tasks that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
    String filterByIntegrationMetadataField5 = "filterByIntegrationMetadataField5_example"; // String | Only include tasks that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
    String hydrateTaskComments = "false"; // String | Include the comments collection for each task in the result set. Note: hydrating the comments collection for each task in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of comments for each task in the result set.
    try {
      String result = apiInstance.tasks0Get(apiKey, filterByEventId, filterByGeneralTasksOnly, filterByIncompleteOnly, filterByCompletedOnly, filterByNoDueDate, filterByDueDateGreaterThanOrEqualTo, filterByDueDateSmallerThanOrEqualTo, filterByHasAssignee, filterByAssigneeUserId, filterByTaskNameContainsText, filterByIntegrationMetadataField1, filterByIntegrationMetadataField2, filterByIntegrationMetadataField3, filterByIntegrationMetadataField4, filterByIntegrationMetadataField5, hydrateTaskComments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasks0Get");
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
| **apiKey** | **String**|  | |
| **filterByEventId** | **BigDecimal**| Only include tasks from this given event. | [optional] |
| **filterByGeneralTasksOnly** | **BigDecimal**| Only include general tasks (tasks on the main task board that do not belong to a particular event). Note: this filter cannot be used in conjunction with the filter_by_event_id filter. | [optional] |
| **filterByIncompleteOnly** | **String**| If you pass in the value \&quot;true\&quot; for this parameter, the result will only include tasks that are NOT marked as Completed. | [optional] [default to false] |
| **filterByCompletedOnly** | **String**| If you pass in the value \&quot;true\&quot; for this parameter, the result will only include tasks that are marked as Completed. | [optional] [default to false] |
| **filterByNoDueDate** | **String**| If you pass in the value \&quot;true\&quot; for this parameter, the result will only include tasks that do not have a due date set. | [optional] [default to false] |
| **filterByDueDateGreaterThanOrEqualTo** | **LocalDate**| Only include tasks that have a due date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter. | [optional] |
| **filterByDueDateSmallerThanOrEqualTo** | **LocalDate**| Only include tasks that have a due date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter. | [optional] |
| **filterByHasAssignee** | **String**| Only include tasks that have an assignee. Unassigned tasks will get excluded. | [optional] [default to false] |
| **filterByAssigneeUserId** | **String**| Only include tasks that are assigned to this user. You can get a list of UserId&#39;s in your workspace from the /v1/references/users_and_resources endpoint. Note: If you want to retrieve the tasks that are unassigned, include this parameter and pass in the word \&quot;null\&quot; as the value for it. | [optional] |
| **filterByTaskNameContainsText** | **String**| Only include tasks that have the given text in the task Name. For example: If you want to retrieve all the tasks that have the word “order” in the task Name field, pass in the value “order” for the filter_by_task_name_contains_text parameter. Note: this text search is not case-sensitive. | [optional] |
| **filterByIntegrationMetadataField1** | **String**| Only include tasks that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] |
| **filterByIntegrationMetadataField2** | **String**| Only include tasks that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] |
| **filterByIntegrationMetadataField3** | **String**| Only include tasks that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] |
| **filterByIntegrationMetadataField4** | **String**| Only include tasks that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] |
| **filterByIntegrationMetadataField5** | **String**| Only include tasks that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] |
| **hydrateTaskComments** | **String**| Include the comments collection for each task in the result set. Note: hydrating the comments collection for each task in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of comments for each task in the result set. | [optional] [default to false] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tasks1Post"></a>
# **tasks1Post**
> String tasks1Post(apiKey, name, eventId, taskSectionId, isCompleted, dueDate, assigneeUserId, details, integrationMetadataField1, integrationMetadataField2, integrationMetadataField3, integrationMetadataField4, integrationMetadataField5)



Add a Task

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String name = "name_example"; // String | The name/short description of the task.
    BigDecimal eventId = new BigDecimal(78); // BigDecimal | The id of the event you would like to add the task under. If this value is not provided, the task will be added as a general (non-event-specific) task in your workspace (under the main Task Board).
    BigDecimal taskSectionId = new BigDecimal(78); // BigDecimal | The id of the event task section that the task should be placed under. Leave this value blank if you don't want to place/categorize the task under a specific event task section. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint.
    String isCompleted = "false"; // String | Boolean representing whether or not the task has been completed.
    LocalDate dueDate = LocalDate.now(); // LocalDate | Task due date (format: YYYY-MM-DD).
    String assigneeUserId = "assigneeUserId_example"; // String | The id of the user you would like to assign the task to. If you want the task to be unassigned, leave the value for this parameter blank. To get a list of all the user ids in your workspace, use the /v1/references/users_and_resources API endpoint. Users that can have tasks assigned to them will have their can_have_tasks_assigned property set to true.
    String details = "details_example"; // String | The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
    String integrationMetadataField1 = "integrationMetadataField1_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField2 = "integrationMetadataField2_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField3 = "integrationMetadataField3_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField4 = "integrationMetadataField4_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField5 = "integrationMetadataField5_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    try {
      String result = apiInstance.tasks1Post(apiKey, name, eventId, taskSectionId, isCompleted, dueDate, assigneeUserId, details, integrationMetadataField1, integrationMetadataField2, integrationMetadataField3, integrationMetadataField4, integrationMetadataField5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasks1Post");
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
| **apiKey** | **String**|  | |
| **name** | **String**| The name/short description of the task. | |
| **eventId** | **BigDecimal**| The id of the event you would like to add the task under. If this value is not provided, the task will be added as a general (non-event-specific) task in your workspace (under the main Task Board). | [optional] |
| **taskSectionId** | **BigDecimal**| The id of the event task section that the task should be placed under. Leave this value blank if you don&#39;t want to place/categorize the task under a specific event task section. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint. | [optional] |
| **isCompleted** | **String**| Boolean representing whether or not the task has been completed. | [optional] [default to false] |
| **dueDate** | **LocalDate**| Task due date (format: YYYY-MM-DD). | [optional] |
| **assigneeUserId** | **String**| The id of the user you would like to assign the task to. If you want the task to be unassigned, leave the value for this parameter blank. To get a list of all the user ids in your workspace, use the /v1/references/users_and_resources API endpoint. Users that can have tasks assigned to them will have their can_have_tasks_assigned property set to true. | [optional] |
| **details** | **String**| The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] |
| **integrationMetadataField1** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField2** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField3** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField4** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField5** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tasks2Patch"></a>
# **tasks2Patch**
> String tasks2Patch(apiKey, id, name, taskSectionId, isCompleted, dueDate, assigneeUserId, details, integrationMetadataField1, integrationMetadataField2, integrationMetadataField3, integrationMetadataField4, integrationMetadataField5)



Update a Task

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal id = new BigDecimal(78); // BigDecimal | The Id of the task you would like to update.
    String name = "name_example"; // String | The name/short description of the task.
    BigDecimal taskSectionId = new BigDecimal(78); // BigDecimal | The id of the event task section that the task should be placed under. If you don't want to place/categorize the task under a specific event task section, pass in the value  ull\" for this parameter. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint.
    String isCompleted = "false"; // String | Boolean representing whether or not the task has been completed.
    LocalDate dueDate = LocalDate.now(); // LocalDate | Task due date (format: YYYY-MM-DD). If you don't want the task to have a due date, pass in the value \"null\" for this parameter.
    String assigneeUserId = "assigneeUserId_example"; // String | The User Id of the user you would like to assign the task to. If you want the task to be unassigned, pass in the value \"null\" for this parameter. To get a list of all the User Ids in your workspace, use the /v1/references/users_and_resources API endpoint; users who can have tasks assigned to them will have their can_have_tasks_assigned property set to true.
    String details = "details_example"; // String | The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
    String integrationMetadataField1 = "integrationMetadataField1_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField2 = "integrationMetadataField2_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField3 = "integrationMetadataField3_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField4 = "integrationMetadataField4_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField5 = "integrationMetadataField5_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    try {
      String result = apiInstance.tasks2Patch(apiKey, id, name, taskSectionId, isCompleted, dueDate, assigneeUserId, details, integrationMetadataField1, integrationMetadataField2, integrationMetadataField3, integrationMetadataField4, integrationMetadataField5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasks2Patch");
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
| **apiKey** | **String**|  | |
| **id** | **BigDecimal**| The Id of the task you would like to update. | |
| **name** | **String**| The name/short description of the task. | [optional] |
| **taskSectionId** | **BigDecimal**| The id of the event task section that the task should be placed under. If you don&#39;t want to place/categorize the task under a specific event task section, pass in the value  ull\&quot; for this parameter. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint. | [optional] |
| **isCompleted** | **String**| Boolean representing whether or not the task has been completed. | [optional] [default to false] |
| **dueDate** | **LocalDate**| Task due date (format: YYYY-MM-DD). If you don&#39;t want the task to have a due date, pass in the value \&quot;null\&quot; for this parameter. | [optional] |
| **assigneeUserId** | **String**| The User Id of the user you would like to assign the task to. If you want the task to be unassigned, pass in the value \&quot;null\&quot; for this parameter. To get a list of all the User Ids in your workspace, use the /v1/references/users_and_resources API endpoint; users who can have tasks assigned to them will have their can_have_tasks_assigned property set to true. | [optional] |
| **details** | **String**| The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] |
| **integrationMetadataField1** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField2** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField3** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField4** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField5** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tasks3Delete"></a>
# **tasks3Delete**
> String tasks3Delete(apiKey, id)



Delete a Task

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal id = new BigDecimal(78); // BigDecimal | The id of the task you would like to delete.
    try {
      String result = apiInstance.tasks3Delete(apiKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasks3Delete");
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
| **apiKey** | **String**|  | |
| **id** | **BigDecimal**| The id of the task you would like to delete. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tasksComment0Get"></a>
# **tasksComment0Get**
> String tasksComment0Get(apiKey, id)



Retrieve a Single Task Comment by id

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal id = new BigDecimal(78); // BigDecimal | Id of the specific task comment that you would like to retrieve.
    try {
      String result = apiInstance.tasksComment0Get(apiKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksComment0Get");
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
| **apiKey** | **String**|  | |
| **id** | **BigDecimal**| Id of the specific task comment that you would like to retrieve. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tasksComment1Post"></a>
# **tasksComment1Post**
> String tasksComment1Post(apiKey, taskId, comment)



Add a Comment to a Task

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal taskId = new BigDecimal(78); // BigDecimal | The id of the task you would like to add the comment to.
    String comment = "comment_example"; // String | The text of comment you would like to add. Only accepts plain text. Any html tags in the value you pass in will be stripped.
    try {
      String result = apiInstance.tasksComment1Post(apiKey, taskId, comment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksComment1Post");
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
| **apiKey** | **String**|  | |
| **taskId** | **BigDecimal**| The id of the task you would like to add the comment to. | |
| **comment** | **String**| The text of comment you would like to add. Only accepts plain text. Any html tags in the value you pass in will be stripped. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tasksComment2Patch"></a>
# **tasksComment2Patch**
> String tasksComment2Patch(apiKey, id, comment)



Update a Task Comment

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal id = new BigDecimal(78); // BigDecimal | The Id of the task comment you would like to update.
    String comment = "comment_example"; // String | The text that you would like to replace the existing comment with. Only accepts plain text. Any html tags in the value you pass in will be stripped.
    try {
      String result = apiInstance.tasksComment2Patch(apiKey, id, comment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksComment2Patch");
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
| **apiKey** | **String**|  | |
| **id** | **BigDecimal**| The Id of the task comment you would like to update. | |
| **comment** | **String**| The text that you would like to replace the existing comment with. Only accepts plain text. Any html tags in the value you pass in will be stripped. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tasksComment3Delete"></a>
# **tasksComment3Delete**
> String tasksComment3Delete(apiKey, id)



Delete a Task Comment

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal id = new BigDecimal(78); // BigDecimal | The Id of the task comment you would like to delete.
    try {
      String result = apiInstance.tasksComment3Delete(apiKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksComment3Delete");
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
| **apiKey** | **String**|  | |
| **id** | **BigDecimal**| The Id of the task comment you would like to delete. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tasksComments0Get"></a>
# **tasksComments0Get**
> String tasksComments0Get(apiKey, filterByEventId, filterByTaskId, hydrateTask)



Retrieve Task Comments

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal filterByEventId = new BigDecimal(78); // BigDecimal | Only include task comment for tasks from this given event.
    BigDecimal filterByTaskId = new BigDecimal(78); // BigDecimal | Only include task comments for this specific task.
    String hydrateTask = "false"; // String | Include the task object for each task comment in the result set. Note: hydrating the task object for each task comment in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the task object each comment in the result set.
    try {
      String result = apiInstance.tasksComments0Get(apiKey, filterByEventId, filterByTaskId, hydrateTask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksComments0Get");
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
| **apiKey** | **String**|  | |
| **filterByEventId** | **BigDecimal**| Only include task comment for tasks from this given event. | [optional] |
| **filterByTaskId** | **BigDecimal**| Only include task comments for this specific task. | [optional] |
| **hydrateTask** | **String**| Include the task object for each task comment in the result set. Note: hydrating the task object for each task comment in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the task object each comment in the result set. | [optional] [default to false] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tasksInfo0Get"></a>
# **tasksInfo0Get**
> String tasksInfo0Get(apiKey, id)



Retrieve a Single Task by id

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
    defaultClient.setBasePath("https://api.exhibitday.com");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal id = new BigDecimal(78); // BigDecimal | Id of the specific task that you would like to retrieve.
    try {
      String result = apiInstance.tasksInfo0Get(apiKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#tasksInfo0Get");
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
| **apiKey** | **String**|  | |
| **id** | **BigDecimal**| Id of the specific task that you would like to retrieve. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

