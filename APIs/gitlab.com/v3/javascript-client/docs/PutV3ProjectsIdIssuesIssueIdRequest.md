# Gitlab.PutV3ProjectsIdIssuesIssueIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **String** | The title of an issue | [optional] 
**updatedAt** | **Date** | Date time when the issue was updated. Available only for admins and project owners. | [optional] 
**stateEvent** | **String** | State of the issue | [optional] 
**description** | **String** | The description of an issue | [optional] 
**assigneeId** | **Number** | The ID of a user to assign issue | [optional] 
**milestoneId** | **Number** | The ID of a milestone to assign issue | [optional] 
**labels** | **String** | Comma-separated list of label names | [optional] 
**dueDate** | **String** | Date time string in the format YEAR-MONTH-DAY | [optional] 
**confidential** | **Boolean** | Boolean parameter if the issue should be confidential | [optional] 
**createdAt** | **String** |  | [optional] 



## Enum: StateEventEnum


* `reopen` (value: `"reopen"`)

* `close` (value: `"close"`)




