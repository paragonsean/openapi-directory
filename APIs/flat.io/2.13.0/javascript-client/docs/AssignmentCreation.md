# FlatApi.AssignmentCreation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignedStudents** | **[String]** | Identifiers for the students that have access to the assignment | [optional] 
**assigneeMode** | **String** | Possible modes of assigning assignments | [optional] 
**attachments** | [**[ClassAttachmentCreation]**](ClassAttachmentCreation.md) |  | [optional] 
**cover** | **String** | The URL of the cover to display | [optional] 
**coverFile** | **String** | The id of the cover to display | [optional] 
**description** | **String** | Description and content of the assignment | [optional] 
**dueDate** | **Date** | The due date of this assignment, late submissions will be marked as paste due. If not set, the assignment won&#39;t have a due date.  | [optional] 
**googleClassroom** | [**AssignmentCreationGoogleClassroom**](AssignmentCreationGoogleClassroom.md) |  | [optional] 
**maxPoints** | **Number** | If set, the grading will be enabled for the assignement with this value as the maximum of points  | [optional] 
**microsoftGraph** | [**AssignmentCreationMicrosoftGraph**](AssignmentCreationMicrosoftGraph.md) |  | [optional] 
**nbPlaybackAuthorized** | **Number** | The number of playback authorized on the scores of the assignment. | [optional] 
**scheduledDate** | **Date** | The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class.  | [optional] 
**state** | **String** | State of the assignment | [optional] 
**title** | **String** | Title of the assignment | [optional] 
**toolset** | **String** | The id of the associated toolset | [optional] 
**type** | [**AssignmentType**](AssignmentType.md) |  | [optional] 



## Enum: AssigneeModeEnum


* `everyone` (value: `"everyone"`)

* `selected` (value: `"selected"`)





## Enum: StateEnum


* `draft` (value: `"draft"`)

* `active` (value: `"active"`)




