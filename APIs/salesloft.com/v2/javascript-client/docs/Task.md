# SalesLoftPlatform.Task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completedAt** | **Date** | Datetime of when the task was completed, ISO-8601 datetime format required | [optional] 
**completedBy** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**createdAt** | **Date** | Datetime of when the Task was created | [optional] 
**createdByUser** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**currentState** | **String** | The state of the task. Valid states are: scheduled, completed | [optional] 
**description** | **String** | A description of the task recorded for person at completion time | [optional] 
**dueAt** | **Date** | Datetime of when the Task is due, can be null.  ISO-8601 datetime format required | [optional] 
**dueDate** | **Date** | Date of when the Task is due, ISO-8601 date format required | [optional] 
**id** | **Number** | ID of Task | [optional] 
**person** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**remindAt** | **Date** | Datetime of when the user will be reminded of the task, ISO-8601 datetime format required | [optional] 
**subject** | **String** | Subject line of the task | [optional] 
**taskType** | **String** | The type of the task.  Valid types are: call, email, general | [optional] 
**updatedAt** | **Date** | Datetime of when the Task was last updated | [optional] 
**user** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 


