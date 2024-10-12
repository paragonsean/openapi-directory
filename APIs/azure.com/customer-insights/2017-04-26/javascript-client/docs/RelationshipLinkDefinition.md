# CustomerInsightsManagementClient.RelationshipLinkDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **{String: String}** | Localized descriptions for the Relationship Link. | [optional] 
**displayName** | **{String: String}** | Localized display name for the Relationship Link. | [optional] 
**interactionType** | **String** | The InteractionType associated with the Relationship Link. | 
**linkName** | **String** | The name of the Relationship Link. | [optional] [readonly] 
**mappings** | [**[RelationshipLinkFieldMapping]**](RelationshipLinkFieldMapping.md) | The mappings between Interaction and Relationship fields. | [optional] 
**profilePropertyReferences** | [**[ParticipantProfilePropertyReference]**](ParticipantProfilePropertyReference.md) | The property references for the Profile of the Relationship. | 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**relatedProfilePropertyReferences** | [**[ParticipantProfilePropertyReference]**](ParticipantProfilePropertyReference.md) | The property references for the Related Profile of the Relationship. | 
**relationshipGuidId** | **String** | The relationship guid id. | [optional] [readonly] 
**relationshipName** | **String** | The Relationship associated with the Link. | 
**tenantId** | **String** | The hub name. | [optional] [readonly] 


