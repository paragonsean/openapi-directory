

# Ticket


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignees** | [**List&lt;Assignee&gt;**](Assignee.md) |  |  [optional] |
|**collectionId** | **String** | The ticket&#39;s collection ID |  [optional] [readonly] |
|**completedAt** | **OffsetDateTime** | When the ticket was completed |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**description** | **String** | The ticket&#39;s description. HTML version of description is mapped if supported by the third-party platform |  [optional] |
|**dueDate** | **OffsetDateTime** | Due date of the ticket |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [readonly] |
|**parentId** | **String** | The ticket&#39;s parent ID |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) | Priority of the ticket |  [optional] |
|**status** | **String** | The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through. |  [optional] |
|**subject** | **String** | Subject of the ticket |  [optional] |
|**tags** | [**List&lt;CollectionTag&gt;**](CollectionTag.md) |  |  [optional] |
|**type** | **String** | The ticket&#39;s type |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| LOW | &quot;low&quot; |
| NORMAL | &quot;normal&quot; |
| HIGH | &quot;high&quot; |
| URGENT | &quot;urgent&quot; |



