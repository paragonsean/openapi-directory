

# UserParticipationInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessLink** | **String** | A link to access this particular participation. The link requires the user to login. Users that access the platform the first time must set a password. This value is null if this participation is not activated.  |  [optional] |
|**activated** | **Boolean** | True if this participation has been activated and can be used |  [optional] |
|**activitiesCompleted** | **BigDecimal** | The number of activities completed |  [optional] |
|**activitiesTotal** | **BigDecimal** | The total number of activities |  [optional] |
|**errorMessage** | **String** | An optional error message that may describe why the participation is in error state. |  [optional] |
|**expiration** | **OffsetDateTime** | The timestamp when this participation will expire. Expiration never happens if this value is *null*. |  [optional] |
|**externalId** | **String** | The external id (foreign key). Must not exceed 255 characters. |  [optional] |
|**firstAccess** | **OffsetDateTime** | The timestamp when the participant accessed the project for the first time. This value can be null |  [optional] |
|**firstActivation** | **OffsetDateTime** | The timestamp when this participation was first activated. This value can be null |  [optional] |
|**firstMail** | **OffsetDateTime** | The timestamp when the first mail was sent to this participant. This value can be null |  [optional] |
|**id** | **Long** | Participation id |  [optional] |
|**inError** | **Boolean** | True if this participation is in an error state. The user is not able to access participations that are in error state. |  [optional] |
|**lastAccess** | **OffsetDateTime** | The timestamp when the participant accessed the project the last time. This value can be null |  [optional] |
|**lastActivation** | **OffsetDateTime** | The timestamp when this participation was last activated. This value can be null |  [optional] |
|**lastMail** | **OffsetDateTime** | The timestamp when the last mail was sent to this participant. This value can be null |  [optional] |
|**projectId** | **Long** | Project id |  [optional] |
|**projectName** | **String** | The internal name of the project |  [optional] |
|**projectOrgId** | **Long** | The organization id |  [optional] |
|**projectStatus** | [**ProjectStatusEnum**](#ProjectStatusEnum) | Project status. Can be either ACTIVATED, NEW or DISABLED |  [optional] |
|**projectThumbnail** | **String** | An url to the project thumbnail. This url can be accessed by anyone. |  [optional] |
|**projectUserTitle** | **String** | The title presented to participants |  [optional] |



## Enum: ProjectStatusEnum

| Name | Value |
|---- | -----|
| ACTIVATED | &quot;ACTIVATED&quot; |
| NEW | &quot;NEW&quot; |
| DISABLED | &quot;DISABLED&quot; |



