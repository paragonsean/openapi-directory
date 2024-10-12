

# GoogleCloudDialogflowV2EntityType

Each intent parameter has a type, called the entity type, which dictates exactly how data from an end-user expression is extracted. Dialogflow provides predefined system entities that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own custom entities for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent. For more information, see the [Entity guide](https://cloud.google.com/dialogflow/docs/entities-overview).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoExpansionMode** | [**AutoExpansionModeEnum**](#AutoExpansionModeEnum) | Optional. Indicates whether the entity type can be automatically expanded. |  [optional] |
|**displayName** | **String** | Required. The name of the entity type. |  [optional] |
|**enableFuzzyExtraction** | **Boolean** | Optional. Enables fuzzy entity extraction during classification. |  [optional] |
|**entities** | [**List&lt;GoogleCloudDialogflowV2EntityTypeEntity&gt;**](GoogleCloudDialogflowV2EntityTypeEntity.md) | Optional. The collection of entity entries associated with the entity type. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Required. Indicates the kind of entity type. |  [optional] |
|**name** | **String** | The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType and EntityTypes.BatchUpdateEntityTypes methods. Format: &#x60;projects//agent/entityTypes/&#x60;. |  [optional] |



## Enum: AutoExpansionModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUTO_EXPANSION_MODE_UNSPECIFIED&quot; |
| DEFAULT | &quot;AUTO_EXPANSION_MODE_DEFAULT&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;KIND_UNSPECIFIED&quot; |
| MAP | &quot;KIND_MAP&quot; |
| LIST | &quot;KIND_LIST&quot; |
| REGEXP | &quot;KIND_REGEXP&quot; |



