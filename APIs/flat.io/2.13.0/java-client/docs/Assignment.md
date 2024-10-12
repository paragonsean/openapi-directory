

# Assignment

Assignment details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;MediaAttachment&gt;**](MediaAttachment.md) |  |  [optional] |
|**canvas** | [**AssignmentCanvas**](AssignmentCanvas.md) |  |  [optional] |
|**classroom** | **String** | The unique identifier of the class where this assignment was posted |  [optional] |
|**cover** | **String** | The URL of the cover to display |  [optional] |
|**coverFile** | **String** | The id of the cover to display |  [optional] |
|**creationDate** | **OffsetDateTime** | The creation date of this assignment |  [optional] |
|**creator** | **String** | The User unique identifier of the creator of this assignment  |  [optional] |
|**description** | **String** | Description and content of the assignment |  [optional] |
|**dueDate** | **OffsetDateTime** | The due date of this assignment, late submissions will be marked as paste due.  |  [optional] |
|**googleClassroom** | [**GoogleClassroomCoursework**](GoogleClassroomCoursework.md) |  |  [optional] |
|**lti** | [**AssignmentLti**](AssignmentLti.md) |  |  [optional] |
|**maxPoints** | **BigDecimal** | If set, the grading will be enabled for the assignement  |  [optional] |
|**mfc** | [**AssignmentMfc**](AssignmentMfc.md) |  |  [optional] |
|**microsoftGraph** | [**MicrosoftGraphAssignment**](MicrosoftGraphAssignment.md) |  |  [optional] |
|**scheduledDate** | **OffsetDateTime** | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class.  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the assignment |  [optional] |
|**submissions** | [**List&lt;AssignmentSubmission&gt;**](AssignmentSubmission.md) |  |  [optional] |
|**title** | **String** | Title of the assignment |  [optional] |
|**type** | **AssignmentType** |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



