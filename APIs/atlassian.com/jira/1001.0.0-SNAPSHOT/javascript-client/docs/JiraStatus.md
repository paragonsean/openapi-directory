# TheJiraCloudPlatformRestApi.JiraStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the status. | [optional] 
**id** | **String** | The ID of the status. | [optional] 
**name** | **String** | The name of the status. | [optional] 
**scope** | [**StatusScope**](StatusScope.md) |  | [optional] 
**statusCategory** | **String** | The category of the status. | [optional] 
**usages** | [**[ProjectIssueTypes]**](ProjectIssueTypes.md) | Projects and issue types where the status is used. Only available if the &#x60;usages&#x60; expand is requested. | [optional] 



## Enum: StatusCategoryEnum


* `TODO` (value: `"TODO"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `DONE` (value: `"DONE"`)




