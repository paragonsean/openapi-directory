

# Invitation

An invitation to join a course.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**courseId** | **String** | Identifier of the course to invite the user to. |  [optional] |
|**id** | **String** | Identifier assigned by Classroom. Read-only. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Role to invite the user to have. Must not be &#x60;COURSE_ROLE_UNSPECIFIED&#x60;. |  [optional] |
|**userId** | **String** | Identifier of the invited user. When specified as a parameter of a request, this identifier can be set to one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| COURSE_ROLE_UNSPECIFIED | &quot;COURSE_ROLE_UNSPECIFIED&quot; |
| STUDENT | &quot;STUDENT&quot; |
| TEACHER | &quot;TEACHER&quot; |
| OWNER | &quot;OWNER&quot; |



