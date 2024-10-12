# OpenapiJsClient.Task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **Boolean** |  | [optional] 
**assignedBy** | **String** | ID of &#x60;/api/users/&#x60; who assigned the task | [optional] [readonly] 
**assigneeGroup** | **Number** | Either &#x60;assignee_user&#x60; or &#x60;assignee_group&#x60; should be set | [optional] 
**assigneeUser** | **String** | Either &#x60;assignee_user&#x60; or &#x60;assignee_group&#x60; should be set | [optional] 
**associatedItems** | [**[AssociatedTaskItem]**](AssociatedTaskItem.md) | Associated task items | [optional] 
**category** | **Number** |  | [optional] 
**createdAt** | **String** |  | [optional] [readonly] 
**createdBy** | **String** | ID of &#x60;/api/users&#x60; who created the task | [optional] [readonly] 
**dueDate** | [**TaskReminder**](TaskReminder.md) |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**notes** | [**[TaskNote1]**](TaskNote1.md) | Additional notes of the task | [optional] 
**priority** | **String** | Can be one of the following 10(Low), 20(Medium), 30(High), 40(Urgent) | [optional] 
**status** | **Number** |  | 
**title** | **String** |  | 
**updatedAt** | **String** |  | [optional] [readonly] 



## Enum: PriorityEnum


* `10` (value: `"10"`)

* `20` (value: `"20"`)

* `30` (value: `"30"`)

* `40` (value: `"40"`)




