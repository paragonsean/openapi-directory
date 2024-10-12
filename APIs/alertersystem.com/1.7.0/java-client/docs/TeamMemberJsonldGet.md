

# TeamMemberJsonldGet

The TeamMember resource is a collection of active team members of the partitions in a user account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atContext** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  |  [optional] |
|**atId** | **String** |  |  [optional] [readonly] |
|**atType** | **String** |  |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] [readonly] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  [optional] |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**teamMemberRoleCode** | **String** | The role of the team member on the team. |  |
|**userAccount** | **String** | The user account that is related to this resource. |  [optional] |



