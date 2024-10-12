

# TeamInvitationJsonldGet

The TeamInvitation resource is a collection of invitations that have been sent to people to become team members of partitions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atContext** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  |  [optional] |
|**atId** | **String** |  |  [optional] [readonly] |
|**atType** | **String** |  |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] [readonly] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**inviteeEmail** | **String** | The email address of the person that is being invited. |  |
|**inviteeFirstName** | **String** | The first name of the person that is being invited. |  |
|**inviteeLastName** | **String** | The last name of the person that is being invited. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**statusAt** | **OffsetDateTime** | When the current status too effect. This date-time is in the UTC timezone.  |  [optional] |
|**teamInvitationStatus** | **String** | The current status of the invitation. |  [optional] [readonly] |
|**teamMemberRoleCode** | **String** | The role of the team member on the team. |  [optional] |



