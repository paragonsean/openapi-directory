

# AssignmentCreation

Assignment creation details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignedStudents** | **List&lt;String&gt;** | Identifiers for the students that have access to the assignment |  [optional] |
|**assigneeMode** | [**AssigneeModeEnum**](#AssigneeModeEnum) | Possible modes of assigning assignments |  [optional] |
|**attachments** | [**List&lt;ClassAttachmentCreation&gt;**](ClassAttachmentCreation.md) |  |  [optional] |
|**cover** | **String** | The URL of the cover to display |  [optional] |
|**coverFile** | **String** | The id of the cover to display |  [optional] |
|**description** | **String** | Description and content of the assignment |  [optional] |
|**dueDate** | **OffsetDateTime** | The due date of this assignment, late submissions will be marked as paste due. If not set, the assignment won&#39;t have a due date.  |  [optional] |
|**googleClassroom** | [**AssignmentCreationGoogleClassroom**](AssignmentCreationGoogleClassroom.md) |  |  [optional] |
|**maxPoints** | **BigDecimal** | If set, the grading will be enabled for the assignement with this value as the maximum of points  |  [optional] |
|**microsoftGraph** | [**AssignmentCreationMicrosoftGraph**](AssignmentCreationMicrosoftGraph.md) |  |  [optional] |
|**nbPlaybackAuthorized** | **BigDecimal** | The number of playback authorized on the scores of the assignment. |  [optional] |
|**scheduledDate** | **OffsetDateTime** | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class.  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the assignment |  [optional] |
|**title** | **String** | Title of the assignment |  [optional] |
|**toolset** | **String** | The id of the associated toolset |  [optional] |
|**type** | **AssignmentType** |  |  [optional] |



## Enum: AssigneeModeEnum

| Name | Value |
|---- | -----|
| EVERYONE | &quot;everyone&quot; |
| SELECTED | &quot;selected&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |



