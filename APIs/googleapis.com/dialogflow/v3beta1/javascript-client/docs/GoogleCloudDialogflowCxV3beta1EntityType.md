# DialogflowApi.GoogleCloudDialogflowCxV3beta1EntityType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoExpansionMode** | **String** | Indicates whether the entity type can be automatically expanded. | [optional] 
**displayName** | **String** | Required. The human-readable name of the entity type, unique within the agent. | [optional] 
**enableFuzzyExtraction** | **Boolean** | Enables fuzzy entity extraction during classification. | [optional] 
**entities** | [**[GoogleCloudDialogflowCxV3beta1EntityTypeEntity]**](GoogleCloudDialogflowCxV3beta1EntityTypeEntity.md) | The collection of entity entries associated with the entity type. | [optional] 
**excludedPhrases** | [**[GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase]**](GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase.md) | Collection of exceptional words and phrases that shouldn&#39;t be matched. For example, if you have a size entity type with entry &#x60;giant&#x60;(an adjective), you might consider adding &#x60;giants&#x60;(a noun) as an exclusion. If the kind of entity type is &#x60;KIND_MAP&#x60;, then the phrases specified by entities and excluded phrases should be mutually exclusive. | [optional] 
**kind** | **String** | Required. Indicates the kind of entity type. | [optional] 
**name** | **String** | The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType. Format: &#x60;projects//locations//agents//entityTypes/&#x60;. | [optional] 
**redact** | **Boolean** | Indicates whether parameters of the entity type should be redacted in log. If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name during logging. | [optional] 



## Enum: AutoExpansionModeEnum


* `UNSPECIFIED` (value: `"AUTO_EXPANSION_MODE_UNSPECIFIED"`)

* `DEFAULT` (value: `"AUTO_EXPANSION_MODE_DEFAULT"`)





## Enum: KindEnum


* `UNSPECIFIED` (value: `"KIND_UNSPECIFIED"`)

* `MAP` (value: `"KIND_MAP"`)

* `LIST` (value: `"KIND_LIST"`)

* `REGEXP` (value: `"KIND_REGEXP"`)




