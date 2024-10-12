

# GoogleCloudContactcenterinsightsV1ConversationParticipant

The call participant speaking for a given utterance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dialogflowParticipant** | **String** | Deprecated. Use &#x60;dialogflow_participant_name&#x60; instead. The name of the Dialogflow participant. Format: projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant} |  [optional] |
|**dialogflowParticipantName** | **String** | The name of the participant provided by Dialogflow. Format: projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant} |  [optional] |
|**obfuscatedExternalUserId** | **String** | Obfuscated user ID from Dialogflow. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | The role of the participant. |  [optional] |
|**userId** | **String** | A user-specified ID representing the participant. |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;ROLE_UNSPECIFIED&quot; |
| HUMAN_AGENT | &quot;HUMAN_AGENT&quot; |
| AUTOMATED_AGENT | &quot;AUTOMATED_AGENT&quot; |
| END_USER | &quot;END_USER&quot; |
| ANY_AGENT | &quot;ANY_AGENT&quot; |



