# DialogflowApi.GoogleCloudDialogflowV2beta1Participant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentsMetadataFilters** | **{String: String}** | Optional. Key-value filters on the metadata of documents returned by article suggestion. If specified, article suggestion only returns suggested documents that match all filters in their Document.metadata. Multiple values for a metadata key should be concatenated by comma. For example, filters to match all documents that have &#39;US&#39; or &#39;CA&#39; in their market metadata values and &#39;agent&#39; in their user metadata values will be &#x60;&#x60;&#x60; documents_metadata_filters { key: \&quot;market\&quot; value: \&quot;US,CA\&quot; } documents_metadata_filters { key: \&quot;user\&quot; value: \&quot;agent\&quot; } &#x60;&#x60;&#x60; | [optional] 
**name** | **String** | Optional. The unique identifier of this participant. Format: &#x60;projects//locations//conversations//participants/&#x60;. | [optional] 
**obfuscatedExternalUserId** | **String** | Optional. Obfuscated user id that should be associated with the created participant. You can specify a user id as follows: 1. If you set this field in CreateParticipantRequest or UpdateParticipantRequest, Dialogflow adds the obfuscated user id with the participant. 2. If you set this field in AnalyzeContent or StreamingAnalyzeContent, Dialogflow will update Participant.obfuscated_external_user_id. Dialogflow uses this user id for billing and measurement. If a user with the same obfuscated_external_user_id is created in a later conversation, Dialogflow will know it&#39;s the same user. Dialogflow also uses this user id for Agent Assist suggestion personalization. For example, Dialogflow can use it to provide personalized smart reply suggestions for this user. Note: * Please never pass raw user ids to Dialogflow. Always obfuscate your user id first. * Dialogflow only accepts a UTF-8 encoded string, e.g., a hex digest of a hash function like SHA-512. * The length of the user id must be &lt;&#x3D; 256 characters. | [optional] 
**role** | **String** | Immutable. The role this participant plays in the conversation. This field must be set during participant creation and is then immutable. | [optional] 



## Enum: RoleEnum


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `HUMAN_AGENT` (value: `"HUMAN_AGENT"`)

* `AUTOMATED_AGENT` (value: `"AUTOMATED_AGENT"`)

* `END_USER` (value: `"END_USER"`)




