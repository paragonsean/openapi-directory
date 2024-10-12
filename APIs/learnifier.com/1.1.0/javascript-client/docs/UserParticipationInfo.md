# Learnifier.UserParticipationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessLink** | **String** | A link to access this particular participation. The link requires the user to login. Users that access the platform the first time must set a password. This value is null if this participation is not activated.  | [optional] 
**activated** | **Boolean** | True if this participation has been activated and can be used | [optional] 
**activitiesCompleted** | **Number** | The number of activities completed | [optional] 
**activitiesTotal** | **Number** | The total number of activities | [optional] 
**errorMessage** | **String** | An optional error message that may describe why the participation is in error state. | [optional] 
**expiration** | **Date** | The timestamp when this participation will expire. Expiration never happens if this value is *null*. | [optional] 
**externalId** | **String** | The external id (foreign key). Must not exceed 255 characters. | [optional] 
**firstAccess** | **Date** | The timestamp when the participant accessed the project for the first time. This value can be null | [optional] 
**firstActivation** | **Date** | The timestamp when this participation was first activated. This value can be null | [optional] 
**firstMail** | **Date** | The timestamp when the first mail was sent to this participant. This value can be null | [optional] 
**id** | **Number** | Participation id | [optional] 
**inError** | **Boolean** | True if this participation is in an error state. The user is not able to access participations that are in error state. | [optional] 
**lastAccess** | **Date** | The timestamp when the participant accessed the project the last time. This value can be null | [optional] 
**lastActivation** | **Date** | The timestamp when this participation was last activated. This value can be null | [optional] 
**lastMail** | **Date** | The timestamp when the last mail was sent to this participant. This value can be null | [optional] 
**projectId** | **Number** | Project id | [optional] 
**projectName** | **String** | The internal name of the project | [optional] 
**projectOrgId** | **Number** | The organization id | [optional] 
**projectStatus** | **String** | Project status. Can be either ACTIVATED, NEW or DISABLED | [optional] 
**projectThumbnail** | **String** | An url to the project thumbnail. This url can be accessed by anyone. | [optional] 
**projectUserTitle** | **String** | The title presented to participants | [optional] 



## Enum: ProjectStatusEnum


* `ACTIVATED` (value: `"ACTIVATED"`)

* `NEW` (value: `"NEW"`)

* `DISABLED` (value: `"DISABLED"`)




