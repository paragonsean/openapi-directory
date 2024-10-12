# IssueTrackingApi.Ticket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**[Assignee]**](Assignee.md) |  | [optional] 
**collectionId** | **String** | The ticket&#39;s collection ID | [optional] [readonly] 
**completedAt** | **Date** | When the ticket was completed | [optional] [readonly] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**description** | **String** | The ticket&#39;s description. HTML version of description is mapped if supported by the third-party platform | [optional] 
**dueDate** | **Date** | Due date of the ticket | [optional] 
**id** | **String** | A unique identifier for an object. | [readonly] 
**parentId** | **String** | The ticket&#39;s parent ID | [optional] 
**priority** | **String** | Priority of the ticket | [optional] 
**status** | **String** | The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through. | [optional] 
**subject** | **String** | Subject of the ticket | [optional] 
**tags** | [**[CollectionTag]**](CollectionTag.md) |  | [optional] 
**type** | **String** | The ticket&#39;s type | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 



## Enum: PriorityEnum


* `low` (value: `"low"`)

* `normal` (value: `"normal"`)

* `high` (value: `"high"`)

* `urgent` (value: `"urgent"`)




