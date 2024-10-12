# GoogleClassroomApi.Announcement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateLink** | **String** | Absolute link to this announcement in the Classroom web UI. This is only populated if &#x60;state&#x60; is &#x60;PUBLISHED&#x60;. Read-only. | [optional] 
**assigneeMode** | **String** | Assignee mode of the announcement. If unspecified, the default value is &#x60;ALL_STUDENTS&#x60;. | [optional] 
**courseId** | **String** | Identifier of the course. Read-only. | [optional] 
**creationTime** | **String** | Timestamp when this announcement was created. Read-only. | [optional] 
**creatorUserId** | **String** | Identifier for the user that created the announcement. Read-only. | [optional] 
**id** | **String** | Classroom-assigned identifier of this announcement, unique per course. Read-only. | [optional] 
**individualStudentsOptions** | [**IndividualStudentsOptions**](IndividualStudentsOptions.md) |  | [optional] 
**materials** | [**[Material]**](Material.md) | Additional materials. Announcements must have no more than 20 material items. | [optional] 
**scheduledTime** | **String** | Optional timestamp when this announcement is scheduled to be published. | [optional] 
**state** | **String** | Status of this announcement. If unspecified, the default state is &#x60;DRAFT&#x60;. | [optional] 
**text** | **String** | Description of this announcement. The text must be a valid UTF-8 string containing no more than 30,000 characters. | [optional] 
**updateTime** | **String** | Timestamp of the most recent change to this announcement. Read-only. | [optional] 



## Enum: AssigneeModeEnum


* `ASSIGNEE_MODE_UNSPECIFIED` (value: `"ASSIGNEE_MODE_UNSPECIFIED"`)

* `ALL_STUDENTS` (value: `"ALL_STUDENTS"`)

* `INDIVIDUAL_STUDENTS` (value: `"INDIVIDUAL_STUDENTS"`)





## Enum: StateEnum


* `ANNOUNCEMENT_STATE_UNSPECIFIED` (value: `"ANNOUNCEMENT_STATE_UNSPECIFIED"`)

* `PUBLISHED` (value: `"PUBLISHED"`)

* `DRAFT` (value: `"DRAFT"`)

* `DELETED` (value: `"DELETED"`)




