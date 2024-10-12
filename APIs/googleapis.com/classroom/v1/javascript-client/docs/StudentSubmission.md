# GoogleClassroomApi.StudentSubmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateLink** | **String** | Absolute link to the submission in the Classroom web UI. Read-only. | [optional] 
**assignedGrade** | **Number** | Optional grade. If unset, no grade was set. This value must be non-negative. Decimal (that is, non-integer) values are allowed, but are rounded to two decimal places. This may be modified only by course teachers. | [optional] 
**assignmentSubmission** | [**AssignmentSubmission**](AssignmentSubmission.md) |  | [optional] 
**associatedWithDeveloper** | **Boolean** | Whether this student submission is associated with the Developer Console project making the request. See CreateCourseWork for more details. Read-only. | [optional] 
**courseId** | **String** | Identifier of the course. Read-only. | [optional] 
**courseWorkId** | **String** | Identifier for the course work this corresponds to. Read-only. | [optional] 
**courseWorkType** | **String** | Type of course work this submission is for. Read-only. | [optional] 
**creationTime** | **String** | Creation time of this submission. This may be unset if the student has not accessed this item. Read-only. | [optional] 
**draftGrade** | **Number** | Optional pending grade. If unset, no grade was set. This value must be non-negative. Decimal (that is, non-integer) values are allowed, but are rounded to two decimal places. This is only visible to and modifiable by course teachers. | [optional] 
**id** | **String** | Classroom-assigned Identifier for the student submission. This is unique among submissions for the relevant course work. Read-only. | [optional] 
**late** | **Boolean** | Whether this submission is late. Read-only. | [optional] 
**multipleChoiceSubmission** | [**MultipleChoiceSubmission**](MultipleChoiceSubmission.md) |  | [optional] 
**shortAnswerSubmission** | [**ShortAnswerSubmission**](ShortAnswerSubmission.md) |  | [optional] 
**state** | **String** | State of this submission. Read-only. | [optional] 
**submissionHistory** | [**[SubmissionHistory]**](SubmissionHistory.md) | The history of the submission (includes state and grade histories). Read-only. | [optional] 
**updateTime** | **String** | Last update time of this submission. This may be unset if the student has not accessed this item. Read-only. | [optional] 
**userId** | **String** | Identifier for the student that owns this submission. Read-only. | [optional] 



## Enum: CourseWorkTypeEnum


* `COURSE_WORK_TYPE_UNSPECIFIED` (value: `"COURSE_WORK_TYPE_UNSPECIFIED"`)

* `ASSIGNMENT` (value: `"ASSIGNMENT"`)

* `SHORT_ANSWER_QUESTION` (value: `"SHORT_ANSWER_QUESTION"`)

* `MULTIPLE_CHOICE_QUESTION` (value: `"MULTIPLE_CHOICE_QUESTION"`)





## Enum: StateEnum


* `SUBMISSION_STATE_UNSPECIFIED` (value: `"SUBMISSION_STATE_UNSPECIFIED"`)

* `NEW` (value: `"NEW"`)

* `CREATED` (value: `"CREATED"`)

* `TURNED_IN` (value: `"TURNED_IN"`)

* `RETURNED` (value: `"RETURNED"`)

* `RECLAIMED_BY_STUDENT` (value: `"RECLAIMED_BY_STUDENT"`)




