

# ModifyCourseWorkAssigneesRequest

Request to modify assignee mode and options of a coursework.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assigneeMode** | [**AssigneeModeEnum**](#AssigneeModeEnum) | Mode of the coursework describing whether it will be assigned to all students or specified individual students. |  [optional] |
|**modifyIndividualStudentsOptions** | [**ModifyIndividualStudentsOptions**](ModifyIndividualStudentsOptions.md) |  |  [optional] |



## Enum: AssigneeModeEnum

| Name | Value |
|---- | -----|
| ASSIGNEE_MODE_UNSPECIFIED | &quot;ASSIGNEE_MODE_UNSPECIFIED&quot; |
| ALL_STUDENTS | &quot;ALL_STUDENTS&quot; |
| INDIVIDUAL_STUDENTS | &quot;INDIVIDUAL_STUDENTS&quot; |



