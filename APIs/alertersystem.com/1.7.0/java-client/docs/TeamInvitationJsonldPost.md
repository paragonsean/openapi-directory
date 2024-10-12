

# TeamInvitationJsonldPost

The TeamInvitation resource is a collection of invitations that have been sent to people to become team members of partitions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**inviteeEmail** | **String** | The email address of the person that is being invited. |  |
|**inviteeFirstName** | **String** | The first name of the person that is being invited. |  |
|**inviteeLastName** | **String** | The last name of the person that is being invited. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**teamMemberRoleCode** | **String** | The role of the team member on the team. |  [optional] |



