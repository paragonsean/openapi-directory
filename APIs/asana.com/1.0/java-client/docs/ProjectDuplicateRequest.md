

# ProjectDuplicateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**include** | [**IncludeEnum**](#IncludeEnum) | The elements that will be duplicated to the new project. Tasks are always included. |  [optional] |
|**name** | **String** | The name of the new project. |  |
|**scheduleDates** | [**ProjectDuplicateRequestScheduleDates**](ProjectDuplicateRequestScheduleDates.md) |  |  [optional] |
|**team** | **String** | Sets the team of the new project. If team is not defined, the new project will be in the same team as the the original project. |  [optional] |



## Enum: IncludeEnum

| Name | Value |
|---- | -----|
| MEMBERS | &quot;members&quot; |
| NOTES | &quot;notes&quot; |
| FORMS | &quot;forms&quot; |
| TASK_NOTES | &quot;task_notes&quot; |
| TASK_ASSIGNEE | &quot;task_assignee&quot; |
| TASK_SUBTASKS | &quot;task_subtasks&quot; |
| TASK_ATTACHMENTS | &quot;task_attachments&quot; |
| TASK_DATES | &quot;task_dates&quot; |
| TASK_DEPENDENCIES | &quot;task_dependencies&quot; |
| TASK_FOLLOWERS | &quot;task_followers&quot; |
| TASK_TAGS | &quot;task_tags&quot; |
| TASK_PROJECTS | &quot;task_projects&quot; |



