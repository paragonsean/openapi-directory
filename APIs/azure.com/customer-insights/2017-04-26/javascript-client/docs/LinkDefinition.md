# CustomerInsightsManagementClient.LinkDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **{String: String}** | Localized descriptions for the Link. | [optional] 
**displayName** | **{String: String}** | Localized display name for the Link. | [optional] 
**linkName** | **String** | The link name. | [optional] [readonly] 
**mappings** | [**[TypePropertiesMapping]**](TypePropertiesMapping.md) | The set of properties mappings between the source and target Types. | [optional] 
**operationType** | **String** | Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only. | [optional] 
**participantPropertyReferences** | [**[ParticipantPropertyReference]**](ParticipantPropertyReference.md) | The properties that represent the participating profile. | 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**referenceOnly** | **Boolean** | Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles. | [optional] 
**sourceEntityType** | **String** | Type of source entity. | 
**sourceEntityTypeName** | **String** | Name of the source Entity Type. | 
**targetEntityType** | **String** | Type of target entity. | 
**targetEntityTypeName** | **String** | Name of the target Entity Type. | 
**tenantId** | **String** | The hub name. | [optional] [readonly] 



## Enum: OperationTypeEnum


* `Upsert` (value: `"Upsert"`)

* `Delete` (value: `"Delete"`)





## Enum: SourceEntityTypeEnum


* `None` (value: `"None"`)

* `Profile` (value: `"Profile"`)

* `Interaction` (value: `"Interaction"`)

* `Relationship` (value: `"Relationship"`)





## Enum: TargetEntityTypeEnum


* `None` (value: `"None"`)

* `Profile` (value: `"Profile"`)

* `Interaction` (value: `"Interaction"`)

* `Relationship` (value: `"Relationship"`)




