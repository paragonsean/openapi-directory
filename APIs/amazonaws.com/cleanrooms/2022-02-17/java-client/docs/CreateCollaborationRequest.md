

# CreateCollaborationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**members** | [**List&lt;MemberSpecification&gt;**](MemberSpecification.md) | A list of initial members, not including the creator. This list is immutable. |  |
|**name** | **String** | The display name for a collaboration. |  |
|**description** | **String** | A description of the collaboration provided by the collaboration owner. |  |
|**creatorMemberAbilities** | **List&lt;MemberAbility&gt;** | The abilities granted to the collaboration creator. |  |
|**creatorDisplayName** | **String** | The display name of the collaboration creator. |  |
|**dataEncryptionMetadata** | [**CreateCollaborationRequestDataEncryptionMetadata**](CreateCollaborationRequestDataEncryptionMetadata.md) |  |  [optional] |
|**queryLogStatus** | [**QueryLogStatusEnum**](#QueryLogStatusEnum) | An indicator as to whether query logging has been enabled or disabled for the collaboration. |  |
|**tags** | **Map&lt;String, String&gt;** | Map of tags assigned to a resource |  [optional] |



## Enum: QueryLogStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |



