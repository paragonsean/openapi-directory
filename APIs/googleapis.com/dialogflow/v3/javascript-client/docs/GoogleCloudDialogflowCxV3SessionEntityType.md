# DialogflowApi.GoogleCloudDialogflowCxV3SessionEntityType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**[GoogleCloudDialogflowCxV3EntityTypeEntity]**](GoogleCloudDialogflowCxV3EntityTypeEntity.md) | Required. The collection of entities to override or supplement the custom entity type. | [optional] 
**entityOverrideMode** | **String** | Required. Indicates whether the additional data should override or supplement the custom entity type definition. | [optional] 
**name** | **String** | Required. The unique identifier of the session entity type. Format: &#x60;projects//locations//agents//sessions//entityTypes/&#x60; or &#x60;projects//locations//agents//environments//sessions//entityTypes/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. | [optional] 



## Enum: EntityOverrideModeEnum


* `UNSPECIFIED` (value: `"ENTITY_OVERRIDE_MODE_UNSPECIFIED"`)

* `OVERRIDE` (value: `"ENTITY_OVERRIDE_MODE_OVERRIDE"`)

* `SUPPLEMENT` (value: `"ENTITY_OVERRIDE_MODE_SUPPLEMENT"`)




