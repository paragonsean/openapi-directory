

# Task


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archived** | **Boolean** |  |  [optional] |
|**assignedBy** | **String** | ID of &#x60;/api/users/&#x60; who assigned the task |  [optional] [readonly] |
|**assigneeGroup** | **Integer** | Either &#x60;assignee_user&#x60; or &#x60;assignee_group&#x60; should be set |  [optional] |
|**assigneeUser** | **String** | Either &#x60;assignee_user&#x60; or &#x60;assignee_group&#x60; should be set |  [optional] |
|**associatedItems** | [**List&lt;AssociatedTaskItem&gt;**](AssociatedTaskItem.md) | Associated task items |  [optional] |
|**category** | **Integer** |  |  [optional] |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**createdBy** | **String** | ID of &#x60;/api/users&#x60; who created the task |  [optional] [readonly] |
|**dueDate** | [**TaskReminder**](TaskReminder.md) |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**notes** | [**List&lt;TaskNote1&gt;**](TaskNote1.md) | Additional notes of the task |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) | Can be one of the following 10(Low), 20(Medium), 30(High), 40(Urgent) |  [optional] |
|**status** | **Integer** |  |  |
|**title** | **String** |  |  |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| _10 | &quot;10&quot; |
| _20 | &quot;20&quot; |
| _30 | &quot;30&quot; |
| _40 | &quot;40&quot; |



