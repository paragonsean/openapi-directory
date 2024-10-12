

# ModifyAnnouncementAssigneesRequest

Request to modify assignee mode and options of an announcement.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assigneeMode** | [**AssigneeModeEnum**](#AssigneeModeEnum) | Mode of the announcement describing whether it is accessible by all students or specified individual students. |  [optional] |
|**modifyIndividualStudentsOptions** | [**ModifyIndividualStudentsOptions**](ModifyIndividualStudentsOptions.md) |  |  [optional] |



## Enum: AssigneeModeEnum

| Name | Value |
|---- | -----|
| ASSIGNEE_MODE_UNSPECIFIED | &quot;ASSIGNEE_MODE_UNSPECIFIED&quot; |
| ALL_STUDENTS | &quot;ALL_STUDENTS&quot; |
| INDIVIDUAL_STUDENTS | &quot;INDIVIDUAL_STUDENTS&quot; |



