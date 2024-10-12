# FlatApi.Assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[MediaAttachment]**](MediaAttachment.md) |  | [optional] 
**canvas** | [**AssignmentCanvas**](AssignmentCanvas.md) |  | [optional] 
**classroom** | **String** | The unique identifier of the class where this assignment was posted | [optional] 
**cover** | **String** | The URL of the cover to display | [optional] 
**coverFile** | **String** | The id of the cover to display | [optional] 
**creationDate** | **Date** | The creation date of this assignment | [optional] 
**creator** | **String** | The User unique identifier of the creator of this assignment  | [optional] 
**description** | **String** | Description and content of the assignment | [optional] 
**dueDate** | **Date** | The due date of this assignment, late submissions will be marked as paste due.  | [optional] 
**googleClassroom** | [**GoogleClassroomCoursework**](GoogleClassroomCoursework.md) |  | [optional] 
**lti** | [**AssignmentLti**](AssignmentLti.md) |  | [optional] 
**maxPoints** | **Number** | If set, the grading will be enabled for the assignement  | [optional] 
**mfc** | [**AssignmentMfc**](AssignmentMfc.md) |  | [optional] 
**microsoftGraph** | [**MicrosoftGraphAssignment**](MicrosoftGraphAssignment.md) |  | [optional] 
**scheduledDate** | **Date** | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class.  | [optional] 
**state** | **String** | State of the assignment | [optional] 
**submissions** | [**[AssignmentSubmission]**](AssignmentSubmission.md) |  | [optional] 
**title** | **String** | Title of the assignment | [optional] 
**type** | [**AssignmentType**](AssignmentType.md) |  | [optional] 



## Enum: StateEnum


* `draft` (value: `"draft"`)

* `active` (value: `"active"`)

* `archived` (value: `"archived"`)




