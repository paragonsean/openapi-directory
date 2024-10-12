# CustomerInsightsManagementClient.RelationshipDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardinality** | **String** | The Relationship Cardinality. | [optional] 
**description** | **{String: String}** | Localized descriptions for the Relationship. | [optional] 
**displayName** | **{String: String}** | Localized display name for the Relationship. | [optional] 
**expiryDateTimeUtc** | **Date** | The expiry date time in UTC. | [optional] 
**fields** | [**[PropertyDefinition]**](PropertyDefinition.md) | The properties of the Relationship. | [optional] 
**lookupMappings** | [**[RelationshipTypeMapping]**](RelationshipTypeMapping.md) | Optional property to be used to map fields in profile to their strong ids in related profile. | [optional] 
**profileType** | **String** | Profile type. | 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**relatedProfileType** | **String** | Related profile being referenced. | 
**relationshipGuidId** | **String** | The relationship guid id. | [optional] [readonly] 
**relationshipName** | **String** | The Relationship name. | [optional] [readonly] 
**tenantId** | **String** | The hub name. | [optional] [readonly] 



## Enum: CardinalityEnum


* `OneToOne` (value: `"OneToOne"`)

* `OneToMany` (value: `"OneToMany"`)

* `ManyToMany` (value: `"ManyToMany"`)




