# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1alpha1ConversationParticipant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dialogflowParticipant** | **String** | Deprecated. Use &#x60;dialogflow_participant_name&#x60; instead. The name of the Dialogflow participant. Format: projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant} | [optional] 
**dialogflowParticipantName** | **String** | The name of the participant provided by Dialogflow. Format: projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant} | [optional] 
**obfuscatedExternalUserId** | **String** | Obfuscated user ID from Dialogflow. | [optional] 
**role** | **String** | The role of the participant. | [optional] 
**userId** | **String** | A user-specified ID representing the participant. | [optional] 



## Enum: RoleEnum


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `HUMAN_AGENT` (value: `"HUMAN_AGENT"`)

* `AUTOMATED_AGENT` (value: `"AUTOMATED_AGENT"`)

* `END_USER` (value: `"END_USER"`)

* `ANY_AGENT` (value: `"ANY_AGENT"`)




