# FilesComApi.AutomationRunsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAutomationRuns**](AutomationRunsApi.md#getAutomationRuns) | **GET** /automation_runs | List Automation Runs
[**getAutomationRunsId**](AutomationRunsApi.md#getAutomationRunsId) | **GET** /automation_runs/{id} | Show Automation Run



## getAutomationRuns

> [AutomationRunEntity] getAutomationRuns(automationId, opts)

List Automation Runs

List Automation Runs

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.AutomationRunsApi();
let automationId = 1; // Number | ID of the associated Automation.
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[created_at]=desc`). Valid fields are `created_at` and `status`.
  'filter': {key: null} // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `status`.
};
apiInstance.getAutomationRuns(automationId, opts, (error, data, response) => {
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
 **automationId** | **Number**| ID of the associated Automation. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[created_at]&#x3D;desc&#x60;). Valid fields are &#x60;created_at&#x60; and &#x60;status&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;status&#x60;. | [optional] 

### Return type

[**[AutomationRunEntity]**](AutomationRunEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAutomationRunsId

> AutomationRunEntity getAutomationRunsId(id)

Show Automation Run

Show Automation Run

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.AutomationRunsApi();
let id = 56; // Number | Automation Run ID.
apiInstance.getAutomationRunsId(id, (error, data, response) => {
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
 **id** | **Number**| Automation Run ID. | 

### Return type

[**AutomationRunEntity**](AutomationRunEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

