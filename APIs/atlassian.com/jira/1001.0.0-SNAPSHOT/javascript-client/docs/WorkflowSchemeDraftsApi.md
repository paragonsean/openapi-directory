# TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWorkflowSchemeDraftFromParent**](WorkflowSchemeDraftsApi.md#createWorkflowSchemeDraftFromParent) | **POST** /rest/api/3/workflowscheme/{id}/createdraft | Create draft workflow scheme
[**deleteDraftDefaultWorkflow**](WorkflowSchemeDraftsApi.md#deleteDraftDefaultWorkflow) | **DELETE** /rest/api/3/workflowscheme/{id}/draft/default | Delete draft default workflow
[**deleteDraftWorkflowMapping**](WorkflowSchemeDraftsApi.md#deleteDraftWorkflowMapping) | **DELETE** /rest/api/3/workflowscheme/{id}/draft/workflow | Delete issue types for workflow in draft workflow scheme
[**deleteWorkflowSchemeDraft**](WorkflowSchemeDraftsApi.md#deleteWorkflowSchemeDraft) | **DELETE** /rest/api/3/workflowscheme/{id}/draft | Delete draft workflow scheme
[**deleteWorkflowSchemeDraftIssueType**](WorkflowSchemeDraftsApi.md#deleteWorkflowSchemeDraftIssueType) | **DELETE** /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType} | Delete workflow for issue type in draft workflow scheme
[**getDraftDefaultWorkflow**](WorkflowSchemeDraftsApi.md#getDraftDefaultWorkflow) | **GET** /rest/api/3/workflowscheme/{id}/draft/default | Get draft default workflow
[**getDraftWorkflow**](WorkflowSchemeDraftsApi.md#getDraftWorkflow) | **GET** /rest/api/3/workflowscheme/{id}/draft/workflow | Get issue types for workflows in draft workflow scheme
[**getWorkflowSchemeDraft**](WorkflowSchemeDraftsApi.md#getWorkflowSchemeDraft) | **GET** /rest/api/3/workflowscheme/{id}/draft | Get draft workflow scheme
[**getWorkflowSchemeDraftIssueType**](WorkflowSchemeDraftsApi.md#getWorkflowSchemeDraftIssueType) | **GET** /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType} | Get workflow for issue type in draft workflow scheme
[**publishDraftWorkflowScheme**](WorkflowSchemeDraftsApi.md#publishDraftWorkflowScheme) | **POST** /rest/api/3/workflowscheme/{id}/draft/publish | Publish draft workflow scheme
[**setWorkflowSchemeDraftIssueType**](WorkflowSchemeDraftsApi.md#setWorkflowSchemeDraftIssueType) | **PUT** /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType} | Set workflow for issue type in draft workflow scheme
[**updateDraftDefaultWorkflow**](WorkflowSchemeDraftsApi.md#updateDraftDefaultWorkflow) | **PUT** /rest/api/3/workflowscheme/{id}/draft/default | Update draft default workflow
[**updateDraftWorkflowMapping**](WorkflowSchemeDraftsApi.md#updateDraftWorkflowMapping) | **PUT** /rest/api/3/workflowscheme/{id}/draft/workflow | Set issue types for workflow in workflow scheme
[**updateWorkflowSchemeDraft**](WorkflowSchemeDraftsApi.md#updateWorkflowSchemeDraft) | **PUT** /rest/api/3/workflowscheme/{id}/draft | Update draft workflow scheme



## createWorkflowSchemeDraftFromParent

> WorkflowScheme createWorkflowSchemeDraftFromParent(id)

Create draft workflow scheme

Create a draft workflow scheme from an active workflow scheme, by copying the active workflow scheme. Note that an active workflow scheme can only have one draft workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the active workflow scheme that the draft is created from.
apiInstance.createWorkflowSchemeDraftFromParent(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the active workflow scheme that the draft is created from. | 

### Return type

[**WorkflowScheme**](WorkflowScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDraftDefaultWorkflow

> WorkflowScheme deleteDraftDefaultWorkflow(id)

Delete draft default workflow

Resets the default workflow for a workflow scheme&#39;s draft. That is, the default workflow is set to Jira&#39;s system workflow (the *jira* workflow).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
apiInstance.deleteDraftDefaultWorkflow(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 

### Return type

[**WorkflowScheme**](WorkflowScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDraftWorkflowMapping

> deleteDraftWorkflowMapping(id, workflowName)

Delete issue types for workflow in draft workflow scheme

Deletes the workflow-issue type mapping for a workflow in a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
let workflowName = "workflowName_example"; // String | The name of the workflow.
apiInstance.deleteDraftWorkflowMapping(id, workflowName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 
 **workflowName** | **String**| The name of the workflow. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteWorkflowSchemeDraft

> deleteWorkflowSchemeDraft(id)

Delete draft workflow scheme

Deletes a draft workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the active workflow scheme that the draft was created from.
apiInstance.deleteWorkflowSchemeDraft(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The ID of the active workflow scheme that the draft was created from. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteWorkflowSchemeDraftIssueType

> WorkflowScheme deleteWorkflowSchemeDraftIssueType(id, issueType)

Delete workflow for issue type in draft workflow scheme

Deletes the issue type-workflow mapping for an issue type in a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
let issueType = "issueType_example"; // String | The ID of the issue type.
apiInstance.deleteWorkflowSchemeDraftIssueType(id, issueType, (error, data, response) => {
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
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 
 **issueType** | **String**| The ID of the issue type. | 

### Return type

[**WorkflowScheme**](WorkflowScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDraftDefaultWorkflow

> DefaultWorkflow getDraftDefaultWorkflow(id)

Get draft default workflow

Returns the default workflow for a workflow scheme&#39;s draft. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
apiInstance.getDraftDefaultWorkflow(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 

### Return type

[**DefaultWorkflow**](DefaultWorkflow.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDraftWorkflow

> IssueTypesWorkflowMapping getDraftWorkflow(id, opts)

Get issue types for workflows in draft workflow scheme

Returns the workflow-issue type mappings for a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
let opts = {
  'workflowName': "workflowName_example" // String | The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow.
};
apiInstance.getDraftWorkflow(id, opts, (error, data, response) => {
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
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 
 **workflowName** | **String**| The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow. | [optional] 

### Return type

[**IssueTypesWorkflowMapping**](IssueTypesWorkflowMapping.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWorkflowSchemeDraft

> WorkflowScheme getWorkflowSchemeDraft(id)

Get draft workflow scheme

Returns the draft workflow scheme for an active workflow scheme. Draft workflow schemes allow changes to be made to the active workflow schemes: When an active workflow scheme is updated, a draft copy is created. The draft is modified, then the changes in the draft are copied back to the active workflow scheme. See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.   Note that:   *  Only active workflow schemes can have draft workflow schemes.  *  An active workflow scheme can only have one draft workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the active workflow scheme that the draft was created from.
apiInstance.getWorkflowSchemeDraft(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the active workflow scheme that the draft was created from. | 

### Return type

[**WorkflowScheme**](WorkflowScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWorkflowSchemeDraftIssueType

> IssueTypeWorkflowMapping getWorkflowSchemeDraftIssueType(id, issueType)

Get workflow for issue type in draft workflow scheme

Returns the issue type-workflow mapping for an issue type in a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
let issueType = "issueType_example"; // String | The ID of the issue type.
apiInstance.getWorkflowSchemeDraftIssueType(id, issueType, (error, data, response) => {
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
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 
 **issueType** | **String**| The ID of the issue type. | 

### Return type

[**IssueTypeWorkflowMapping**](IssueTypeWorkflowMapping.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishDraftWorkflowScheme

> publishDraftWorkflowScheme(id, publishDraftWorkflowScheme, opts)

Publish draft workflow scheme

Publishes a draft workflow scheme.  Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to update issues with the original workflow status to the new workflow status.  This operation is [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
let publishDraftWorkflowScheme = {"statusMappings":[{"issueTypeId":"10001","newStatusId":"1","statusId":"3"},{"issueTypeId":"10001","newStatusId":"2","statusId":"2"},{"issueTypeId":"10002","newStatusId":"10003","statusId":"10005"},{"issueTypeId":"10003","newStatusId":"1","statusId":"4"}]}; // PublishDraftWorkflowScheme | Details of the status mappings.
let opts = {
  'validateOnly': false // Boolean | Whether the request only performs a validation.
};
apiInstance.publishDraftWorkflowScheme(id, publishDraftWorkflowScheme, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 
 **publishDraftWorkflowScheme** | [**PublishDraftWorkflowScheme**](PublishDraftWorkflowScheme.md)| Details of the status mappings. | 
 **validateOnly** | **Boolean**| Whether the request only performs a validation. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setWorkflowSchemeDraftIssueType

> WorkflowScheme setWorkflowSchemeDraftIssueType(id, issueType, issueTypeWorkflowMapping)

Set workflow for issue type in draft workflow scheme

Sets the workflow for an issue type in a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
let issueType = "issueType_example"; // String | The ID of the issue type.
let issueTypeWorkflowMapping = {"issueType":"10000","updateDraftIfNeeded":false,"workflow":"jira"}; // IssueTypeWorkflowMapping | The issue type-project mapping.
apiInstance.setWorkflowSchemeDraftIssueType(id, issueType, issueTypeWorkflowMapping, (error, data, response) => {
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
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 
 **issueType** | **String**| The ID of the issue type. | 
 **issueTypeWorkflowMapping** | [**IssueTypeWorkflowMapping**](IssueTypeWorkflowMapping.md)| The issue type-project mapping. | 

### Return type

[**WorkflowScheme**](WorkflowScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDraftDefaultWorkflow

> WorkflowScheme updateDraftDefaultWorkflow(id, defaultWorkflow)

Update draft default workflow

Sets the default workflow for a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
let defaultWorkflow = {"updateDraftIfNeeded":false,"workflow":"jira"}; // DefaultWorkflow | The object for the new default workflow.
apiInstance.updateDraftDefaultWorkflow(id, defaultWorkflow, (error, data, response) => {
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
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 
 **defaultWorkflow** | [**DefaultWorkflow**](DefaultWorkflow.md)| The object for the new default workflow. | 

### Return type

[**WorkflowScheme**](WorkflowScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDraftWorkflowMapping

> WorkflowScheme updateDraftWorkflowMapping(id, workflowName, issueTypesWorkflowMapping)

Set issue types for workflow in workflow scheme

Sets the issue types for a workflow in a workflow scheme&#39;s draft. The workflow can also be set as the default workflow for the draft workflow scheme. Unmapped issues types are mapped to the default workflow.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the workflow scheme that the draft belongs to.
let workflowName = "workflowName_example"; // String | The name of the workflow.
let issueTypesWorkflowMapping = {"issueTypes":["10000"],"updateDraftIfNeeded":true,"workflow":"jira"}; // IssueTypesWorkflowMapping | 
apiInstance.updateDraftWorkflowMapping(id, workflowName, issueTypesWorkflowMapping, (error, data, response) => {
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
 **id** | **Number**| The ID of the workflow scheme that the draft belongs to. | 
 **workflowName** | **String**| The name of the workflow. | 
 **issueTypesWorkflowMapping** | [**IssueTypesWorkflowMapping**](IssueTypesWorkflowMapping.md)|  | 

### Return type

[**WorkflowScheme**](WorkflowScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkflowSchemeDraft

> WorkflowScheme updateWorkflowSchemeDraft(id, workflowScheme)

Update draft workflow scheme

Updates a draft workflow scheme. If a draft workflow scheme does not exist for the active workflow scheme, then a draft is created. Note that an active workflow scheme can only have one draft workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeDraftsApi();
let id = 789; // Number | The ID of the active workflow scheme that the draft was created from.
let workflowScheme = {"defaultWorkflow":"jira","description":"The description of the example workflow scheme.","issueTypeMappings":{"10000":"scrum workflow"},"name":"Example workflow scheme","updateDraftIfNeeded":false}; // WorkflowScheme | 
apiInstance.updateWorkflowSchemeDraft(id, workflowScheme, (error, data, response) => {
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
 **id** | **Number**| The ID of the active workflow scheme that the draft was created from. | 
 **workflowScheme** | [**WorkflowScheme**](WorkflowScheme.md)|  | 

### Return type

[**WorkflowScheme**](WorkflowScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

