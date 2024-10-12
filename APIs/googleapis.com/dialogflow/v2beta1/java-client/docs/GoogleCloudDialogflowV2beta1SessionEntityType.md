

# GoogleCloudDialogflowV2beta1SessionEntityType

A session represents a conversation between a Dialogflow agent and an end-user. You can create special entities, called session entities, during a session. Session entities can extend or replace custom entity types and only exist during the session that they were created for. All session data, including session entities, is stored by Dialogflow for 20 minutes. For more information, see the [session entity guide](https://cloud.google.com/dialogflow/docs/entities-session).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entities** | [**List&lt;GoogleCloudDialogflowV2beta1EntityTypeEntity&gt;**](GoogleCloudDialogflowV2beta1EntityTypeEntity.md) | Required. The collection of entities associated with this session entity type. |  [optional] |
|**entityOverrideMode** | [**EntityOverrideModeEnum**](#EntityOverrideModeEnum) | Required. Indicates whether the additional data should override or supplement the custom entity type definition. |  [optional] |
|**name** | **String** | Required. The unique identifier of this session entity type. Supported formats: - &#x60;projects//agent/sessions//entityTypes/&#x60; - &#x60;projects//locations//agent/sessions//entityTypes/&#x60; - &#x60;projects//agent/environments//users//sessions//entityTypes/&#x60; - &#x60;projects//locations//agent/environments/ /users//sessions//entityTypes/&#x60; If &#x60;Location ID&#x60; is not specified we assume default &#39;us&#39; location. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. If &#x60;User ID&#x60; is not specified, we assume default &#39;-&#39; user. &#x60;&#x60; must be the display name of an existing entity type in the same agent that will be overridden or supplemented. |  [optional] |



## Enum: EntityOverrideModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITY_OVERRIDE_MODE_UNSPECIFIED&quot; |
| OVERRIDE | &quot;ENTITY_OVERRIDE_MODE_OVERRIDE&quot; |
| SUPPLEMENT | &quot;ENTITY_OVERRIDE_MODE_SUPPLEMENT&quot; |



