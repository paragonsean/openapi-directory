# TheJiraCloudPlatformRestApi.AppMigrationApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appIssueFieldValueUpdateResourceUpdateIssueFieldsPut**](AppMigrationApi.md#appIssueFieldValueUpdateResourceUpdateIssueFieldsPut) | **PUT** /rest/atlassian-connect/1/migration/field | Bulk update custom field value
[**migrationResourceUpdateEntityPropertiesValuePut**](AppMigrationApi.md#migrationResourceUpdateEntityPropertiesValuePut) | **PUT** /rest/atlassian-connect/1/migration/properties/{entityType} | Bulk update entity properties
[**migrationResourceWorkflowRuleSearchPost**](AppMigrationApi.md#migrationResourceWorkflowRuleSearchPost) | **POST** /rest/atlassian-connect/1/migration/workflow/rule/search | Get workflow transition rule configurations



## appIssueFieldValueUpdateResourceUpdateIssueFieldsPut

> Object appIssueFieldValueUpdateResourceUpdateIssueFieldsPut(atlassianTransferId, connectCustomFieldValues)

Bulk update custom field value

Updates the value of a custom field added by Connect apps on one or more issues. The values of up to 200 custom fields can be updated.  **[Permissions](#permissions) required:** Only Connect apps can make this request.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';

let apiInstance = new TheJiraCloudPlatformRestApi.AppMigrationApi();
let atlassianTransferId = "atlassianTransferId_example"; // String | The ID of the transfer.
let connectCustomFieldValues = {"updateValueList":[{"_type":"StringIssueField","fieldID":10076,"issueID":10001,"string":"new string value"},{"_type":"TextIssueField","fieldID":10077,"issueID":10002,"text":"new text value"},{"_type":"SingleSelectIssueField","fieldID":10078,"issueID":10003,"optionID":"1"},{"_type":"MultiSelectIssueField","fieldID":10079,"issueID":10004,"optionID":"2"},{"_type":"RichTextIssueField","fieldID":10080,"issueID":10005,"richText":"new rich text value"},{"_type":"NumberIssueField","fieldID":10082,"issueID":10006,"number":54}]}; // ConnectCustomFieldValues | 
apiInstance.appIssueFieldValueUpdateResourceUpdateIssueFieldsPut(atlassianTransferId, connectCustomFieldValues, (error, data, response) => {
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
 **atlassianTransferId** | **String**| The ID of the transfer. | 
 **connectCustomFieldValues** | [**ConnectCustomFieldValues**](ConnectCustomFieldValues.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## migrationResourceUpdateEntityPropertiesValuePut

> migrationResourceUpdateEntityPropertiesValuePut(atlassianTransferId, entityType, entityPropertyDetails)

Bulk update entity properties

Updates the values of multiple entity properties for an object, up to 50 updates per request. This operation is for use by Connect apps during app migration.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';

let apiInstance = new TheJiraCloudPlatformRestApi.AppMigrationApi();
let atlassianTransferId = "atlassianTransferId_example"; // String | The app migration transfer ID.
let entityType = "entityType_example"; // String | The type indicating the object that contains the entity properties.
let entityPropertyDetails = [new TheJiraCloudPlatformRestApi.EntityPropertyDetails()]; // [EntityPropertyDetails] | 
apiInstance.migrationResourceUpdateEntityPropertiesValuePut(atlassianTransferId, entityType, entityPropertyDetails, (error, data, response) => {
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
 **atlassianTransferId** | **String**| The app migration transfer ID. | 
 **entityType** | **String**| The type indicating the object that contains the entity properties. | 
 **entityPropertyDetails** | [**[EntityPropertyDetails]**](EntityPropertyDetails.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## migrationResourceWorkflowRuleSearchPost

> WorkflowRulesSearchDetails migrationResourceWorkflowRuleSearchPost(atlassianTransferId, workflowRulesSearch)

Get workflow transition rule configurations

Returns configurations for workflow transition rules migrated from server to cloud and owned by the calling Connect app.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';

let apiInstance = new TheJiraCloudPlatformRestApi.AppMigrationApi();
let atlassianTransferId = "atlassianTransferId_example"; // String | The app migration transfer ID.
let workflowRulesSearch = new TheJiraCloudPlatformRestApi.WorkflowRulesSearch(); // WorkflowRulesSearch | 
apiInstance.migrationResourceWorkflowRuleSearchPost(atlassianTransferId, workflowRulesSearch, (error, data, response) => {
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
 **atlassianTransferId** | **String**| The app migration transfer ID. | 
 **workflowRulesSearch** | [**WorkflowRulesSearch**](WorkflowRulesSearch.md)|  | 

### Return type

[**WorkflowRulesSearchDetails**](WorkflowRulesSearchDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

