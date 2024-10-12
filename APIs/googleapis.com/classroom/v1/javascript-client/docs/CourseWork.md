# GoogleClassroomApi.CourseWork

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateLink** | **String** | Absolute link to this course work in the Classroom web UI. This is only populated if &#x60;state&#x60; is &#x60;PUBLISHED&#x60;. Read-only. | [optional] 
**assigneeMode** | **String** | Assignee mode of the coursework. If unspecified, the default value is &#x60;ALL_STUDENTS&#x60;. | [optional] 
**assignment** | [**Assignment**](Assignment.md) |  | [optional] 
**associatedWithDeveloper** | **Boolean** | Whether this course work item is associated with the Developer Console project making the request. See CreateCourseWork for more details. Read-only. | [optional] 
**courseId** | **String** | Identifier of the course. Read-only. | [optional] 
**creationTime** | **String** | Timestamp when this course work was created. Read-only. | [optional] 
**creatorUserId** | **String** | Identifier for the user that created the coursework. Read-only. | [optional] 
**description** | **String** | Optional description of this course work. If set, the description must be a valid UTF-8 string containing no more than 30,000 characters. | [optional] 
**dueDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**dueTime** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**gradeCategory** | [**GradeCategory**](GradeCategory.md) |  | [optional] 
**id** | **String** | Classroom-assigned identifier of this course work, unique per course. Read-only. | [optional] 
**individualStudentsOptions** | [**IndividualStudentsOptions**](IndividualStudentsOptions.md) |  | [optional] 
**materials** | [**[Material]**](Material.md) | Additional materials. CourseWork must have no more than 20 material items. | [optional] 
**maxPoints** | **Number** | Maximum grade for this course work. If zero or unspecified, this assignment is considered ungraded. This must be a non-negative integer value. | [optional] 
**multipleChoiceQuestion** | [**MultipleChoiceQuestion**](MultipleChoiceQuestion.md) |  | [optional] 
**scheduledTime** | **String** | Optional timestamp when this course work is scheduled to be published. | [optional] 
**state** | **String** | Status of this course work. If unspecified, the default state is &#x60;DRAFT&#x60;. | [optional] 
**submissionModificationMode** | **String** | Setting to determine when students are allowed to modify submissions. If unspecified, the default value is &#x60;MODIFIABLE_UNTIL_TURNED_IN&#x60;. | [optional] 
**title** | **String** | Title of this course work. The title must be a valid UTF-8 string containing between 1 and 3000 characters. | [optional] 
**topicId** | **String** | Identifier for the topic that this coursework is associated with. Must match an existing topic in the course. | [optional] 
**updateTime** | **String** | Timestamp of the most recent change to this course work. Read-only. | [optional] 
**workType** | **String** | Type of this course work. The type is set when the course work is created and cannot be changed. | [optional] 



## Enum: AssigneeModeEnum


* `ASSIGNEE_MODE_UNSPECIFIED` (value: `"ASSIGNEE_MODE_UNSPECIFIED"`)

* `ALL_STUDENTS` (value: `"ALL_STUDENTS"`)

* `INDIVIDUAL_STUDENTS` (value: `"INDIVIDUAL_STUDENTS"`)





## Enum: StateEnum


* `COURSE_WORK_STATE_UNSPECIFIED` (value: `"COURSE_WORK_STATE_UNSPECIFIED"`)

* `PUBLISHED` (value: `"PUBLISHED"`)

* `DRAFT` (value: `"DRAFT"`)

* `DELETED` (value: `"DELETED"`)





## Enum: SubmissionModificationModeEnum


* `SUBMISSION_MODIFICATION_MODE_UNSPECIFIED` (value: `"SUBMISSION_MODIFICATION_MODE_UNSPECIFIED"`)

* `MODIFIABLE_UNTIL_TURNED_IN` (value: `"MODIFIABLE_UNTIL_TURNED_IN"`)

* `MODIFIABLE` (value: `"MODIFIABLE"`)





## Enum: WorkTypeEnum


* `COURSE_WORK_TYPE_UNSPECIFIED` (value: `"COURSE_WORK_TYPE_UNSPECIFIED"`)

* `ASSIGNMENT` (value: `"ASSIGNMENT"`)

* `SHORT_ANSWER_QUESTION` (value: `"SHORT_ANSWER_QUESTION"`)

* `MULTIPLE_CHOICE_QUESTION` (value: `"MULTIPLE_CHOICE_QUESTION"`)




