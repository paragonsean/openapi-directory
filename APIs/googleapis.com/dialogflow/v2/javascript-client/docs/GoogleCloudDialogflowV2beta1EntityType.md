# DialogflowApi.GoogleCloudDialogflowV2beta1EntityType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoExpansionMode** | **String** | Optional. Indicates whether the entity type can be automatically expanded. | [optional] 
**displayName** | **String** | Required. The name of the entity type. | [optional] 
**enableFuzzyExtraction** | **Boolean** | Optional. Enables fuzzy entity extraction during classification. | [optional] 
**entities** | [**[GoogleCloudDialogflowV2beta1EntityTypeEntity]**](GoogleCloudDialogflowV2beta1EntityTypeEntity.md) | Optional. The collection of entity entries associated with the entity type. | [optional] 
**kind** | **String** | Required. Indicates the kind of entity type. | [optional] 
**name** | **String** | The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType and EntityTypes.BatchUpdateEntityTypes methods. Supported formats: - &#x60;projects//agent/entityTypes/&#x60; - &#x60;projects//locations//agent/entityTypes/&#x60; | [optional] 



## Enum: AutoExpansionModeEnum


* `UNSPECIFIED` (value: `"AUTO_EXPANSION_MODE_UNSPECIFIED"`)

* `DEFAULT` (value: `"AUTO_EXPANSION_MODE_DEFAULT"`)





## Enum: KindEnum


* `UNSPECIFIED` (value: `"KIND_UNSPECIFIED"`)

* `MAP` (value: `"KIND_MAP"`)

* `LIST` (value: `"KIND_LIST"`)

* `REGEXP` (value: `"KIND_REGEXP"`)




