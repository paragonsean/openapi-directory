# TestTheExhibitDayApiWithSwagger.TasksApi

All URIs are relative to *https://api.exhibitday.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks0Get**](TasksApi.md#tasks0Get) | **GET** /v1/tasks/ | 
[**tasks1Post**](TasksApi.md#tasks1Post) | **POST** /v1/tasks/ | 
[**tasks2Patch**](TasksApi.md#tasks2Patch) | **PATCH** /v1/tasks/ | 
[**tasks3Delete**](TasksApi.md#tasks3Delete) | **DELETE** /v1/tasks/ | 
[**tasksComment0Get**](TasksApi.md#tasksComment0Get) | **GET** /v1/tasks/comment | 
[**tasksComment1Post**](TasksApi.md#tasksComment1Post) | **POST** /v1/tasks/comment | 
[**tasksComment2Patch**](TasksApi.md#tasksComment2Patch) | **PATCH** /v1/tasks/comment | 
[**tasksComment3Delete**](TasksApi.md#tasksComment3Delete) | **DELETE** /v1/tasks/comment | 
[**tasksComments0Get**](TasksApi.md#tasksComments0Get) | **GET** /v1/tasks/comments | 
[**tasksInfo0Get**](TasksApi.md#tasksInfo0Get) | **GET** /v1/tasks/info | 



## tasks0Get

> String tasks0Get(apiKey, opts)



Retrieve Tasks

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'filterByEventId': 3.4, // Number | Only include tasks from this given event.
  'filterByGeneralTasksOnly': 3.4, // Number | Only include general tasks (tasks on the main task board that do not belong to a particular event). Note: this filter cannot be used in conjunction with the filter_by_event_id filter.
  'filterByIncompleteOnly': "'false'", // String | If you pass in the value \"true\" for this parameter, the result will only include tasks that are NOT marked as Completed.
  'filterByCompletedOnly': "'false'", // String | If you pass in the value \"true\" for this parameter, the result will only include tasks that are marked as Completed.
  'filterByNoDueDate': "'false'", // String | If you pass in the value \"true\" for this parameter, the result will only include tasks that do not have a due date set.
  'filterByDueDateGreaterThanOrEqualTo': new Date("2013-10-20"), // Date | Only include tasks that have a due date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter.
  'filterByDueDateSmallerThanOrEqualTo': new Date("2013-10-20"), // Date | Only include tasks that have a due date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter.
  'filterByHasAssignee': "'false'", // String | Only include tasks that have an assignee. Unassigned tasks will get excluded.
  'filterByAssigneeUserId': "filterByAssigneeUserId_example", // String | Only include tasks that are assigned to this user. You can get a list of UserId's in your workspace from the /v1/references/users_and_resources endpoint. Note: If you want to retrieve the tasks that are unassigned, include this parameter and pass in the word \"null\" as the value for it.
  'filterByTaskNameContainsText': "filterByTaskNameContainsText_example", // String | Only include tasks that have the given text in the task Name. For example: If you want to retrieve all the tasks that have the word “order” in the task Name field, pass in the value “order” for the filter_by_task_name_contains_text parameter. Note: this text search is not case-sensitive.
  'filterByIntegrationMetadataField1': "filterByIntegrationMetadataField1_example", // String | Only include tasks that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
  'filterByIntegrationMetadataField2': "filterByIntegrationMetadataField2_example", // String | Only include tasks that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
  'filterByIntegrationMetadataField3': "filterByIntegrationMetadataField3_example", // String | Only include tasks that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
  'filterByIntegrationMetadataField4': "filterByIntegrationMetadataField4_example", // String | Only include tasks that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
  'filterByIntegrationMetadataField5': "filterByIntegrationMetadataField5_example", // String | Only include tasks that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: A task's IntegrationMetadataField5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \"external id\" of the task from another system you're integrating with).
  'hydrateTaskComments': "'false'" // String | Include the comments collection for each task in the result set. Note: hydrating the comments collection for each task in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of comments for each task in the result set.
};
apiInstance.tasks0Get(apiKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **filterByEventId** | **Number**| Only include tasks from this given event. | [optional] 
 **filterByGeneralTasksOnly** | **Number**| Only include general tasks (tasks on the main task board that do not belong to a particular event). Note: this filter cannot be used in conjunction with the filter_by_event_id filter. | [optional] 
 **filterByIncompleteOnly** | **String**| If you pass in the value \&quot;true\&quot; for this parameter, the result will only include tasks that are NOT marked as Completed. | [optional] [default to &#39;false&#39;]
 **filterByCompletedOnly** | **String**| If you pass in the value \&quot;true\&quot; for this parameter, the result will only include tasks that are marked as Completed. | [optional] [default to &#39;false&#39;]
 **filterByNoDueDate** | **String**| If you pass in the value \&quot;true\&quot; for this parameter, the result will only include tasks that do not have a due date set. | [optional] [default to &#39;false&#39;]
 **filterByDueDateGreaterThanOrEqualTo** | **Date**| Only include tasks that have a due date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter. | [optional] 
 **filterByDueDateSmallerThanOrEqualTo** | **Date**| Only include tasks that have a due date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter. | [optional] 
 **filterByHasAssignee** | **String**| Only include tasks that have an assignee. Unassigned tasks will get excluded. | [optional] [default to &#39;false&#39;]
 **filterByAssigneeUserId** | **String**| Only include tasks that are assigned to this user. You can get a list of UserId&#39;s in your workspace from the /v1/references/users_and_resources endpoint. Note: If you want to retrieve the tasks that are unassigned, include this parameter and pass in the word \&quot;null\&quot; as the value for it. | [optional] 
 **filterByTaskNameContainsText** | **String**| Only include tasks that have the given text in the task Name. For example: If you want to retrieve all the tasks that have the word “order” in the task Name field, pass in the value “order” for the filter_by_task_name_contains_text parameter. Note: this text search is not case-sensitive. | [optional] 
 **filterByIntegrationMetadataField1** | **String**| Only include tasks that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] 
 **filterByIntegrationMetadataField2** | **String**| Only include tasks that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] 
 **filterByIntegrationMetadataField3** | **String**| Only include tasks that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] 
 **filterByIntegrationMetadataField4** | **String**| Only include tasks that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] 
 **filterByIntegrationMetadataField5** | **String**| Only include tasks that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with). | [optional] 
 **hydrateTaskComments** | **String**| Include the comments collection for each task in the result set. Note: hydrating the comments collection for each task in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of comments for each task in the result set. | [optional] [default to &#39;false&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasks1Post

> String tasks1Post(apiKey, name, opts)



Add a Task

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let name = "name_example"; // String | The name/short description of the task.
let opts = {
  'eventId': 3.4, // Number | The id of the event you would like to add the task under. If this value is not provided, the task will be added as a general (non-event-specific) task in your workspace (under the main Task Board).
  'taskSectionId': 3.4, // Number | The id of the event task section that the task should be placed under. Leave this value blank if you don't want to place/categorize the task under a specific event task section. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint.
  'isCompleted': "'false'", // String | Boolean representing whether or not the task has been completed.
  'dueDate': new Date("2013-10-20"), // Date | Task due date (format: YYYY-MM-DD).
  'assigneeUserId': "assigneeUserId_example", // String | The id of the user you would like to assign the task to. If you want the task to be unassigned, leave the value for this parameter blank. To get a list of all the user ids in your workspace, use the /v1/references/users_and_resources API endpoint. Users that can have tasks assigned to them will have their can_have_tasks_assigned property set to true.
  'details': "details_example", // String | The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
  'integrationMetadataField1': "integrationMetadataField1_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField2': "integrationMetadataField2_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField3': "integrationMetadataField3_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField4': "integrationMetadataField4_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField5': "integrationMetadataField5_example" // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
};
apiInstance.tasks1Post(apiKey, name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **name** | **String**| The name/short description of the task. | 
 **eventId** | **Number**| The id of the event you would like to add the task under. If this value is not provided, the task will be added as a general (non-event-specific) task in your workspace (under the main Task Board). | [optional] 
 **taskSectionId** | **Number**| The id of the event task section that the task should be placed under. Leave this value blank if you don&#39;t want to place/categorize the task under a specific event task section. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint. | [optional] 
 **isCompleted** | **String**| Boolean representing whether or not the task has been completed. | [optional] [default to &#39;false&#39;]
 **dueDate** | **Date**| Task due date (format: YYYY-MM-DD). | [optional] 
 **assigneeUserId** | **String**| The id of the user you would like to assign the task to. If you want the task to be unassigned, leave the value for this parameter blank. To get a list of all the user ids in your workspace, use the /v1/references/users_and_resources API endpoint. Users that can have tasks assigned to them will have their can_have_tasks_assigned property set to true. | [optional] 
 **details** | **String**| The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] 
 **integrationMetadataField1** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField2** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField3** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField4** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField5** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasks2Patch

> String tasks2Patch(apiKey, id, opts)



Update a Task

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let id = 3.4; // Number | The Id of the task you would like to update.
let opts = {
  'name': "name_example", // String | The name/short description of the task.
  'taskSectionId': 3.4, // Number | The id of the event task section that the task should be placed under. If you don't want to place/categorize the task under a specific event task section, pass in the value  ull\" for this parameter. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint.
  'isCompleted': "'false'", // String | Boolean representing whether or not the task has been completed.
  'dueDate': new Date("2013-10-20"), // Date | Task due date (format: YYYY-MM-DD). If you don't want the task to have a due date, pass in the value \"null\" for this parameter.
  'assigneeUserId': "assigneeUserId_example", // String | The User Id of the user you would like to assign the task to. If you want the task to be unassigned, pass in the value \"null\" for this parameter. To get a list of all the User Ids in your workspace, use the /v1/references/users_and_resources API endpoint; users who can have tasks assigned to them will have their can_have_tasks_assigned property set to true.
  'details': "details_example", // String | The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
  'integrationMetadataField1': "integrationMetadataField1_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField2': "integrationMetadataField2_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField3': "integrationMetadataField3_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField4': "integrationMetadataField4_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField5': "integrationMetadataField5_example" // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular task. For example, you can use it to store the \"external id\" of the task (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
};
apiInstance.tasks2Patch(apiKey, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **id** | **Number**| The Id of the task you would like to update. | 
 **name** | **String**| The name/short description of the task. | [optional] 
 **taskSectionId** | **Number**| The id of the event task section that the task should be placed under. If you don&#39;t want to place/categorize the task under a specific event task section, pass in the value  ull\&quot; for this parameter. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint. | [optional] 
 **isCompleted** | **String**| Boolean representing whether or not the task has been completed. | [optional] [default to &#39;false&#39;]
 **dueDate** | **Date**| Task due date (format: YYYY-MM-DD). If you don&#39;t want the task to have a due date, pass in the value \&quot;null\&quot; for this parameter. | [optional] 
 **assigneeUserId** | **String**| The User Id of the user you would like to assign the task to. If you want the task to be unassigned, pass in the value \&quot;null\&quot; for this parameter. To get a list of all the User Ids in your workspace, use the /v1/references/users_and_resources API endpoint; users who can have tasks assigned to them will have their can_have_tasks_assigned property set to true. | [optional] 
 **details** | **String**| The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] 
 **integrationMetadataField1** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField2** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField3** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField4** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField5** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasks3Delete

> String tasks3Delete(apiKey, id)



Delete a Task

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let id = 3.4; // Number | The id of the task you would like to delete.
apiInstance.tasks3Delete(apiKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **id** | **Number**| The id of the task you would like to delete. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksComment0Get

> String tasksComment0Get(apiKey, id)



Retrieve a Single Task Comment by id

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let id = 3.4; // Number | Id of the specific task comment that you would like to retrieve.
apiInstance.tasksComment0Get(apiKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **id** | **Number**| Id of the specific task comment that you would like to retrieve. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksComment1Post

> String tasksComment1Post(apiKey, taskId, comment)



Add a Comment to a Task

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let taskId = 3.4; // Number | The id of the task you would like to add the comment to.
let comment = "comment_example"; // String | The text of comment you would like to add. Only accepts plain text. Any html tags in the value you pass in will be stripped.
apiInstance.tasksComment1Post(apiKey, taskId, comment, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **taskId** | **Number**| The id of the task you would like to add the comment to. | 
 **comment** | **String**| The text of comment you would like to add. Only accepts plain text. Any html tags in the value you pass in will be stripped. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksComment2Patch

> String tasksComment2Patch(apiKey, id, comment)



Update a Task Comment

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let id = 3.4; // Number | The Id of the task comment you would like to update.
let comment = "comment_example"; // String | The text that you would like to replace the existing comment with. Only accepts plain text. Any html tags in the value you pass in will be stripped.
apiInstance.tasksComment2Patch(apiKey, id, comment, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **id** | **Number**| The Id of the task comment you would like to update. | 
 **comment** | **String**| The text that you would like to replace the existing comment with. Only accepts plain text. Any html tags in the value you pass in will be stripped. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksComment3Delete

> String tasksComment3Delete(apiKey, id)



Delete a Task Comment

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let id = 3.4; // Number | The Id of the task comment you would like to delete.
apiInstance.tasksComment3Delete(apiKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **id** | **Number**| The Id of the task comment you would like to delete. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksComments0Get

> String tasksComments0Get(apiKey, opts)



Retrieve Task Comments

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'filterByEventId': 3.4, // Number | Only include task comment for tasks from this given event.
  'filterByTaskId': 3.4, // Number | Only include task comments for this specific task.
  'hydrateTask': "'false'" // String | Include the task object for each task comment in the result set. Note: hydrating the task object for each task comment in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the task object each comment in the result set.
};
apiInstance.tasksComments0Get(apiKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **filterByEventId** | **Number**| Only include task comment for tasks from this given event. | [optional] 
 **filterByTaskId** | **Number**| Only include task comments for this specific task. | [optional] 
 **hydrateTask** | **String**| Include the task object for each task comment in the result set. Note: hydrating the task object for each task comment in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the task object each comment in the result set. | [optional] [default to &#39;false&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksInfo0Get

> String tasksInfo0Get(apiKey, id)



Retrieve a Single Task by id

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.TasksApi();
let apiKey = "apiKey_example"; // String | 
let id = 3.4; // Number | Id of the specific task that you would like to retrieve.
apiInstance.tasksInfo0Get(apiKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **id** | **Number**| Id of the specific task that you would like to retrieve. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

