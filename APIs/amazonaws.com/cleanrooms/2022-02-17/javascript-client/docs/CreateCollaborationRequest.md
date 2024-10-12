# AwsCleanRoomsService.CreateCollaborationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**[MemberSpecification]**](MemberSpecification.md) | A list of initial members, not including the creator. This list is immutable. | 
**name** | **String** | The display name for a collaboration. | 
**description** | **String** | A description of the collaboration provided by the collaboration owner. | 
**creatorMemberAbilities** | [**[MemberAbility]**](MemberAbility.md) | The abilities granted to the collaboration creator. | 
**creatorDisplayName** | **String** | The display name of the collaboration creator. | 
**dataEncryptionMetadata** | [**CreateCollaborationRequestDataEncryptionMetadata**](CreateCollaborationRequestDataEncryptionMetadata.md) |  | [optional] 
**queryLogStatus** | **String** | An indicator as to whether query logging has been enabled or disabled for the collaboration. | 
**tags** | **{String: String}** | Map of tags assigned to a resource | [optional] 



## Enum: QueryLogStatusEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)




