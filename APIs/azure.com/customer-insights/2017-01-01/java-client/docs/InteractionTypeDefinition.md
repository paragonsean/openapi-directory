

# InteractionTypeDefinition

The Interaction Type Definition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourcePrecedenceRules** | [**List&lt;DataSourcePrecedence&gt;**](DataSourcePrecedence.md) | This is specific to interactions modeled as activities. Data sources are used to determine where data is stored and also in precedence rules. |  [optional] [readonly] |
|**defaultDataSource** | [**DataSource**](DataSource.md) |  |  [optional] |
|**idPropertyNames** | **List&lt;String&gt;** | The id property names. Properties which uniquely identify an interaction instance. |  [optional] |
|**isActivity** | **Boolean** | An interaction can be tagged as an activity only during create. This enables the interaction to be editable and can enable merging of properties from multiple data sources based on precedence, which is defined at a link level. |  [optional] |
|**participantProfiles** | [**List&lt;Participant&gt;**](Participant.md) | Profiles that participated in the interaction. |  [optional] |
|**primaryParticipantProfilePropertyName** | **String** | The primary participant property name for an interaction ,This is used to logically represent the agent of the interaction, Specify the participant name here from ParticipantName. |  [optional] |
|**apiEntitySetName** | **String** | The api entity set name. This becomes the odata entity set name for the entity Type being referred in this object. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | Type of entity. |  [optional] |
|**fields** | [**List&lt;PropertyDefinition&gt;**](PropertyDefinition.md) | The properties of the Profile. |  [optional] |
|**instancesCount** | **Integer** | The instance count. |  [optional] |
|**lastChangedUtc** | **OffsetDateTime** | The last changed time for the type definition. |  [optional] [readonly] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**schemaItemTypeLink** | **String** | The schema org link. This helps ACI identify and suggest semantic models. |  [optional] |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |
|**timestampFieldName** | **String** | The timestamp property name. Represents the time when the interaction or profile update happened. |  [optional] |
|**typeName** | **String** | The name of the entity. |  [optional] |
|**attributes** | **Map&lt;String, List&lt;String&gt;&gt;** | The attributes for the Type. |  [optional] |
|**description** | **Map&lt;String, String&gt;** | Localized descriptions for the property. |  [optional] |
|**displayName** | **Map&lt;String, String&gt;** | Localized display names for the property. |  [optional] |
|**largeImage** | **String** | Large Image associated with the Property or EntityType. |  [optional] |
|**localizedAttributes** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Any custom localized attributes for the Type. |  [optional] |
|**mediumImage** | **String** | Medium Image associated with the Property or EntityType. |  [optional] |
|**smallImage** | **String** | Small Image associated with the Property or EntityType. |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PROFILE | &quot;Profile&quot; |
| INTERACTION | &quot;Interaction&quot; |
| RELATIONSHIP | &quot;Relationship&quot; |



