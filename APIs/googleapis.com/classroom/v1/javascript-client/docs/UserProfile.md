# GoogleClassroomApi.UserProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emailAddress** | **String** | Email address of the user. Must request &#x60;https://www.googleapis.com/auth/classroom.profile.emails&#x60; scope for this field to be populated in a response body. Read-only. | [optional] 
**id** | **String** | Identifier of the user. Read-only. | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 
**permissions** | [**[GlobalPermission]**](GlobalPermission.md) | Global permissions of the user. Read-only. | [optional] 
**photoUrl** | **String** | URL of user&#39;s profile photo. Must request &#x60;https://www.googleapis.com/auth/classroom.profile.photos&#x60; scope for this field to be populated in a response body. Read-only. | [optional] 
**verifiedTeacher** | **Boolean** | Represents whether a Google Workspace for Education user&#39;s domain administrator has explicitly verified them as being a teacher. This field is always false if the user is not a member of a Google Workspace for Education domain. Read-only | [optional] 


