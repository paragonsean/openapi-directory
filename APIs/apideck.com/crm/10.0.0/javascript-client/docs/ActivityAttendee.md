# CrmApi.ActivityAttendee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactId** | **String** | The identifier for a related contact | [optional] [readonly] 
**createdAt** | **Date** | The time the attendee was created (ISO 8601) | [optional] [readonly] 
**emailAddress** | **String** | Email address of the attendee | [optional] 
**firstName** | **String** | First name of the attendee | [optional] 
**id** | **String** | Unique identifier for the attendee | [optional] [readonly] 
**isOrganizer** | **Boolean** | Whether the attendee is the organizer of the activity | [optional] 
**lastName** | **String** | Last name of the attendee | [optional] 
**middleName** | **String** | Middle name of the attendee | [optional] 
**name** | **String** | Full name of the attendee | [optional] 
**prefix** | **String** | Prefix of the attendee | [optional] 
**status** | **String** | Status of the attendee | [optional] 
**suffix** | **String** | Suffix of the attendee | [optional] 
**updatedAt** | **Date** | The last time the attendee was updated (ISO 8601) | [optional] [readonly] 
**userId** | **String** | The identifier for a related user | [optional] [readonly] 



## Enum: StatusEnum


* `accepted` (value: `"accepted"`)

* `tentative` (value: `"tentative"`)

* `declined` (value: `"declined"`)




