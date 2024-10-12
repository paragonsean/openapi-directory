

# RelationshipDefinition

The definition of Relationship.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardinality** | [**CardinalityEnum**](#CardinalityEnum) | The Relationship Cardinality. |  [optional] |
|**description** | **Map&lt;String, String&gt;** | Localized descriptions for the Relationship. |  [optional] |
|**displayName** | **Map&lt;String, String&gt;** | Localized display name for the Relationship. |  [optional] |
|**expiryDateTimeUtc** | **OffsetDateTime** | The expiry date time in UTC. |  [optional] |
|**fields** | [**List&lt;PropertyDefinition&gt;**](PropertyDefinition.md) | The properties of the Relationship. |  [optional] |
|**lookupMappings** | [**List&lt;RelationshipTypeMapping&gt;**](RelationshipTypeMapping.md) | Optional property to be used to map fields in profile to their strong ids in related profile. |  [optional] |
|**profileType** | **String** | Profile type. |  |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**relatedProfileType** | **String** | Related profile being referenced. |  |
|**relationshipGuidId** | **String** | The relationship guid id. |  [optional] [readonly] |
|**relationshipName** | **String** | The Relationship name. |  [optional] [readonly] |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |



## Enum: CardinalityEnum

| Name | Value |
|---- | -----|
| ONE_TO_ONE | &quot;OneToOne&quot; |
| ONE_TO_MANY | &quot;OneToMany&quot; |
| MANY_TO_MANY | &quot;ManyToMany&quot; |



