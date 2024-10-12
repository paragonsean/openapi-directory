

# InvitationProperties

Invitation property bag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**invitationId** | **String** | unique invitation id |  [optional] [readonly] |
|**invitationStatus** | [**InvitationStatusEnum**](#InvitationStatusEnum) | The status of the invitation. |  [optional] [readonly] |
|**respondedAt** | **OffsetDateTime** | The time the recipient responded to the invitation. |  [optional] [readonly] |
|**sentAt** | **OffsetDateTime** | Gets the time at which the invitation was sent. |  [optional] [readonly] |
|**targetActiveDirectoryId** | **String** | The target Azure AD Id. Can&#39;t be combined with email. |  [optional] |
|**targetEmail** | **String** | The email the invitation is directed to. |  [optional] |
|**targetObjectId** | **String** | The target user or application Id that invitation is being sent to.  Must be specified along TargetActiveDirectoryId. This enables sending  invitations to specific users or applications in an AD tenant. |  [optional] |
|**userEmail** | **String** | Email of the user who created the resource |  [optional] [readonly] |
|**userName** | **String** | Name of the user who created the resource |  [optional] [readonly] |



## Enum: InvitationStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;Pending&quot; |
| ACCEPTED | &quot;Accepted&quot; |
| REJECTED | &quot;Rejected&quot; |
| WITHDRAWN | &quot;Withdrawn&quot; |



