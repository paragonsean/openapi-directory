

# RelationshipLinkDefinition

The definition of relationship link.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **Map&lt;String, String&gt;** | Localized descriptions for the Relationship Link. |  [optional] |
|**displayName** | **Map&lt;String, String&gt;** | Localized display name for the Relationship Link. |  [optional] |
|**interactionType** | **String** | The InteractionType associated with the Relationship Link. |  |
|**linkName** | **String** | The name of the Relationship Link. |  [optional] [readonly] |
|**mappings** | [**List&lt;RelationshipLinkFieldMapping&gt;**](RelationshipLinkFieldMapping.md) | The mappings between Interaction and Relationship fields. |  [optional] |
|**profilePropertyReferences** | [**List&lt;ParticipantProfilePropertyReference&gt;**](ParticipantProfilePropertyReference.md) | The property references for the Profile of the Relationship. |  |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**relatedProfilePropertyReferences** | [**List&lt;ParticipantProfilePropertyReference&gt;**](ParticipantProfilePropertyReference.md) | The property references for the Related Profile of the Relationship. |  |
|**relationshipGuidId** | **String** | The relationship guid id. |  [optional] [readonly] |
|**relationshipName** | **String** | The Relationship associated with the Link. |  |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |



