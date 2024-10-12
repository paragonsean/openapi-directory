# GoogleClassroomApi.CourseWorkMaterial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateLink** | **String** | Absolute link to this course work material in the Classroom web UI. This is only populated if &#x60;state&#x60; is &#x60;PUBLISHED&#x60;. Read-only. | [optional] 
**assigneeMode** | **String** | Assignee mode of the course work material. If unspecified, the default value is &#x60;ALL_STUDENTS&#x60;. | [optional] 
**courseId** | **String** | Identifier of the course. Read-only. | [optional] 
**creationTime** | **String** | Timestamp when this course work material was created. Read-only. | [optional] 
**creatorUserId** | **String** | Identifier for the user that created the course work material. Read-only. | [optional] 
**description** | **String** | Optional description of this course work material. The text must be a valid UTF-8 string containing no more than 30,000 characters. | [optional] 
**id** | **String** | Classroom-assigned identifier of this course work material, unique per course. Read-only. | [optional] 
**individualStudentsOptions** | [**IndividualStudentsOptions**](IndividualStudentsOptions.md) |  | [optional] 
**materials** | [**[Material]**](Material.md) | Additional materials. A course work material must have no more than 20 material items. | [optional] 
**scheduledTime** | **String** | Optional timestamp when this course work material is scheduled to be published. | [optional] 
**state** | **String** | Status of this course work material. If unspecified, the default state is &#x60;DRAFT&#x60;. | [optional] 
**title** | **String** | Title of this course work material. The title must be a valid UTF-8 string containing between 1 and 3000 characters. | [optional] 
**topicId** | **String** | Identifier for the topic that this course work material is associated with. Must match an existing topic in the course. | [optional] 
**updateTime** | **String** | Timestamp of the most recent change to this course work material. Read-only. | [optional] 



## Enum: AssigneeModeEnum


* `ASSIGNEE_MODE_UNSPECIFIED` (value: `"ASSIGNEE_MODE_UNSPECIFIED"`)

* `ALL_STUDENTS` (value: `"ALL_STUDENTS"`)

* `INDIVIDUAL_STUDENTS` (value: `"INDIVIDUAL_STUDENTS"`)





## Enum: StateEnum


* `COURSEWORK_MATERIAL_STATE_UNSPECIFIED` (value: `"COURSEWORK_MATERIAL_STATE_UNSPECIFIED"`)

* `PUBLISHED` (value: `"PUBLISHED"`)

* `DRAFT` (value: `"DRAFT"`)

* `DELETED` (value: `"DELETED"`)




