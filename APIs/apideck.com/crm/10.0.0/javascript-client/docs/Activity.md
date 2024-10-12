# CrmApi.Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account related to the activity | [optional] 
**activityDate** | **String** | The date of the activity | [optional] 
**activityDatetime** | **String** | The date and time of the activity | [optional] 
**allDayEvent** | **Boolean** | Whether the Activity is an all day event or not | [optional] 
**archived** | **Boolean** | Whether the activity is archived or not | [optional] 
**assetId** | **String** | The asset related to the activity | [optional] 
**attendees** | [**[ActivityAttendee]**](ActivityAttendee.md) |  | [optional] 
**campaignId** | **String** | The campaign related to the activity | [optional] 
**caseId** | **String** | The case related to the activity | [optional] 
**child** | **Boolean** | Whether the activity is a child of another activity or not | [optional] 
**companyId** | **String** | The company related to the activity | [optional] 
**contactId** | **String** | The contact related to the activity | [optional] 
**contractId** | **String** | The contract related to the activity | [optional] 
**createdAt** | **String** | The date and time when the activity was created | [optional] [readonly] 
**createdBy** | **String** | The user who created the activity | [optional] [readonly] 
**customFields** | [**[CustomField]**](CustomField.md) | Custom fields of the activity | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**customObjectId** | **String** | The custom object related to the activity | [optional] 
**deleted** | **Boolean** | Whether the activity is deleted or not | [optional] 
**description** | **String** | A description of the activity | [optional] 
**done** | **Boolean** | Whether the Activity is done or not | [optional] 
**downstreamId** | **String** | The third-party API ID of original entity | [optional] [readonly] 
**durationMinutes** | **Number** | The duration of the activity in minutes | [optional] [readonly] 
**durationSeconds** | **Number** | The duration of the activity in seconds | [optional] 
**endDate** | **String** | The end date of the activity | [optional] 
**endDatetime** | **String** | The end date and time of the activity | [optional] 
**eventSubType** | **String** | The sub type of the group event | [optional] 
**groupEvent** | **Boolean** | Whether the Activity is a group event or not | [optional] 
**groupEventType** | **String** | The type of the group event | [optional] 
**id** | **String** | The unique identifier of the activity | [optional] [readonly] 
**leadId** | **String** | The lead related to the activity | [optional] 
**location** | **String** | The location of the activity | [optional] 
**locationAddress** | [**Address**](Address.md) |  | [optional] 
**note** | **String** | An internal note about the activity | [optional] 
**opportunityId** | **String** | The opportunity related to the activity | [optional] 
**ownerId** | **String** | The owner of the activity | [optional] 
**_private** | **Boolean** | Whether the Activity is private or not | [optional] 
**productId** | **String** | The product related to the activity | [optional] 
**recurrent** | **Boolean** | Whether the activity is recurrent or not | [optional] 
**reminderDatetime** | **String** | The date and time of the reminder | [optional] 
**reminderSet** | **Boolean** | Whether the reminder is set or not | [optional] 
**showAs** | **String** |  | [optional] 
**solutionId** | **String** | The solution related to the activity | [optional] 
**startDatetime** | **String** | The start date and time of the activity | [optional] 
**title** | **String** | The title of the activity | [optional] 
**type** | **String** | The type of the activity | 
**updatedAt** | **String** | The date and time when the activity was last updated | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the activity | [optional] [readonly] 
**userId** | **String** | The user related to the activity | [optional] 
**videoConferenceId** | **String** | The ID of the video conference | [optional] 
**videoConferenceUrl** | **String** | The URL of the video conference | [optional] 



## Enum: ShowAsEnum


* `free` (value: `"free"`)

* `busy` (value: `"busy"`)





## Enum: TypeEnum


* `call` (value: `"call"`)

* `meeting` (value: `"meeting"`)

* `email` (value: `"email"`)

* `note` (value: `"note"`)

* `task` (value: `"task"`)

* `deadline` (value: `"deadline"`)

* `send-letter` (value: `"send-letter"`)

* `send-quote` (value: `"send-quote"`)

* `other` (value: `"other"`)




