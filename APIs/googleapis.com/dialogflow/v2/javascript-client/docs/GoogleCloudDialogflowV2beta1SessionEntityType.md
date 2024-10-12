# DialogflowApi.GoogleCloudDialogflowV2beta1SessionEntityType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**[GoogleCloudDialogflowV2beta1EntityTypeEntity]**](GoogleCloudDialogflowV2beta1EntityTypeEntity.md) | Required. The collection of entities associated with this session entity type. | [optional] 
**entityOverrideMode** | **String** | Required. Indicates whether the additional data should override or supplement the custom entity type definition. | [optional] 
**name** | **String** | Required. The unique identifier of this session entity type. Supported formats: - &#x60;projects//agent/sessions//entityTypes/&#x60; - &#x60;projects//locations//agent/sessions//entityTypes/&#x60; - &#x60;projects//agent/environments//users//sessions//entityTypes/&#x60; - &#x60;projects//locations//agent/environments/ /users//sessions//entityTypes/&#x60; If &#x60;Location ID&#x60; is not specified we assume default &#39;us&#39; location. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. If &#x60;User ID&#x60; is not specified, we assume default &#39;-&#39; user. &#x60;&#x60; must be the display name of an existing entity type in the same agent that will be overridden or supplemented. | [optional] 



## Enum: EntityOverrideModeEnum


* `UNSPECIFIED` (value: `"ENTITY_OVERRIDE_MODE_UNSPECIFIED"`)

* `OVERRIDE` (value: `"ENTITY_OVERRIDE_MODE_OVERRIDE"`)

* `SUPPLEMENT` (value: `"ENTITY_OVERRIDE_MODE_SUPPLEMENT"`)




