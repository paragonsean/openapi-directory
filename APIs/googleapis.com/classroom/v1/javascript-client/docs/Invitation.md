# GoogleClassroomApi.Invitation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courseId** | **String** | Identifier of the course to invite the user to. | [optional] 
**id** | **String** | Identifier assigned by Classroom. Read-only. | [optional] 
**role** | **String** | Role to invite the user to have. Must not be &#x60;COURSE_ROLE_UNSPECIFIED&#x60;. | [optional] 
**userId** | **String** | Identifier of the invited user. When specified as a parameter of a request, this identifier can be set to one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user | [optional] 



## Enum: RoleEnum


* `COURSE_ROLE_UNSPECIFIED` (value: `"COURSE_ROLE_UNSPECIFIED"`)

* `STUDENT` (value: `"STUDENT"`)

* `TEACHER` (value: `"TEACHER"`)

* `OWNER` (value: `"OWNER"`)




