# FlatApi.AssignmentSubmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment** | **String** | Unique identifier of the assignment | [optional] 
**attachments** | [**[MediaAttachment]**](MediaAttachment.md) |  | [optional] 
**classroom** | **String** | Unique identifier of the classroom where the assignment was posted  | [optional] 
**creationDate** | **String** | The date when the submission was created | [optional] 
**creator** | **String** | The User identifier of the student who created the submission | [optional] 
**draftGrade** | **Number** | Optional grade. If unset, no grade was set. This value is only visible by the teacher, and we will be set to &#x60;grade&#x60; once the teacher returns the submission | [optional] 
**googleClassroom** | [**GoogleClassroomSubmission**](GoogleClassroomSubmission.md) |  | [optional] 
**grade** | **Number** | Optional grade. If unset, no grade was set. | [optional] 
**id** | **String** | Unique identifier of the submission | [optional] 
**maxPoints** | **Number** | Optional max points for the grade. If set, a corresponding &#x60;draftGrade&#x60; or &#x60;grade&#x60; will be set. | [optional] 
**microsoftGraph** | [**MicrosoftGraphSubmission**](MicrosoftGraphSubmission.md) |  | [optional] 
**returnCreator** | **String** | The User unique identifier of the teacher who returned the submission  | [optional] 
**returnDate** | **String** | The date when the teacher returned the work | [optional] 
**state** | [**AssignmentSubmissionState**](AssignmentSubmissionState.md) |  | [optional] 
**submissionDate** | **String** | The date when the student submitted his work | [optional] 


