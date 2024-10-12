

# LinkDefinition

The definition of Link.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **Map&lt;String, String&gt;** | Localized descriptions for the Link. |  [optional] |
|**displayName** | **Map&lt;String, String&gt;** | Localized display name for the Link. |  [optional] |
|**linkName** | **String** | The link name. |  [optional] [readonly] |
|**mappings** | [**List&lt;TypePropertiesMapping&gt;**](TypePropertiesMapping.md) | The set of properties mappings between the source and target Types. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only. |  [optional] |
|**participantPropertyReferences** | [**List&lt;ParticipantPropertyReference&gt;**](ParticipantPropertyReference.md) | The properties that represent the participating profile. |  |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**referenceOnly** | **Boolean** | Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles. |  [optional] |
|**sourceEntityType** | [**SourceEntityTypeEnum**](#SourceEntityTypeEnum) | Type of source entity. |  |
|**sourceEntityTypeName** | **String** | Name of the source Entity Type. |  |
|**targetEntityType** | [**TargetEntityTypeEnum**](#TargetEntityTypeEnum) | Type of target entity. |  |
|**targetEntityTypeName** | **String** | Name of the target Entity Type. |  |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| UPSERT | &quot;Upsert&quot; |
| DELETE | &quot;Delete&quot; |



## Enum: SourceEntityTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PROFILE | &quot;Profile&quot; |
| INTERACTION | &quot;Interaction&quot; |
| RELATIONSHIP | &quot;Relationship&quot; |



## Enum: TargetEntityTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PROFILE | &quot;Profile&quot; |
| INTERACTION | &quot;Interaction&quot; |
| RELATIONSHIP | &quot;Relationship&quot; |



