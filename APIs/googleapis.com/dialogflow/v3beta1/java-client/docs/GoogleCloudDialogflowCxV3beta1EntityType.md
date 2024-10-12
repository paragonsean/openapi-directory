

# GoogleCloudDialogflowCxV3beta1EntityType

Entities are extracted from user input and represent parameters that are meaningful to your application. For example, a date range, a proper name such as a geographic location or landmark, and so on. Entities represent actionable data for your application. When you define an entity, you can also include synonyms that all map to that entity. For example, \"soft drink\", \"soda\", \"pop\", and so on. There are three types of entities: * **System** - entities that are defined by the Dialogflow API for common data types such as date, time, currency, and so on. A system entity is represented by the `EntityType` type. * **Custom** - entities that are defined by you that represent actionable data that is meaningful to your application. For example, you could define a `pizza.sauce` entity for red or white pizza sauce, a `pizza.cheese` entity for the different types of cheese on a pizza, a `pizza.topping` entity for different toppings, and so on. A custom entity is represented by the `EntityType` type. * **User** - entities that are built for an individual user such as favorites, preferences, playlists, and so on. A user entity is represented by the SessionEntityType type. For more information about entity types, see the [Dialogflow documentation](https://cloud.google.com/dialogflow/docs/entities-overview).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoExpansionMode** | [**AutoExpansionModeEnum**](#AutoExpansionModeEnum) | Indicates whether the entity type can be automatically expanded. |  [optional] |
|**displayName** | **String** | Required. The human-readable name of the entity type, unique within the agent. |  [optional] |
|**enableFuzzyExtraction** | **Boolean** | Enables fuzzy entity extraction during classification. |  [optional] |
|**entities** | [**List&lt;GoogleCloudDialogflowCxV3beta1EntityTypeEntity&gt;**](GoogleCloudDialogflowCxV3beta1EntityTypeEntity.md) | The collection of entity entries associated with the entity type. |  [optional] |
|**excludedPhrases** | [**List&lt;GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase&gt;**](GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhrase.md) | Collection of exceptional words and phrases that shouldn&#39;t be matched. For example, if you have a size entity type with entry &#x60;giant&#x60;(an adjective), you might consider adding &#x60;giants&#x60;(a noun) as an exclusion. If the kind of entity type is &#x60;KIND_MAP&#x60;, then the phrases specified by entities and excluded phrases should be mutually exclusive. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Required. Indicates the kind of entity type. |  [optional] |
|**name** | **String** | The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType. Format: &#x60;projects//locations//agents//entityTypes/&#x60;. |  [optional] |
|**redact** | **Boolean** | Indicates whether parameters of the entity type should be redacted in log. If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name during logging. |  [optional] |



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



